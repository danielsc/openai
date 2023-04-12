:::image type="content" source="./media/how-to-run-batch-predictions-designer/set-default-pipeline.png" alt-text="Screenshot of set up published pipeline with set as default pipeline for this endpoint checked." :::

You can also set a new default pipeline in the **Published pipelines** tab of your endpoint.

:::image type="content" source="./media/how-to-run-batch-predictions-designer/set-new-default-pipeline.png" alt-text="Screenshot of sample pipeline tab with set as default highlighted." :::

## Update pipeline endpoint

If you make some modifications in your training pipeline, you may want to update the newly trained model to the pipeline endpoint.

1. After your modified training pipeline completes successfully, go to the job detail page.

1. Right click **Train Model** component and select **Register data**

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset.png" alt-text="Screenshot of the train model component options with register data highlighted." lightbox= "./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset.png" :::

    Input name and select **File** type.

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset-2.png" alt-text="Screenshot of register as data asset with new data asset selected." lightbox= "./media/how-to-run-batch-predictions-designer/register-train-model-as-dataset-2.png" :::

1. Find the previous batch inference pipeline draft, or you can just **Clone** the published pipeline into a new draft.

1. Replace the **MD-** node in the inference pipeline draft with the registered data in the step above.

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/update-inference-pipeline-draft.png" alt-text="Screenshot of updating the inference pipeline draft with the registered data in the step above." :::

1. Updating data transformation node **TD-** is the same as the trained model.

1. Then you can submit the inference pipeline with the updated model and transformation, and publish again.

## Next steps

* Follow the [designer tutorial to train and deploy a regression model](tutorial-designer-automobile-price-train-score.md).
* For how to publish and run a published pipeline using the SDK v1, see the [How to deploy pipelines](v1/how-to-deploy-pipelines.md) article.
