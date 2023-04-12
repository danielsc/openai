
# Secure Azure Kubernetes Service inferencing environment

If you have an Azure Kubernetes (AKS) cluster behind of VNet, you would need to secure Azure Machine Learning workspace resources and a compute environment using the same or peered VNet. In this article, you'll learn: 
  * What is a secure AKS inferencing environment
  * How to configure a secure AKS inferencing environment

## Limitations

* If your AKS cluster is behind of a VNet, your workspace and its associated resources (storage, key vault, Azure Container Registry) must have private endpoints or service endpoints in the same or peered VNet as AKS cluster's VNet. For more information on securing the workspace and associated resources, see [create a secure workspace](tutorial-create-secure-workspace.md).
* If your workspace has a __private endpoint__, the Azure Kubernetes Service cluster must be in the same Azure region as the workspace.
* Using a [public fully qualified domain name (FQDN) with a private AKS cluster](../aks/private-clusters.md) is __not supported__ with Azure Machine learning.

## What is a secure AKS inferencing environment

Azure Machine Learning AKS inferencing environment consists of workspace, your AKS cluster, and workspace associated resources - Azure Storage, Azure Key Vault, and Azure Container Services(ARC). The following table compares how services access different part of Azure Machine Learning network with or without a VNet.

| Scenario | Workspace | Associated resources (Storage account, Key Vault, ACR) | AKS cluster |
|-|-|-|-|-|
|**No virtual network**| Public IP | Public IP | Public IP |
|**Public workspace, all other resources in a virtual network** | Public IP | Public IP (service endpoint) <br> **- or -** <br> Private IP (private endpoint) | Private IP  |
|**Secure resources in a virtual network**| Private IP (private endpoint) | Public IP (service endpoint) <br> **- or -** <br> Private IP (private endpoint) | Private IP  | 

In a secure AKS inferencing environment, AKS cluster accesses different part of Azure Machine Learning services with private endpoint only (private IP). The following network diagram shows a secured Azure Machine Learning workspace with a private AKS cluster or default AKS cluster behind of VNet.

 [![A secure AKS inferencing envrionment: AKS cluster accesses different part of AzureML services with private endpoint, including workspace and its associated resources](./media/how-to-network-security-overview/secure-inferencing-environment.svg)](./media/how-to-network-security-overview/secure-inferencing-environment.svg)

## How to configure a secure AKS inferencing environment

To configure a secure AKS inferencing environment, you must have VNet information for AKS. [VNet](../virtual-network/quick-create-portal.md) can be created independently or during AKS cluster deployment. There are two options for AKS cluster in a VNet:
  * Deploy default AKS cluster to your VNet
  * Or create private AKS cluster to your VNet

For default AKS cluster, you can find VNet information under the resource group of `MC_[rg_name][aks_name][region]`. 

After you have VNet information for AKS cluster and if you already have workspace available, use following steps to configure a secure AKS inferencing environment:
  
  * Use your AKS cluster VNet information to add new private endpoints for the Azure Storage Account, Azure Key Vault, and Azure Container Registry used by your workspace. These private endpoints should exist in the same or peered VNet as AKS cluster. For more information, see the [secure workspace with private endpoint](./how-to-secure-workspace-vnet.md#secure-the-workspace-with-private-endpoint) article.
  * If you have other storage that is used by your AzureML workloads, add a new private endpoint for that storage. The private endpoint should be in the same or peered VNet as AKS cluster and have private DNS zone integration enabled.
  * Add a new private endpoint to your workspace. This private endpoint should be in the same or peered VNet as your AKS cluster and have private DNS zone integration enabled.
