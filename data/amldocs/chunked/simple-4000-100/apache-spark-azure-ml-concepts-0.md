
# Apache Spark in Azure Machine Learning (preview)

Azure Machine Learning integration with Azure Synapse Analytics (preview) provides easy access to distributed computation resources through the Apache Spark framework. This integration offers these Apache Spark computing experiences:

- Managed (Automatic) Spark compute
- Attached Synapse Spark pool

## Managed (Automatic) Spark compute

With the Apache Spark framework, Azure Machine Learning Managed (Automatic) Spark compute is the easiest way to accomplish distributed computing tasks in the Azure Machine Learning environment. Azure Machine Learning offers a fully managed, serverless, on-demand Apache Spark compute cluster. Its users can avoid the need to create an Azure Synapse workspace and a Synapse Spark pool.

Users can define resources, including instance type and Apache Spark runtime version. They can then use those resources to access Managed (Automatic) Spark compute in Azure Machine Learning notebooks for:

- [Interactive Spark code development](./interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Spark batch job submissions](./how-to-submit-spark-jobs.md)
- [Running machine learning pipelines with a Spark component](./how-to-submit-spark-jobs.md#spark-component-in-a-pipeline-job)

### Points to consider

Managed (Automatic) Spark compute works well for most user scenarios that require quick access to distributed computing through Apache Spark. However, to make an informed decision, users should consider the advantages and disadvantages of this approach.

Advantages:
  
- No dependencies on other Azure resources to be created for Apache Spark (Azure Synapse infrastructure operates under the hood).
- No required subscription permissions to create Azure Synapse-related resources.
- No need for SQL pool quotas.

Disadvantages:

- A persistent Hive metastore is missing. Managed (Automatic) Spark compute supports only in-memory Spark SQL.
- No available tables or databases.
- Missing Azure Purview integration.
- No available linked services.
- Fewer data sources and connectors.
- No pool-level configuration.
- No pool-level library management.
- Only partial support for `mssparkutils`.

### Network configuration

As of January 2023, creation of a Managed (Automatic) Spark compute, inside a virtual network, and creation of a private endpoint to Azure Synapse, aren't supported.

### Inactivity periods and tear-down mechanism

At first launch, Managed (Automatic) Spark compute (*cold start*) resource might need three to five minutes to start the Spark session itself. The automated Managed (Automatic) Spark compute provisioning, backed by Azure Synapse, causes this delay. After the Managed (Automatic) Spark compute is provisioned, and an Apache Spark session starts, subsequent code executions (*warm start*) won't experience this delay.

The Spark session configuration offers an option that defines a session timeout (in minutes). The Spark session will end after an inactivity period that exceeds the user-defined timeout. If another Spark session doesn't start in the following ten minutes, resources provisioned for the Managed (Automatic) Spark compute will be torn down.

After the Managed (Automatic) Spark compute resource tear-down happens, submission of the next job will require a *cold start*. The next visualization shows some session inactivity period and cluster teardown scenarios.

:::image type="content" source="./media/apache-spark-azure-ml-concepts/spark-session-timeout-teardown.png" lightbox="./media/apache-spark-azure-ml-concepts/spark-session-timeout-teardown.png" alt-text="Expandable diagram that shows scenarios for Apache Spark session inactivity period and cluster teardown.":::

> [!NOTE]
> For a session-level conda package:
> - *Cold start* time will need about ten to fifteen minutes.
> - *Warm start* time using same conda package will need about one minute.
> - *Warm start* with a different conda package will also need about ten to fifteen minutes.
