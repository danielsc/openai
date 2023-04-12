
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


### Registering the model in the registry

Ensure your model is registered in Azure Machine Learning registry. Deployment of unregistered models is not supported in Azure Machine Learning. You can register a new model using the MLflow SDK:

# [Azure CLI](#tab/cli)

```azurecli
MODEL_NAME='heart-classifier'
az ml model create --name $MODEL_NAME --type "mlflow_model" --path "model"
```

# [Python (Azure ML SDK)](#tab/sdk)

```python
model_name = 'heart-classifier'
model_local_path = "model"

model = ml_client.models.create_or_update(
     Model(name=model_name, path=model_local_path, type=AssetTypes.MLFLOW_MODEL)
)
```

# [Python (MLflow SDK)](#tab/mlflow)

```python
model_name = 'heart-classifier'
model_local_path = "model"

registered_model = mlflow_client.create_model_version(
    name=model_name, source=f"file://{model_local_path}"
)
version = registered_model.version
```


## Create an online endpoint

Online endpoints are endpoints that are used for online (real-time) inferencing. Online endpoints contain deployments that are ready to receive data from clients and can send responses back in real time.

We are going to exploit this functionality by deploying multiple versions of the same model under the same endpoint. However, the new deployment will receive 0% of the traffic at the begging. Once we are sure about the new model to work correctly, we are going to progressively move traffic from one deployment to the other.

1. Endpoints require a name, which needs to be unique in the same region. Let's ensure to create one that doesn't exist:

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    ENDPOINT_SUFIX=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w ${1:-5} | head -n 1)
    ENDPOINT_NAME="heart-classifier-$ENDPOINT_SUFIX"
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    import random
    import string
    
    # Creating a unique endpoint name by including a random suffix
    allowed_chars = string.ascii_lowercase + string.digits
    endpoint_suffix = "".join(random.choice(allowed_chars) for x in range(5))
    endpoint_name = "heart-classifier-" + endpoint_suffix
    
    print(f"Endpoint name: {endpoint_name}")
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    import random
    import string
    
    # Creating a unique endpoint name by including a random suffix
    allowed_chars = string.ascii_lowercase + string.digits
    endpoint_suffix = "".join(random.choice(allowed_chars) for x in range(5))
    endpoint_name = "heart-classifier-" + endpoint_suffix
    
    print(f"Endpoint name: {endpoint_name}")
    ```

1. Configure the endpoint

    # [Azure CLI](#tab/cli)
    
    __endpoint.yml__

    ```yaml
    $schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
    name: heart-classifier-edp
    auth_mode: key
    ```
