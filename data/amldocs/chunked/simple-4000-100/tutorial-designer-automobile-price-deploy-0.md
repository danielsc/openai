
# Tutorial: Designer - deploy a machine learning model

Use the designer to deploy a machine learning model to predict the price of cars. This tutorial is part two of a two-part series.

In [part one of the tutorial](tutorial-designer-automobile-price-train-score.md) you trained a linear regression model on car prices. In part two, you deploy the model to give others a chance to use it. In this tutorial, you:

> [!div class="checklist"]
> * Create a real-time inference pipeline.
> * Create an inferencing cluster.
> * Deploy the real-time endpoint.
> * Test the real-time endpoint.

## Prerequisites

Complete [part one of the tutorial](tutorial-designer-automobile-price-train-score.md) to learn how to train and score a machine learning model in the designer.

[!INCLUDE [machine-learning-missing-ui](../../includes/machine-learning-missing-ui.md)]

## Create a real-time inference pipeline

To deploy your pipeline, you must first convert the training pipeline into a real-time inference pipeline. This process removes training components and adds web service inputs and outputs to handle requests.

> [!NOTE]
> Create inference pipeline only supports training pipelines which contain only the designer built-in components and must have a component like **Train Model**  which outputs the trained model.

### Create a real-time inference pipeline

1. On pipeline job detail page, above the pipeline canvas, select **Create inference pipeline** > **Real-time inference pipeline**.

     :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/create-real-time-inference.png" alt-text="Screenshot of create inference pipeline in pipeline job detail page.":::

    Your new pipeline will now look like this:

    :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/real-time-inference-pipeline.png" alt-text="Screenshot showing the expected configuration of the pipeline after preparing it for deployment.":::

    When you select **Create inference pipeline**, several things happen:
    
    * The trained model is stored as a **Dataset** component in the component palette. You can find it under **My Datasets**.
    * Training components like **Train Model** and **Split Data** are removed.
    * The saved trained model is added back into the pipeline.
    * **Web Service Input** and **Web Service Output** components are added. These components show where user data enters the pipeline and where data is returned.

    > [!NOTE]
    > By default, the **Web Service Input** will expect the same data schema as the component output data which connects to the same downstream port as it. In this sample, **Web Service Input** and **Automobile price data (Raw)** connect to the same downstream component, hence **Web Service Input** expect the same data schema as **Automobile price data (Raw)** and target variable column `price` is included in the schema.
    > However, usually When you score the data, you won't know the target variable values. For such case, you can remove the target variable column in the inference pipeline using **Select Columns in Dataset** component. Make sure that the output of **Select Columns in Dataset** removing target variable column is connected to the same port as the output of the **Web Service Input** component.

1. Select **Submit**, and use the same compute target and experiment that you used in part one.

    If this is the first job, it may take up to 20 minutes for your pipeline to finish running. The default compute settings have a minimum node size of 0, which means that the designer must allocate resources after being idle. Repeated pipeline jobs will take less time since the compute resources are already allocated. Additionally, the designer uses cached results for each component to further improve efficiency.

1. Go to the real-time inference pipeline job detail by selecting **Job detail** link in the left pane.

1. Select **Deploy** in the job detail page.

     :::image type="content" source="./media/tutorial-designer-automobile-price-deploy/deploy-in-job-detail-page.png" alt-text="Screenshot showing deploying in job detail page.":::
