
# Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

Data wrangling becomes one of the most important steps in machine learning projects. The Azure Machine Learning integration, with Azure Synapse Analytics (preview), provides access to an Apache Spark pool - backed by Azure Synapse - for interactive data wrangling using Azure Machine Learning Notebooks.

In this article, you will learn how to perform data wrangling using

- Managed (Automatic) Synapse Spark compute
- Attached Synapse Spark pool

## Prerequisites
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- An Azure Data Lake Storage (ADLS) Gen 2 storage account. See [Create an Azure Data Lake Storage (ADLS) Gen 2 storage account](../storage/blobs/create-data-lake-storage-account.md).
- To enable this feature:
  1. Navigate to Azure Machine Learning studio UI.
  2. Select **Manage preview features** (megaphone icon) among the icons on the top right side of the screen.
  3. In **Managed preview feature** panel, toggle on **Run notebooks and jobs on managed Spark** feature.
  :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/how_to_enable_managed_spark_preview.png" alt-text="Screenshot showing option for enabling Managed Spark preview.":::
- (Optional): An Azure Key Vault. See [Create an Azure Key Vault](../key-vault/general/quick-create-portal.md).
- (Optional): A Service Principal. See [Create a Service Principal](../active-directory/develop/howto-create-service-principal-portal.md).
- [(Optional): An attached Synapse Spark pool in the Azure Machine Learning workspace](./how-to-manage-synapse-spark-pool.md).

Before starting data wrangling tasks, you will need familiarity with the process of storing secrets

- Azure Blob storage account access key
- Shared Access Signature (SAS) token
- Azure Data Lake Storage (ADLS) Gen 2 service principal information

in the Azure Key Vault. You will also need to know how to handle role assignments in the Azure storage accounts. The following sections review these concepts. Then, we will explore the details of interactive data wrangling using the Spark pools in Azure Machine Learning Notebooks.

> [!TIP]
> If you access data in your storage accounts using user identity passthrough, you can skip to [Add role assignments in Azure storage accounts](#add-role-assignments-in-azure-storage-accounts).

## Store Azure storage account credentials as secrets in Azure Key Vault

To store Azure storage account credentials as secrets in the Azure Key Vault using the Azure portal user interface:

1. Navigate to your Azure Key Vault in the Azure portal.
1. Select **Secrets** from the left panel.
1. Select **+ Generate/Import**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/azure-key-vault-secrets-generate-import.png" alt-text="Screenshot showing the Azure Key Vault Secrets Generate Or Import tab.":::

1. At the **Create a secret** screen, enter a **Name** for the secret you want to create.
1. Navigate to Azure Blob Storage Account, in the Azure portal, as seen in the image below.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/storage-account-access-keys.png" alt-text="Screenshot showing the Azure access key and connection string values screen.":::
1. Select **Access keys** from the Azure Blob Storage Account page left panel.
1. Select **Show** next to **Key 1**, and then **Copy to clipboard** to get the storage account access key.
    > [!Note] 
    > Select appropriate options to copy
    >  - Azure Blob storage container shared access signature (SAS) tokens
    >  - Azure Data Lake Storage (ADLS) Gen 2 storage account service principal credentials
