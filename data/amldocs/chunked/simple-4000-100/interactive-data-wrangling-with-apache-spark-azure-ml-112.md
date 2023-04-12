Azure Machine Learning offers Managed (Automatic) Spark compute, and [attached Synapse Spark pool](./how-to-manage-synapse-spark-pool.md), for interactive data wrangling with Apache Spark, in Azure Machine Learning Notebooks. The Managed (Automatic) Spark compute does not require creation of resources in the Azure Synapse workspace. Instead, a fully managed automatic Spark compute becomes directly available in the Azure Machine Learning Notebooks. Using a Managed (Automatic) Spark compute is the easiest approach to access a Spark cluster in Azure Machine Learning.

### Managed (Automatic) Spark compute in Azure Machine Learning Notebooks

A Managed (Automatic) Spark compute is available in Azure Machine Learning Notebooks by default. To access it in a notebook, select **AzureML Spark Compute** under **Azure Machine Learning Spark** from the **Compute** selection menu.

:::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/select-azure-ml-spark-compute.png" alt-text="Screenshot highlighting the selected Azure Machine Learning Spark option at the Compute selection menu.":::

The Notebooks UI also provides options for Spark session configuration, for the Managed (Automatic) Spark compute. To configure a Spark session:

1. Select **Configure session** at the bottom of the screen.
1. Select a version of **Apache Spark** from the dropdown menu.
1. Select **Instance type** from the dropdown menu. The following instance types are currently supported:
    - `Standard_E4s_v3`
    - `Standard_E8s_v3`
    - `Standard_E16s_v3`
    - `Standard_E32s_v3`
    - `Standard_E64s_v3`
1. Input a Spark **Session timeout** value, in minutes.
1. Select the number of **Executors** for the Spark session.
1. Select **Executor size** from the dropdown menu.
1. Select **Driver size** from the dropdown menu.
1. To use a conda file to configure a Spark session, check the **Upload conda file** checkbox. Then, select **Browse**, and choose the conda file with the Spark session configuration you want.
1. Add **Configuration settings** properties, input values in the **Property** and **Value** textboxes, and select **Add**.
1. Select **Apply**.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/azure-ml-session-configuration.png" alt-text="Screenshot showing the Spark session configuration options.":::

1. Select **Stop now** in the **Stop current session** pop-up.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/stop-current-session.png" alt-text="Screenshot showing the stop current session dialog box.":::

The session configuration changes will persist and will become available to another notebook session that is started using the Managed (Automatic) Spark compute.

### Import and wrangle data from Azure Data Lake Storage (ADLS) Gen 2

You can access and wrangle data stored in Azure Data Lake Storage (ADLS) Gen 2 storage accounts with `abfss://` data URIs following one of the two data access mechanisms:

- User identity passthrough
- Service principal-based data access

> [!TIP]
> Data wrangling with a Managed (Automatic) Spark compute, and user identity passthrough to access data in Azure Data Lake Storage (ADLS) Gen 2 storage account requires the least number of configuration steps.

To start interactive data wrangling with the user identity passthrough:

- Verify that the user identity has **Contributor** and **Storage Blob Data Contributor** [role assignments](#add-role-assignments-in-azure-storage-accounts) in the Azure Data Lake Storage (ADLS) Gen 2 storage account.

- To use the Managed (Automatic) Spark compute, select **AzureML Spark Compute**, under **Azure Machine Learning Spark**, from the **Compute** selection menu.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/select-azure-machine-learning-spark.png" alt-text="Screenshot showing use of a Managed (Automatic) Spark compute.":::
