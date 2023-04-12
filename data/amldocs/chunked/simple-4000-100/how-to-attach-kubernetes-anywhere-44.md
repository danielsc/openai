Train model in cloud, deploy model on-premises | Cloud | Make use of cloud compute. Either because of elastic compute needs or special hardware such as a GPU.<br/>Model must be deployed on-premises because of security, compliance, or latency requirements | 1. Azure managed compute in cloud.<br/>2. Customer managed Kubernetes on-premises.<br/>3. Fully automated MLOps in hybrid mode, including training and model deployment steps transitioning seamlessly from cloud to on-premises and vice versa.<br/>4. Repeatable, with all assets tracked properly. Model retrained when necessary, and model deployment updated automatically after retraining. |
| Train model on-premises, deploy model in cloud | On-premises | Data must remain on-premises due to data-residency requirements.<br/>Deploy model in the cloud for global service access or for compute elasticity for scale and throughput. | 1. Azure managed compute in cloud.<br/>2. Customer managed Kubernetes on-premises.<br/>3. Fully automated MLOps in hybrid mode, including training and model deployment steps transitioning seamlessly from cloud to on-premises and vice versa.<br/>4. Repeatable, with all assets tracked properly. Model retrained when necessary, and model deployment updated automatically after retraining. |
| Bring your own AKS in Azure | Cloud | More security and controls.<br/>All private IP machine learning to prevent data exfiltration. | 1. AKS cluster behind an Azure VNet.<br/>2. Create private endpoints in the same VNet for AzureML workspace and its associated resources.<br/>3. Fully automated MLOps. |
| Full ML lifecycle on-premises | On-premises | Secure sensitive data or proprietary IP, such as ML models and code/scripts. | 1. Outbound proxy server connection on-premises.<br/>2. Azure ExpressRoute and Azure Arc private link to Azure resources.<br/>3. Customer managed Kubernetes on-premises.<br/>4. Fully automated MLOps. |

## Recommended best practices

**Separation of responsibilities between the IT-operations team and data-science team**. As we mentioned above, managing your own compute and infrastructure for ML workload is a complicated task, and it's best to be done by IT-operations team so data-science team can focus on ML models for organizational efficiency.

**Create and manage instance types for different ML workload scenarios**. Each ML workload uses different amounts of compute resources such as CPU/GPU and memory. AzureML implements instance type as Kubernetes custom resource definition (CRD) with properties of nodeSelector and resource request/limit. With a carefully curated list of instance types, IT-operations can target ML workload on specific node(s) and manage compute resource utilization efficiently.

**Multiple AzureML workspaces share the same Kubernetes cluster**. You can attach Kubernetes cluster multiple times to the same AzureML workspace or different AzureML workspaces, creating multiple compute targets in one workspace or multiple workspaces. Since many customers organize data science projects around AzureML workspace, multiple data science projects can now share the same Kubernetes cluster. This significantly reduces ML infrastructure management overheads and IT cost saving.

**Team/project workload isolation using Kubernetes namespace**. When you attach Kubernetes cluster to AzureML workspace, you can specify a Kubernetes namespace for the compute target. All workloads run by the compute target will be placed under the specified namespace.

## KubernetesCompute and legacy AksCompute

With AzureML CLI/Python SDK v1, you can deploy models on AKS using AksCompute target. Both KubernetesCompute target and AksCompute target support AKS integration, however they support it differently. The following table shows their key differences:

|Capabilities  |AKS integration with AksCompute (legacy)  |AKS integration with KubernetesCompute|
|--|--|--|
|CLI/SDK v1 | Yes | No|
|CLI/SDK v2 | No | Yes|
|Training | No | Yes|
|Real-time inference | Yes | Yes |
|Batch inference | No | Yes |
