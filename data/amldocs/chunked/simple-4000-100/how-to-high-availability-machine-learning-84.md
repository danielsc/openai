* Use Azure Resource Manager templates. Templates are 'infrastructure-as-code', and allow you to quickly deploy services in both regions.
* To avoid drift between the two regions, update your continuous integration and deployment pipelines to deploy to both regions.
* When automating deployments, include the configuration of workspace attached compute resources such as Azure Kubernetes Service.
* Create role assignments for users in both regions.
* Create network resources such as Azure Virtual Networks and private endpoints for both regions. Make sure that users have access to both network environments. For example, VPN and DNS configurations for both virtual networks.

### Compute and data services

Depending on your needs, you may have more compute or data services that are used by Azure Machine Learning. For example, you may use Azure Kubernetes Services or Azure SQL Database. Use the following information to learn how to configure these services for high availability.

__Compute resources__

* **Azure Kubernetes Service**: See [Best practices for business continuity and disaster recovery in Azure Kubernetes Service (AKS)](../aks/operator-best-practices-multi-region.md) and [Create an Azure Kubernetes Service (AKS) cluster that uses availability zones](../aks/availability-zones.md). If the AKS cluster was created by using the Azure Machine Learning Studio, SDK, or CLI, cross-region high availability is not supported.
* **Azure Databricks**: See [Regional disaster recovery for Azure Databricks clusters](/azure/databricks/scenarios/howto-regional-disaster-recovery).
* **Container Instances**: An orchestrator is responsible for failover. See [Azure Container Instances and container orchestrators](../container-instances/container-instances-orchestrator-relationship.md).
* **HDInsight**: See [High availability services supported by Azure HDInsight](../hdinsight/hdinsight-high-availability-components.md).

__Data services__

* **Azure Blob container / Azure Files / Data Lake Storage Gen2**: See [Azure Storage redundancy](../storage/common/storage-redundancy.md).
* **Data Lake Storage Gen1**: See [High availability and disaster recovery guidance for Data Lake Storage Gen1](../data-lake-store/data-lake-store-disaster-recovery-guidance.md).
* **SQL Database**: See [High availability for Azure SQL Database and SQL Managed Instance](/azure/azure-sql/database/high-availability-sla).
* **Azure Database for PostgreSQL**: See [High availability concepts in Azure Database for PostgreSQL - Single Server](../postgresql/concepts-high-availability.md).
* **Azure Database for MySQL**: See [Understand business continuity in Azure Database for MySQL](../mysql/concepts-business-continuity.md).
* **Azure Databricks File System**: See [Regional disaster recovery for Azure Databricks clusters](/azure/databricks/scenarios/howto-regional-disaster-recovery).

> [!TIP]
> If you provide your own customer-managed key to deploy an Azure Machine Learning workspace, Azure Cosmos DB is also provisioned within your subscription. In that case, you're responsible for configuring its high-availability settings. See [High availability with Azure Cosmos DB](../cosmos-db/high-availability.md).

## Design for high availability

### Deploy critical components to multiple regions

Determine the level of business continuity that you are aiming for. The level may differ between the components of your solution. For example, you may want to have a hot/hot configuration for production pipelines or model deployments, and hot/cold for experimentation.

### Manage training data on isolated storage

By keeping your data storage isolated from the default storage the workspace uses for logs, you can:

* Attach the same storage instances as datastores to the primary and secondary workspaces.
* Make use of geo-replication for data storage accounts and maximize your uptime.

### Manage machine learning assets as code

> [!NOTE]
> Backup and restore of workspace metadata such as run history, models and environments is unavailable. Specifying assets and configurations as code using YAML specs, will help you re-recreate assets across workspaces in case of a disaster.
