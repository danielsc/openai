

> [!TIP]
> You typically see display names of Azure regions such as 'East US' in the Azure Portal but the registry creation YAML needs names of regions without spaces and lower case letters. Use `az account list-locations -o table` to find the mapping of region display names to the name of the region that can be specified in YAML.

Run the registry create command.

`az ml registry create --file registry.yml`

# [AzureML studio](#tab/studio)

You can create registries in AzureML studio using the following steps:

1. In the [AzureML studio](https://ml.azure.com), select the __Registries__, and then __Manage registries__. Select __+ Create registry__.

    > [!TIP]
    > If you are in a workspace, navigate to the global UI by clicking your organization or tenant name in the navigation pane to find the __Registries__ entry.  You can also go directly there by navigating to [https://ml.azure.com/registries](https://ml.azure.com/registries).

    :::image type="content" source="./media/how-to-manage-registries/studio-create-registry-button.png" lightbox="./media/how-to-manage-registries/studio-create-registry-button.png" alt-text="Screenshot of the create registry screen.":::
	
1. Enter the registry name, select the subscription and resource group and then select __Next__.

    :::image type="content" source="./media/how-to-manage-registries/studio-create-registry-basics.png" alt-text="Screenshot of the registry creation basics tab.":::

1. Select the __Primary region__ and __Additional region__, then select __Next__.

    :::image type="content" source="./media/how-to-manage-registries/studio-registry-select-regions.png" alt-text="Screenshot of the registry region selection":::

1. Review the information you provided, and then select __Create__. You can track the progress of the create operation in the Azure portal. Once the registry is successfully created, you can find it listed in the __Manage Registries__ tab.

    :::image type="content" source="./media/how-to-manage-registries/studio-create-registry-review.png" alt-text="Screenshot of the create + review tab.":::
# [Azure portal](#tab/portal)

1. From the [Azure portal](https://portal.azure.com), navigate to the Azure Machine Learning service. You can get there by searching for __Azure Machine Learning__ in the search bar at the top of the page or going to __All Services__ looking for __Azure Machine Learning__ under the __AI + machine learning__ category. 

1. Select __Create__, and then select __Azure Machine Learning registry__. Enter the registry name, select the subscription, resource group and primary region, then select __Next__.
	
1. Select the additional regions the registry must support, then select __Next__ until you arrive at the __Review + Create__ tab.

    :::image type="content" source="./media/how-to-manage-registries/create-registry-review.png" alt-text="Screenshot of the review + create tab.":::

1. Review the information and select __Create__.


## Specify storage account type and SKU (optional)

> [!TIP]
> Specifying the Azure Storage Account type and SKU is only available from the Azure CLI.

Azure storage offers several types of storage accounts with different features and pricing. For more information, see the [Types of storage accounts](../storage/common/storage-account-overview.md#types-of-storage-accounts) article. Once you identify the optimal storage account SKU that best suites your needs, [find the value for the appropriate SKU type](/rest/api/storagerp/srp_sku_types). In the YAML file, use your selected SKU type as the value of the `storage_account_type` field. This field is under each `location` in the `replication_locations` list.

Next, decide if you want to use an [Azure Blob storage](../storage/blobs/storage-blobs-introduction.md) account or [Azure Data Lake Storage Gen2](../storage/blobs/data-lake-storage-introduction.md). To create Azure Data Lake Storage Gen2, set `storage_account_hns` to `true`. To create Azure Blob Storage, set `storage_account_hns` to `false`. The `storage_account_hns` field is under each `location` in the `replication_locations` list.
