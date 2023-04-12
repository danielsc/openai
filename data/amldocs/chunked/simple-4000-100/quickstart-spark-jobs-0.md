
# Quickstart: Apache Spark jobs in Azure Machine Learning (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

The Azure Machine Learning integration, with Azure Synapse Analytics (preview), provides easy access to distributed computing capability - backed by Azure Synapse - for scaling Apache Spark jobs on Azure Machine Learning.

In this quickstart guide, you learn how to submit a Spark job using Azure Machine Learning Managed (Automatic) Spark compute, Azure Data Lake Storage (ADLS) Gen 2 storage account, and user identity passthrough in a few simple steps.

For more information about **Apache Spark in Azure Machine Learning** concepts, see [this resource](./apache-spark-azure-ml-concepts.md).

## Prerequisites

# [CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- An Azure Data Lake Storage (ADLS) Gen 2 storage account. See [Create an Azure Data Lake Storage (ADLS) Gen 2 storage account](../storage/blobs/create-data-lake-storage-account.md).
- [Create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public).

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- An Azure Data Lake Storage (ADLS) Gen 2 storage account. See [Create an Azure Data Lake Storage (ADLS) Gen 2 storage account](../storage/blobs/create-data-lake-storage-account.md).
- [Configure your development environment](./how-to-configure-environment.md), or [create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme).

# [Studio UI](#tab/studio-ui)
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- An Azure Data Lake Storage (ADLS) Gen 2 storage account. See [Create an Azure Data Lake Storage (ADLS) Gen 2 storage account](../storage/blobs/create-data-lake-storage-account.md).
- To enable this feature:
  1. Navigate to Azure Machine Learning studio UI.
  2. Select **Manage preview features** (megaphone icon) among the icons on the top right side of the screen.
  3. In **Managed preview feature** panel, toggle on **Run notebooks and jobs on managed Spark** feature.
  :::image type="content" source="media/quickstart-spark-jobs/how-to-enable-managed-spark-preview.png" lightbox="media/quickstart-spark-jobs/how-to-enable-managed-spark-preview.png" alt-text="Expandable screenshot showing option for enabling Managed Spark preview.":::


## Add role assignments in Azure storage accounts

Before we submit an Apache Spark job, we must ensure that input, and output, data paths are accessible. Assign **Contributor** and **Storage Blob Data Contributor** roles to the user identity of the logged-in user to enable read and write access.

To assign appropriate roles to the user identity:

1. Open the [Microsoft Azure portal](https://portal.azure.com).
1. Search for, and select, the **Storage accounts** service.

    :::image type="content" source="media/quickstart-spark-jobs/find-storage-accounts-service.png" lightbox="media/quickstart-spark-jobs/find-storage-accounts-service.png" alt-text="Expandable screenshot showing search for and selection of Storage accounts service, in Microsoft Azure portal.":::
