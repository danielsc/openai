
# [Python](#tab/python)

Use `output_path` to configure any folder in an Azure Machine Learning registered datastore. The syntax for the `--output-path` is the same as `--input` when you're specifying a folder, that is, `azureml://datastores/<datastore-name>/paths/<path-on-datastore>/`. Use `output_file_name=<your-file-name>` to configure a new output file name.

```python
job = ml_client.batch_endpoints.invoke(
    endpoint_name=endpoint_name,
    inputs={ 
        "input": Input(path="https://pipelinedata.blob.core.windows.net/sampledata/mnist", type=AssetTypes.URI_FOLDER) 
    },
    output_path={ 
        "score": Input(path=f"azureml://datastores/workspaceblobstore/paths/{endpoint_name}") 
    },
    output_file_name="predictions.csv"
)
```

# [Studio](#tab/azure-studio)

1. Navigate to the __Endpoints__ tab on the side menu.
1. Select the tab __Batch endpoints__.
1. Select the batch endpoint you just created.
1. Select __Create job__.

    :::image type="content" source="./media/how-to-use-batch-endpoints-studio/create-batch-job.png" alt-text="Screenshot of the create job option to start batch scoring.":::

1. On __Deployment__, select the deployment you want to execute.
1. Select __Next__.
1. Check the option __Override deployment settings__.

    :::image type="content" source="./media/how-to-use-batch-endpoints-studio/overwrite-setting.png" alt-text="Screenshot of the overwrite setting when starting a batch job.":::

1. You can now configure __Output file name__ and some extra properties of the deployment execution. Just this execution will be affected.
1. On __Select data source__, select the data input you want to use.
1. On __Configure output location__, check the option __Enable output configuration__.

    :::image type="content" source="./media/how-to-use-batch-endpoints-studio/configure-output-location.png" alt-text="Screenshot of optionally configuring output location.":::

1. Configure the __Blob datastore__ where the outputs should be placed.


> [!WARNING]
> You must use a unique output location. If the output file exists, the batch scoring job will fail.

> [!IMPORTANT]
> As opposite as for inputs, only Azure Machine Learning data stores running on blob storage accounts are supported for outputs.

## Overwrite deployment configuration per each job

Some settings can be overwritten when invoke to make best use of the compute resources and to improve performance. The following settings can be configured in a per-job basis:

* Use __instance count__ to overwrite the number of instances to request from the compute cluster. For example, for larger volume of data inputs, you may want to use more instances to speed up the end to end batch scoring.
* Use __mini-batch size__  to overwrite the number of files to include on each mini-batch. The number of mini batches is decided by total input file counts and mini_batch_size. Smaller mini_batch_size generates more mini batches. Mini batches can be run in parallel, but there might be extra scheduling and invocation overhead.
* Other settings can be overwritten other settings including __max retries__, __timeout__, and __error threshold__. These settings might impact the end to end batch scoring time for different workloads.

# [Azure CLI](#tab/azure-cli)

