
# Attach and manage a Synapse Spark pool in Azure Machine Learning (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

In this article, you will learn how to attach a [Synapse Spark Pool](../synapse-analytics/spark/apache-spark-concepts.md#spark-pools) in Azure Machine Learning. You can attach a Synapse Spark Pool in Azure Machine Learning in one of these ways:

- Using Azure Machine Learning studio UI
- Using Azure Machine Learning CLI
- Using Azure Machine Learning Python SDK

## Prerequisites
# [Studio UI](#tab/studio-ui)
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- [Create an Azure Synapse Analytics workspace in Azure portal](../synapse-analytics/quickstart-create-workspace.md).
- [Create an Apache Spark pool using the Azure portal](../synapse-analytics/quickstart-create-apache-spark-pool-portal.md).
- To enable this feature:
  1. Navigate to Azure Machine Learning studio UI.
  2. Select **Manage preview features** (megaphone icon) among the icons on the top right side of the screen.
  3. In **Managed preview feature** panel, toggle on **Run notebooks and jobs on managed Spark** feature.
  :::image type="content" source="media/how-to-manage-synapse-spark-pool/how_to_enable_managed_spark_preview.png" alt-text="Screenshot showing option for enabling Managed Spark preview.":::

# [CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- [Create an Azure Synapse Analytics workspace in Azure portal](../synapse-analytics/quickstart-create-workspace.md).
- [Create an Apache Spark pool using the Azure portal](../synapse-analytics/quickstart-create-apache-spark-pool-portal.md).
- [Create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install Azure Machine Learning CLI](./how-to-configure-cli.md?tabs=public).

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
- An Azure subscription; if you don't have an Azure subscription, [create a free account](https://azure.microsoft.com/free) before you begin.
- An Azure Machine Learning workspace. See [Create workspace resources](./quickstart-create-resources.md).
- [Create an Azure Synapse Analytics workspace in Azure portal](../synapse-analytics/quickstart-create-workspace.md).
- [Create an Apache Spark pool using the Azure portal](../synapse-analytics/quickstart-create-apache-spark-pool-portal.md).
- [Configure your development environment](./how-to-configure-environment.md), or [create an Azure Machine Learning compute instance](./concept-compute-instance.md#create).
- [Install the Azure Machine Learning SDK for Python](/python/api/overview/azure/ai-ml-readme).


## Attach a Synapse Spark pool in Azure Machine Learning
Azure Machine Learning provides multiple options for attaching and managing a Synapse Spark pool.  

# [Studio UI](#tab/studio-ui)

To attach a Synapse Spark Pool using the Studio Compute tab: 

:::image type="content" source="media/how-to-manage-synapse-spark-pool/synapse_compute_synapse_spark_pool.png" alt-text="Screenshot showing creation of a new Synapse Spark Pool.":::

1. In the **Manage** section of the left pane, select **Compute**.
1. Select **Attached computes**.
1. On the **Attached computes** screen, select **New**, to see the options for attaching different types of computes.
1. Select **Synapse Spark pool (preview)**.

The **Attach Synapse Spark pool (preview)** panel will open on the right side of the screen. In this panel:

1. Enter a **Name**, which will refer to the attached Synapse Spark Pool inside the Azure Machine Learning.
