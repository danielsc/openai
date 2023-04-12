| Version | Version of the image used while Node/VM is created |
| SubnetId | SubnetId of the cluster |
| AllocationState | Cluster allocation state |
| CurrentNodeCount | Current node count of the cluster |
| TargetNodeCount | Target node count of the cluster while scaling up/down |
| EventType | Type of event during cluster creation. |
| NodeIdleTimeSecondsBeforeScaleDown | Idle time in seconds before cluster is scaled down |
| PreemptedNodeCount | Preempted node count of the cluster |
| IsResizeGrow | Flag indicating that cluster is scaling up |
| VmFamilyName | Name of the VM family of the nodes that can be created inside cluster |
| LeavingNodeCount | Leaving node count of the cluster |
| UnusableNodeCount | Unusable node count of the cluster |
| IdleNodeCount | Idle node count of the cluster |
| RunningNodeCount | Running node count of the cluster |
| PreparingNodeCount | Preparing node count of the cluster |
| QuotaAllocated | Allocated quota to the cluster |
| QuotaUtilized | Utilized quota of the cluster |
| AllocationStateTransitionTime | Transition time from one state to another |
| ClusterErrorCodes | Error code received during cluster creation or scaling |
| CreationApiVersion | Api version used while creating the cluster |

### AmlComputeClusterNodeEvent table

| Property | Description |
|:--- |:--- |
| TimeGenerated | Time when the log entry was generated |
| OperationName | Name of the operation associated with the log event |
| Category | Name of the log event |
| ClusterName | Name of the cluster |
| NodeId | ID of the cluster node created |
| VmSize | Vm size of the node |
| VmFamilyName | Vm family to which the node belongs |
| VmPriority | Priority of the node created Dedicated/LowPriority |
| Publisher | Publisher of the vm image. For example, microsoft-dsvm |
| Offer | Offer associated with the VM creation |
| Sku | Sku of the Node/VM created |
| Version | Version of the image used while Node/VM is created |
| ClusterCreationTime | Time when cluster was created |
| ResizeStartTime | Time when cluster scale up/down started |
| ResizeEndTime | Time when cluster scale up/down ended |
| NodeAllocationTime | Time when Node was allocated |
| NodeBootTime | Time when Node was booted up |
| StartTaskStartTime | Time when task was assigned to a node and started |
| StartTaskEndTime | Time when task assigned to a node ended |
| TotalE2ETimeInSeconds | Total time node was active |

> [!NOTE]
> Effective February 2022, the AmlComputeClusterNodeEvent table will be deprecated. We recommend that you instead use the AmlComputeClusterEvent table.

### AmlComputeInstanceEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlComputeInstanceEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| CorrelationId | A GUID used to group together a set of related events, when applicable. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlComputeInstanceName | "The name of the compute instance associated with the log entry. |

### AmlDataLabelEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlDataLabelEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| CorrelationId | A GUID used to group together a set of related events, when applicable. |
| OperationName | The name of the operation associated with the log entry |
