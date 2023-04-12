> Enabling these settings requires additional Azure services (storage account, event hub, or Log Analytics), which may increase your cost. To calculate an estimated cost, visit the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator).

You can configure the following logs for Azure Machine Learning:

| Category | Description |
|:---|:---|
| AmlComputeClusterEvent | Events from Azure Machine Learning compute clusters. |
| AmlComputeClusterNodeEvent (deprecated) | Events from nodes within an Azure Machine Learning compute cluster. |
| AmlComputeJobEvent | Events from jobs running on Azure Machine Learning compute. |
| AmlComputeCpuGpuUtilization | ML services compute CPU and GPU utilization logs. |
| AmlRunStatusChangedEvent | ML run status changes. |
| ModelsChangeEvent | Events when ML model is accessed created or deleted. |
| ModelsReadEvent | Events when ML model is read. |
| ModelsActionEvent | Events when ML model is accessed. |
| DeploymentReadEvent | Events when a model deployment is read. |
| DeploymentEventACI | Events when a model deployment happens on ACI (very chatty). |
| DeploymentEventAKS | Events when a model deployment happens on AKS (very chatty). |
| InferencingOperationAKS | Events for inference or related operation on AKS compute type. |
| InferencingOperationACI | Events for inference or related operation on ACI compute type. |
| EnvironmentChangeEvent | Events when ML environment configurations are created or deleted. |
| EnvironmentReadEvent | Events when ML environment configurations are read (very chatty). |
| DataLabelChangeEvent | Events when data label(s) or its projects is created or deleted.  |
| DataLabelReadEvent | Events when data label(s) or its projects is read.  |
| ComputeInstanceEvent | Events when ML Compute Instance is accessed (very chatty). |
| DataStoreChangeEvent | Events when ML datastore is created or deleted. |
| DataStoreReadEvent | Events when ML datastore is read. |
| DataSetChangeEvent | Events when ML datastore is created or deleted. |
| DataSetReadEvent | Events when ML datastore is read.  |
| PipelineChangeEvent | Events when ML pipeline draft or endpoint or module are created or deleted.  |
| PipelineReadEvent | Events when ML pipeline draft or endpoint or module are read.  |
| RunEvent | Events when ML experiments are created or deleted. |
| RunReadEvent | Events when ML experiments are read. |

> [!NOTE]
> Effective February 2022, the AmlComputeClusterNodeEvent category will be deprecated. We recommend that you instead use the AmlComputeClusterEvent category.

> [!NOTE]
> When you enable metrics in a diagnostic setting, dimension information is not currently included as part of the information sent to a storage account, event hub, or log analytics.

The metrics and logs you can collect are discussed in the following sections.

## Analyzing metrics

You can analyze metrics for Azure Machine Learning, along with metrics from other Azure services, by opening **Metrics** from the **Azure Monitor** menu. See [Getting started with Azure Metrics Explorer](../azure-monitor/essentials/metrics-getting-started.md) for details on using this tool.

For a list of the platform metrics collected, see [Monitoring Azure Machine Learning data reference metrics](monitor-resource-reference.md#metrics).

All metrics for Azure Machine Learning are in the namespace **Machine Learning Service Workspace**.

![Metrics Explorer with Machine Learning Service Workspace selected](./media/monitor-azure-machine-learning/metrics.png)

For reference, you can see a list of [all resource metrics supported in Azure Monitor](../azure-monitor/essentials/metrics-supported.md).

> [!TIP]
> Azure Monitor metrics data is available for 90 days. However, when creating charts only 30 days can be visualized. For example, if you want to visualize a 90 day period, you must break it into three charts of 30 days within the 90 day period.
### Filtering and splitting

For metrics that support dimensions, you can apply filters using a dimension value. For example, filtering **Active Cores** for a **Cluster Name** of `cpu-cluster`. 
