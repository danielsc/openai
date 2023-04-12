

### Use different CPU and GPU instance types

The preceding YAML uses a general-purpose type (`Standard_DS2_v2`) and a non-GPU Docker image (in the YAML, see the `image` attribute). For GPU compute, choose a GPU compute type SKU and a GPU Docker image.

For supported general-purpose and GPU instance types, see [Managed online endpoints supported VM SKUs](reference-managed-online-endpoints-vm-sku-list.md). For a list of Azure Machine Learning CPU and GPU base images, see [Azure Machine Learning base images](https://github.com/Azure/AzureML-Containers).

> [!NOTE]
> To use Kubernetes instead of managed endpoints as a compute target, see [Introduction to Kubernetes compute target](./how-to-attach-kubernetes-anywhere.md)

### Use more than one model

Currently, you can specify only one model per deployment in the YAML. If you've more than one model, when you register the model, copy all the models as files or subdirectories into a folder that you use for registration. In your scoring script, use the environment variable `AZUREML_MODEL_DIR` to get the path to the model root folder. The underlying directory structure is retained. For an example of deploying multiple models to one deployment, see [Deploy multiple models to one deployment](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/minimal/multimodel).

## Understand the scoring script

> [!TIP]
> The format of the scoring script for online endpoints is the same format that's used in the preceding version of the CLI and in the Python SDK.

# [Azure CLI](#tab/azure-cli)
As noted earlier, the script specified in `code_configuration.scoring_script` must have an `init()` function and a `run()` function. 

# [Python](#tab/python)
As noted earlier, the script specified in `CodeConfiguration(scoring_script="score.py")` must have an `init()` function and a `run()` function. 

# [ARM template](#tab/arm)

As noted earlier, the script specified in `code_configuration.scoring_script` must have an `init()` function and a `run()` function. This example uses the [score.py file](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/model-1/onlinescoring/score.py). 

When using a template for deployment, you must first upload the scoring file(s) to an Azure Blob store, and then register it:

1. The following example uses the Azure CLI command `az storage blob upload-batch` to upload the scoring file(s):

```azurecli
set -x

#<get_access_token>
TOKEN=$(az account get-access-token --query accessToken -o tsv)
#</get_access_token>

# <create_variables>
SUBSCRIPTION_ID=$(az account show --query id | tr -d '\r"')
LOCATION=$(az ml workspace show --query location | tr -d '\r"')
RESOURCE_GROUP=$(az group show --query name | tr -d '\r"')
WORKSPACE=$(az configure -l | jq -r '.[] | select(.name=="workspace") | .value')
#</create_variables>

# <set_endpoint_name>
export ENDPOINT_NAME=endpoint-`echo $RANDOM`
# </set_endpoint_name>

#<api_version>
API_VERSION="2022-05-01"
#</api_version>

echo -e "Using:\nSUBSCRIPTION_ID=$SUBSCRIPTION_ID\nLOCATION=$LOCATION\nRESOURCE_GROUP=$RESOURCE_GROUP\nWORKSPACE=$WORKSPACE"

# define how to wait  
wait_for_completion () {
    operation_id=$1
    status="unknown"

    if [[ $operation_id == "" || -z $operation_id  || $operation_id == "null" ]]; then
        echo "operation id cannot be empty"
        exit 1
    fi

    while [[ $status != "Succeeded" && $status != "Failed" ]]
    do
        echo "Getting operation status from: $operation_id"
        operation_result=$(curl --location --request GET $operation_id --header "Authorization: Bearer $TOKEN")
        # TODO error handling here
        status=$(echo $operation_result | jq -r '.status')
        echo "Current operation status: $status"
        sleep 5
    done

    if [[ $status == "Failed" ]]
    then
        error=$(echo $operation_result | jq -r '.error')
        echo "Error: $error"
    fi
}

# <get_storage_details>
# Get values for storage account
response=$(curl --location --request GET "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/datastores?api-version=$API_VERSION&isDefault=true" \
--header "Authorization: Bearer $TOKEN")
AZUREML_DEFAULT_DATASTORE=$(echo $response | jq -r '.value[0].name')
AZUREML_DEFAULT_CONTAINER=$(echo $response | jq -r '.value[0].properties.containerName')
export AZURE_STORAGE_ACCOUNT=$(echo $response | jq -r '.value[0].properties.accountName')
# </get_storage_details>

# <upload_code>
az storage blob upload-batch -d $AZUREML_DEFAULT_CONTAINER/score -s cli/endpoints/online/model-1/onlinescoring --account-name $AZURE_STORAGE_ACCOUNT
# </upload_code>

# <create_code>
az deployment group create -g $RESOURCE_GROUP \
--template-file arm-templates/code-version.json \
--parameters \
workspaceName=$WORKSPACE \
codeAssetName="score-sklearn" \
codeUri="https://$AZURE_STORAGE_ACCOUNT.blob.core.windows.net/$AZUREML_DEFAULT_CONTAINER/score"
# </create_code>

# <upload_model>
az storage blob upload-batch -d $AZUREML_DEFAULT_CONTAINER/model -s cli/endpoints/online/model-1/model --account-name $AZURE_STORAGE_ACCOUNT
# </upload_model>

# <create_model>
az deployment group create -g $RESOURCE_GROUP \
--template-file arm-templates/model-version.json \
--parameters \
workspaceName=$WORKSPACE \
modelAssetName="sklearn" \
modelUri="azureml://subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/workspaces/$WORKSPACE/datastores/$AZUREML_DEFAULT_DATASTORE/paths/model/sklearn_regression_model.pkl"
# </create_model>

# <read_condafile>
CONDA_FILE=$(cat cli/endpoints/online/model-1/environment/conda.yml)
# </read_condafile>

# <create_environment>
ENV_VERSION=$RANDOM
az deployment group create -g $RESOURCE_GROUP \
--template-file arm-templates/environment-version.json \
--parameters \
workspaceName=$WORKSPACE \
environmentAssetName=sklearn-env \
environmentAssetVersion=$ENV_VERSION \
dockerImage=mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1 \
condaFile="$CONDA_FILE"
# </create_environment>

# <create_endpoint>
az deployment group create -g $RESOURCE_GROUP \
--template-file arm-templates/online-endpoint.json \
--parameters \
workspaceName=$WORKSPACE \
onlineEndpointName=$ENDPOINT_NAME \
identityType=SystemAssigned \
authMode=AMLToken \
location=$LOCATION
# </create_endpoint>

# <get_endpoint>
response=$(curl --location --request GET "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/onlineEndpoints/$ENDPOINT_NAME?api-version=$API_VERSION" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer $TOKEN")

operation_id=$(echo $response | jq -r '.properties' | jq -r '.properties' | jq -r '.AzureAsyncOperationUri')
wait_for_completion $operation_id
# </get_endpoint>

# <create_deployment>
resourceScope="/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices"
az deployment group create -g $RESOURCE_GROUP \
 --template-file arm-templates/online-endpoint-deployment.json \
 --parameters \
 workspaceName=$WORKSPACE \
 location=$LOCATION \
 onlineEndpointName=$ENDPOINT_NAME \
 onlineDeploymentName=blue \
 codeId="$resourceScope/workspaces/$WORKSPACE/codes/score-sklearn/versions/1" \
 scoringScript=score.py \
 environmentId="$resourceScope/workspaces/$WORKSPACE/environments/sklearn-env/versions/$ENV_VERSION" \
 model="$resourceScope/workspaces/$WORKSPACE/models/score-sklearn/versions/1" \
 endpointComputeType=Managed \
 skuName=Standard_F2s_v2 \
 skuCapacity=1
 # </create_deployment>

# <get_deployment>
response=$(curl --location --request GET "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/onlineEndpoints/$ENDPOINT_NAME/deployments/blue?api-version=$API_VERSION" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer $TOKEN")

operation_id=$(echo $response | jq -r '.properties' | jq -r '.properties' | jq -r '.AzureAsyncOperationUri')
wait_for_completion $operation_id

scoringUri=$(echo $response | jq -r '.properties' | jq -r '.scoringUri')
# </get_endpoint>

# <get_endpoint_access_token>
response=$(curl -H "Content-Length: 0" --location --request POST "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/onlineEndpoints/$ENDPOINT_NAME/token?api-version=$API_VERSION" \
--header "Authorization: Bearer $TOKEN")
accessToken=$(echo $response | jq -r '.accessToken')
# </get_endpoint_access_token>

# <score_endpoint>
curl --location --request POST $scoringUri \
--header "Authorization: Bearer $accessToken" \
--header "Content-Type: application/json" \
--data-raw @cli/endpoints/online/model-1/sample-request.json
# </score_endpoint>

# <get_deployment_logs>
curl --location --request POST "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/onlineEndpoints/$ENDPOINT_NAME/deployments/blue/getLogs?api-version=$API_VERSION" \
--header "Authorization: Bearer $TOKEN" \
--header "Content-Type: application/json" \
--data-raw "{ \"tail\": 100 }"
# </get_deployment_logs>

# <delete_endpoint>
curl --location --request DELETE "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/onlineEndpoints/$ENDPOINT_NAME?api-version=$API_VERSION" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer $TOKEN" || true
# </delete_endpoint>

```
