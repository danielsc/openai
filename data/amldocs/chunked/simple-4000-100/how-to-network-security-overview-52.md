* **Training compute access** - Access training compute targets like Azure Machine Learning Compute Instance and Azure Machine Learning Compute Clusters with public or private IP addresses.
* **Inference compute access** - Access Azure Kubernetes Services (AKS) compute clusters with private IP addresses.


The next sections show you how to secure the network scenario described above. To secure your network, you must:

1. Secure the [**workspace and associated resources**](#secure-the-workspace-and-associated-resources).
1. Secure the [**training environment**](#secure-the-training-environment).
1. Secure the [**inferencing environment**](#secure-the-inferencing-environment).
1. Optionally: [**enable studio functionality**](#optional-enable-studio-functionality).
1. Configure [**firewall settings**](#configure-firewall-settings).
1. Configure [**DNS name resolution**](#custom-dns).

## Public workspace and secured resources

If you want to access the workspace over the public internet while keeping all the associated resources secured in a virtual network, use the following steps:

1. Create an [Azure Virtual Network](../virtual-network/virtual-networks-overview.md) that will contain the resources used by the workspace.
1. Use __one__ of the following options to create a publicly accessible workspace:

    * Create an Azure Machine Learning workspace that __does not__ use the virtual network. For more information, see [Manage Azure Machine Learning workspaces](how-to-manage-workspace.md).
    * Create a [Private Link-enabled workspace](how-to-secure-workspace-vnet.md#secure-the-workspace-with-private-endpoint) to enable communication between your VNet and workspace. Then [enable public access to the workspace](#optional-enable-public-access).

1. Add the following services to the virtual network by using _either_ a __service endpoint__ or a __private endpoint__. Also allow trusted Microsoft services to access these services:

    | Service | Endpoint information | Allow trusted information |
    | ----- | ----- | ----- |
    | __Azure Key Vault__| [Service endpoint](../key-vault/general/overview-vnet-service-endpoints.md)</br>[Private endpoint](../key-vault/general/private-link-service.md) | [Allow trusted Microsoft services to bypass this firewall](how-to-secure-workspace-vnet.md#secure-azure-key-vault) |
    | __Azure Storage Account__ | [Service and private endpoint](how-to-secure-workspace-vnet.md?tabs=se#secure-azure-storage-accounts)</br>[Private endpoint](how-to-secure-workspace-vnet.md?tabs=pe#secure-azure-storage-accounts) | [Grant access to trusted Azure services](../storage/common/storage-network-security.md#grant-access-to-trusted-azure-services) |
    | __Azure Container Registry__ | [Private endpoint](../container-registry/container-registry-private-link.md) | [Allow trusted services](../container-registry/allow-access-trusted-services.md) |

1. In properties for the Azure Storage Account(s) for your workspace, add your client IP address to the allowed list in firewall settings. For more information, see [Configure firewalls and virtual networks](../storage/common/storage-network-security.md#configuring-access-from-on-premises-networks).

## Secure the workspace and associated resources

Use the following steps to secure your workspace and associated resources. These steps allow your services to communicate in the virtual network.

1. Create an [Azure Virtual Networks](../virtual-network/virtual-networks-overview.md) that will contain the workspace and other resources. Then create a [Private Link-enabled workspace](how-to-secure-workspace-vnet.md#secure-the-workspace-with-private-endpoint) to enable communication between your VNet and workspace.
1. Add the following services to the virtual network by using _either_ a __service endpoint__ or a __private endpoint__. Also allow trusted Microsoft services to access these services:

    | Service | Endpoint information | Allow trusted information |
    | ----- | ----- | ----- |
