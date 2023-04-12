    > See how the path `paths` is appended to the resource id of the data store to indicate that what follows is a path inside of it.

    > [!TIP]
    > You can also use `azureml://datastores/<data-store>/paths/<data-path>` as a way to indicate the input.

1. Run the deployment:

    # [Azure CLI](#tab/cli)
   
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input $INPUT_PATH)
    ```
   
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

## Input data from Azure Storage Accounts

Azure Machine Learning batch endpoints can read data from cloud locations in Azure Storage Accounts, both public and private. Use the following steps to run a batch endpoint job using data stored in a storage account:

> [!NOTE]
> Check the section [Security considerations when reading data](#security-considerations-when-reading-data) for learn more about additional configuration required to successfully read data from storage accoutns.

1. Create a data input:

    # [Azure CLI](#tab/cli)

    ```azurecli
    INPUT_DATA = "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
    ```

    If your data is a file:

    ```azurecli
    INPUT_DATA = "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
    ```

    # [Python](#tab/sdk)

    ```python
    input = Input(
        type=AssetTypes.URI_FOLDER, 
        path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
    )
    ```

    If your data is a file, change `type=AssetTypes.URI_FILE`:

    ```python
    input = Input(
        type=AssetTypes.URI_FILE,
        path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
    )
    ```

    # [REST](#tab/rest)

    __Body__

   ```json
   {
       "properties": {
           "InputData": {
               "mnistinput": {
                   "JobInputType" : "UriFolder",
                   "Uri": "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
               }
           }
       }
   }
   ```

   If your data is a file, change `JobInputType`:

   __Body__

   ```json
   {
       "properties": {
           "InputData": {
               "mnistinput": {
                   "JobInputType" : "UriFolder",
                   "Uri": "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
               }
           }
       }
   }
   ```

1. Run the deployment:

    # [Azure CLI](#tab/cli)
    
    If your data is a folder, use `--input-type uri_folder`:
    
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input-type uri_folder --input $INPUT_DATA)
    ```

    If your data is a file, use `--input-type uri_file`:

    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input-type uri_file --input $INPUT_DATA)
    ```

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
    

## Security considerations when reading data

Batch endpoints ensure that only authorized users are able to invoke batch deployments and generate jobs. However, depending on how the input data is configured, other credentials may be used to read the underlying data. Use the following table to understand which credentials are used and any additional requirements.

| Data input type              | Credential in store             | Credentials used                                              | Access granted by |
