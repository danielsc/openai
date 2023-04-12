You can set a **Default compute target** for the entire pipeline, which will tell every component to use the same compute target by default. However, you can specify compute targets on a per-module basis.

1. Select ![Screenshot of the gear icon that is in the UI.](./media/tutorial-designer-automobile-price-train-score/gear-icon.png)**Settings** to the right of the canvas to open the **Settings** pane.

1. Select **Create Azure ML compute instance**.

    If you already have an available compute target, you can select it from the **Select Azure ML compute instance** drop-down to run this pipeline.

1. Enter a name for the compute resource.

1. Select **Create**.

    > [!NOTE]
    > It takes approximately five minutes to create a compute resource. After the resource is created, you can reuse it and skip this wait time for future jobs.
    >
    > The compute resource autoscales to zero nodes when it's idle to save cost. When you use it again after a delay, you might experience approximately five minutes of wait time while it scales back up.

## Import data

There are several sample datasets included in the designer for you to experiment with. For this tutorial, use **Automobile price data (Raw)**.

1. To the left of the pipeline canvas is a palette of datasets and components. Select **Component** -> **Sample data**.

1. Select the dataset **Automobile price data (Raw)**, and drag it onto the canvas.

   :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/automobile-data.png" alt-text="Gif of dragging the Automobile price data to the canvas.":::


### Visualize the data

You can visualize the data to understand the dataset that you'll use.

1. Right-click the **Automobile price data (Raw)** and select **Preview Data**.

1. Select the different columns in the data window to view information about each one.

    Each row represents an automobile, and the variables associated with each automobile appear as columns. There are 205 rows and 26 columns in this dataset.

## Prepare data

Datasets typically require some preprocessing before analysis. You might have noticed some missing values when you inspected the dataset. These missing values must be cleaned so that the model can analyze the data correctly.

### Remove a column

When you train a model, you have to do something about the data that's missing. In this dataset, the **normalized-losses** column is missing many values, so you'll exclude that column from the model altogether.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Select Columns in Dataset** component.

1. Drag the **Select Columns in Dataset** component onto the canvas. Drop the component below the dataset component.

1. Connect the **Automobile price data (Raw)** dataset to the **Select Columns in Dataset** component. Drag from the dataset's output port, which is the small circle at the bottom of the dataset on the canvas, to the input port of **Select Columns in Dataset**, which is the small circle at the top of the component.

    > [!TIP]
    > You create a flow of data through your pipeline when you connect the output port of one component to an input port of another.

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/connect-modules.gif" alt-text="Screenshot of connecting Automobile price data component to select columns in dataset component.":::

1. Select the **Select Columns in Dataset** component.

1. Click on the arrow icon under Settings to the right of the canvas to open the component details pane. Alternatively, you can double-click the **Select Columns in Dataset** component to open the details pane.

1. Select **Edit column** to the right of the pane.

1. Expand the **Column names** drop down next to **Include**, and select  **All columns**.

1. Select the **+** to add a new rule.

1. From the drop-down menus, select **Exclude** and **Column names**.

1. Enter *normalized-losses* in the text box.
