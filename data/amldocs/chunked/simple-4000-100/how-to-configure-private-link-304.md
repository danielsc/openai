Azure Machine Learning supports multiple private endpoints for a workspace. Multiple private endpoints are often used when you want to keep different environments separate. The following are some scenarios that are enabled by using multiple private endpoints:

* Client development environments in a separate VNet.
* An Azure Kubernetes Service (AKS) cluster in a separate VNet.
* Other Azure services in a separate VNet. For example, Azure Synapse and Azure Data Factory can use a Microsoft managed virtual network. In either case, a private endpoint for the workspace can be added to the managed VNet used by those services. For more information on using a managed virtual network with these services, see the following articles:

    * [Synapse managed private endpoints](../synapse-analytics/security/synapse-workspace-managed-private-endpoints.md)
    * [Azure Data Factory managed virtual network](../data-factory/managed-virtual-network-private-endpoint.md).

    > [!IMPORTANT]
    > [Synapse's data exfiltration protection](../synapse-analytics/security/workspace-data-exfiltration-protection.md) is not supported with Azure Machine Learning.

> [!IMPORTANT]
> Each VNet that contains a private endpoint for the workspace must also be able to access the Azure Storage Account, Azure Key Vault, and Azure Container Registry used by the workspace. For example, you might create a private endpoint for the services in each VNet.

Adding multiple private endpoints uses the same steps as described in the [Add a private endpoint to a workspace](#add-a-private-endpoint-to-a-workspace) section.

### Scenario: Isolated clients

If you want to isolate the development clients, so they don't have direct access to the compute resources used by Azure Machine Learning, use the following steps:

> [!NOTE]
> These steps assume that you have an existing workspace, Azure Storage Account, Azure Key Vault, and Azure Container Registry. Each of these services has a private endpoints in an existing VNet.

1. Create another VNet for the clients. This VNet might contain Azure Virtual Machines that act as your clients, or it may contain a VPN Gateway used by on-premises clients to connect to the VNet.
1. Add a new private endpoint for the Azure Storage Account, Azure Key Vault, and Azure Container Registry used by your workspace. These private endpoints should exist in the client VNet.
1. If you have another storage that is used by your workspace, add a new private endpoint for that storage. The private endpoint should exist in the client VNet and have private DNS zone integration enabled.
1. Add a new private endpoint to your workspace. This private endpoint should exist in the client VNet and have private DNS zone integration enabled.
1. Use the steps in the [Use studio in a virtual network](how-to-enable-studio-virtual-network.md#datastore-azure-storage-account) article to enable studio to access the storage account(s).

The following diagram illustrates this configuration. The __Workload__ VNet contains computes created by the workspace for training & deployment. The __Client__ VNet contains clients or client ExpressRoute/VPN connections. Both VNets contain private endpoints for the workspace, Azure Storage Account, Azure Key Vault, and Azure Container Registry.

:::image type="content" source="./media/how-to-configure-private-link/multiple-private-endpoint-workspace-client.png" alt-text="Diagram of isolated client VNet":::

### Scenario: Isolated Azure Kubernetes Service

If you want to create an isolated Azure Kubernetes Service used by the workspace, use the following steps:

> [!NOTE]
> These steps assume that you have an existing workspace, Azure Storage Account, Azure Key Vault, and Azure Container Registry. Each of these services has a private endpoints in an existing VNet.

1. Create an Azure Kubernetes Service instance. During creation, AKS creates a VNet that contains the AKS cluster.
1. Add a new private endpoint for the Azure Storage Account, Azure Key Vault, and Azure Container Registry used by your workspace. These private endpoints should exist in the client VNet.
