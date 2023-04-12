
# Manage Azure Machine Learning environments with the CLI & SDK (v2)

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK or CLI extension you are using:"]
> * [v1](./v1/how-to-use-environments.md)
> * [v2 (current version)](how-to-manage-environments-v2.md)



Azure Machine Learning environments define the execution environments for your jobs or deployments and encapsulate the dependencies for your code. Azure ML uses the environment specification to create the Docker container that your training or scoring code runs in on the specified compute target. You can define an environment from a conda specification, Docker image, or Docker build context.

In this article, learn how to create and manage Azure ML environments using the SDK & CLI (v2).


## Prerequisites

[!INCLUDE [sdk/cliv2](../../includes/machine-learning-cli-sdk-v2-prereqs.md)]

> [!TIP]
> For a full-featured development environment, use Visual Studio Code and the [Azure Machine Learning extension](how-to-setup-vs-code.md) to [manage Azure Machine Learning resources](how-to-manage-resources-vscode.md) and [train machine learning models](tutorial-train-deploy-image-classification-model-vscode.md).

### Clone examples repository

To run the training examples, first clone the examples repository. For the CLI examples, change into the `cli` directory. For the SDK examples, change into the `SDK` directory:

```azurecli
git clone --depth 1 https://github.com/Azure/azureml-examples
```

Note that `--depth 1` clones only the latest commit to the repository, which reduces time to complete the operation.

### Connect to the workspace

> [!TIP]
> Use the tabs below to select the method you want to use to work with environments. Selecting a tab will automatically switch all the tabs in this article to the same tab. You can select another tab at any time.

# [Azure CLI](#tab/cli)

When using the Azure CLI, you need identifier parameters - a subscription, resource group, and workspace name. While you can specify these parameters for each command, you can also set defaults that will be used for all the commands. Use the following commands to set default values. Replace `<subscription ID>`, `<AzureML workspace name>`, and `<resource group>` with the values for your configuration:

```azurecli
az account set --subscription <subscription ID>
az configure --defaults workspace=<AzureML workspace name> group=<resource group>
```

# [Python SDK](#tab/python)

To connect to the workspace, you need identifier parameters - a subscription, resource group, and workspace name. You'll use these details in the `MLClient` from the `azure.ai.ml` namespace to get a handle to the required Azure Machine Learning workspace. To authenticate, you use the [default Azure authentication](/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python&preserve-view=true). Check this [example](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/configuration.ipynb) for more details on how to configure credentials and connect to a workspace.

```python
#import required libraries for workspace
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

#import required libraries for environments examples
from azure.ai.ml.entities import Environment, BuildContext

#Enter details of your AzureML workspace
subscription_id = '<SUBSCRIPTION_ID>'
resource_group = '<RESOURCE_GROUP>'
workspace = '<AZUREML_WORKSPACE_NAME>'

#connect to the workspace
ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
```


## Curated environments

There are two types of environments in Azure ML: curated and custom environments. Curated environments are predefined environments containing popular ML frameworks and tooling. Custom environments are user-defined and can be created via `az ml environment create`.

Curated environments are provided by Azure ML and are available in your workspace by default. Azure ML routinely updates these environments with the latest framework version releases and maintains them for bug fixes and security patches. They're backed by cached Docker images, which reduce job preparation cost and model deployment time.
