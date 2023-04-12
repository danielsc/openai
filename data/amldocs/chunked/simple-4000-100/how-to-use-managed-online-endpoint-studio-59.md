    :::image type="content" source="media/how-to-create-managed-online-endpoint-studio/deploy-from-models-page.png" lightbox="media/how-to-create-managed-online-endpoint-studio/deploy-from-models-page.png" alt-text="A screenshot of creating a managed online endpoint from the Models UI.":::

1. Enter an __Endpoint name__ and select __Managed__ as the compute type.
1. Select __Next__, accepting defaults, until you're prompted for the environment. Here, select the following:

    * __Select scoring file and dependencies__: Browse and select the `\azureml-examples\cli\endpoints\online\model-1\onlinescoring\score.py` file from the repo you downloaded earlier.
    * __Choose an environment__ section: Select the **Scikit-learn 0.24.1** curated environment.

1. Select __Next__, accepting defaults, until you're prompted to create the deployment. Select the __Create__ button.

## View managed online endpoints

You can view your managed online endpoints in the **Endpoints** page. Use the endpoint details page to find critical information including the endpoint URI, status, testing tools, activity monitors, deployment logs, and sample consumption code:

1. In the left navigation bar, select **Endpoints**.
1. (Optional) Create a **Filter** on **Compute type** to show only **Managed** compute types.
1. Select an endpoint name to view the endpoint detail page.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/managed-endpoint-details-page.png" lightbox="media/how-to-create-managed-online-endpoint-studio/managed-endpoint-details-page.png" alt-text="Screenshot of managed endpoint details view.":::

### Test

Use the **Test** tab in the endpoints details page to test your managed online deployment. Enter sample input and view the results.

1. Select the **Test** tab in the endpoint's detail page.
1. Use the dropdown to select the deployment you want to test.
1. Enter sample input.
1. Select **Test**.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/test-deployment.png" lightbox="media/how-to-create-managed-online-endpoint-studio/test-deployment.png" alt-text="A screenshot of testing a deployment by providing sample data, directly in your browser.":::

### Monitoring

Use the **Monitoring** tab to see high-level activity monitor graphs for your managed online endpoint.

To use the monitoring tab, you must select "**Enable Application Insight diagnostic and data collection**" when you create your endpoint.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/monitor-endpoint.png" lightbox="media/how-to-create-managed-online-endpoint-studio/monitor-endpoint.png" alt-text="A screenshot of monitoring endpoint-level metrics in the studio.":::

For more information on viewing other monitors and alerts, see [How to monitor managed online endpoints](how-to-monitor-online-endpoints.md).

### Deployment logs

You can get logs from the containers that are running on the VM where the model is deployed. The amount of information you get depends on the provisioning status of the deployment. If the specified container is up and running, you'll see its console output; otherwise, you'll get a message to try again later.

Use the **Deployment logs** tabs in the endpoint's details page to see log output from container.

1. Select the **Deployment logs** tab in the endpoint's details page.
1. Use the dropdown to select the deployment whose log you want to see.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/deployment-logs.png" lightbox="media/how-to-create-managed-online-endpoint-studio/deployment-logs.png" alt-text="A screenshot of observing deployment logs in the studio.":::

The logs are pulled from the inference server. Logs include the console log (from the inference server) which contains print/log statements from your scoring script (`score.py`).

To get logs from the storage initializer container, use the Azure CLI or Python SDK. These logs contain information on whether code and model data were successfully downloaded to the container. See the [get container logs section in troubleshooting online endpoints deployment](how-to-troubleshoot-online-endpoints.md#get-container-logs).
