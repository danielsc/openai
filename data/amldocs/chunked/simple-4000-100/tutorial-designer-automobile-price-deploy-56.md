     :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/deploy-in-job-detail-page.png" alt-text="Screenshot showing deploying in job detail page.":::

## Create an inferencing cluster

In the dialog box that appears, you can select from any existing Azure Kubernetes Service (AKS) clusters to deploy your model to. If you don't have an AKS cluster, use the following steps to create one.

1. Select **Compute** in the dialog box that appears to go to the **Compute** page.

1. On the navigation ribbon, select **Inference Clusters** > **+ New**.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/new-inference-cluster.png" alt-text="Screenshot showing how to get to the new inference cluster pane.":::
   
1. In the inference cluster pane, configure a new Kubernetes Service.

1. Enter *aks-compute* for the **Compute name**.
    
1. Select a nearby region that's available for the **Region**.

1. Select **Create**.

    > [!NOTE]
    > It takes approximately 15 minutes to create a new AKS service. You can check the provisioning state on the **Inference Clusters** page.

## Deploy the real-time endpoint

After your AKS service has finished provisioning, return to the real-time inferencing pipeline to complete deployment.

1. Select **Deploy** above the canvas.

1. Select **Deploy new real-time endpoint**.

1. Select the AKS cluster you created.

     :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/setup-endpoint.png" alt-text="Screenshot showing how to set up a new real-time endpoint.":::

    You can also change **Advanced** setting for your real-time endpoint.

    |Advanced setting|Description|
    |---|---|
    |Enable Application Insights diagnostics and data collection| Whether to enable Azure Application Insights to collect data from the deployed endpoints. </br> By default: false. |
    |Scoring timeout| A timeout in milliseconds to enforce for scoring calls to the web service.</br>By default: 60000.|
    |Auto scale enabled|   Whether to enable autoscaling for the web service.</br>By default: true.|
    |Min replicas| The minimum number of containers to use when autoscaling this web service.</br>By default: 1.|
    |Max replicas| The maximum number of containers to use when autoscaling this web service.</br> By default: 10.|
    |Target utilization|The target utilization (in percent out of 100) that the autoscaler should attempt to maintain for this web service.</br> By default: 70.|
    |Refresh period|How often (in seconds) the autoscaler attempts to scale this web service.</br> By default: 1.|
    |CPU reserve capacity|The number of CPU cores to allocate for this web service.</br> By default: 0.1.|
    |Memory reserve capacity|The amount of memory (in GB) to allocate for this web service.</br> By default: 0.5.|

1. Select **Deploy**.

    A success notification from the notification center appears after deployment finishes. It might take a few minutes.

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/deploy-notification.png" alt-text="Screenshot showing deployment notification.":::

> [!TIP]
> You can also deploy to **Azure Container Instance** (ACI) if you select **Azure Container Instance** for **Compute type** in the real-time endpoint setting box.
> Azure Container Instance is used for testing or development. Use ACI for low-scale CPU-based workloads that require less than 48 GB of RAM.

## Test the real-time endpoint

After deployment finishes, you can view your real-time endpoint by going to the **Endpoints** page.

1. On the **Endpoints** page, select the endpoint you deployed.

    In the **Details** tab, you can see more information such as the REST URI, Swagger definition, status, and tags.

    In the **Consume** tab, you can find sample consumption code, security keys, and set authentication methods.

    In the **Deployment logs** tab, you can find the detailed deployment logs of your real-time endpoint.
