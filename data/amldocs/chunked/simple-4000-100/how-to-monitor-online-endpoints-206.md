| ResponseThrottlingDelayMs | Delay in milliseconds in response data transfer due to network throttling. 

**AMLOnlineEndpointConsoleLog**

| Field Name | Description |
| ----- | ----- |
| TimeGenerated | The timestamp (UTC) of when the log was generated. 
| OperationName | The operation associated with log record. 
| InstanceId | The ID of the instance that generated this log record. 
| DeploymentName | The name of the deployment associated with the log record. 
| ContainerName | The name of the container where the log was generated. 
| Message | The content of the log. 

**AMLOnlineEndpointEventLog** (preview)


| Field Name | Description |
| ----- | ----- |
| TimeGenerated | The timestamp (UTC) of when the log was generated. 
| OperationName | The operation associated with log record. 
| InstanceId | The ID of the instance that generated this log record. 
| DeploymentName | The name of the deployment associated with the log record. 
| Name | The name of the event. 
| Message | The content of the event. 



## Next steps

* Learn how to [view costs for your deployed endpoint](./how-to-view-online-endpoints-costs.md).
* Read more about [metrics explorer](../azure-monitor/essentials/metrics-charts.md).
