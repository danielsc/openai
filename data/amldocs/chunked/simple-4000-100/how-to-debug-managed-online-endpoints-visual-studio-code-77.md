The examples in this article can be found in the [Debug online endpoints locally in Visual Studio Code](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/debug-online-endpoints-locally-in-visual-studio-code.ipynb) notebook within the[azureml-examples](https://github.com/azure/azureml-examples) repository. To run the code locally, clone the repo and then change directories to the notebook's parent directory `sdk/endpoints/online/managed`. 

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples
cd sdk/python/endpoints/online/managed
```

Import the required modules: 

```python
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    CodeConfiguration,
    Environment,
)
from azure.identity import DefaultAzureCredential
``` 

Set up variables for the workspace and endpoint: 

```python 
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"

endpoint_name = "<ENDPOINT_NAME>"
``` 


## Launch development container

# [Azure CLI](#tab/cli)

Azure Machine Learning local endpoints use Docker and VS Code development containers (dev container) to build and configure a local debugging environment. With dev containers, you can take advantage of VS Code features from inside a Docker container. For more information on dev containers, see [Create a development container](https://code.visualstudio.com/docs/remote/create-dev-container).

To debug online endpoints locally in VS Code, use the `--vscode-debug` flag when creating or updating and Azure Machine Learning online deployment. The following command uses a deployment example from the examples repo:

```azurecli
az ml online-deployment create --file endpoints/online/managed/sample/blue-deployment.yml --local --vscode-debug
```

> [!IMPORTANT]
> On Windows Subsystem for Linux (WSL), you'll need to update your PATH environment variable to include the path to the VS Code executable or use WSL interop. For more information, see [Windows interoperability with Linux](/windows/wsl/interop).

A Docker image is built locally. Any environment configuration or model file errors are surfaced at this stage of the process.

> [!NOTE]
> The first time you launch a new or updated dev container it can take several minutes.

Once the image successfully builds, your dev container opens in a VS Code window.

You'll use a few VS Code extensions to debug your deployments in the dev container. Azure Machine Learning automatically installs these extensions in your dev container.

- Inference Debug
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

> [!IMPORTANT]
> Before starting your debug session, make sure that the VS Code extensions have finished installing in your dev container.  


# [Python](#tab/python)

Azure Machine Learning local endpoints use Docker and VS Code development containers (dev container) to build and configure a local debugging environment. With dev containers, you can take advantage of VS Code features from inside a Docker container. For more information on dev containers, see [Create a development container](https://code.visualstudio.com/docs/remote/create-dev-container).

Get a handle to the workspace: 

```python 
credential = DefaultAzureCredential()
ml_client = MLClient(
    credential,
    subscription_id=subscription_id,
    resource_group_name=resource_group,
    workspace_name=workspace_name,
)
``` 

To debug online endpoints locally in VS Code, set the `vscode-debug` and `local` flags when creating or updating an Azure Machine Learning online deployment. The following code mirrors a deployment example from the examples repo:

```python
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint_name,
    model=Model(path="../model-1/model/sklearn_regression_model.pkl"),
    code_configuration=CodeConfiguration(
        code="../model-1/onlinescoring", scoring_script="score.py"
    ),
    environment=Environment(
        conda_file="../model-1/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:20210727.v1",
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1,
)

deployment = ml_client.online_deployments.begin_create_or_update(
    deployment, local=True, vscode_debug=True
).result()
```
