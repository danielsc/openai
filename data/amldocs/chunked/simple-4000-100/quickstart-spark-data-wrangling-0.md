
# Quickstart: Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

To handle interactive Azure Machine Learning notebook data wrangling, Azure Machine Learning integration, with Azure Synapse Analytics (preview), provides easy access to the Apache Spark framework. This access allows for Azure Machine Learning Notebook interactive data wrangling.

In this quickstart guide, you'll learn how to perform interactive data wrangling using Azure Machine Learning Managed (Automatic) Synapse Spark compute, Azure Data Lake Storage (ADLS) Gen 2 storage account, and user identity passthrough.

## Prerequisites
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- An Azure Data Lake Storage (ADLS) Gen 2 storage account. See [Create an Azure Data Lake Storage (ADLS) Gen 2 storage account](../storage/blobs/create-data-lake-storage-account.md).
- To enable this feature:
  1. Navigate to the Azure Machine Learning studio UI
  2. In the icon section at the top right of the screen, select **Manage preview features** (megaphone icon)
  3. In the **Managed preview feature** panel, toggle the **Run notebooks and jobs on managed Spark** feature to **on**
  :::image type="content" source="media/quickstart-spark-data-wrangling/how-to-enable-managed-spark-preview.png" lightbox="media/quickstart-spark-data-wrangling/how-to-enable-managed-spark-preview.png" alt-text="Screenshot showing the option to enable the Managed Spark preview.":::

## Add role assignments in Azure storage accounts

We must ensure that the input and output data paths are accessible, before we start interactive data wrangling. To enable read and write access, assign **Contributor** and **Storage Blob Data Contributor** roles to the user identity of the logged-in user.

To assign appropriate roles to the user identity:

1. Open the [Microsoft Azure portal](https://portal.azure.com).
1. Search and select the **Storage accounts** service.

    :::image type="content" source="media/quickstart-spark-data-wrangling/find-storage-accounts-service.png" lightbox="media/quickstart-spark-data-wrangling/find-storage-accounts-service.png" alt-text="Expandable screenshot showing Storage accounts service search and selection, in Microsoft Azure portal.":::

1. On the **Storage accounts** page, select the Azure Data Lake Storage (ADLS) Gen 2 storage account from the list. A page showing the storage account **Overview** will open.

    :::image type="content" source="media/quickstart-spark-data-wrangling/storage-accounts-list.png" lightbox="media/quickstart-spark-data-wrangling/storage-accounts-list.png" alt-text="Expandable screenshot showing selection of the Azure Data Lake Storage (ADLS) Gen 2 storage account  Storage account.":::

1. Select **Access Control (IAM)** from the left panel
1. Select **Add role assignment**

    :::image type="content" source="media/quickstart-spark-data-wrangling/storage-account-add-role-assignment.png" lightbox="media/quickstart-spark-data-wrangling/storage-account-add-role-assignment.png" alt-text="Screenshot showing the Azure access keys screen.":::

1. Find and select role **Storage Blob Data Contributor**
1. Select **Next**

    :::image type="content" source="media/quickstart-spark-data-wrangling/add-role-assignment-choose-role.png" lightbox="media/quickstart-spark-data-wrangling/add-role-assignment-choose-role.png" alt-text="Screenshot showing the Azure add role assignment screen.":::

1. Select **User, group, or service principal**.
1. Select **+ Select members**.
1. Search for the user identity below **Select**
1. Select the user identity from the list, so that it shows under **Selected members**
1. Select the appropriate user identity
1. Select **Next**
