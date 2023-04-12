
- If you want to manage your data as Azure ML registered V2 data asset as `uri_folder`, you can follow the two steps below:

    1. Create the V2 data asset:

    ```rest-api
    DATA_NAME="mnist"
    DATA_VERSION=$RANDOM
    
    response=$(curl --location --request PUT https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/data/$DATA_NAME/versions/$DATA_VERSION?api-version=$API_VERSION \
    --header "Content-Type: application/json" \
    --header "Authorization: Bearer $TOKEN" \
    --data-raw "{
        \"properties\": {
            \"dataType\": \"uri_folder\",
      \"dataUri\": \"https://pipelinedata.blob.core.windows.net/sampledata/mnist\",
      \"description\": \"Mnist data asset\"
        }
    }")
    ```

    2. Reference the data asset in the batch scoring job:

    ```rest-api
    response=$(curl --location --request POST $SCORING_URI \
    --header "Authorization: Bearer $SCORING_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
        \"properties\": {
            \"InputData\": {
                \"mnistInput\": {
                    \"JobInputType\" : \"UriFolder\",
                    \"Uri": \"azureml://locations/$LOCATION_NAME/workspaces/$WORKSPACE_NAME/data/$DATA_NAME/versions/$DATA_VERSION/\"
                }
            }
        }
    }")
    
    JOB_ID=$(echo $response | jq -r '.id')
    JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
    ```

- If your data is a single file publicly available from the web, you can use the following snippet:

    ```rest-api
    response=$(curl --location --request POST $SCORING_URI \
    --header "Authorization: Bearer $SCORING_TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
        \"properties\": {
            \"InputData\": {
                \"mnistInput\": {
                    \"JobInputType\" : \"UriFile\",
                    \"Uri": \"https://pipelinedata.blob.core.windows.net/sampledata/mnist/0.png\"
                }
            }
        }
    }")
    
    JOB_ID=$(echo $response | jq -r '.id')
    JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
    ```

> [!NOTE]
> We strongly recommend using the latest REST API version for batch scoring.
> - If you want to use local data, you can upload it to Azure Machine Learning registered datastore and use REST API for Cloud data.
> - If you are using existing V1 FileDataset for batch endpoint, we recommend migrating them to V2 data assets and refer to them directly when invoking batch endpoints. Currently only data assets of type `uri_folder` or `uri_file` are supported. Batch endpoints created with GA CLIv2 (2.4.0 and newer) or GA REST API (2022-05-01 and newer) will not support V1 Dataset.
> - You can also extract the URI or path on datastore extracted from V1 FileDataset by using `az ml dataset show` command with `--query` parameter and use that information for invoke.
> - While Batch endpoints created with earlier APIs will continue to support V1 FileDataset, we will be adding further V2 data assets support with the latest API versions for even more usability and flexibility. For more information on V2 data assets, see [Work with data using SDK v2](how-to-read-write-data-v2.md). For more information on the new V2 experience, see [What is v2](concept-v2.md).

#### Configure the output location and overwrite settings

The batch scoring results are by default stored in the workspace's default blob store within a folder named by job name (a system-generated GUID). You can configure where to store the scoring outputs when you invoke the batch endpoint. Use `OutputData` to configure the output file path on an Azure Machine Learning registered datastore. `OutputData` has `JobOutputType` and `Uri` keys. `UriFile` is the only supported value for `JobOutputType`. The syntax for `Uri` is the same as that of `InputData`, i.e., `azureml://datastores/<datastore-name>/paths/<path-on-datastore>/<file-name>`.
