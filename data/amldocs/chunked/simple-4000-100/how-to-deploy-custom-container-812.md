
# [Python SDK](#tab/python)

### Connect to Azure Machine Learning workspace
Connect to Azure Machine Learning Workspace, configure workspace details, and get a handle to the workspace as follows:

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

2. Configure workspace details and get a handle to the workspace:

```python
# enter details of your AzureML workspace
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace = "<AZUREML_WORKSPACE_NAME>"

# get a handle to the workspace
ml_client = MLClient(
   DefaultAzureCredential(), subscription_id, resource_group, workspace
)
```

For more information, see [Deploy machine learning models to managed online endpoint using Python SDK v2](how-to-deploy-managed-online-endpoint-sdk-v2.md).

### Configure online endpoint

> [!TIP]
> * `name`: The name of the endpoint. It must be unique in the Azure region. The name for an endpoint must start with an upper- or lowercase letter and only consist of '-'s and alphanumeric characters. For more information on the naming rules, see [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).
> * `auth_mode` : Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. A `key` doesn't expire, but `aml_token` does expire. For more information on authenticating, see [Authenticate to an online endpoint](how-to-authenticate-online-endpoint.md).

Optionally, you can add description, tags to your endpoint.

```python
# Creating a unique endpoint name with current datetime to avoid conflicts
import datetime

online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is a sample online endpoint",
    auth_mode="key",
    tags={"foo": "bar"},
)
```

### Configure online deployment

A deployment is a set of resources required for hosting the model that does the actual inferencing. We'll create a deployment for our endpoint using the `ManagedOnlineDeployment` class.

> [!TIP]
> - `name` - Name of the deployment.
> - `endpoint_name` - Name of the endpoint to create the deployment under.
> - `model` - The model to use for the deployment. This value can be either a reference to an existing versioned > model in the workspace or an inline model specification.
> - `environment` - The environment to use for the deployment. This value can be either a reference to an existing > versioned environment in the workspace or an inline environment specification.
> - `code_configuration` - the configuration for the source code and scoring script
>     - `path`- Path to the source code directory for scoring the model
>     - `scoring_script` - Relative path to the scoring file in the source code directory
> - `instance_type` - The VM size to use for the deployment. For the list of supported sizes, see [endpoints SKU list](reference-managed-online-endpoints-vm-sku-list.md).
> - `instance_count` - The number of instances to use for the deployment

```python
# create a blue deployment
model = Model(name="tfserving-mounted", version="1", path="half_plus_two")

env = Environment(
    image="docker.io/tensorflow/serving:latest",
    inference_config={
        "liveness_route": {"port": 8501, "path": "/v1/models/half_plus_two"},
        "readiness_route": {"port": 8501, "path": "/v1/models/half_plus_two"},
        "scoring_route": {"port": 8501, "path": "/v1/models/half_plus_two:predict"},
    },
)

blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=online_endpoint_name,
    model=model,
    environment=env,
    environment_variables={
        "MODEL_BASE_PATH": "/var/azureml-app/azureml-models/tfserving-mounted/1",
        "MODEL_NAME": "half_plus_two",
    },
    instance_type="Standard_DS2_v2",
    instance_count=1,
)
```
