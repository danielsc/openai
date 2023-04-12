        :::image type="content" source="./media/tutorial-create-secure-workspace/vnet-add-training-subnet.png" alt-text="Screenshot of Training subnet.":::

    1. To create a subnet for compute resources used to _score_ your models, select __+ Add subnet__ again, and set the name and address range:
        * __Subnet name__: Scoring
        * __Starting address__: 172.16.1.0
        * __Subnet size__: /24 (256 addresses)

        :::image type="content" source="./media/tutorial-create-secure-workspace/vnet-add-scoring-subnet.png" alt-text="Screenshot of Scoring subnet.":::

    1. To create a subnet for _Azure Bastion_, select __+ Add subnet__ and set the template, starting address, and subnet size:
        * __Subnet template__: Azure Bastion
        * __Starting address__: 172.16.2.0
        * __Subnet size__: /26 (64 addresses)

        :::image type="content" source="./media/tutorial-create-secure-workspace/vnet-add-azure-bastion-subnet.png" alt-text="Screenshot of Azure Bastion subnet.":::

1. Select __Review + create__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-vnet-ip-address-final.png" alt-text="Screenshot showing the review + create button":::

1. Verify that the information is correct, and then select __Create__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-vnet-review.png" alt-text="Screenshot of the review page":::

## Create a storage account

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Storage account__. Select the __Storage Account__ entry, and then select __Create__.
1. From the __Basics__ tab, select the __subscription__, __resource group__, and __region__ you previously used for the virtual network. Enter a unique __Storage account name__, and set __Redundancy__ to __Locally-redundant storage (LRS)__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-storage.png" alt-text="Image of storage account basic config":::

1. From the __Networking__ tab, select __Private endpoint__ and then select __+ Add private endpoint__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-enable-private-endpoint.png" alt-text="UI to add the blob private network":::

1. On the __Create private endpoint__ form, use the following values:
    * __Subscription__: The same Azure subscription that contains the previous resources you've created.
    * __Resource group__: The same Azure resource group that contains the previous resources you've created.
    * __Location__: The same Azure region that contains the previous resources you've created.
    * __Name__: A unique name for this private endpoint.
    * __Target sub-resource__: blob
    * __Virtual network__: The virtual network you created earlier.
    * __Subnet__: Training (172.16.0.0/24)
    * __Private DNS integration__: Yes
    * __Private DNS Zone__: privatelink.blob.core.windows.net

    Select __OK__ to create the private endpoint.

1. Select __Review + create__. Verify that the information is correct, and then select __Create__.

1. Once the Storage Account has been created, select __Go to resource__:

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-go-to-resource.png" alt-text="Go to new storage resource":::

1. From the left navigation, select __Networking__ the __Private endpoint connections__ tab, and then select __+ Private endpoint__:

    > [!NOTE]
    > While you created a private endpoint for Blob storage in the previous steps, you must also create one for File storage.

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-file-networking.png" alt-text="UI for storage account networking":::

1. On the __Create a private endpoint__ form, use the same __subscription__, __resource group__, and __Region__ that you've used for previous resources. Enter a unique __Name__.
