     :::image type="content" source="./media/how-to-run-batch-predictions-designer/create-pipeline-parameter.png" alt-text="Screenshot of cleaned dataset tab with set as pipeline parameter checked." lightbox= "./media/how-to-run-batch-predictions-designer/create-pipeline-parameter.png":::


1. Submit the batch inference pipeline and go to job detail page by selecting the job link in the left pane.

## Publish your batch inference pipeline

Now you're ready to deploy the inference pipeline. This will deploy the pipeline and make it available for others to use.

1. Select the **Publish** button.

1. In the dialog that appears, expand the drop-down for **PipelineEndpoint**, and select **New PipelineEndpoint**.

1. Provide an endpoint name and optional description.

    Near the bottom of the dialog, you can see the parameter you configured with a default value of the dataset ID used during training.

1. Select **Publish**.

:::image type="content" source="./media/how-to-run-batch-predictions-designer/publish-inference-pipeline.png" alt-text="Screenshot of set up published pipeline." lightbox= "./media/how-to-run-batch-predictions-designer/publish-inference-pipeline.png":::

## Consume an endpoint

Now, you have a published pipeline with a dataset parameter. The pipeline will use the trained model created in the training pipeline to score the dataset you provide as a parameter.

### Submit a pipeline job

In this section, you'll set up a manual pipeline job and alter the pipeline parameter to score new data.

1. After the deployment is complete, go to the **Endpoints** section.

1. Select **Pipeline endpoints**.

1. Select the name of the endpoint you created.

:::image type="content" source="./media/how-to-run-batch-predictions-designer/manage-endpoints.png" alt-text="Screenshot of the pipeline endpoint tab." :::

1. Select **Published pipelines**.

    This screen shows all published pipelines published under this endpoint.

1. Select the pipeline you published.

    The pipeline details page shows you a detailed job history and connection string information for your pipeline.
    
1. Select **Submit** to create a manual run of the pipeline.

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/submit-manual-run.png" alt-text="Screenshot of set up pipeline job with parameters highlighted." lightbox= "./media/how-to-run-batch-predictions-designer/submit-manual-run.png" :::
    
1. Change the parameter to use a different dataset.
    
1. Select **Submit** to run the pipeline.

### Use the REST endpoint

You can find information on how to consume pipeline endpoints and published pipeline in the **Endpoints** section.

You can find the REST endpoint of a pipeline endpoint in the job overview panel. By calling the endpoint, you're consuming its default published pipeline.

You can also consume a published pipeline in the **Published pipelines** page. Select a published pipeline and you can find the REST endpoint of it in the **Published pipeline overview** panel to the right of the graph. 

To make a REST call, you'll need an OAuth 2.0 bearer-type authentication header. See the following [tutorial section](tutorial-pipeline-batch-scoring-classification.md#publish-and-run-from-a-rest-endpoint) for more detail on setting up authentication to your workspace and making a parameterized REST call.

## Versioning endpoints

The designer assigns a version to each subsequent pipeline that you publish to an endpoint. You can specify the pipeline version that you want to execute as a parameter in your REST call. If you don't specify a version number, the designer will use the default pipeline.

When you publish a pipeline, you can choose to make it the new default pipeline for that endpoint.

:::image type="content" source="./media/how-to-run-batch-predictions-designer/set-default-pipeline.png" alt-text="Screenshot of set up published pipeline with set as default pipeline for this endpoint checked." :::

You can also set a new default pipeline in the **Published pipelines** tab of your endpoint.
