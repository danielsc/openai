1. On the __Create a private endpoint__ form, use the same __subscription__, __resource group__, and __Region__ that you've used for previous resources. Enter a unique __Name__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-file-private-endpoint.png" alt-text="UI to add the file private endpoint":::

1. Select __Next : Resource__, and then set __Target sub-resource__ to __file__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-file-private-endpoint-resource.png" alt-text="Add the subresource of 'file'":::

1. Select __Next : Configuration__, and then use the following values:
    * __Virtual network__: The network you created previously
    * __Subnet__: Training
    * __Integrate with private DNS zone__: Yes
    * __Private DNS zone__: privatelink.file.core.windows.net

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-file-private-endpoint-config.png" alt-text="UI to configure the file private endpoint":::

1. Select __Review + Create__. Verify that the information is correct, and then select __Create__.

> [!TIP]
> If you plan to use a [batch endpoint](concept-endpoints.md) or an Azure Machine Learning pipeline that uses a [ParallelRunStep](./tutorial-pipeline-batch-scoring-classification.md), it is also required to configure private endpoints target **queue** and **table** sub-resources. ParallelRunStep uses queue and table under the hood for task scheduling and dispatching.

## Create a key vault

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Key Vault__. Select the __Key Vault__ entry, and then select __Create__.
1. From the __Basics__ tab, select the __subscription__, __resource group__, and __region__ you previously used for the virtual network. Enter a unique __Key vault name__. Leave the other fields at the default value.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-key-vault.png" alt-text="Create a new key vault":::

1. From the __Networking__ tab, select __Private endpoint__ and then select __+ Add__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/key-vault-networking.png" alt-text="Key vault networking":::

1. On the __Create private endpoint__ form, use the following values:
    * __Subscription__: The same Azure subscription that contains the previous resources you've created.
    * __Resource group__: The same Azure resource group that contains the previous resources you've created.
    * __Location__: The same Azure region that contains the previous resources you've created.
    * __Name__: A unique name for this private endpoint.
    * __Target sub-resource__: Vault
    * __Virtual network__: The virtual network you created earlier.
    * __Subnet__: Training (172.16.0.0/24)
    * __Private DNS integration__: Yes
    * __Private DNS Zone__: privatelink.vaultcore.azure.net

    Select __OK__ to create the private endpoint.

    :::image type="content" source="./media/tutorial-create-secure-workspace/key-vault-private-endpoint.png" alt-text="Configure a key vault private endpoint":::

1. Select __Review + create__. Verify that the information is correct, and then select __Create__.

## Create a container registry

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Container Registry__. Select the __Container Registry__ entry, and then select __Create__.
1. From the __Basics__ tab, select the __subscription__, __resource group__, and __location__ you previously used for the virtual network. Enter a unique __Registry name__ and set the __SKU__ to __Premium__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-container-registry.png" alt-text="Create a container registry":::
