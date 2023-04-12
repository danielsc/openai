For metrics that support dimensions, you can apply filters using a dimension value. For example, filtering **Active Cores** for a **Cluster Name** of `cpu-cluster`. 

You can also split a metric by dimension to visualize how different segments of the metric compare with each other. For example, splitting out the **Pipeline Step Type** to see a count of the types of steps used in the pipeline.

For more information of filtering and splitting, see [Advanced features of Azure Monitor](../azure-monitor/essentials/metrics-charts.md).

<a id="analyzing-log-data"></a>
## Analyzing logs

Using Azure Monitor Log Analytics requires you to create a diagnostic configuration and enable __Send information to Log Analytics__. For more information, see the [Collection and routing](#collection-and-routing) section.

Data in Azure Monitor Logs is stored in tables, with each table having its own set of unique properties. Azure Machine Learning stores data in the following tables:

| Table | Description |
|:---|:---|
| AmlComputeClusterEvent | Events from Azure Machine Learning compute clusters.|
| AmlComputeClusterNodeEvent (deprecated) | Events from nodes within an Azure Machine Learning compute cluster. |
| AmlComputeJobEvent | Events from jobs running on Azure Machine Learning compute. |
| AmlComputeInstanceEvent | Events when ML Compute Instance is accessed (read/write). Category includes:ComputeInstanceEvent (very chatty). |
| AmlDataLabelEvent | Events when data label(s) or its projects is accessed (read, created, or deleted). Category includes:DataLabelReadEvent,DataLabelChangeEvent.  |
| AmlDataSetEvent | Events when a registered or unregistered ML dataset is accessed (read, created, or deleted). Category includes:DataSetReadEvent,DataSetChangeEvent. |
| AmlDataStoreEvent | Events when ML datastore is accessed (read, created, or deleted). Category includes:DataStoreReadEvent,DataStoreChangeEvent. |
| AmlDeploymentEvent | Events when a model deployment happens on ACI or AKS. Category includes:DeploymentReadEvent,DeploymentEventACI,DeploymentEventAKS. |
| AmlInferencingEvent | Events for inference or related operation on AKS or ACI compute type. Category includes:InferencingOperationACI (very chatty),InferencingOperationAKS (very chatty). |
| AmlModelsEvent | Events when ML model is accessed (read, created, or deleted). Includes events when packaging of models and assets happen into ready-to-build packages. Category includes:ModelsReadEvent,ModelsActionEvent .|
| AmlPipelineEvent | Events when ML pipeline draft or endpoint or module are accessed (read, created, or deleted).Category includes:PipelineReadEvent,PipelineChangeEvent. |
| AmlRunEvent | Events when ML experiments are accessed (read, created, or deleted). Category includes:RunReadEvent,RunEvent. |
| AmlEnvironmentEvent | Events when ML environment configurations (read, created, or deleted). Category includes:EnvironmentReadEvent (very chatty),EnvironmentChangeEvent. |

> [!NOTE]
> Effective February 2022, the AmlComputeClusterNodeEvent table will be deprecated. We recommend that you instead use the AmlComputeClusterEvent table.

> [!IMPORTANT]
> When you select **Logs** from the Azure Machine Learning menu, Log Analytics is opened with the query scope set to the current workspace. This means that log queries will only include data from that resource. If you want to run a query that includes data from other databases or data from other Azure services, select **Logs** from the **Azure Monitor** menu. See [Log query scope and time range in Azure Monitor Log Analytics](../azure-monitor/logs/scope.md) for details.

For a detailed reference of the logs and metrics, see [Azure Machine Learning monitoring data reference](monitor-resource-reference.md).

### Sample Kusto queries

> [!IMPORTANT]
> When you select **Logs** from the [service-name] menu, Log Analytics is opened with the query scope set to the current Azure Machine Learning workspace. This means that log queries will only include data from that resource. If you want to run a query that includes data from other workspaces or data from other Azure services, select **Logs** from the **Azure Monitor** menu. See [Log query scope and time range in Azure Monitor Log Analytics](../azure-monitor/logs/scope.md) for details.
