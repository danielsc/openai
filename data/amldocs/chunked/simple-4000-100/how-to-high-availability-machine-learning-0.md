
# Failover for business continuity and disaster recovery

To maximize your uptime, plan ahead to maintain business continuity and prepare for disaster recovery with Azure Machine Learning. 

Microsoft strives to ensure that Azure services are always available. However, unplanned service outages may occur. We recommend having a disaster recovery plan in place for handling regional service outages. In this article, you'll learn how to:

* Plan for a multi-regional deployment of Azure Machine Learning and associated resources.
* Maximize chances to recover logs, notebooks, docker images, and other metadata.
* Design for high availability of your solution.
* Initiate a failover to another region.

> [!IMPORTANT]
> Azure Machine Learning itself does not provide automatic failover or disaster recovery. Backup and restore of workspace metadata such as run history is unavailable.

In case you have accidentally deleted your workspace or corresponding components, this article also provides you with currently supported recovery options.

## Understand Azure services for Azure Machine Learning

Azure Machine Learning depends on multiple Azure services. Some of these services are provisioned in your subscription. You're responsible for the high-availability configuration of these services. Other services are created in a Microsoft subscription and are managed by Microsoft. 

Azure services include:

* **Azure Machine Learning infrastructure**: A Microsoft-managed environment for the Azure Machine Learning workspace.

* **Associated resources**: Resources provisioned in your subscription during Azure Machine Learning workspace creation. These resources include Azure Storage, Azure Key Vault, Azure Container Registry, and Application Insights.
  * Default storage has data such as model, training log data, and dataset.
  * Key Vault has credentials for Azure Storage, Container Registry, and data stores.
  * Container Registry has a Docker image for training and inferencing environments.
  * Application Insights is for monitoring Azure Machine Learning.

* **Compute resources**: Resources you create after workspace deployment. For example, you might create a compute instance or compute cluster to train a Machine Learning model.
  * Compute instance and compute cluster: Microsoft-managed model development environments.
  * Other resources: Microsoft computing resources that you can attach to Azure Machine Learning, such as Azure Kubernetes Service (AKS), Azure Databricks, Azure Container Instances, and Azure HDInsight. You're responsible for configuring high-availability settings for these resources.

* **Other data stores**: Azure Machine Learning can mount other data stores such as Azure Storage, Azure Data Lake Storage, and Azure SQL Database for training data.  These data stores are provisioned within your subscription. You're responsible for configuring their high-availability settings.

The following table shows the Azure services are managed by Microsoft and which are managed by you. It also indicates the services that are highly available by default.

| Service | Managed by | High availability by default |
| ----- | ----- | ----- |
| **Azure Machine Learning infrastructure** | Microsoft | |
| **Associated resources** |
| Azure Storage | You | |
| Key Vault | You | ✓ |
| Container Registry | You | |
| Application Insights | You | NA |
| **Compute resources** |
| Compute instance | Microsoft |  |
| Compute cluster | Microsoft |  |
| Other compute resources such as AKS, <br>Azure Databricks, Container Instances, HDInsight | You |  |
| **Other data stores** such as Azure Storage, SQL Database,<br> Azure Database for PostgreSQL, Azure Database for MySQL, <br>Azure Databricks File System | You | |

The rest of this article describes the actions you need to take to make each of these services highly available.

## Plan for multi-regional deployment

A multi-regional deployment relies on creation of Azure Machine Learning and other resources (infrastructure) in two Azure regions. If a regional outage occurs, you can switch to the other region. When planning on where to deploy your resources, consider:
