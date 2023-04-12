
# Reference for configuring Kubernetes cluster for Azure Machine Learning

This article contains reference information that may be useful when [configuring Kubernetes with Azure Machine Learning](./how-to-attach-kubernetes-anywhere.md).


## Supported Kubernetes version and region


- Kubernetes clusters installing AzureML extension have a version support window of "N-2", that is aligned with [Azure Kubernetes Service (AKS) version support policy](../aks/supported-kubernetes-versions.md#kubernetes-version-support-policy), where 'N' is the latest GA minor version of Azure Kubernetes Service.

  - For example, if AKS introduces 1.20.a today, versions 1.20.a, 1.20.b, 1.19.c, 1.19.d, 1.18.e, and 1.18.f are supported.

  - If customers are running an unsupported Kubernetes version, they'll be asked to upgrade when requesting support for the cluster. Clusters running unsupported Kubernetes releases aren't covered by the AzureML extension support policies.
- AzureML extension region availability: 
  - AzureML extension can be deployed to AKS or Azure Arc-enabled Kubernetes in supported regions listed in [Azure Arc enabled Kubernetes region support](https://azure.microsoft.com/global-infrastructure/services/?products=azure-arc&regions=all).

## Recommended resource planning

When you deploy the AzureML extension, some related services will be deployed to your Kubernetes cluster for Azure Machine Learning. The following table lists the **Related Services and their resource usage** in the cluster:

|Deploy/Daemonset |Replica # |Training |Inference|CPU Request(m) |CPU Limit(m)| Memory Request(Mi) | Memory Limit(Mi) |
|-- |--|--|--|--|--|--|--|
|metrics-controller-manager  |1 |**&check;**|**&check;**|10|100|20|300|
|prometheus-operator  |1 |**&check;**|**&check;**|100|400|128|512|
|prometheus |1 |**&check;**|**&check;**| 100|1000|512|4096|
|kube-state-metrics  |1 |**&check;**|**&check;**|10|100|32|256|
|gateway |1 |**&check;**|**&check;**|50 |500|256|2048|
|fluent-bit  |1 per Node |**&check;**|**&check;**|10|200|100|300|
|inference-operator-controller-manager |1 |**&check;**|N/A|100|1000|128|1024|
|amlarc-identity-controller |1 |**&check;**|N/A |200|1000|200|1024|
|amlarc-identity-proxy |1 |**&check;**|N/A |200|1000|200|1024|
|azureml-ingress-nginx-controller  |1 |**&check;**|N/A | 100|1000|64|512|
|azureml-fe-v2  |**1** (for Test purpose) <br>or <br>**3** (for Production purpose) |**&check;**|N/A |900|2000|800|1200|
|online-deployment |1 per Deployment | User-created|N/A |\<user-define> |\<user-define> |\<user-define> |\<user-define> |
|online-deployment/identity-sidecar |1 per Deployment |**&check;**|N/A |10|50|100|100|
|aml-operator |1  |N/A |**&check;**|20|1020|124|2168|
|volcano-admission |1  |N/A |**&check;**|10|100|64|256|
|volcano-controller |1  |N/A |**&check;**|50|500|128|512|
|volcano-schedular |1  |N/A |**&check;**|50|500|128|512|


Excluding your own deployments/pods, the **total minimum system resources requirements** are as follows:

|Scenario | Enabled Inference | Enabled Training | CPU Request(m) |CPU Limit(m)| Memory Request(Mi) | Memory Limit(Mi) | Node count | Recommended minimum VM size | Corresponding AKS VM SKU |
|-- |-- |--|--|--|--|--|--|--|--|
|For Test | **&check;** | N/A | **1780** |8300 |**2440** | 12296 |1 Node |2 vCPU, 7 GiB Memory, 6400 IOPS, 1500Mbps BW| DS2v2|
|For Test | N/A| **&check;**  | **410** | 4420 |**1492** | 10960 |1 Node |2 vCPU, 7 GiB Memory, 6400 IOPS, 1500Mbps BW|DS2v2|
|For Test | **&check;** | **&check;**  | **1910** | 10420 |**2884** | 15744 |1 Node |4 vCPU, 14 GiB Memory, 12800 IOPS, 1500Mbps BW|DS3v2|
|For Production |**&check;** | N/A | 3600 |**12700**|4240|**15296**|3 Node(s)|4 vCPU, 14 GiB Memory, 12800 IOPS, 1500Mbps BW|  DS3v2|
|For Production |N/A | **&check;**| 410 |**4420**|1492|**10960**|1 Node(s)|8 vCPU, 28GiB Memroy, 25600 IOPs, 6000Mbps BW|DS4v2|
|For Production |**&check;** | **&check;**  | 3730 |**14820**|4684|**18744**|3 Node(s)|4 vCPU, 14 GiB Memory, 12800 IOPS, 1500Mbps BW| DS4v2|
