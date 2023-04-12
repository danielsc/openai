To follow along with this article, first clone the [examples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, go to the repository's `cli/` directory:

```azurecli
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples
cd cli
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository. This reduces the time to complete the operation.

The commands in this tutorial are in the file `deploy-safe-rollout-online-endpoints.sh` in the `cli` directory, and the YAML configuration files are in the `endpoints/online/managed/sample/` subdirectory.

> [!NOTE]
> The YAML configuration files for Kubernetes online endpoints are in the `endpoints/online/kubernetes/` subdirectory.

# [Python](#tab/python)

### Clone the examples repository

To run the training examples, first clone the [examples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, go into the `azureml-examples/sdk/python/endpoints/online/managed` directory:

```bash
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/sdk/python/endpoints/online/managed
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository. This reduces the time to complete the operation.

The information in this article is based on the [online-endpoints-safe-rollout.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/online-endpoints-safe-rollout.ipynb) notebook. It contains the same content as this article, although the order of the codes is slightly different.

> [!NOTE]
> The steps for the Kubernetes online endpoint are based on the [kubernetes-online-endpoints-safe-rollout.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/kubernetes/kubernetes-online-endpoints-safe-rollout.ipynb) notebook.

### Connect to Azure Machine Learning workspace

The [workspace](concept-workspace.md) is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace where you'll perform deployment tasks.

1. Import the required libraries:

```python
# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration,
)
from azure.identity import DefaultAzureCredential
```

    > [!NOTE]
    > If you're using the Kubernetes online endpoint, import the `KubernetesOnlineEndpoint` and `KubernetesOnlineDeployment` class from the `azure.ai.ml.entities` library.

1. Configure workspace details and get a handle to the workspace:

    To connect to a workspace, we need identifier parameters—a subscription, resource group and workspace name. We'll use these details in the `MLClient` from `azure.ai.ml` to get a handle to the required Azure Machine Learning workspace. This example uses the [default Azure authentication](/python/api/azure-identity/azure.identity.defaultazurecredential).

```python
# enter details of your AML workspace
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace = "<AML_WORKSPACE_NAME>"
```

```python
# get a handle to the workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)
```


## Define the endpoint and deployment

Online endpoints are used for online (real-time) inferencing. Online endpoints contain deployments that are ready to receive data from clients and can send responses back in real time.

# [Azure CLI](#tab/azure-cli)

### Create online endpoint

To create an online endpoint:

1. Set your endpoint name:

   For Unix, run this command (replace `YOUR_ENDPOINT_NAME` with a unique name):

```azurecli
set -e

# <set_endpoint_name>
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

#  endpoint name
export ENDPOINT_NAME=endpt-sr-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_blue>
az ml online-deployment create --name blue --endpoint-name $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml --all-traffic
# </create_blue>

# <test_blue>
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_blue>

# <scale_blue>
az ml online-deployment update --name blue --endpoint-name $ENDPOINT_NAME --set instance_count=2
# </scale_blue>

# <create_green>
az ml online-deployment create --name green --endpoint-name $ENDPOINT_NAME -f endpoints/online/managed/sample/green-deployment.yml
# </create_green>

# <get_traffic>
az ml online-endpoint show -n $ENDPOINT_NAME --query traffic
# </get_traffic>

# <test_green>
az ml online-endpoint invoke --name $ENDPOINT_NAME --deployment-name green --request-file endpoints/online/model-2/sample-request.json
# </test_green>

# supress printing secret
set +x

# <test_green_using_curl_get_key>
#get the key
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
# </test_green_using_curl_get_key>

set -x

# <test_green_using_curl>
# get the scoring uri
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)
# use curl to invoke the endpoint
curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --header "azureml-model-deployment: green" --data @endpoints/online/model-2/sample-request.json
# </test_green_using_curl>

# <test_green_with_mirror_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --mirror-traffic "green=10"
# </test_green_with_mirror_traffic>

# <reset_mirror_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --mirror-traffic "green=0"
# </reset_mirror_traffic>

# <green_10pct_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --traffic "blue=90 green=10"
# </green_10pct_traffic>

# <green_100pct_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --traffic "blue=0 green=100"
# </green_100pct_traffic>

# <delete_blue>
az ml online-deployment delete --name blue --endpoint $ENDPOINT_NAME --yes --no-wait
# </delete_blue>

# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>

```
