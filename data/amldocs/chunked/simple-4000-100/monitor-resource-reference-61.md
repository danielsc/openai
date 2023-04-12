| Not Started Runs | Count | Number of runs in Not Started state for this workspace. Count is updated when a request is received to create a run but run information has not yet been populated. |
| Preparing Runs | Count | Number of runs that are preparing for this workspace. Count is updated when a run enters Preparing state while the run environment is being prepared. |
| Provisioning Runs | Count | Number of runs that are provisioning for this workspace. Count is updated when a run is waiting on compute target creation or provisioning. |
| Queued Runs | Count | Number of runs that are queued for this workspace. Count is updated when a run is queued in compute target. Can occur when waiting for required compute nodes to be ready. |
| Started Runs | Count | Number of runs running for this workspace. Count is updated when run starts running on required resources. |
| Starting Runs | Count | Number of runs started for this workspace. Count is updated after request to create run and run info, such as the Run ID, has been populated |
| Errors | Count | Number of run errors in this workspace. Count is updated whenever run encounters an error. |
| Warnings | Count | Number of run warnings in this workspace. Count is updated whenever a run encounters a warning. |

## Metric dimensions

For more information on what metric dimensions are, see [Multi-dimensional metrics](../azure-monitor/essentials/data-platform-metrics.md#multi-dimensional-metrics).

Azure Machine Learning has the following dimensions associated with its metrics.

| Dimension | Description |
| ---- | ---- |
| Cluster Name | The name of the compute cluster resource. Available for all quota metrics. |
| Vm Family Name | The name of the VM family used by the cluster. Available for quota utilization percentage. |
| Vm Priority | The priority of the VM. Available for quota utilization percentage.
| CreatedTime | Only available for CpuUtilization and GpuUtilization. |
| DeviceId | ID of the device (GPU). Only available for GpuUtilization. |
| NodeId | ID of the node created where job is running. Only available for CpuUtilization and GpuUtilization. |
| RunId | ID of the run/job. Only available for CpuUtilization and GpuUtilization. |
| ComputeType | The compute type that the run used. Only available for Completed runs, Failed runs, and Started runs. |
| PipelineStepType | The type of [PipelineStep](/python/api/azureml-pipeline-core/azureml.pipeline.core.pipelinestep) used in the run. Only available for Completed runs, Failed runs, and Started runs. |
| PublishedPipelineId | The ID of the published pipeline used in the run. Only available for Completed runs, Failed runs, and Started runs. |
| RunType | The type of run. Only available for Completed runs, Failed runs, and Started runs. |

The valid values for the RunType dimension are:

| Value | Description |
| ----- | ----- |
| Experiment | Non-pipeline runs. |
| PipelineRun | A pipeline run, which is the parent of a StepRun. |
| StepRun | A run for a pipeline step. |
| ReusedStepRun | A run for a pipeline step that reuses a previous run. |

## Activity log

The following table lists the operations related to Azure Machine Learning that may be created in the Activity log.

| Operation | Description |
|:---|:---|
| Creates or updates a Machine Learning workspace | A workspace was created or updated |
| CheckComputeNameAvailability | Check if a compute name is already in use |
| Creates or updates the compute resources | A compute resource was created or updated |
| Deletes the compute resources | A compute resource was deleted |
| List secrets | On operation listed secrets for a Machine Learning workspace |

## Resource logs

This section lists the types of resource logs you can collect for Azure Machine Learning workspace.

Resource Provider and Type: [Microsoft.MachineLearningServices/workspace](../azure-monitor/essentials/resource-logs-categories.md#microsoftmachinelearningservicesworkspaces).

| Category | Display Name |
| ----- | ----- |
