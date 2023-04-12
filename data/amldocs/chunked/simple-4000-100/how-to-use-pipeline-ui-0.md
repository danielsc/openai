
# How to use studio UI to build and debug Azure Machine Learning pipelines

Azure Machine Learning studio provides UI to build and debug your pipeline. You can use components to author a pipeline in the designer, and you can debug your pipeline in the job detail page.

This article will introduce how to use the studio UI to build and debug machine learning pipelines.

## Build machine learning pipeline

### Drag and drop components to build pipeline

In the designer homepage, you can select **New pipeline** to open a blank pipeline draft.

In the asset library left of the canvas, there are **Data assets** and **Components** tabs, which contain components and data registered to the workspace. For what is component and how to create custom component, you can refer to the [component concept article](concept-component.md).

You can quickly filter **My assets** or **Designer built-in assets**.

:::image type="content" source="./media/how-to-use-pipeline-ui/asset-library.png" alt-text="Screenshot showing the asset library with filter by selected." lightbox= "./media/how-to-use-pipeline-ui/asset-library.png":::

Then you can drag and drop either built-in components or custom components to the canvas. You can construct your pipeline or configure your components in any order. Just hide the right pane to construct your pipeline first, and open the right pane to configure your component.

> [!NOTE]
> Currently built-in components and custom components cannot be used together.

:::image type="content" source="./media/how-to-use-pipeline-ui/hide-right-pane.png" alt-text="Screenshot showing the close and open button." lightbox= "./media/how-to-use-pipeline-ui/hide-right-pane.png":::

### Submit pipeline

Now you've built your pipeline. Select **Submit** button above the canvas, and configure your pipeline job.

:::image type="content" source="./media/how-to-use-pipeline-ui/submit-pipeline.png" alt-text="Screenshot showing setup pipeline job with the submit button highlighted." lightbox= "./media/how-to-use-pipeline-ui/submit-pipeline.png":::

After you submit your pipeline job, you'll see a submitted job list in the left pane, which shows all the pipeline job you create from the current pipeline draft in the same session. There's also notification popping up from the notification center. You can select through the pipeline job link in the submission list or the notification to check pipeline job status or debugging.

> [!NOTE]
> Pipeline job status and results will not be filled back to the authoring page.

If you want to try a few different parameter values for the same pipeline, you can change values and submit for multiple times, without having to waiting for the running status.

:::image type="content" source="./media/how-to-use-pipeline-ui/submission-list.png" alt-text="Screenshot showing submitted job list and notification." lightbox= "./media/how-to-use-pipeline-ui/submission-list.png":::

> [!NOTE]
> The submission list only contains jobs submitted in the same session.
> If you refresh current page, it will not preserve the previous submitted job list.

On the pipeline job detail page, you can check the status of the overall job and each node inside, and logs of each node.

:::image type="content" source="./media/how-to-use-pipeline-ui/pipeline-job-detail-page.png" alt-text="Screenshot showing pipeline job detail page." lightbox= "./media/how-to-use-pipeline-ui/pipeline-job-detail-page.png":::

## Debug your pipeline in job detail page

### Using outline to quickly find node

In pipeline job detail page, there's an outline left to the canvas, which shows the overall structure of your pipeline job. Hovering on any row, you can select the "Locate" button to locate that node in the canvas.

:::image type="content" source="./media/how-to-use-pipeline-ui/outline.png" alt-text="Screenshot showing outline and locate in the canvas." lightbox= "./media/how-to-use-pipeline-ui/outline.png":::

You can filter failed or completed nodes, and filter by only components or dataset for further search. The left pane will show the matched nodes with more information including status, duration, and created time.
