
# Train models with Azure Machine Learning CLI, SDK, and REST API

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Azure Machine Learning provides multiple ways to submit ML training jobs. In this article, you'll learn how to submit jobs using the following methods:

* Azure CLI extension for machine learning: The `ml` extension, also referred to as CLI v2.
* Python SDK v2 for Azure Machine Learning.
* REST API: The API that the CLI and SDK are built on.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
* An Azure Machine Learning workspace. If you don't have one, you can use the steps in the [Quickstart: Create Azure ML resources](quickstart-create-resources.md) article.

# [Python SDK](#tab/python)

To use the __SDK__ information, install the Azure Machine Learning [SDK v2 for Python](https://aka.ms/sdk-v2-install).

# [Azure CLI](#tab/azurecli)

To use the __CLI__ information, install the [Azure CLI and extension for machine learning](how-to-configure-cli.md).

# [REST API](#tab/restapi)

To use the __REST API__ information, you need the following items:

- A __service principal__ in your workspace. Administrative REST requests use [service principal authentication](how-to-setup-authentication.md#use-service-principal-authentication).
- A service principal __authentication token__. Follow the steps in [Retrieve a service principal authentication token](./how-to-manage-rest.md#retrieve-a-service-principal-authentication-token) to retrieve this token. 
- The __curl__ utility. The curl program is available in the [Windows Subsystem for Linux](/windows/wsl/install-win10) or any UNIX distribution. 

    > [!TIP]
    > In PowerShell, `curl` is an alias for `Invoke-WebRequest` and `curl -d "key=val" -X POST uri` becomes `Invoke-WebRequest -Body "key=val" -Method POST -Uri uri`.
    >
    > While it is possible to call the REST API from PowerShell, the examples in this article assume you are using Bash.

- The [jq](https://stedolan.github.io/jq/) utility for processing JSON. This utility is used to extract values from the JSON documents that are returned from REST API calls.


### Clone the examples repository

The code snippets in this article are based on examples in the [Azure ML examples GitHub repo](https://github.com/azure/azureml-examples). To clone the repository to your development environment, use the following command:

```bash
git clone --depth 1 https://github.com/Azure/azureml-examples
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository, which reduces time to complete the operation.

## Example job

The examples in this article use the iris flower dataset to train an MLFlow model.

## Train in the cloud

When training in the cloud, you must connect to your Azure Machine Learning workspace and select a compute resource that will be used to run the training job.

### 1. Connect to the workspace

> [!TIP]
> Use the tabs below to select the method you want to use to train a model. Selecting a tab will automatically switch all the tabs in this article to the same tab. You can select another tab at any time.

# [Python SDK](#tab/python)

To connect to the workspace, you need identifier parameters - a subscription, resource group, and workspace name. You'll use these details in the `MLClient` from the `azure.ai.ml` namespace to get a handle to the required Azure Machine Learning workspace. To authenticate, you use the [default Azure authentication](/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python&preserve-view=true). Check this [example](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/configuration.ipynb) for more details on how to configure credentials and connect to a workspace.

```python
#import required libraries
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

#Enter details of your AzureML workspace
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCE_GROUP>'
workspace = '<AZUREML_WORKSPACE_NAME>'

#connect to the workspace
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
```
