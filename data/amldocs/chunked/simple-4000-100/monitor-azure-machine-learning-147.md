> When you select **Logs** from the [service-name] menu, Log Analytics is opened with the query scope set to the current Azure Machine Learning workspace. This means that log queries will only include data from that resource. If you want to run a query that includes data from other workspaces or data from other Azure services, select **Logs** from the **Azure Monitor** menu. See [Log query scope and time range in Azure Monitor Log Analytics](../azure-monitor/logs/scope.md) for details.

Following are queries that you can use to help you monitor your Azure Machine Learning resources: 

+ Get failed jobs in the last five days:

    ```Kusto
    AmlComputeJobEvent
    | where TimeGenerated > ago(5d) and EventType == "JobFailed"
    | project  TimeGenerated , ClusterId , EventType , ExecutionState , ToolType
    ```

+ Get records for a specific job name:

    ```Kusto
    AmlComputeJobEvent
    | where JobName == "automl_a9940991-dedb-4262-9763-2fd08b79d8fb_setup"
    | project  TimeGenerated , ClusterId , EventType , ExecutionState , ToolType
    ```

+ Get cluster events in the last five days for clusters where the VM size is Standard_D1_V2:

    ```Kusto
    AmlComputeClusterEvent
    | where TimeGenerated > ago(4d) and VmSize == "STANDARD_D1_V2"
    | project  ClusterName , InitialNodeCount , MaximumNodeCount , QuotaAllocated , QuotaUtilized
    ```

+ Get the cluster node allocations in the last eight days::

    ```Kusto
    AmlComputeClusterEvent
    | where TimeGenerated > ago(8d) and TargetNodeCount  > CurrentNodeCount
    | project TimeGenerated, ClusterName, CurrentNodeCount, TargetNodeCount
    ```

When you connect multiple Azure Machine Learning workspaces to the same Log Analytics workspace, you can query across all resources. 

+ Get number of running nodes across workspaces and clusters in the last day:

    ```Kusto
    AmlComputeClusterEvent
    | where TimeGenerated > ago(1d)
    | summarize avgRunningNodes=avg(TargetNodeCount), maxRunningNodes=max(TargetNodeCount)
             by Workspace=tostring(split(_ResourceId, "/")[8]), ClusterName, ClusterType, VmSize, VmPriority
    ```

### Create a workspace monitoring dashboard by using a template

A dashboard is a focused and organized view of your cloud resources in the Azure portal. For more information about creating dashboards, see [Create, view, and manage metric alerts using Azure Monitor](../azure-portal/azure-portal-dashboards.md).

To deploy a sample dashboard, you can use a publicly available [template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-monitoring-dashboard). The sample dashboard is based on [Kusto queries](../machine-learning/monitor-azure-machine-learning.md#sample-kusto-queries), so you must enable [Log Analytics data collection](../machine-learning/monitor-azure-machine-learning.md#collection-and-routing) for your Azure Machine Learning workspace before you deploy the dashboard.

## Alerts

You can access alerts for Azure Machine Learning by opening **Alerts** from the **Azure Monitor** menu. See [Create, view, and manage metric alerts using Azure Monitor](../azure-monitor/alerts/alerts-metric.md) for details on creating alerts.

The following table lists common and recommended metric alert rules for Azure Machine Learning:

| Alert type | Condition | Description |
|:---|:---|:---|
| Model Deploy Failed | Aggregation type: Total, Operator: Greater than, Threshold value: 0 | When one or more model deployments have failed |
| Quota Utilization Percentage | Aggregation type: Average, Operator: Greater than, Threshold value: 90| When the quota utilization percentage is greater than 90% |
| Unusable Nodes | Aggregation type: Total, Operator: Greater than, Threshold value: 0 | When there are one or more unusable nodes |

## Next steps

- For a reference of the logs and metrics, see [Monitoring Azure Machine Learning data reference](monitor-resource-reference.md).
