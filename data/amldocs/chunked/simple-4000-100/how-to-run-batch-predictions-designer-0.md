
# Run batch predictions using Azure Machine Learning designer

In this article, you learn how to use the designer to create a batch prediction pipeline. Batch prediction lets you continuously score large datasets on-demand using a web service that can be triggered from any HTTP library.

In this how-to, you learn to do the following tasks:

> [!div class="checklist"]
> * Create and publish a batch inference pipeline
> * Consume a pipeline endpoint
> * Manage endpoint versions

To learn how to set up batch scoring services using the SDK, see the accompanying [tutorial on pipeline batch scoring](./tutorial-pipeline-batch-scoring-classification.md).

[!INCLUDE [endpoints-option](../../includes/machine-learning-endpoints-preview-note.md)]

## Prerequisites

This how-to assumes you already have a training pipeline. For a guided introduction to the designer, complete [part one of the designer tutorial](tutorial-designer-automobile-price-train-score.md).

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

## Create a batch inference pipeline

Your training pipeline must be run at least once to be able to create an inferencing pipeline.

1. Go to the **Designer** tab in your workspace.

1. Select the training pipeline that trains the model you want to use to make prediction.

1. **Submit** the pipeline.

![Submit the pipeline](./media/how-to-run-batch-predictions-designer/run-training-pipeline.png)

 :::image type="content" source="./media/how-to-run-batch-predictions-designer/run-training-pipeline.png" alt-text="Screenshot showing the set up pipeline job with the experiment drop-down and submit button highlighted." lightbox= "./media/how-to-run-batch-predictions-designer/run-training-pipeline.png":::

You'll see a submission list on the left of canvas. You can select the job detail link to go to the job detail page, and after the training pipeline job completes, you can create a batch inference pipeline.

 :::image type="content" source="./media/how-to-run-batch-predictions-designer/submission-list.png" alt-text="Screenshot showing the submitted job list." lightbox= "./media/how-to-run-batch-predictions-designer/submission-list.png":::

1. In job detail page, above the canvas, select the dropdown **Create inference pipeline**. Select **Batch inference pipeline**.

    > [!NOTE]
    > Currently auto-generating inference pipeline only works for training pipeline built purely by the designer built-in components.

    :::image type="content" source="./media/how-to-run-batch-predictions-designer/create-batch-inference.png" alt-text="Screenshot of the create inference pipeline drop-down with batch inference pipeline highlighted." lightbox= "./media/how-to-run-batch-predictions-designer/create-batch-inference.png":::
    
    It will create a batch inference pipeline draft for you. The batch inference pipeline draft uses the trained model as **MD-** node and transformation as **TD-** node from the training pipeline job.

    You can also modify this inference pipeline draft to better handle your input data for batch inference.

     :::image type="content" source="./media/how-to-run-batch-predictions-designer/batch-inference-draft.png" alt-text="Screenshot showing a batch inference pipeline draft." lightbox= "./media/how-to-run-batch-predictions-designer/batch-inference-draft.png":::

### Add a pipeline parameter

To create predictions on new data, you can either manually connect a different dataset in this pipeline draft view or create a parameter for your dataset. Parameters let you change the behavior of the batch inferencing process at runtime.

In this section, you create a dataset parameter to specify a different dataset to make predictions on.

1. Select the dataset component.

1. A pane will appear to the right of the canvas. At the bottom of the pane, select **Set as pipeline parameter**.
   
    Enter a name for the parameter, or accept the default value.

     :::image type="content" source="./media/how-to-run-batch-predictions-designer/create-pipeline-parameter.png" alt-text="Screenshot of cleaned dataset tab with set as pipeline parameter checked." lightbox= "./media/how-to-run-batch-predictions-designer/create-pipeline-parameter.png":::
