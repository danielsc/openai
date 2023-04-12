|For Production |**&check;** | **&check;**  | 3730 |**14820**|4684|**18744**|3 Node(s)|4 vCPU, 14 GiB Memory, 12800 IOPS, 1500Mbps BW| DS4v2|

> [!NOTE]
> 
> * For **test purpose**, you should refer tp the resource **request**. 
> * For **production purpose**, you should refer to the resource **limit**.


> [!IMPORTANT]
>
> Here are some other considerations for reference:
> * For **higher network bandwidth and better disk I/O performance**, we recommend a larger SKU. 
>     * Take [DV2/DSv2](../virtual-machines/dv2-dsv2-series.md#dsv2-series) as example, using the large SKU can reduce the time of pulling image for better network/storage performance. 
>     * More information about AKS reservation can be found in [AKS reservation](../aks/concepts-clusters-workloads.md#resource-reservations).
> * If you are using AKS cluster, you may need to consider about the **size limit on a container image** in AKS, more information you can found in [AKS container image size limit](../aks/faq.md#what-is-the-size-limit-on-a-container-image-in-aks).

## Prerequisites for ARO or OCP clusters
### Disable Security Enhanced Linux (SELinux) 

[AzureML dataset](v1/how-to-train-with-datasets.md) (an SDK v1 feature used in AzureML training jobs) isn't supported on machines with SELinux enabled. Therefore, you need to disable `selinux`  on all workers in order to use AzureML dataset.

### Privileged setup for ARO and OCP

For AzureML extension deployment on ARO or OCP cluster, grant privileged access to AzureML service accounts, run ```oc edit scc privileged``` command, and add following service accounts under "users:":

* ```system:serviceaccount:azure-arc:azure-arc-kube-aad-proxy-sa```
* ```system:serviceaccount:azureml:{EXTENSION-NAME}-kube-state-metrics``` 
* ```system:serviceaccount:azureml:prom-admission```
* ```system:serviceaccount:azureml:default```
* ```system:serviceaccount:azureml:prom-operator```
* ```system:serviceaccount:azureml:load-amlarc-selinux-policy-sa```
* ```system:serviceaccount:azureml:azureml-fe-v2```
* ```system:serviceaccount:azureml:prom-prometheus```
* ```system:serviceaccount:{KUBERNETES-COMPUTE-NAMESPACE}:default```
* ```system:serviceaccount:azureml:azureml-ingress-nginx```
* ```system:serviceaccount:azureml:azureml-ingress-nginx-admission```

> [!NOTE]
> * `{EXTENSION-NAME}`: is the extension name specified with the `az k8s-extension create --name` CLI command. 
>* `{KUBERNETES-COMPUTE-NAMESPACE}`: is the namespace of the Kubernetes compute specified when attaching the compute to the Azure Machine Learning workspace. Skip configuring `system:serviceaccount:{KUBERNETES-COMPUTE-NAMESPACE}:default` if `KUBERNETES-COMPUTE-NAMESPACE` is `default`.

## Collected log details

Some logs about AzureML workloads in the cluster will be collected through extension components, such as status, metrics, life cycle, etc. The following list shows all the log details collected, including the type of logs collected and where they were sent to or stored.

|Pod  |Resource description |Detail logging info |
|--|--|--|
|amlarc-identity-controller	|Request and renew Azure Blob/Azure Container Registry token through managed identity.	|Only used when `enableInference=true` is set when installing the extension. It has trace logs for status on getting identity for endpoints to authenticate with AzureML service.|
|amlarc-identity-proxy	|Request and renew Azure Blob/Azure Container Registry token through managed identity.	|Only used when `enableInference=true` is set when installing the extension. It has trace logs for status on getting identity for the cluster to authenticate with AzureML service.|
|aml-operator	| Manage the lifecycle of training jobs.	|The logs contain AzureML training job pod status in the cluster.|
|azureml-fe-v2|	The front-end component that routes incoming inference requests to deployed services.	|Access logs at request level, including request ID, start time, response code, error details and durations for request latency. Trace logs for service metadata changes, service running healthy status, etc. for debugging purpose.|
