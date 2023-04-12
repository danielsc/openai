
<!-- # Virtual network isolation and privacy overview -->
# Secure Azure Machine Learning workspace resources using virtual networks (VNets)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK or CLI version you are using:"]
> * [SDK/CLI v1](v1/how-to-network-security-overview.md)
> * [SDK/CLI v2 (current version)](how-to-network-security-overview.md)

Secure Azure Machine Learning workspace resources and compute environments using virtual networks (VNets). This article uses an example scenario to show you how to configure a complete virtual network.

> [!TIP]
> This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:
>
> * [Secure the workspace resources](how-to-secure-workspace-vnet.md)
> * [Secure the training environment](how-to-secure-training-vnet.md)
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md)
> * [Enable studio functionality](how-to-enable-studio-virtual-network.md)
> * [Use custom DNS](how-to-custom-dns.md)
> * [Use a firewall](how-to-access-azureml-behind-firewall.md)
> * [API platform network isolation](how-to-configure-network-isolation-with-v2.md)
>
> For a tutorial on creating a secure workspace, see [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md) or [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md).

## Prerequisites

This article assumes that you have familiarity with the following topics:
+ [Azure Virtual Networks](../virtual-network/virtual-networks-overview.md)
+ [IP networking](../virtual-network/ip-services/public-ip-addresses.md)
+ [Azure Machine Learning workspace with private endpoint](how-to-configure-private-link.md)
+ [Network Security Groups (NSG)](../virtual-network/network-security-groups-overview.md)
+ [Network firewalls](../firewall/overview.md)
## Example scenario

In this section, you learn how a common network scenario is set up to secure Azure Machine Learning communication with private IP addresses.

The following table compares how services access different parts of an Azure Machine Learning network with and without a VNet:

| Scenario | Workspace | Associated resources | Training compute environment | Inferencing compute environment |
|-|-|-|-|-|-|
|**No virtual network**| Public IP | Public IP | Public IP | Public IP |
|**Public workspace, all other resources in a virtual network** | Public IP | Public IP (service endpoint) <br> **- or -** <br> Private IP (private endpoint) | Public IP | Private IP  |
|**Secure resources in a virtual network**| Private IP (private endpoint) | Public IP (service endpoint) <br> **- or -** <br> Private IP (private endpoint) | Private IP | Private IP  | 

* **Workspace** - Create a private endpoint for your workspace. The private endpoint connects the workspace to the vnet through several private IP addresses.
    * **Public access** - You can optionally enable public access for a secured workspace.
* **Associated resource** - Use service endpoints or private endpoints to connect to workspace resources like Azure storage, Azure Key Vault. For Azure Container Services, use a private endpoint.
    * **Service endpoints** provide the identity of your virtual network to the Azure service. Once you enable service endpoints in your virtual network, you can add a virtual network rule to secure the Azure service resources to your virtual network. Service endpoints use public IP addresses.
    * **Private endpoints** are network interfaces that securely connect you to a service powered by Azure Private Link. Private endpoint uses a private IP address from your VNet, effectively bringing the service into your VNet.
* **Training compute access** - Access training compute targets like Azure Machine Learning Compute Instance and Azure Machine Learning Compute Clusters with public or private IP addresses.
