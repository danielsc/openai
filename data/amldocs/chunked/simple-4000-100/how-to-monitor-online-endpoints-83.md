You can create custom dashboards to visualize data from multiple sources in the Azure portal, including the metrics for your online endpoint. For more information, see [Create custom KPI dashboards using Application Insights](../azure-monitor/app/tutorial-app-dashboards.md#add-custom-metric-chart).
    
### Create an alert

You can also create custom alerts to notify you of important status updates to your online endpoint:

1. At the top right of the metrics page, select **New alert rule**.

    :::image type="content" source="./media/how-to-monitor-online-endpoints/online-endpoints-new-alert-rule.png" alt-text="Monitoring online endpoints: screenshot showing 'New alert rule' button surrounded by a red box":::

1. Select a condition name to specify when your alert should be triggered.

    :::image type="content" source="./media/how-to-monitor-online-endpoints/online-endpoints-configure-signal-logic.png" alt-text="Monitoring online endpoints: screenshot showing 'Configure signal logic' button surrounded by a red box":::

1. Select **Add action groups** > **Create action groups** to specify what should happen when your alert is triggered.

1. Choose **Create alert rule** to finish creating your alert.

## Logs

There are three logs that can be enabled for online endpoints:

* **AMLOnlineEndpointTrafficLog** (preview): You could choose to enable traffic logs if you want to check the information of your request. Below are some cases: 

    * If the response isn't 200, check the value of the column “ResponseCodeReason” to see what happened. Also check the reason in the "HTTPS status codes" section of the [Troubleshoot online endpoints](how-to-troubleshoot-online-endpoints.md#http-status-codes) article.

    * You could check the response code and response reason of your model from the column “ModelStatusCode” and “ModelStatusReason”. 

    * You want to check the duration of the request like total duration, the request/response duration, and the delay caused by the network throttling. You could check it from the logs to see the breakdown latency. 

    * If you want to check how many requests or failed requests recently. You could also enable the logs. 

* **AMLOnlineEndpointConsoleLog**: Contains logs that the containers output to the console. Below are some cases: 

    * If the container fails to start, the console log may be useful for debugging. 

    * Monitor container behavior and make sure that all requests are correctly handled. 

    * Write request IDs in the console log. Joining the request ID, the AMLOnlineEndpointConsoleLog, and AMLOnlineEndpointTrafficLog in the Log Analytics workspace, you can trace a request from the network entry point of an online endpoint to the container.  

    * You may also use this log for performance analysis in determining the time required by the model to process each request. 

* **AMLOnlineEndpointEventLog** (preview): Contains event information regarding the container’s life cycle. Currently, we provide information on the following types of events: 

    | Name | Message |
    | ----- | ----- | 
    | BackOff | Back-off restarting failed container 
    | Pulled | Container image "\<IMAGE\_NAME\>" already present on machine 
    | Killing | Container inference-server failed liveness probe, will be restarted 
    | Created | Created container image-fetcher 
    | Created | Created container inference-server 
    | Created | Created container model-mount 
    | Unhealthy | Liveness probe failed: \<FAILURE\_CONTENT\> 
    | Unhealthy | Readiness probe failed: \<FAILURE\_CONTENT\> 
    | Started | Started container image-fetcher 
    | Started | Started container inference-server 
    | Started | Started container model-mount 
    | Killing | Stopping container inference-server 
    | Killing | Stopping container model-mount 

### How to enable/disable logs

> [!IMPORTANT]
> Logging uses Azure Log Analytics. If you do not currently have a Log Analytics workspace, you can create one using the steps in [Create a Log Analytics workspace in the Azure portal](../azure-monitor/logs/quick-create-workspace.md#create-a-workspace).
