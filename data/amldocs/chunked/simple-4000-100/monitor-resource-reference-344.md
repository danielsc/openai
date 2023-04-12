| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| ResultSignature | The HTTP status code of the event. Typical values include 200, 201, 202 etc. |
| AmlModelName | The name of the AzureML Model. |

### AmlPipelineEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlPipelineEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| AmlWorkspaceId | A GUID and unique ID of the AzureML workspace. |
| AmlWorkspaceId | The name of the AzureML workspace. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlModuleId | A GUID and unique ID of the module.|
| AmlModelName | The name of the AzureML Model. |
| AmlPipelineId | The ID of the AzureML pipeline. |
| AmlParentPipelineId | The ID of the parent AzureML pipeline (in the case of cloning). |
| AmlPipelineDraftId | The ID of the AzureML pipeline draft. |
| AmlPipelineDraftName | The name of the AzureML pipeline draft. |
| AmlPipelineEndpointId | The ID of the AzureML pipeline endpoint. |
| AmlPipelineEndpointName | The name of the AzureML pipeline endpoint. |


### AmlRunEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlRunEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| OperationName | The name of the operation associated with the log entry |
| AmlWorkspaceId | A GUID and unique ID of the AzureML workspace. |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| RunId | The unique ID of the run. |

### AmlEnvironmentEvent  table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlEnvironmentEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlEnvironmentName | The name of the AzureML environment configuration. |
| AmlEnvironmentVersion | The name of the AzureML environment configuration version. |


## See also

- See [Monitoring Azure Machine Learning](monitor-azure-machine-learning.md) for a description of monitoring Azure Machine Learning.
- See [Monitoring Azure resources with Azure Monitor](../azure-monitor/essentials/monitor-azure-resource.md) for details on monitoring Azure resources.
