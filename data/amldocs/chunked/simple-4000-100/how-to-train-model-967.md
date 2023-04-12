
# [REST API](#tab/restapi)

As part of job submission, the training scripts and data must be uploaded to a cloud storage location that your AzureML workspace can access. 

1. Use the following Azure CLI command to upload the training script. The command specifies the _directory_ that contains the files needed for training, not an individual file. If you'd like to use REST to upload the data instead, see the [Put Blob](/rest/api/storageservices/put-blob) reference:

    ```azurecli
    az storage blob upload-batch -d $AZUREML_DEFAULT_CONTAINER/testjob -s cli/jobs/single-step/scikit-learn/iris/src/ --account-name $AZURE_STORAGE_ACCOUNT
    ```

1. Create a versioned reference to the training data. In this example, the data is already in the cloud and located at `https://azuremlexamples.blob.core.windows.net/datasets/iris.csv`. For more information on referencing data, see [Data in Azure Machine Learning](concept-data.md):

    ```bash
    DATA_VERSION=$RANDOM
    curl --location --request PUT "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/data/iris-data/versions/$DATA_VERSION?api-version=$API_VERSION" \
    --header "Authorization: Bearer $TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
            \"properties\": {
            \"description\": \"Iris dataset\",
            \"dataType\": \"uri_file\",
            \"dataUri\": \"https://azuremlexamples.blob.core.windows.net/datasets/iris.csv\"
        }
    }"
    ```

1. Register a versioned reference to the training script for use with a job. In this example, the script location is the default storage account and container you uploaded to in step 1. The ID of the versioned training code is returned and stored in the `$TRAIN_CODE` variable:

    ```bash
    TRAIN_CODE=$(curl --location --request PUT "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/codes/train-lightgbm/versions/1?api-version=$API_VERSION" \
    --header "Authorization: Bearer $TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
            \"properties\": {
            \"description\": \"Train code\",
            \"codeUri\": \"https://$AZURE_STORAGE_ACCOUNT.blob.core.windows.net/$AZUREML_DEFAULT_CONTAINER/testjob\"
        }
    }" | jq -r '.id')
    ```

1. Create the environment that the cluster will use to run the training script. In this example, we use a curated or ready-made environment provided by AzureML called `AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu`. The following command retrieves a list of the environment versions, with the newest being at the top of the collection. `jq` is used to retrieve the ID of the latest (`[0]`) version, which is then stored into the `$ENVIRONMENT` variable.

    ```bash
    ENVIRONMENT=$(curl --location --request GET "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/environments/AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu/versions?api-version=$API_VERSION" --header "Authorization: Bearer $TOKEN" | jq -r .value[0].id)
    ```

1. Finally, submit the job. The following example shows how to submit the job, reference the training code ID, environment ID, URL for the input data, and the ID of the compute cluster. The job output location will be stored in the `$JOB_OUTPUT` variable:

    > [!TIP]
    > The job name must be unique. In this example, `uuidgen` is used to generate a unique value for the name.

    ```bash
    run_id=$(uuidgen)
    curl --location --request PUT "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/jobs/$run_id?api-version=$API_VERSION" \
    --header "Authorization: Bearer $TOKEN" \
    --header "Content-Type: application/json" \
    --data-raw "{
        \"properties\": {
            \"jobType\": \"Command\",
            \"codeId\": \"$TRAIN_CODE\",
            \"command\": \"python main.py --iris-csv \$AZURE_ML_INPUT_iris\",
            \"environmentId\": \"$ENVIRONMENT\",
            \"inputs\": {
                \"iris\": {
                    \"jobInputType\": \"uri_file\",
                    \"uri\": \"https://azuremlexamples.blob.core.windows.net/datasets/iris.csv\"
                }
            },
            \"experimentName\": \"lightgbm-iris\",
            \"computeId\": \"/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/computes/$COMPUTE_NAME\"
        }
    }"
    ```
