To get logs from the storage initializer container, use the Azure CLI or Python SDK. These logs contain information on whether code and model data were successfully downloaded to the container. See the [get container logs section in troubleshooting online endpoints deployment](how-to-troubleshoot-online-endpoints.md#get-container-logs).

## Add a deployment to a managed online endpoint

You can add a deployment to your existing managed online endpoint.

From the **Endpoint details page**

1. Select **+ Add Deployment** button in the [endpoint details page](#view-managed-online-endpoints).
2. Follow the instructions to complete the deployment.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/add-deploy-option-from-endpoint-page.png" lightbox="media/how-to-create-managed-online-endpoint-studio/add-deploy-option-from-endpoint-page.png" alt-text="A screenshot of Add deployment option from Endpoint details page.":::

Alternatively, you can use the **Models** page to add a deployment:

1. In the left navigation bar, select the **Models** page.
1. Select a model by checking the circle next to the model name.
1. Select **Deploy** > **Deploy to real-time endpoint**.
1. Choose to deploy to an existing managed online endpoint.

:::image type="content" source="media/how-to-create-managed-online-endpoint-studio/select-existing-managed-endpoints.png" lightbox="media/how-to-create-managed-online-endpoint-studio/select-existing-managed-endpoints.png" alt-text="A screenshot of Add deployment option from Models page.":::

> [!NOTE]
> You can adjust the traffic balance between deployments in an endpoint when adding a new deployment.
>
> :::image type="content" source="media/how-to-create-managed-online-endpoint-studio/adjust-deployment-traffic.png" lightbox="media/how-to-create-managed-online-endpoint-studio/adjust-deployment-traffic.png" alt-text="A screenshot of how to use sliders to control traffic distribution across multiple deployments.":::

## Update managed online endpoints

You can update deployment traffic percentage and instance count from Azure Machine Learning studio.

### Update deployment traffic allocation

Use **deployment traffic allocation** to control the percentage of incoming of requests going to each deployment in an endpoint.

1. In the endpoint details page, Select  **Update traffic**.
2. Adjust your traffic and select **Update**.

> [!TIP]
> The **Total traffic percentage** must sum to either 0% (to disable traffic) or 100% (to enable traffic).

### Update deployment instance count

Use the following instructions to scale an individual deployment up or down by adjusting the number of instances:

1. In the endpoint details page. Find the card for the deployment you want to update.
1. Select the **edit icon** in the deployment detail card.
1. Update the instance count.
1. Select **Update**.

## Delete managed online endpoints and deployments

Learn how to delete an entire managed online endpoint and it's associated deployments. Or, delete an individual deployment from a managed online endpoint.

### Delete a managed online endpoint

Deleting a managed online endpoint also deletes any deployments associated with it.

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Endpoints** page.
1. Select an endpoint by checking the circle next to the model name.
1. Select **Delete**.

Alternatively, you can delete a managed online endpoint directly in the [endpoint details page](#view-managed-online-endpoints). 

### Delete an individual deployment

Use the following steps to delete an individual deployment from a managed online endpoint. This does affect the other deployments in the managed online endpoint:

> [!NOTE]
> You cannot delete a deployment that has allocated traffic. You must first [set traffic allocation](#update-deployment-traffic-allocation) for the deployment to 0% before deleting it.

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
