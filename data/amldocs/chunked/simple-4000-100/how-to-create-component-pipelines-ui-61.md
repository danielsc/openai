    Select the **Gear icon** ![Screenshot of the gear icon that is in the UI.](./media/tutorial-designer-automobile-price-train-score/gear-icon.png) at the top right of the canvas to open the **Settings** pane. Select the default compute target for your pipeline.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/set-default-compute.png" alt-text="Screenshot showing setting default compute for the pipeline." lightbox ="./media/how-to-create-component-pipelines-ui/set-default-compute.png":::

    > [!Important]
    > Attached compute is not supported, use [compute instances or clusters](concept-compute-target.md#azure-machine-learning-compute-managed) instead.

1. In asset library, you can see **Data assets** and **Components** tabs. Switch to **Components** tab, you can see the components registered from previous section.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/asset-library.png" alt-text="Screenshot showing registered component in asset library." lightbox ="./media/how-to-create-component-pipelines-ui/asset-library.png":::

    Drag the components and drop on the canvas. By default it will use the default version of the component, and you can change to a specific version in the right pane of component if your component has multiple versions.
    
      :::image type="content" source="./media/how-to-create-component-pipelines-ui/change-component-version.png" alt-text="Screenshot showing changing version of component." lightbox ="./media/how-to-create-component-pipelines-ui/change-component-version.png":::
    
1. Connect the upstream component output ports to the downstream component input ports.

1. Select one component, you'll see a right pane where you can configure the component.

    For components with primitive type inputs like number, integer, string and boolean, you can change values of such inputs in the component detailed pane.

    You can also change the output settings and compute target where this component run in the right pane.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/component-parameter.png" alt-text="Screenshot showing component parameter settings." lightbox ="./media/how-to-create-component-pipelines-ui/component-parameter.png":::

> [!NOTE]
> Currently registered components and the designer built-in components cannot be used together.

## Submit pipeline

1. Select submit, and fill in the required information for your pipeline job.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/submit-pipeline.png" alt-text="Screenshot of set up pipeline job with submit highlighted." lightbox ="./media/how-to-create-component-pipelines-ui/submit-pipeline.png":::

1. After submit successfully, you'll see a job detail page link in the left page. Select **Job detail** to go to pipeline job detail page for checking status and debugging.

    :::image type="content" source="./media/how-to-create-component-pipelines-ui/submission-list.png" alt-text="Screenshot showing the submitted jobs list." lightbox ="./media/how-to-create-component-pipelines-ui/submission-list.png":::

    > [!NOTE]
    > The **Submitted jobs** list only contains pipeline jobs submitted during an active session. A page reload will clear out the content.

## Next steps

- Use [these Jupyter notebooks on GitHub](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/pipelines-with-components) to explore machine learning pipelines further
- Learn [how to use CLI v2 to create pipeline using components](how-to-create-component-pipelines-cli.md).
- Learn [how to use SDK v2 to create pipeline using components](how-to-create-component-pipeline-python.md)
