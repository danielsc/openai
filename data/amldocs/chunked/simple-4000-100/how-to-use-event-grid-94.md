* Generic webhooks, which may be hosted on the Azure platform or elsewhere

## Set up in Azure portal

1. Open the [Azure portal](https://portal.azure.com) and go to your Azure Machine Learning workspace.

1. From the left bar, select __Events__ and then select **Event Subscriptions**. 

    :::image type="content" source="./media/how-to-use-event-grid/select-event.png" alt-text="Screenshot showing the Event Subscription selection.":::

1. Select the event type to consume. For example, the following screenshot has selected __Model registered__, __Model deployed__, __Run completed__, and __Dataset drift detected__:

    :::image type="content" source="./media/how-to-use-event-grid/add-event-type-updated.png" alt-text="Screenshot of the Create Event Subscription form.":::

1. Select the endpoint to publish the event to. In the following screenshot, __Event hub__ is the selected endpoint:

    ![Screenshot shows the Create Event Subscription pane with Select Event Hub open.](./media/how-to-use-event-grid/select-event-handler.png)

Once you have confirmed your selection, click __Create__. After configuration, these events will be pushed to your endpoint.


### Set up with the CLI

You can either install the latest [Azure CLI](/cli/azure/install-azure-cli), or use the Azure Cloud Shell that is provided as part of your Azure subscription.

To install the Event Grid extension, use the following command from the CLI:

```azurecli-interactive
az add extension --name eventgrid
```

The following example demonstrates how to select an Azure subscription and creates e a new event subscription for Azure Machine Learning:

```azurecli-interactive
# Select the Azure subscription that contains the workspace
az account set --subscription "<name or ID of the subscription>"

# Subscribe to the machine learning workspace. This example uses EventHub as a destination. 
az eventgrid event-subscription create --name {eventGridFilterName} \
  --source-resource-id /subscriptions/{subId}/resourceGroups/{RG}/providers/Microsoft.MachineLearningServices/workspaces/{wsName} \
  --endpoint-type eventhub \
  --endpoint /subscriptions/{SubID}/resourceGroups/TestRG/providers/Microsoft.EventHub/namespaces/n1/eventhubs/EH1 \
  --included-event-types Microsoft.MachineLearningServices.ModelRegistered \
  --subject-begins-with "models/mymodelname"
```

## Examples

### Example: Send email alerts

Use [Azure Logic Apps](../logic-apps/index.yml) to configure emails for all your events. Customize with conditions and specify recipients to enable collaboration and awareness across teams working together.

1. In the Azure portal, go to your Azure Machine Learning workspace and select the events tab from the left bar. From here, select __Logic apps__. 

    :::image type="content" source="./media/how-to-use-event-grid/select-logic-ap.png" alt-text="Screenshot showing the Logic Apps selection.":::

1. Sign into the Logic App UI and select Machine Learning service as the topic type. 

    ![Screenshot shows the When a resource event occurs dialog box with machine learning selected as a resource type.](./media/how-to-use-event-grid/select-topic-type.png)

1. Select which event(s) to be notified for. For example, the following screenshot __RunCompleted__.

    :::image type="content" source="./media/how-to-use-event-grid/select-event-runcomplete.png" alt-text="Screenshot showing the Machine Learning service as the resource type.":::

1. Next, add a step to consume this event and search for email. There are several different mail accounts you can use to receive events. You can also configure conditions on when to send an email alert.

    ![Screenshot shows the Choose an action dialog box with email entered in the search line.](./media/how-to-use-event-grid/select-email-action.png)

1. Select __Send an email__ and fill in the parameters. In the subject, you can include the __Event Type__ and __Topic__ to help filter events. You can also include a link to the workspace page for runs in the message body. 
