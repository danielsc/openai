A multi-regional deployment relies on creation of Azure Machine Learning and other resources (infrastructure) in two Azure regions. If a regional outage occurs, you can switch to the other region. When planning on where to deploy your resources, consider:

* __Regional availability__: Use regions that are close to your users. To check regional availability for Azure Machine Learning, see [Azure products by region](https://azure.microsoft.com/global-infrastructure/services/).
* __Azure paired regions__: Paired regions coordinate platform updates and prioritize recovery efforts where needed. For more information, see [Azure paired regions](../availability-zones/cross-region-replication-azure.md).
* __Service availability__: Decide whether the resources used by your solution should be hot/hot, hot/warm, or hot/cold.
    
    * __Hot/hot__: Both regions are active at the same time, with one region ready to begin use immediately.
    * __Hot/warm__: Primary region active, secondary region has critical resources (for example, deployed models) ready to start. Non-critical resources would need to be manually deployed in the secondary region.
    * __Hot/cold__: Primary region active, secondary region has Azure Machine Learning and other resources deployed, along with needed data. Resources such as models, model deployments, or pipelines would need to be manually deployed.

> [!TIP]
> Depending on your business requirements, you may decide to treat different Azure Machine Learning resources differently. For example, you may want to use hot/hot for deployed models (inference), and hot/cold for experiments (training).

Azure Machine Learning builds on top of other services. Some services can be configured to replicate to other regions. Others you must manually create in multiple regions. The following table provides a list of services, who is responsible for replication, and an overview of the configuration:

| Azure service | Geo-replicated by | Configuration |
| ----- | ----- | ----- |
| Machine Learning workspace | You | Create a workspace in the selected regions. |
| Machine Learning compute | You | Create the compute resources in the selected regions. For compute resources that can dynamically scale, make sure that both regions provide sufficient compute quota for your needs. |
| Key Vault | Microsoft | Use the same Key Vault instance with the Azure Machine Learning workspace and resources in both regions. Key Vault automatically fails over to a secondary region. For more information, see [Azure Key Vault availability and redundancy](../key-vault/general/disaster-recovery-guidance.md).|
| Container Registry | Microsoft | Configure the Container Registry instance to geo-replicate registries to the paired region for Azure Machine Learning. Use the same instance for both workspace instances. For more information, see [Geo-replication in Azure Container Registry](../container-registry/container-registry-geo-replication.md). |
| Storage Account | You | Azure Machine Learning does not support __default storage-account__ failover using geo-redundant storage (GRS), geo-zone-redundant storage (GZRS), read-access geo-redundant storage (RA-GRS), or read-access geo-zone-redundant storage (RA-GZRS). Create a separate storage account for the default storage of each workspace. </br>Create separate storage accounts or services for other data storage. For more information, see [Azure Storage redundancy](../storage/common/storage-redundancy.md). |
| Application Insights | You | Create Application Insights for the workspace in both regions. To adjust the data-retention period and details, see [Data collection, retention, and storage in Application Insights](../azure-monitor/app/data-retention-privacy.md#how-long-is-the-data-kept). |

To enable fast recovery and restart in the secondary region, we recommend the following development practices:

* Use Azure Resource Manager templates. Templates are 'infrastructure-as-code', and allow you to quickly deploy services in both regions.
