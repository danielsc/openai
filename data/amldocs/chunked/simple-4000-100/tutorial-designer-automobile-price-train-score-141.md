1. From the drop-down menus, select **Exclude** and **Column names**.

1. Enter *normalized-losses* in the text box.

1. In the lower right, select **Save** to close the column selector.

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/exclude-column.png" alt-text="Screenshot of select columns with exclude highlighted.":::

1. In the **Select Columns in Dataset** component details pane, expand **Node info**.

1. Select the **Comment** text box and enter *Exclude normalized losses*.

    Comments will appear on the graph to help you organize your pipeline.

### Clean missing data

Your dataset still has missing values after you remove the **normalized-losses** column. You can remove the remaining missing data by using the **Clean Missing Data** component.

> [!TIP]
> Cleaning the missing values from input data is a prerequisite for using most of the components in the designer.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Clean Missing Data** component.

1. Drag the **Clean Missing Data** component to the pipeline canvas. Connect it to the **Select Columns in Dataset** component.

1. Select the **Clean Missing Data** component.

1. Click on the arrow icon under Settings to the right of the canvas to open the component details pane. Alternatively, you can double-click the **Clean Missing Data** component to open the details pane.

1. Select **Edit column** to the right of the pane.

1. In the **Columns to be cleaned** window that appears, expand the drop-down menu next to **Include**. Select, **All columns**

1. Select **Save**

1. In the **Clean Missing Data** component details pane, under **Cleaning mode**, select **Remove entire row**.

1. In the **Clean Missing Data** component details pane, expand **Node info**. 

1. Select the **Comment** text box and enter *Remove missing value rows*.

    Your pipeline should now look something like this:

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/pipeline-clean.png" alt-text="Screenshot of automobile price data connected to select columns in dataset component, which is connected to clean missing data.":::

## Train a machine learning model

Now that you have the components in place to process the data, you can set up the training components.

Because you want to predict price, which is a number, you can use a regression algorithm. For this example, you use a linear regression model.

### Split the data

Splitting data is a common task in machine learning. You'll split your data into two separate datasets. One dataset will train the model and the other will test how well the model performed.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Split Data** component.

1. Drag the **Split Data** component to the pipeline canvas.

1. Connect the left port of the **Clean Missing Data** component to the **Split Data** component.

    > [!IMPORTANT]
    > Make sure that the left output port of **Clean Missing Data** connects to **Split Data**. The left port contains the cleaned data. The right port contains the discarded data.

1. Select the **Split Data** component.

1. Click on the arrow icon under Settings to the right of the canvas to open the component details pane. Alternatively, you can double-click the **Split Data** component to open the details pane.

1. In the **Split Data** details pane, set the **Fraction of rows in the first output dataset** to 0.7.

    This option splits 70 percent of the data to train the model and 30 percent for testing it. The 70 percent dataset will be accessible through the left output port. The remaining data will be available through the right output port.

1. In the **Split Data** details pane, expand **Node info**.

1. Select the **Comment** text box and enter *Split the dataset into training set (0.7) and test set (0.3)*.

### Train the model
