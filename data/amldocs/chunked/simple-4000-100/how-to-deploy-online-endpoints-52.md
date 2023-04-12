> While the Azure CLI and CLI extension for machine learning are used in these steps, they're not the main focus. they're used more as utilities, passing templates to Azure and checking the status of template deployments.

[!INCLUDE [basic prereqs cli](../../includes/machine-learning-cli-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

> [!IMPORTANT]
> The examples in this document assume that you are using the Bash shell. For example, from a Linux system or [Windows Subsystem for Linux](/windows/wsl/about). 


## Prepare your system

# [Azure CLI](#tab/azure-cli)

### Clone the sample repository

To follow along with this article, first clone the [samples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, run the following code to go to the samples directory:

```azurecli
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples
cd cli
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository, which reduces time to complete the operation.

### Set an endpoint name

To set your endpoint name, run the following command (replace `YOUR_ENDPOINT_NAME` with a unique name).

For Unix, run this command:

```azurecli
set -e

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --local -n $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --local -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME --local
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --local --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --local --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_endpoint>
az ml online-endpoint invoke --local --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_endpoint>

# <test_endpoint_using_curl>
SCORING_URI=$(az ml online-endpoint show --local -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
# </test_endpoint_using_curl>

# <get_logs>
az ml online-deployment get-logs --local -n blue --endpoint $ENDPOINT_NAME
# </get_logs>

# <delete_endpoint>
az ml online-endpoint delete --local --name $ENDPOINT_NAME --yes
# </delete_endpoint>
```

> [!NOTE]
> Endpoint names must be unique within an Azure region. For example, in the Azure `westus2` region, there can be only one endpoint with the name `my-endpoint`. 

# [Python](#tab/python)

### Clone the sample repository
