| CorrelationId | A GUID used to group together a set of related events, when applicable. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlProjectId | The unique identifier of the AzureML project. |
| AmlProjectName | The name of the AzureML project. |
| AmlLabelNames | The label class names which are created for the project. |
| AmlDataStoreName | The name of the data store where the project's data is stored. |

### AmlDataSetEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlDataSetEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| AmlWorkspaceId | A GUID and unique ID of the AzureML workspace. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlDatasetId | The ID of the AzureML Data Set. |
| AmlDatasetName | The name of the AzureML Data Set. |

### AmlDataStoreEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlDataStoreEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| AmlWorkspaceId | A GUID and unique ID of the AzureML workspace. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlDatastoreName | The name of the AzureML Data Store. |

### AmlDeploymentEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlDeploymentEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlServiceName | The name of the AzureML Service. |

### AmlInferencingEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlInferencingEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
| OperationName | The name of the operation associated with the log entry |
| Identity | The identity of the user or application that performed the operation. |
| AadTenantId | The AAD tenant ID the operation was submitted for. |
| AmlServiceName | The name of the AzureML Service. |

### AmlModelsEvent table

| Property | Description |
|:--- |:--- |
| Type | Name of the log event, AmlModelsEvent |
| TimeGenerated | Time (UTC) when the log entry was generated |
| Level | The severity level of the event. Must be one of Informational, Warning, Error, or Critical. |
| ResultType | The status of the event. Typical values include Started, In Progress, Succeeded, Failed, Active, and Resolved. |
