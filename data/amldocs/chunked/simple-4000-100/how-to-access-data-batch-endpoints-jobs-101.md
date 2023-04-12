
    # [Python](#tab/sdk)

    ```python
    input = Input(type=AssetTypes.URI_FOLDER, path=heart_dataset_unlabeled.id)
    ```

    # [REST](#tab/rest)

    __Body__

    ```json
    {
        "properties": {
            "InputData": {
                "mnistinput": {
                    "JobInputType" : "UriFolder",
                    "Uri": "azureml://locations/<location>/workspaces/<workspace>/data/<dataset_name>/versions/labels/latest"
                }
            }
        }
    }
    ```

    > [!NOTE]
    > Data assets ID would look like `/subscriptions/<subscription>/resourcegroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/data/<data-asset>/versions/<version>`.


1. Run the deployment:

    # [Azure CLI](#tab/cli)
   
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input $DATASET_ID)
    ```

    > [!TIP]
    > You can also use `--input azureml:/<dataasset_name>@latest` as a way to indicate the input.

    # [Python](#tab/sdk)
   
    ```python
    job = ml_client.batch_endpoints.invoke(
       endpoint_name=endpoint.name,
       input=input,
    )
    ```

   # [REST](#tab/rest)

   __Request__
    
    ```http
    POST jobs HTTP/1.1
    Host: <ENDPOINT_URI>
    Authorization: Bearer <TOKEN>
    Content-Type: application/json
    ```

## Input data from data stores

Data from Azure Machine Learning registered data stores can be directly referenced by batch deployments jobs. In this example, we're going to first upload some data to the default data store in the Azure Machine Learning workspace and then run a batch deployment on it. Follow these steps to run a batch endpoint job using data stored in a data store:

1. Let's get access to the default data store in the Azure Machine Learning workspace. If your data is in a different store, you can use that store instead. There's no requirement of using the default data store. 

    # [Azure CLI](#tab/cli)

    ```azurecli
    DATASTORE_ID=$(az ml datastore show -n workspaceblobstore | jq -r '.id')
    ```
    
    > [!NOTE]
    > Data stores ID would look like `/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/datastores/<data-store>`.

    # [Python](#tab/sdk)

    ```python
    default_ds = ml_client.datastores.get_default()
    ```

    # [REST](#tab/rest)

    Use the Azure ML CLI, Azure ML SDK for Python, or Studio to get the data store information.
    
    
    > [!TIP]
    > The default blob data store in a workspace is called __workspaceblobstore__. You can skip this step if you already know the resource ID of the default data store in your workspace.

1. We'll need to upload some sample data to it. This example assumes you've uploaded the sample data included in the repo in the folder `sdk/python/endpoints/batch/heart-classifier/data` in the folder `heart-classifier/data` in the blob storage account. Ensure you have done that before moving forward.

1. Create a data input:

    # [Azure CLI](#tab/cli)
    
    Let's place the file path in the following variable:

    ```azurecli
    DATA_PATH="heart-disease-uci-unlabeled"
    INPUT_PATH="$DATASTORE_ID/paths/$DATA_PATH"
    ```

    # [Python](#tab/sdk)

    ```python
    data_path = "heart-classifier/data"
    input = Input(type=AssetTypes.URI_FOLDER, path=f"{default_ds.id}/paths/{data_path})
    ```

    # [REST](#tab/rest)

    __Body__

    ```json
    {
        "properties": {
            "InputData": {
                "mnistinput": {
                    "JobInputType" : "UriFolder",
                    "Uri": "azureml:/subscriptions/<subscription>/resourceGroups/<resource-group/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/datastores/<data-store>/paths/<data-path>"
                }
            }
        }
    }
    ```
    
    > [!NOTE]
    > See how the path `paths` is appended to the resource id of the data store to indicate that what follows is a path inside of it.
