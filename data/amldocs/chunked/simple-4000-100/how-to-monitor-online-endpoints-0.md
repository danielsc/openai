
# Monitor online endpoints

In this article, you learn how to monitor [Azure Machine Learning online endpoints](concept-endpoints.md). Use Application Insights to view metrics and create alerts to stay up to date with your online endpoints.

In this article you learn how to:

> [!div class="checklist"]
> * View metrics for your online endpoint
> * Create a dashboard for your metrics
> * Create a metric alert

## Prerequisites

- Deploy an Azure Machine Learning online endpoint.
- You must have at least [Reader access](../role-based-access-control/role-assignments-portal.md) on the endpoint.

## Metrics

You can view metrics pages for online endpoints or deployments in the Azure portal. An easy way to access these metrics pages is through links available in the Azure Machine Learning studio user interface—specifically in the **Details** tab of an endpoint's page. Following these links will take you to the exact metrics page in the Azure portal for the endpoint or deployment. Alternatively, you can also go into the Azure portal to search for the metrics page for the endpoint or deployment.

To access the metrics pages through links available in the studio:

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Endpoints** page.
1. Select an endpoint by clicking its name.
1. Select **View metrics** in the **Attributes** section of the endpoint to open up the endpoint's metrics page in the Azure portal.
1. Select **View metrics** in the section for each available deployment to open up the deployment's metrics page in the Azure portal.

    :::image type="content" source="media/how-to-monitor-online-endpoints/online-endpoints-access-metrics-from-studio.png" alt-text="A screenshot showing how to access the metrics of an endpoint and deployment from the studio UI." lightbox="media/how-to-monitor-online-endpoints/online-endpoints-access-metrics-from-studio.png":::

To access metrics directly from the Azure portal:

1. Go to the [Azure portal](https://portal.azure.com).
1. Navigate to the online endpoint or deployment resource.

    Online endpoints and deployments are Azure Resource Manager (ARM) resources that can be found by going to their owning resource group. Look for the resource types **Machine Learning online endpoint** and **Machine Learning online deployment**.

1. In the left-hand column, select **Metrics**.

### Available metrics

Depending on the resource that you select, the metrics that you see will be different. Metrics are scoped differently for online endpoints and online deployments.

#### Metrics at endpoint scope

- Request Latency
- Request Latency P50 (Request latency at the 50th percentile)
- Request Latency P90 (Request latency at the 90th percentile)
- Request Latency P95 (Request latency at the 95th percentile)
- Requests per minute
- New connections per second
- Active connection count
- Network bytes

Split on the following dimensions:

- Deployment
- Status Code
- Status Code Class

**Bandwidth throttling**

Bandwidth will be throttled if the limits are exceeded for _managed_ online endpoints (see managed online endpoints section in [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints)). To determine if requests are throttled:
- Monitor the "Network bytes" metric
- The response trailers will have the fields: `ms-azureml-bandwidth-request-delay-ms` and `ms-azureml-bandwidth-response-delay-ms`. The values of the fields are the delays, in milliseconds, of the bandwidth throttling.

#### Metrics at deployment scope

- CPU Utilization Percentage
- Deployment Capacity (the number of instances of the requested instance type)
- Disk Utilization
- GPU Memory Utilization (only applicable to GPU instances)
- GPU Utilization (only applicable to GPU instances)
- Memory Utilization Percentage

Split on the following dimension:

- InstanceId

### Create a dashboard

You can create custom dashboards to visualize data from multiple sources in the Azure portal, including the metrics for your online endpoint. For more information, see [Create custom KPI dashboards using Application Insights](../azure-monitor/app/tutorial-app-dashboards.md#add-custom-metric-chart).
