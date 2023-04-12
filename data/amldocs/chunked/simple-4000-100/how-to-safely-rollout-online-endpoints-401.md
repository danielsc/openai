
# [Python](#tab/python)

### Create online endpoint

To create a managed online endpoint, use the `ManagedOnlineEndpoint` class. This class allows users to configure the following key aspects of the endpoint:

* `name` - Name of the endpoint. Needs to be unique at the Azure region level
* `auth_mode` - The authentication method for the endpoint. Key-based authentication and Azure ML token-based authentication are supported. Key-based authentication doesn't expire but Azure ML token-based authentication does. Possible values are `key` or `aml_token`.
* `identity`- The managed identity configuration for accessing Azure resources for endpoint provisioning and inference.
    * `type`- The type of managed identity. Azure Machine Learning supports `system_assigned` or `user_assigned` identity.
    * `user_assigned_identities` - List (array) of fully qualified resource IDs of the user-assigned identities. This property is required if `identity.type` is user_assigned.
* `description`- Description of the endpoint.

1. Configure the endpoint:

```python
# Creating a unique endpoint name with current datetime to avoid conflicts
import random

online_endpoint_name = "endpt-moe-" + str(random.randint(0, 10000))

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is a sample online endpoint",
    auth_mode="key",
    tags={"foo": "bar"},
)
```

    > [!NOTE]
    > To create a Kubernetes online endpoint, use the `KubernetesOnlineEndpoint` class.

1. Create the endpoint:

```python
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```

### Create the 'blue' deployment

A deployment is a set of resources required for hosting the model that does the actual inferencing. To create a deployment for your managed online endpoint, use the `ManagedOnlineDeployment` class. This class allows users to configure the following key aspects of the deployment:

**Key aspects of deployment**
* `name` - Name of the deployment.
* `endpoint_name` - Name of the endpoint to create the deployment under.
* `model` - The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification.
* `environment` - The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification.
* `code_configuration` - the configuration for the source code and scoring script
    * `path`- Path to the source code directory for scoring the model
    * `scoring_script` - Relative path to the scoring file in the source code directory
* `instance_type` - The VM size to use for the deployment. For the list of supported sizes, see [Managed online endpoints SKU list](reference-managed-online-endpoints-vm-sku-list.md).
* `instance_count` - The number of instances to use for the deployment

1. Configure blue deployment:

```python
# create blue deployment
model = Model(path="../model-1/model/sklearn_regression_model.pkl")
env = Environment(
    conda_file="../model-1/environment/conda.yml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
)

blue_deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=online_endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="../model-1/onlinescoring", scoring_script="score.py"
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1,
)
```

    > [!NOTE]
    > To create a deployment for a Kubernetes online endpoint, use the `KubernetesOnlineDeployment` class.

1. Create the deployment:

```python
ml_client.online_deployments.begin_create_or_update(blue_deployment).result()
```

```python
# blue deployment takes 100 traffic
endpoint.traffic = {"blue": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```


## Confirm your existing deployment

# [Azure CLI](#tab/azure-cli)

You can view the status of your existing endpoint and deployment by running:
