
# Deploy AzureML extension on AKS or Arc Kubernetes cluster

To enable your AKS or Arc Kubernetes cluster to run training jobs or inference workloads, you must first deploy the AzureML extension on an AKS or Arc Kubernetes cluster. The AzureML extension is built on the [cluster extension for AKS](../aks/cluster-extensions.md) and [cluster extension or Arc Kubernetes](../azure-arc/kubernetes/conceptual-extensions.md), and its lifecycle can be managed easily with Azure CLI [k8s-extension](/cli/azure/k8s-extension).

In this article, you can learn:
> [!div class="checklist"]
> * Prerequisites
> * Limitations
> * Review AzureML extension config settings 
> * AzureML extension deployment scenarios
> * Verify AzureML extension deployment
> * Review AzureML extension components
> * Manage AzureML extension

## Prerequisites

* An AKS cluster running in Azure. If you have not previously used cluster extensions, you need to [register the KubernetesConfiguration service provider](../aks/dapr.md#register-the-kubernetesconfiguration-service-provider).
* Or an Arc Kubernetes cluster is up and running. Follow instructions in [connect existing Kubernetes cluster to Azure Arc](../azure-arc/kubernetes/quickstart-connect-cluster.md).
  * If the cluster is an Azure RedHat OpenShift Service (ARO) cluster or OpenShift Container Platform (OCP) cluster, you must satisfy other prerequisite steps as documented in the [Reference for configuring Kubernetes cluster](./reference-kubernetes.md#prerequisites-for-aro-or-ocp-clusters) article.
* For production purposes, the Kubernetes cluster must have a minimum of **4 vCPU cores and 14-GB memory**. For more information on resource detail and cluster size recommendations, see [Recommended resource planning](./reference-kubernetes.md).
* Cluster running behind an outbound proxy server or firewall needs extra [network configurations](./how-to-access-azureml-behind-firewall.md).
* Install or upgrade Azure CLI to version 2.24.0 or higher.
* Install or upgrade Azure CLI extension `k8s-extension` to version 1.2.3 or higher.
  

## Limitations

- [Using a service principal with AKS](../aks/kubernetes-service-principal.md) is **not supported** by Azure Machine Learning. The AKS cluster must use a **managed identity** instead. Both **system-assigned managed identity** and **user-assigned managed identity** are supported. For more information, see [Use a managed identity in Azure Kubernetes Service](../aks/use-managed-identity.md).
- [Disabling local accounts](../aks/managed-aad.md#disable-local-accounts) for AKS is **not supported**  by Azure Machine Learning. When the AKS Cluster is deployed, local accounts are enabled by default.
- If your AKS cluster has an [Authorized IP range enabled to access the API server](../aks/api-server-authorized-ip-ranges.md), enable the AzureML control plane IP ranges for the AKS cluster. The AzureML control plane is deployed across paired regions. Without access to the API server, the machine learning pods can't be deployed. Use the [IP ranges](https://www.microsoft.com/download/confirmation.aspx?id=56519) for both the [paired regions](../availability-zones/cross-region-replication-azure.md) when enabling the IP ranges in an AKS cluster.
- Azure Machine Learning does not guarantee support for all preview stage features in AKS. For example, [Azure AD pod identity](../aks/use-azure-ad-pod-identity.md) is not supported.
- If you've previously followed the steps from [AzureML AKS v1 document](./v1/how-to-create-attach-kubernetes.md) to create or attach your AKS as inference cluster, use the following link to [clean up the legacy azureml-fe related resources](./v1/how-to-create-attach-kubernetes.md#delete-azureml-fe-related-resources) before you continue the next step.
- We currently don't support attaching your AKS cluster across subscription, which means that your AKS cluster must be in the same subscription as your workspace. 
   - The workaround to meet your cross-subscription requirement is to first connect AKS to Azure-ARC and then attach this ARC-Kubernetes resource.
