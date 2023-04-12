    | `endpoint_uri`        | The endpoint scoring URI  | `https://<endpoint_name>.<region>.inference.ml.azure.com/jobs` |
    
    > [!IMPORTANT]
    > `endpoint_uri` is the URI of the endpoint you are trying to execute. The endpoint must have a default deployment configured.

    > [!TIP]
    > Use the values configured at [Authenticating against batch endpoints](#authenticating-against-batch-endpoints).

## Add the trigger

We want to trigger the Logic App each time a new file is created in a given folder (data asset) of a Storage Account. The Logic App will also use the information of the event to invoke the batch endpoint and passing the specific file to be processed.

1. On the workflow designer, under the search box, select **Built-in**.

1. In the search box, enter **event grid**, and select the trigger named **When a resource event occurs**.

1. Configure the trigger as follows:

   | Property | Value | Description |
   |----------|-------|-------------|
   | **Subscription** | Your subscription name | The subscription where the Azure Storage Account is placed. |
   | **Resource Type** | `Microsoft.Storage.StorageAccounts` | The resource type emitting the events. |
   | **Resource Name** | Your storage account name | The name of the Storage Account where the files will be generated. |
   | **Event Type Item** | `Microsoft.Storage.BlobCreated` | The event type. |

1. Click on __Add new parameter__ and select __Prefix Filter__. Add the value `/blobServices/default/containers/<container_name>/blobs/<path_to_data_folder>`.

   > [!IMPORTANT]
   > __Prefix Filter__ allows Event Grid to only notify the workflow when a blob is created in the specific path we indicated. In this case, we are assumming that files will be created by some external process in the folder `<path_to_data_folder>` inside the container `<container_name>` in the selected Storage Account. Configure this parameter to match the location of your data. Otherwise, the event will be fired for any file created at any location of the Storage Account. See [Event filtering for Event Grid](../event-grid/event-filtering.md) for more details.

   The trigger will look as follows:
   
   :::image type="content" source="./media/how-to-use-event-grid-batch/create-trigger.png" alt-text="Screenshot of the trigger activity of the Logic App.":::

## Configure the actions

1. Click on __+ New step__. 

1. On the workflow designer, under the search box, select **Built-in** and then click on __HTTP__:

1. Configure the action as follows:

   | Property | Value | Notes |
   |----------|-------|-------------|
   | **Method** | `POST` | The HTTP method |
   | **URI** | `concat('https://login.microsoftonline.com/', parameters('tenant_id'), '/oauth2/token')` | Click on __Add dynamic context__, then __Expression__, to enter this expression. |
   | **Headers** | `Content-Type` with value `application/x-www-form-urlencoded` |  |
   | **Body**    | `concat('grant_type=client_credentials&client_id=', parameters('client_id'), '&client_secret=', parameters('client_secret'), '&resource=https://ml.azure.com')` | Click on __Add dynamic context__, then __Expression__, to enter this expression. |
   
   The action will look as follows:
   
   :::image type="content" source="./media/how-to-use-event-grid-batch/authorize.png" alt-text="Screenshot of the authorize activity of the Logic App.":::

1. Click on __+ New step__. 

1. On the workflow designer, under the search box, select **Built-in** and then click on __HTTP__:

1. Configure the action as follows:

   | Property | Value | Notes |
   |----------|-------|-------------|
   | **Method** | `POST` | The HTTP method |
   | **URI** | `endpoint_uri` | Click on __Add dynamic context__, then select it under `parameters`. |
   | **Headers** | `Content-Type` with value `application/json` |  |
   | **Headers** | `Authorization` with value `concat('Bearer ', body('Authorize')['access_token'])` | Click on __Add dynamic context__, then __Expression__, to enter this expression. |