```azurecli
az --version

set -e

# <set_variables>
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
export DEPLOYMENT_NAME="<YOUR_DEPLOYMENT_NAME>"
# </set_variables>

export ENDPOINT_NAME=endpt-`echo $RANDOM`
export DEPLOYMENT_NAME="mnist-torch-dpl"

echo "Creating compute"
# <create_compute>
az ml compute create -n batch-cluster --type amlcompute --min-instances 0 --max-instances 5
# </create_compute>

echo "Creating batch endpoint $ENDPOINT_NAME"
# <create_batch_endpoint>
az ml batch-endpoint create --name $ENDPOINT_NAME
# </create_batch_endpoint>

echo "Creating batch deployment nonmlflowdp for endpoint $ENDPOINT_NAME"
# <create_batch_deployment_set_default>
az ml batch-deployment create --file endpoints/batch/mnist-torch-deployment.yml --endpoint-name $ENDPOINT_NAME --set-default
# </create_batch_deployment_set_default>

echo "Showing details of the batch endpoint"
# <check_batch_endpooint_detail>
az ml batch-endpoint show --name $ENDPOINT_NAME
# </check_batch_endpooint_detail>

echo "Showing details of the batch deployment"
# <check_batch_deployment_detail>
az ml batch-deployment show --name $DEPLOYMENT_NAME --endpoint-name $ENDPOINT_NAME
# </check_batch_deployment_detail>

echo "Invoking batch endpoint with public URI (MNIST)"
# <start_batch_scoring_job>
JOB_NAME=$(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://pipelinedata.blob.core.windows.net/sampledata/mnist --input-type uri_folder --query name -o tsv)
# </start_batch_scoring_job>

echo "Showing job detail"
# <show_job_in_studio>
az ml job show -n $JOB_NAME --web
# </show_job_in_studio>

echo "Stream job logs to console"
# <stream_job_logs_to_console>
az ml job stream -n $JOB_NAME
# </stream_job_logs_to_console>

# <check_job_status>
STATUS=$(az ml job show -n $JOB_NAME --query status -o tsv)
echo $STATUS
if [[ $STATUS == "Completed" ]]
then
  echo "Job completed"
elif [[ $STATUS ==  "Failed" ]]
then
  echo "Job failed"
  exit 1
else 
  echo "Job status not failed or completed"
  exit 2
fi
# </check_job_status>

echo "Invoke batch endpoint with specific output file name"
# <start_batch_scoring_job_configure_output_settings>
export OUTPUT_FILE_NAME=predictions_`echo $RANDOM`.csv
JOB_NAME=$(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://pipelinedata.blob.core.windows.net/sampledata/mnist --input-type uri_folder --output-path azureml://datastores/workspaceblobstore/paths/$ENDPOINT_NAME --set output_file_name=$OUTPUT_FILE_NAME --query name -o tsv)
# </start_batch_scoring_job_configure_output_settings>

echo "Invoke batch endpoint with specific overwrites"
# <start_batch_scoring_job_overwrite>
export OUTPUT_FILE_NAME=predictions_`echo $RANDOM`.csv
JOB_NAME=$(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://pipelinedata.blob.core.windows.net/sampledata/mnist --input-type uri_folder --mini-batch-size 20 --instance-count 5 --query name -o tsv)
# </start_batch_scoring_job_overwrite>

echo "Stream job detail"
# <stream_job_logs_to_console>
az ml job stream -n $JOB_NAME
# </stream_job_logs_to_console>

# <check_job_status>
STATUS=$(az ml job show -n $JOB_NAME --query status -o tsv)
echo $STATUS
if [[ $STATUS == "Completed" ]]
then
  echo "Job completed"
elif [[ $STATUS ==  "Failed" ]]
then
  echo "Job failed"
  exit 1
else 
  echo "Job status not failed or completed"
  exit 2
fi
# </check_job_status>

echo "List all jobs under the batch deployment"
# <list_all_jobs>
az ml batch-deployment list-jobs --name $DEPLOYMENT_NAME --endpoint-name $ENDPOINT_NAME --query [].name
# </list_all_jobs>

echo "Create a new batch deployment (mnist-keras-dpl), not setting it as default this time"
# <create_new_deployment_not_default>
az ml batch-deployment create --file endpoints/batch/mnist-keras-deployment.yml --endpoint-name $ENDPOINT_NAME
# </create_new_deployment_not_default>

echo "Invoke batch endpoint with public data"
# <test_new_deployment>
DEPLOYMENT_NAME="mnist-keras-dpl"
JOB_NAME=$(az ml batch-endpoint invoke --name $ENDPOINT_NAME --deployment-name $DEPLOYMENT_NAME --input https://pipelinedata.blob.core.windows.net/sampledata/mnist --input-type uri_folder --query name -o tsv)
# </test_new_deployment>

echo "Show job detail"
# <show_job_in_studio>
az ml job show -n $JOB_NAME --web
# </show_job_in_studio>

echo "Stream job logs to console"
# <stream_job_logs_to_console>
az ml job stream -n $JOB_NAME
# </stream_job_logs_to_console>

# <check_job_status>
STATUS=$(az ml job show -n $JOB_NAME --query status -o tsv)
echo $STATUS
if [[ $STATUS == "Completed" ]]
then
  echo "Job completed"
elif [[ $STATUS ==  "Failed" ]]
then
  echo "Job failed"
  exit 1
else 
  echo "Job status not failed or completed"
  exit 2
fi
# </check_job_status>

echo "Update the batch deployment as default for the endpoint"
# <update_default_deployment>
az ml batch-endpoint update --name $ENDPOINT_NAME --set defaults.deployment_name=$DEPLOYMENT_NAME
# </update_default_deployment>

echo "Verify default deployment. In this example, it should be mlflowdp."
# <verify_default_deployment>
az ml batch-endpoint show --name $ENDPOINT_NAME --query "{Name:name, Defaults:defaults}"
# </verify_default_deployment>

echo "Invoke batch endpoint with the new default deployment with public URI"
# <test_new_default_deployment>
JOB_NAME=$(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://pipelinedata.blob.core.windows.net/sampledata/mnist --input-type uri_folder --query name -o tsv)
# </test_new_default_deployment>

echo "Stream job logs to console"
# <stream_job_logs_to_console>
az ml job stream -n $JOB_NAME
# </stream_job_logs_to_console>

# <check_job_status>
STATUS=$(az ml job show -n $JOB_NAME --query status -o tsv)
echo $STATUS
if [[ $STATUS == "Completed" ]]
then
  echo "Job completed"
elif [[ $STATUS ==  "Failed" ]]
then
  echo "Job failed"
  exit 1
else 
  echo "Job status not failed or completed"
  exit 2
fi
# </check_job_status>

echo "Get Scoring URI"
# <get_scoring_uri>
SCORING_URI=$(az ml batch-endpoint show --name $ENDPOINT_NAME --query scoring_uri -o tsv)
# </get_scoring_uri>

echo "Get Token"
# <get_token>
AUTH_TOKEN=$(az account get-access-token --resource https://ml.azure.com --query accessToken -o tsv)
# </get_token>

echo "Invoke batch endpoint with REST API call"
# <start_batch_scoring_job_rest>
RESPONSE=$(curl --location --request POST "$SCORING_URI" \
--header "Authorization: Bearer $AUTH_TOKEN" \
--header "Content-Type: application/json" \
--data-raw "{
  \"properties\": {
    \"dataset\": {
      \"dataInputType\": \"DataUrl\",
      \"Path\": \"https://pipelinedata.blob.core.windows.net/sampledata/mnist\"
    }
  }
}")
# </start_batch_scoring_job_rest>

# <check_job_status_rest>
# define how to wait  
wait_for_completion () {
    operation_id=$1
    access_token=$2
    status="unknown"

    while [[ $status != "Completed" && $status != "Succeeded" && $status != "Failed" && $status != "Canceled" ]]
    do
        echo "Getting operation status from: $operation_id"
        operation_result=$(curl --location --request GET $operation_id --header "Authorization: Bearer $access_token")
        # TODO error handling here
        status=$(echo $operation_result | jq -r '.status')
        if [[ -z $status || $status == "null" ]]
        then
            status=$(echo $operation_result | jq -r '.properties.status')
        fi

        # Fail early if job submission failed and there is nothing to poll on
        if [[ -z $status || $status == "null" ]]
        then
            echo "No status found on operation, setting to failed."
            status="Failed"
        fi

        echo "Current operation status: $status"
        sleep 10
    done

    if [[ $status == "Failed" ]]
    then
        error=$(echo $operation_result | jq -r '.error')
        echo "Error: $error"
    fi
}

# get job from invoke response and wait for completion
JOB_ID=$(echo $RESPONSE | jq -r '.id')
JOB_ID_SUFFIX=$(echo ${JOB_ID##/*/})
wait_for_completion $SCORING_URI/$JOB_ID_SUFFIX $AUTH_TOKEN
# </check_job_status_rest>

# <delete_deployment>
az ml batch-deployment delete --name nonmlflowdp --endpoint-name $ENDPOINT_NAME --yes
# </delete_deployment>

# <delete_endpoint>
az ml batch-endpoint delete --name $ENDPOINT_NAME --yes
# </delete_endpoint>

```
