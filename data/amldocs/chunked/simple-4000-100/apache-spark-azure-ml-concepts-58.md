> - *Warm start* time using same conda package will need about one minute.
> - *Warm start* with a different conda package will also need about ten to fifteen minutes.

## Attached Synapse Spark pool

A Spark pool created in an Azure Synapse workspace becomes available in the Azure Machine Learning workspace with the attached Synapse Spark pool. This option might be suitable for users who want to reuse an existing Synapse Spark pool.

Attachment of a Synapse Spark pool to an Azure Machine Learning workspace requires [other steps](./how-to-manage-synapse-spark-pool.md) before you can use the pool in Azure Machine Learning for:

- [Interactive Spark code development](./interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Spark batch job submission](./how-to-submit-spark-jobs.md)
- [Running machine learning pipelines with a Spark component](./how-to-submit-spark-jobs.md#spark-component-in-a-pipeline-job)

An attached Synapse Spark pool provides access to native Azure Synapse features. The user is responsible for the Synapse Spark pool provisioning, attaching, configuration, and management.

The Spark session configuration for an attached Synapse Spark pool also offers an option to define a session timeout (in minutes). The session timeout behavior resembles the description in [the previous section](#inactivity-periods-and-tear-down-mechanism), except that the associated resources are never torn down after the session timeout.

## Defining Spark cluster size

You can define Spark cluster size with three parameter values in Azure Machine Learning Spark jobs:

- Number of executors
- Executor cores
- Executor memory

You should consider an Azure Machine Learning Apache Spark executor as an equivalent of Azure Spark worker nodes. An example can explain these parameters. Let's say that you defined the number of executors as 6 (equivalent to six worker nodes), executor cores as 4, and executor memory as 28 GB. Your Spark job then has access to a cluster with 24 cores and 168 GB of memory.

## Ensuring resource access for Spark jobs

To access data and other resources, a Spark job can use either a user identity passthrough or a managed identity. This table summarizes the mechanisms that Spark jobs use to access resources.

|Spark pool|Supported identities|Default identity|
| ---------- | -------------------- | ---------------- |
|Managed (Automatic) Spark compute|User identity and managed identity|User identity|
|Attached Synapse Spark pool|User identity and managed identity|Managed identity - compute identity of the attached Synapse Spark pool|

[This article](./how-to-submit-spark-jobs.md#ensuring-resource-access-for-spark-jobs) describes resource access for Spark jobs. In a notebook session, both the Managed (Automatic) Spark compute and the attached Synapse Spark pool use user identity passthrough for data access during [interactive data wrangling](./interactive-data-wrangling-with-apache-spark-azure-ml.md).

> [!NOTE]
> - To ensure successful Spark job execution, assign **Contributor** and **Storage Blob Data Contributor** roles (on the Azure storage account used for data input and output) to the identity that's used for submitting the Spark job.
> - If an [attached Synapse Spark pool](./how-to-manage-synapse-spark-pool.md) points to a Synapse Spark pool in an Azure Synapse workspace, and that workspace has an associated managed virtual network, [configure a managed private endpoint to a storage account](../synapse-analytics/security/connect-to-a-secure-storage-account.md). This configuration will help ensure data access.
> - Both Managed (Automatic) Spark compute and attached Synapse Spark pool do not work in a notebook created in a private link enabled workspace.

[This quickstart](./quickstart-spark-data-wrangling.md) describes how to start using Managed (Automatic) Spark compute in Azure Machine Learning.

## Next steps

- [Quickstart: Submit Apache Spark jobs in Azure Machine Learning (preview)](./quickstart-spark-jobs.md)
