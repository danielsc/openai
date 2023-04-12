- Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the owner or contributor role for the Azure Machine Learning workspace, or a custom role allowing Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
- You must have a MLflow model registered in your workspace. Particularly, this example will register a model trained for the [Diabetes dataset](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).

Additionally, you will need to:

# [Azure CLI](#tab/cli)

- Install the Azure CLI and the ml extension to the Azure CLI. For more information, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

# [Python (Azure ML SDK)](#tab/sdk)

- Install the Azure Machine Learning SDK for Python
    
    ```bash
    pip install azure-ai-ml
    ```
    
# [Python (MLflow SDK)](#tab/mlflow)

- Install the MLflow SDK package `mlflow` and the Azure Machine Learning plug-in for MLflow `azureml-mlflow`.

    ```bash
    pip install mlflow azureml-mlflow
    ```

- If you are not running in Azure Machine Learning compute, configure the MLflow tracking URI or MLflow's registry URI to point to the workspace you are working on. See [Configure MLflow for Azure Machine Learning](how-to-use-mlflow-configure-tracking.md) for more details.

# [Studio](#tab/studio)

There are no additional prerequisites when working in Azure Machine Learning studio.



### Connect to your workspace

First, let's connect to Azure Machine Learning workspace where we are going to work on.

# [Azure CLI](#tab/cli)

```azurecli
az account set --subscription <subscription>
az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
```

# [Python (Azure ML SDK)](#tab/sdk)

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace in which you'll perform deployment tasks.

1. Import the required libraries:

    ```python
    from azure.ai.ml import MLClient, Input
    from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model
    from azure.ai.ml.constants import AssetTypes
    from azure.identity import DefaultAzureCredential
    ```

2. Configure workspace details and get a handle to the workspace:

    ```python
    subscription_id = "<subscription>"
    resource_group = "<resource-group>"
    workspace = "<workspace>"
    
    ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
    ```

# [Python (MLflow SDK)](#tab/mlflow)

1. Import the required libraries

    ```python
    import json
    import mlflow
    import requests
    import pandas as pd
    from mlflow.deployments import get_deploy_client
    ```

1. Configure the deployment client

    ```python
    deployment_client = get_deploy_client(mlflow.get_tracking_uri())    
    ```

# [Studio](#tab/studio)

Navigate to [Azure Machine Learning studio](https://ml.azure.com).


### Registering the model

Online Endpoint can only deploy registered models. In this case, we already have a local copy of the model in the repository, so we only need to publish the model to the registry in the workspace. You can skip this step if the model you are trying to deploy is already registered.
   
# [Azure CLI](#tab/cli)

```azurecli
MODEL_NAME='sklearn-diabetes'
az ml model create --name $MODEL_NAME --type "mlflow_model" --path "sklearn-diabetes/model"
```

# [Python (Azure ML SDK)](#tab/sdk)

```python
model_name = 'sklearn-diabetes'
model_local_path = "sklearn-diabetes/model"
model = ml_client.models.create_or_update(
        Model(name=model_name, path=model_local_path, type=AssetTypes.MLFLOW_MODEL)
)
```

# [Python (MLflow SDK)](#tab/mlflow)
