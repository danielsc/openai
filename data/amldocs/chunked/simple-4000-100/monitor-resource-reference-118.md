Resource Provider and Type: [Microsoft.MachineLearningServices/workspace](../azure-monitor/essentials/resource-logs-categories.md#microsoftmachinelearningservicesworkspaces).

| Category | Display Name |
| ----- | ----- |
| AmlComputeClusterEvent | AmlComputeClusterEvent |
| AmlComputeClusterNodeEvent (deprecated) | AmlComputeClusterNodeEvent |
| AmlComputeCpuGpuUtilization | AmlComputeCpuGpuUtilization |
| AmlComputeJobEvent | AmlComputeJobEvent |
| AmlRunStatusChangedEvent | AmlRunStatusChangedEvent |
| ModelsChangeEvent | ModelsChangeEvent |
| ModelsReadEvent | ModelsReadEvent |
| ModelsActionEvent | ModelsActionEvent |
| DeploymentReadEvent | DeploymentReadEvent |
| DeploymentEventACI | DeploymentEventACI |
| DeploymentEventAKS | DeploymentEventAKS |
| InferencingOperationAKS | InferencingOperationAKS |
| InferencingOperationACI | InferencingOperationACI |
| EnvironmentChangeEvent | EnvironmentChangeEvent |
| EnvironmentReadEvent | EnvironmentReadEvent |
| DataLabelChangeEvent | DataLabelChangeEvent |
| DataLabelReadEvent | DataLabelReadEvent |
| ComputeInstanceEvent | ComputeInstanceEvent |
| DataStoreChangeEvent | DataStoreChangeEvent |
| DataStoreReadEvent | DataStoreReadEvent |
| DataSetChangeEvent | DataSetChangeEvent |
| DataSetReadEvent | DataSetReadEvent |
| PipelineChangeEvent | PipelineChangeEvent |
| PipelineReadEvent | PipelineReadEvent |
| RunEvent | RunEvent |
| RunReadEvent | RunReadEvent |


## Schemas

The following schemas are in use by Azure Machine Learning

### AmlComputeJobEvent table

| Property | Description |
|:--- |:---|
| TimeGenerated | Time when the log entry was generated |
| OperationName | Name of the operation associated with the log event |
| Category | Name of the log event |
| JobId | ID of the Job submitted |
| ExperimentId | ID of the Experiment |
| ExperimentName | Name of the Experiment |
| CustomerSubscriptionId | SubscriptionId where Experiment and Job as submitted |
| WorkspaceName | Name of the machine learning workspace |
| ClusterName | Name of the Cluster |
| ProvisioningState | State of the Job submission |
| ResourceGroupName | Name of the resource group |
| JobName | Name of the Job |
| ClusterId | ID of the cluster |
| EventType | Type of the Job event. For example, JobSubmitted, JobRunning, JobFailed, JobSucceeded. |
| ExecutionState | State of the job (the Run). For example, Queued, Running, Succeeded, Failed |
| ErrorDetails | Details of job error |
| CreationApiVersion | Api version used to create the job |
| ClusterResourceGroupName | Resource group name of the cluster |
| TFWorkerCount | Count of TF workers |
| TFParameterServerCount | Count of TF parameter server |
| ToolType | Type of tool used |
| RunInContainer | Flag describing if job should be run inside a container |
| JobErrorMessage | detailed message of Job error |
| NodeId | ID of the node created where job is running |

### AmlComputeClusterEvent table

| Property | Description |
|:--- |:--- |
| TimeGenerated | Time when the log entry was generated |
| OperationName | Name of the operation associated with the log event |
| Category | Name of the log event |
| ProvisioningState | Provisioning state of the cluster |
| ClusterName | Name of the cluster |
| ClusterType | Type of the cluster |
| CreatedBy | User who created the cluster |
| CoreCount | Count of the cores in the cluster |
| VmSize | Vm size of the cluster |
| VmPriority | Priority of the nodes created inside a cluster Dedicated/LowPriority |
| ScalingType | Type of cluster scaling manual/auto |
| InitialNodeCount | Initial node count of the cluster |
| MinimumNodeCount | Minimum node count of the cluster |
| MaximumNodeCount | Maximum node count of the cluster |
| NodeDeallocationOption | How the node should be deallocated |
| Publisher | Publisher of the cluster type |
| Offer | Offer with which the cluster is created |
| Sku | Sku of the Node/VM created inside cluster |
| Version | Version of the image used while Node/VM is created |
| SubnetId | SubnetId of the cluster |
