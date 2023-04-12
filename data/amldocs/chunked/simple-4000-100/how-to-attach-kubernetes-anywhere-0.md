
# Introduction to Kubernetes compute target in AzureML

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

With AzureML CLI/Python SDK v2, AzureML introduced a new compute target - Kubernetes compute target. You can easily enable an existing **Azure Kubernetes Service** (AKS) cluster or **Azure Arc-enabled Kubernetes** (Arc Kubernetes) cluster to become a Kubernetes compute target in AzureML, and use it to train or deploy models. 

:::image type="content" source="./media/how-to-attach-kubernetes-to-workspace/machine-learning-anywhere-overview.png" alt-text="Diagram illustrating how Azure ML connects to Kubernetes." lightbox="./media/how-to-attach-kubernetes-to-workspace/machine-learning-anywhere-overview.png":::
 
In this article, you learn about:
> [!div class="checklist"]
> * How it works
> * Usage scenarios
> * Recommended best practices
> * KubernetesCompute and legacy AksCompute

## How it works

AzureML Kubernetes compute supports two kinds of Kubernetes cluster:
* **[AKS cluster](https://azure.microsoft.com/services/kubernetes-service/)** in Azure. With your self-managed AKS cluster in Azure, you can gain security and controls to meet compliance requirement and flexibility to manage teams' ML workload.
* **[Arc Kubernetes cluster](../azure-arc/kubernetes/overview.md)** outside of Azure. With Arc Kubernetes cluster, you can train or deploy models in any infrastructure on-premises, across multicloud, or the edge. 

With a simple cluster extension deployment on AKS or Arc Kubernetes cluster, Kubernetes cluster is seamlessly supported in AzureML to run training or inference workload. It's easy to enable and use an existing Kubernetes cluster for AzureML workload with the following simple steps:

1. Prepare an [Azure Kubernetes Service cluster](../aks/learn/quick-kubernetes-deploy-cli.md) or [Arc Kubernetes cluster](../azure-arc/kubernetes/quickstart-connect-cluster.md).
1. [Deploy the AzureML extension](how-to-deploy-kubernetes-extension.md).
1. [Attach Kubernetes cluster to your Azure ML workspace](how-to-attach-kubernetes-to-workspace.md).
1. Use the Kubernetes compute target from CLI v2, SDK v2, and the Studio UI.

**IT-operation team**. The IT-operation team is responsible for the first 3 steps above: prepare an AKS or Arc Kubernetes cluster, deploy Azure ML cluster extension, and attach Kubernetes cluster to Azure ML workspace. In addition to these essential compute setup steps, IT-operation team also uses familiar tools such as Azure CLI or kubectl to take care of the following tasks for the data-science team:

- Network and security configurations, such as outbound proxy server connection or Azure firewall configuration, inference router (azureml-fe) setup, SSL/TLS termination, and VNET configuration.
- Create and manage instance types for different ML workload scenarios and gain efficient compute resource utilization.
- Trouble shooting workload issues related to Kubernetes cluster.

**Data-science team**. Once the IT-operations team finishes compute setup and compute target(s) creation, the data-science team can discover a list of available compute targets and instance types in AzureML workspace. These compute resources can be used for training or inference workload. Data science specifies compute target name and instance type name using their preferred tools or APIs such as AzureML CLI v2, Python SDK v2, or Studio UI.

## Kubernetes usage scenarios

With Arc Kubernetes cluster, you can build, train, and deploy models in any infrastructure on-premises and across multicloud using Kubernetes. This opens some new use patterns previously not possible in cloud setting environment. The following table provides a summary of the new use patterns enabled by AzureML Kubernetes compute:

| Usage pattern | Location of data | Motivation | Infra setup & Azure ML implementation |
| ----- | ----- | ----- | ----- |
Train model in cloud, deploy model on-premises | Cloud | Make use of cloud compute. Either because of elastic compute needs or special hardware such as a GPU.<br/>Model must be deployed on-premises because of security, compliance, or latency requirements | 1. Azure managed compute in cloud.<br/>2. Customer managed Kubernetes on-premises.<br/>3. Fully automated MLOps in hybrid mode, including training and model deployment steps transitioning seamlessly from cloud to on-premises and vice versa.<br/>4. Repeatable, with all assets tracked properly. Model retrained when necessary, and model deployment updated automatically after retraining. |
