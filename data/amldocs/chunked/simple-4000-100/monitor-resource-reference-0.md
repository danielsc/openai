
# Monitoring Azure machine learning data reference

Learn about the data and resources collected by Azure Monitor from your Azure Machine Learning workspace. See [Monitoring Azure Machine Learning](monitor-azure-machine-learning.md) for details on collecting and analyzing monitoring data.

## Metrics

This section lists all the automatically collected platform metrics collected for Azure Machine Learning. The resource provider for these metrics is [Microsoft.MachineLearningServices/workspaces](../azure-monitor/essentials/metrics-supported.md#microsoftmachinelearningservicesworkspaces).

**Model**

| Metric | Unit | Description |
|--|--|--|
| Model Register Succeeded | Count | Number of model registrations that succeeded in this workspace |
| Model Register Failed | Count | Number of model registrations that failed in this workspace |
| Model Deploy Started | Count | Number of model deployments started in this workspace |
| Model Deploy Succeeded | Count | Number of model deployments that succeeded in this workspace |
| Model Deploy Failed | Count | Number of model deployments that failed in this workspace |

**Quota**

Quota information is for Azure Machine Learning compute only.

| Metric | Unit | Description |
|--|--|--|
| Total Nodes | Count | Number of total nodes. This total includes some of Active Nodes, Idle Nodes, Unusable Nodes, Preempted Nodes, Leaving Nodes |
| Active Nodes | Count | Number of Active nodes. The nodes that are actively running a job. |
| Idle Nodes | Count | Number of idle nodes. Idle nodes are the nodes that are not running any jobs but can accept new job if available. |
| Unusable Nodes | Count | Number of unusable nodes. Unusable nodes are not functional due to some unresolvable issue. Azure will recycle these nodes. |
| Preempted Nodes | Count | Number of preempted nodes. These nodes are the low-priority nodes that are taken away from the available node pool. |
| Leaving Nodes | Count | Number of leaving nodes. Leaving nodes are the nodes that just finished processing a job and will go to Idle state. |
| Total Cores | Count | Number of total cores |
| Active Cores | Count | Number of active cores |
| Idle Cores | Count | Number of idle cores |
| Unusable Cores | Count | Number of unusable cores |
| Preempted Cores | Count | Number of preempted cores |
| Leaving Cores | Count | Number of leaving cores |
| Quota Utilization Percentage | Count | Percent of quota utilized |

**Resource**

| Metric| Unit | Description |
|--|--|--|
| CpuUtilization | Count | Percentage of utilization on a CPU node. Utilization is reported at one-minute intervals. |
| GpuUtilization | Count | Percentage of utilization on a GPU node. Utilization is reported at one-minute intervals. |
| GpuMemoryUtilization | Count | Percentage of memory utilization on a GPU node. Utilization is reported at one-minute intervals. |
| GpuEnergyJoules | Count | Interval energy in Joules on a GPU node. Energy is reported at one-minute intervals. |

**Run**

Information on training runs for the workspace.

| Metric | Unit | Description |
|--|--|--|
| Cancelled Runs | Count | Number of runs canceled for this workspace. Count is updated when a run is successfully canceled. |
| Cancel Requested Runs | Count | Number of runs where cancel was requested for this workspace. Count is updated when cancellation request has been received for a run. |
| Completed Runs | Count | Number of runs completed successfully for this workspace. Count is updated when a run has completed and output has been collected. |
| Failed Runs | Count | Number of runs failed for this workspace. Count is updated when a run fails. |
| Finalizing Runs | Count | Number of runs entered finalizing state for this workspace. Count is updated when a run has completed but output collection still in progress. | 
| Not Responding Runs | Count | Number of runs not responding for this workspace. Count is updated when a run enters Not Responding state. |
| Not Started Runs | Count | Number of runs in Not Started state for this workspace. Count is updated when a request is received to create a run but run information has not yet been populated. |
