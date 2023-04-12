
# Submit Spark jobs in Azure Machine Learning (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

Azure Machine Learning supports submission of standalone machine learning jobs, and creation of [machine learning pipelines](./concept-ml-pipelines.md), that involve multiple machine learning workflow steps. Azure Machine Learning handles both standalone Spark job creation, and creation of reusable Spark components that Azure Machine Learning pipelines can use. In this article, you'll learn how to submit Spark jobs using:
- Azure Machine Learning Studio UI
- Azure Machine Learning CLI
- Azure Machine Learning SDK

See [this resource](./apache-spark-azure-ml-concepts.md) for more information about **Apache Spark in Azure Machine Learning** concepts.

## Prerequisites

# [CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- [Create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public).
- [(Optional): An attached Synapse Spark pool in the Azure Machine Learning workspace](./how-to-manage-synapse-spark-pool.md).

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- [Configure your development environment](./how-to-configure-environment.md), or [create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install the Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme).
- [(Optional): An attached Synapse Spark pool in the Azure Machine Learning workspace](./how-to-manage-synapse-spark-pool.md).

# [Studio UI](#tab/ui)
These prerequisites cover the submission of a Spark job from Azure Machine Learning Studio UI:
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- To enable this feature:
  1. Navigate to Azure Machine Learning Studio UI.
  2. Select **Manage preview features** (megaphone icon) from the icons on the top right side of the screen.
  3. In **Managed preview feature** panel, toggle on **Run notebooks and jobs on managed Spark** feature.
  :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/how_to_enable_managed_spark_preview.png" alt-text="Screenshot showing option for enabling Managed Spark preview.":::
- [(Optional): An attached Synapse Spark pool in the Azure Machine Learning workspace](./how-to-manage-synapse-spark-pool.md).


## Ensuring resource access for Spark jobs
Spark jobs can use either user identity passthrough, or a managed identity, to access data and other resources. The following table summarizes the different mechanisms for resource access while using Azure Machine Learning Managed (Automatic) Spark compute and attached Synapse Spark pool.

|Spark pool|Supported identities|Default identity|
| ---------- | -------------------- | ---------------- |
|Managed (Automatic) Spark compute|User identity and managed identity|User identity|
|Attached Synapse Spark pool|User identity and managed identity|Managed identity - compute identity of the attached Synapse Spark pool|

If the CLI or SDK code defines an option to use managed identity, Azure Machine Learning Managed (Automatic) Spark compute uses user-assigned managed identity attached to the workspace. You can attach a user-assigned managed identity to an existing Azure Machine Learning workspace using Azure Machine Learning CLI v2, or with `ARMClient`.
