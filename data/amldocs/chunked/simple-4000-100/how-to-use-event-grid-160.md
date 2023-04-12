1. Select __Send an email__ and fill in the parameters. In the subject, you can include the __Event Type__ and __Topic__ to help filter events. You can also include a link to the workspace page for runs in the message body. 

    ![Screenshot shows the Send an email dialog box with Topic and Event Type added to the subject line from the list to the right.](./media/how-to-use-event-grid/configure-email-body.png)

1. To save this action, select **Save As** on the left corner of the page. From the right bar  that appears, confirm creation of this action.

    ![Screenshot shows the Save As and Create buttons in the Logic Apps Designer.](./media/how-to-use-event-grid/confirm-logic-app-create.png)


### Example: Data drift triggers retraining

> [!IMPORTANT]
> This example relies on a feature (data drift) that is only available when using Azure Machine Learning SDK v1 or Azure CLI extension v1 for Azure Machine Learning. For more information, see [What is Azure ML CLI & SDK v2](concept-v2.md).

Models go stale over time, and not remain useful in the context it is running in. One way to tell if it's time to retrain the model is detecting data drift. 

This example shows how to use event grid with an Azure Logic App to trigger retraining. The example triggers an Azure Data Factory pipeline when data drift occurs between a model's training and serving datasets.

Before you begin, perform the following actions:

* Set up a dataset monitor to [detect data drift (SDK/CLI v1)](v1/how-to-monitor-datasets.md) in a workspace
* Create a published [Azure Data Factory pipeline](../data-factory/index.yml).

In this example, a simple Data Factory pipeline is used to copy files into a blob store and run a published Machine Learning pipeline. For more information on this scenario, see how to set up a [Machine Learning step in Azure Data Factory](../data-factory/transform-data-machine-learning-service.md)

:::image type="content" source="./media/how-to-use-event-grid/adf-mlpipeline-stage.png" alt-text="Screenshot showing the training pipeline in Azure Data Factory.":::

1. Start with creating the logic app. Go to the [Azure portal](https://portal.azure.com), search for Logic Apps, and select create.

    ![search-logic-app](./media/how-to-use-event-grid/search-for-logic-app.png)

1. Fill in the requested information. To simplify the experience, use the same subscription and resource group as your Azure Data Factory Pipeline and Azure Machine Learning workspace.

    ![Screenshot shows the Logic App Create pane.](./media/how-to-use-event-grid/set-up-logic-app-for-adf.png)

1. Once you have created the logic app, select __When an Event Grid resource event occurs__. 

    ![Screenshot shows the Logic Apps Designer with Start with a common trigger options, including When an Event Grid resource event occurs.](./media/how-to-use-event-grid/select-event-grid-trigger.png)

1. Login and fill in the details for the event. Set the __Resource Name__ to the workspace name. Set the __Event Type__ to __DatasetDriftDetected__.

    :::image type="content" source="./media/how-to-use-event-grid/login-and-add-event.png" alt-text="Screenshot showing the data drift event type item.":::

1. Add a new step, and search for __Azure Data Factory__. Select __Create a pipeline run__. 

    ![Screenshot shows the Choose an action pane with Create a pipeline run selected.](./media/how-to-use-event-grid/create-adfpipeline-run.png)

1. Login and specify the published Azure Data Factory pipeline to run.

    ![Screenshot shows the Create a pipeline run pane with various values.](./media/how-to-use-event-grid/specify-adf-pipeline.png)

1. Save and create the logic app using the **save** button on the top left of the page. To view your app, go to your workspace in the [Azure portal](https://portal.azure.com) and click on **Events**.

    ![Screenshot shows events with the Logic App highlighted.](./media/how-to-use-event-grid/show-logic-app-webhook.png)

Now the data factory pipeline is triggered when drift occurs. View details on your data drift run and machine learning pipeline in [Azure Machine Learning studio](https://ml.azure.com). 
