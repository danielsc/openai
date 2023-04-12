    * **Table** - Only needed if you plan to use [Batch endpoints](concept-endpoints.md#what-are-batch-endpoints) or the [ParallelRunStep](./tutorial-pipeline-batch-scoring-classification.md) in an Azure Machine Learning pipeline.

    :::image type="content" source="./media/how-to-enable-studio-virtual-network/configure-storage-private-endpoint.png" alt-text="Screenshot showing private endpoint configuration page with blob and file options":::

    > [!TIP]
    > When configuring a storage account that is **not** the default storage, select the **Target subresource** type that corresponds to the storage account you want to add.

1. After creating the private endpoints for the storage resources, select the __Firewalls and virtual networks__ tab under __Networking__ for the storage account.
1. Select __Selected networks__, and then under __Resource instances__, select `Microsoft.MachineLearningServices/Workspace` as the __Resource type__. Select your workspace using __Instance name__. For more information, see [Trusted access based on system-assigned managed identity](../storage/common/storage-network-security.md#trusted-access-based-on-system-assigned-managed-identity).

    > [!TIP]
    > Alternatively, you can select __Allow Azure services on the trusted services list to access this storage account__ to more broadly allow access from trusted services. For more information, see [Configure Azure Storage firewalls and virtual networks](../storage/common/storage-network-security.md#trusted-microsoft-services).

    :::image type="content" source="./media/how-to-enable-virtual-network/storage-firewalls-and-virtual-networks-no-vnet.png" alt-text="The networking area on the Azure Storage page in the Azure portal when using private endpoint":::

1. Select __Save__ to save the configuration.

> [!TIP]
> When using a private endpoint, you can also disable public access. For more information, see [disallow public read access](../storage/blobs/anonymous-read-access-configure.md#allow-or-disallow-public-read-access-for-a-storage-account).

# [Service endpoint](#tab/se)

1. In the Azure portal, select the Azure Storage Account.

1. From the __Security + networking__ section on the left of the page, select __Networking__ and then select the __Firewalls and virtual networks__ tab.

1. Select __Selected networks__. Under __Virtual networks__, select the __Add existing virtual network__ link and select the virtual network that your workspace uses.

    > [!IMPORTANT]
    > The storage account must be in the same virtual network and subnet as the compute instances or clusters used for training or inference.

1. Under __Resource instances__, select `Microsoft.MachineLearningServices/Workspace` as the __Resource type__ and select your workspace using __Instance name__. For more information, see [Trusted access based on system-assigned managed identity](../storage/common/storage-network-security.md#trusted-access-based-on-system-assigned-managed-identity).

    > [!TIP]
    > Alternatively, you can select __Allow Azure services on the trusted services list to access this storage account__ to more broadly allow access from trusted services. For more information, see [Configure Azure Storage firewalls and virtual networks](../storage/common/storage-network-security.md#trusted-microsoft-services).

    :::image type="content" source="./media/how-to-enable-virtual-network/storage-firewalls-and-virtual-networks.png" alt-text="The networking area on the Azure Storage page in the Azure portal":::

1. Select __Save__ to save the configuration.

> [!TIP]
> When using a service endpoint, you can also disable public access. For more information, see [disallow public read access](../storage/blobs/anonymous-read-access-configure.md#allow-or-disallow-public-read-access-for-a-storage-account).


## Secure Azure Key Vault

Azure Machine Learning uses an associated Key Vault instance to store the following credentials:
* The associated storage account connection string
