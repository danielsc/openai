   
3. Create a deployment definition

    # [Azure CLI](#tab/azure-cli)
    
    __mnist-keras-deployment.yml__
    
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
name: mnist-keras-dpl
description: A deployment using Keras with TensorFlow to solve the MNIST classification dataset.
endpoint_name: mnist-batch
model: 
  path: ./mnist-keras/model/
code_configuration:
  code: ./mnist-keras/code/
  scoring_script: batch_driver.py
environment:
  conda_file: ./mnist-keras/environment/conda.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
compute: azureml:batch-cluster
resources:
  instance_count: 1
max_concurrency_per_instance: 2
mini_batch_size: 10
output_action: append_row
output_file_name: predictions.csv
```
    
    # [Python](#tab/python)
    
    ```python
    deployment = BatchDeployment(
        name="non-mlflow-deployment",
        description="this is a sample non-mlflow deployment",
        endpoint_name=batch_endpoint_name,
        model=model,
        code_path="./mnist-keras/code/",
        scoring_script="batch_driver.py",
        environment=env,
        compute=compute_name,
        instance_count=2,
        max_concurrency_per_instance=2,
        mini_batch_size=10,
        output_action=BatchDeploymentOutputAction.APPEND_ROW,
        output_file_name="predictions.csv",
        retry_settings=BatchRetrySettings(max_retries=3, timeout=30),
        logging_level="info",
    )
    ```
    
    # [Studio](#tab/azure-studio)

    1. Navigate to the __Endpoints__ tab on the side menu.
    1. Select the tab __Batch endpoints__.
    1. Select the existing batch endpoint where you want to add the deployment.
    1. Select __Add deployment__.

        :::image type="content" source="./media/how-to-use-batch-endpoints-studio/add-deployment-option.png" alt-text="Screenshot of add new deployment option.":::

    1. On the model list, select the model `mnist` and select __Next__.
    1. On the deployment configuration page, give the deployment a name.
    1. On __Output action__, ensure __Append row__ is selected.
    1. On __Output file name__, ensure the batch scoring output file is the one you need. Default is `predictions.csv`.
    1. On __Mini batch size__, adjust the size of the files that will be included on each mini-batch. This will control the amount of data your scoring script receives per each batch.
    1. On __Scoring timeout (seconds)__, ensure you're giving enough time for your deployment to score a given batch of files. If you increase the number of files, you usually have to increase the timeout value too. More expensive models (like those based on deep learning), may require high values in this field.
    1. On __Max concurrency per instance__, configure the number of executors you want to have per each compute instance you get in the deployment. A higher number here guarantees a higher degree of parallelization but it also increases the memory pressure on the compute instance. Tune this value altogether with __Mini batch size__.
    1. Once done, select __Next__.
    1. On environment, go to __Select scoring file and dependencies__ and select __Browse__.
    1. Select the scoring script file on `/mnist-keras/code/batch_driver.py`.
    1. On the section __Choose an environment__, select the environment you created a previous step.
    1. Select __Next__.
    1. On the section __Compute__, select the compute cluster you created in a previous step.
    1. On __Instance count__, enter the number of compute instances you want for the deployment. In this case, we'll use 2.
    1. Select __Next__.

1. Create the deployment:

    # [Azure CLI](#tab/azure-cli)
    
    Run the following code to create a batch deployment under the batch endpoint and set it as the default deployment.
    
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
