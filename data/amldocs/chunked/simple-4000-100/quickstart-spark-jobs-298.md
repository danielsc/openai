        1. For **Executor size**:
            1. Enter the number of executor **Cores** as 2 and executor **Memory (GB)** as 2.
            2. For **Dynamically allocated executors**, select **Disabled**.
            3. Enter the number of **Executor instances** as 2.
        2. For **Driver size**, enter number of driver **Cores** as 1 and driver **Memory (GB)** as 2.
    6. Select **Next**.
6. On the **Review** screen:
    1. Review the job specification before submitting it.
    2. Select **Create** to submit the standalone Spark job.

> [!NOTE]
> A standalone job submitted from the Studio UI using an Azure Machine Learning Managed (Automatic) Spark compute defaults to user identity passthrough for data access.



> [!TIP]
> You might have an existing Synapse Spark pool in your Azure Synapse workspace. To use an existing Synapse Spark pool, please follow the instructions to [attach a Synapse Spark pool in Azure Machine Learning workspace](./how-to-manage-synapse-spark-pool.md).

## Next steps
- [Apache Spark in Azure Machine Learning (preview)](./apache-spark-azure-ml-concepts.md)
- [Quickstart: Interactive Data Wrangling with Apache Spark (preview)](./quickstart-spark-data-wrangling.md)
- [Attach and manage a Synapse Spark pool in Azure Machine Learning (preview)](./how-to-manage-synapse-spark-pool.md)
- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](./interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Submit Spark jobs in Azure Machine Learning (preview)](./how-to-submit-spark-jobs.md)
- [Code samples for Spark jobs using Azure Machine Learning CLI](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/spark)
- [Code samples for Spark jobs using Azure Machine Learning Python SDK](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/spark)
