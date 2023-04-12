1. Select the **Comment** text box and enter *Split the dataset into training set (0.7) and test set (0.3)*.

### Train the model

Train the model by giving it a dataset that includes the price. The algorithm constructs a model that explains the relationship between the features and the price as presented by the training data.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Linear Regression** component.

1. Drag the **Linear Regression** component to the pipeline canvas.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Train Model** component.

1. Drag the **Train Model** component to the pipeline canvas.

1. Connect the output of the **Linear Regression** component to the left input of the **Train Model** component.

1. Connect the training data output (left port) of the **Split Data** component to the right input of the **Train Model** component.

    > [!IMPORTANT]
    > Make sure that the left output port of **Split Data** connects to **Train Model**. The left port contains the training set. The right port contains the test set.

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/pipeline-train-model.png" alt-text="Screenshot showing the Linear Regression  connects to left port of Train Model  and the Split Data connects to right port of Train Model.":::

1. Select the **Train Model** component.

1. Click on the arrow icon under Settings to the right of the canvas to open the component details pane. Alternatively, you can double-click the **Train Model** component to open the details pane.

1. Select **Edit column** to the right of the pane.

1. In the **Label column** window that appears, expand the drop-down menu and select **Column names**.

1. In the text box, enter *price* to specify the value that your model is going to predict.

    >[!IMPORTANT]
    > Make sure you enter the column name exactly. Do not capitalize **price**.

    Your pipeline should look like this:

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/pipeline-train-graph.png" alt-text="Screenshot showing the correct configuration of the pipeline after adding the Train Model component.":::

### Add the Score Model component

After you train your model by using 70 percent of the data, you can use it to score the other 30 percent to see how well your model functions.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Score Model** component.

1. Drag the **Score Model** component to the pipeline canvas.

1. Connect the output of the **Train Model** component to the left input port of **Score Model**. Connect the test data output (right port) of the **Split Data** component to the right input port of **Score Model**.

### Add the Evaluate Model component

Use the **Evaluate Model** component to evaluate how well your model scored the test dataset.

1. In the datasets and component palette to the left of the canvas, click **Component** and search for the **Evaluate Model** component.

1. Drag the **Evaluate Model** component to the pipeline canvas.

1. Connect the output of the **Score Model** component to the left input of **Evaluate Model**.

    The final pipeline should look something like this:

    :::image type="content" source="./media/tutorial-designer-automobile-price-train-score/pipeline-final-graph.png" alt-text="Screenshot showing the correct configuration of the pipeline.":::

## Submit the pipeline

Now that your pipeline is all setup, you can submit a pipeline job to train your machine learning model. You can submit a valid pipeline job at any point, which can be used to review changes to your pipeline during development.

1. At the top of the canvas, select **Submit**.

1. In the **Set up pipeline job** dialog box, select **Create new**.

    > [!NOTE]
    > Experiments group similar pipeline jobs together. If you run a pipeline multiple times, you can select the same experiment for successive jobs.
