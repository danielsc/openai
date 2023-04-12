   |aml-operator|Kubernetes deployment|**&check;**|N/A|**&check;**|Manage the lifecycle of training jobs.| Token exchange with the cloud token service for authentication and authorization of Azure Container Registry.|
   |metrics-controller-manager|Kubernetes deployment|**&check;**|**&check;**|**&check;**|Manage the configuration for Prometheus|N/A|
   |{EXTENSION-NAME}-kube-state-metrics|Kubernetes deployment|**&check;**|**&check;**|**&check;**|Export the cluster-related metrics to Prometheus.|N/A|
   |{EXTENSION-NAME}-prometheus-operator|Kubernetes deployment|Optional|Optional|Optional| Provide Kubernetes native deployment and management of Prometheus and related monitoring components.|N/A|
   |amlarc-identity-controller|Kubernetes deployment|N/A|**&check;**|**&check;**|Request and renew Azure Blob/Azure Container Registry token through managed identity.|Token exchange with the cloud token service for authentication and authorization of Azure Container  Registry and Azure Blob used by inference/model deployment.|
   |amlarc-identity-proxy|Kubernetes deployment|N/A|**&check;**|**&check;**|Request and renew Azure Blob/Azure Container Registry token  through managed identity.|Token exchange with the cloud token service for authentication and authorization of Azure Container  Registry and Azure Blob used by inference/model deployment.|
   |azureml-fe-v2|Kubernetes deployment|N/A|**&check;**|**&check;**|The front-end component that routes incoming inference requests to deployed services.|Send service logs to Azure Blob.|
   |inference-operator-controller-manager|Kubernetes deployment|N/A|**&check;**|**&check;**|Manage the lifecycle of inference endpoints. |N/A|
   |volcano-admission|Kubernetes deployment|Optional|N/A|Optional|Volcano admission webhook.|N/A|
   |volcano-controllers|Kubernetes deployment|Optional|N/A|Optional|Manage the lifecycle of Azure Machine Learning training job pods.|N/A|
   |volcano-scheduler |Kubernetes deployment|Optional|N/A|Optional|Used to perform in-cluster job scheduling.|N/A|
   |fluent-bit|Kubernetes daemonset|**&check;**|**&check;**|**&check;**|Gather the components' system log.| Upload the components' system log to cloud.|
   |{EXTENSION-NAME}-dcgm-exporter|Kubernetes daemonset|Optional|Optional|Optional|dcgm-exporter exposes GPU metrics for Prometheus.|N/A|
   |nvidia-device-plugin-daemonset|Kubernetes daemonset|Optional|Optional|Optional|nvidia-device-plugin-daemonset exposes GPUs on each node of your cluster| N/A|
   |prometheus-prom-prometheus|Kubernetes statefulset|**&check;**|**&check;**|**&check;**|Gather and send job metrics to cloud.|Send job metrics like cpu/gpu/memory utilization to cloud.|

> [!IMPORTANT]
   > * Azure Relay resource  is under the same resource group as the Arc cluster resource. It is used to communicate with the Kubernetes cluster and modifying them will break attached compute targets.
   > * By default, the kubernetes deployment resources are randomly deployed to 1 or more nodes of the cluster, and daemonset resources are deployed to ALL nodes. If you want to restrict the extension deployment to specific nodes, use `nodeSelector` configuration setting described in [configuration settings table](#review-azureml-extension-configuration-settings).

> [!NOTE]
   > * **{EXTENSION-NAME}:** is the extension name specified with `az k8s-extension create --name` CLI command. 


### Manage AzureML extension

Update, list, show and delete an AzureML extension.

- For AKS cluster without Azure Arc connected, refer to  [Usage of AKS extensions](../aks/cluster-extensions.md#usage-of-cluster-extensions).
- For Azure Arc-enabled Kubernetes, refer to [Usage of cluster extensions](../azure-arc/kubernetes/extensions.md#usage-of-cluster-extensions).


## Next steps

- [Step 2: Attach Kubernetes cluster to workspace](how-to-attach-kubernetes-to-workspace.md)
- [Create and manage instance types](./how-to-manage-kubernetes-instance-types.md)
- [AzureML inference router and connectivity requirements](./how-to-kubernetes-inference-routing-azureml-fe.md)
