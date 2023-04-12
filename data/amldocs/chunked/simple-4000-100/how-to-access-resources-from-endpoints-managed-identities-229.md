
Next, specify what you want to name your blob storage account, blob container, and file. These variable names are defined here, and are referred to in the storage account and container creation code by the `StorageManagementClient` and `ContainerClient`. 

```python
storage_account_name = "<STORAGE_ACCOUNT_NAME>"
storage_container_name = "<CONTAINER_TO_ACCESS>"
file_name = "<FILE_TO_ACCESS>"
```

After these variables are assigned, create a text file locally. When the endpoint is deployed, the scoring script will access this text file using the user-assigned managed identity that's generated upon endpoint creation.

Decide on the name of your user identity name:
```python
uai_name = "<USER_ASSIGNED_IDENTITY_NAME>"
```

Now, get a handle to the workspace and retrieve its location:

```python
from azure.ai.ml import MLClient
from azure.identity import AzureCliCredential
from azure.ai.ml.entities import (
    ManagedOnlineDeployment,
    ManagedOnlineEndpoint,
    Model,
    CodeConfiguration,
    Environment,
)

credential = AzureCliCredential()
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

workspace_location = ml_client.workspaces.get(workspace_name).location
```

We will use this value to create a storage account. 


## Define the deployment configuration


# [System-assigned (CLI)](#tab/system-identity-cli)

To deploy an online endpoint with the CLI, you need to define the configuration in a YAML file. For more information on the YAML schema, see [online endpoint YAML reference](reference-yaml-endpoint-online.md) document.

The YAML files in the following examples are used to create online endpoints. 

The following YAML example is located at `endpoints/online/managed/managed-identities/1-sai-create-endpoint`. The file, 

* Defines the name by which you want to refer to the endpoint, `my-sai-endpoint`.
* Specifies the type of authorization to use to access the endpoint, `auth-mode: key`.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-sai-endpoint
auth_mode: key

```

This YAML example, `2-sai-deployment.yml`,

* Specifies that the type of endpoint you want to create is an `online` endpoint.
* Indicates that the endpoint has an associated deployment called `blue`.
* Configures the details of the deployment such as, which model to deploy and which environment and scoring script to use.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: blue
model:
  path: ../../model-1/model/
code_configuration:
  code: ../../model-1/onlinescoring/
  scoring_script: score_managedidentity.py
environment:
  conda_file: ../../model-1/environment/conda-managedidentity.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
instance_type: Standard_DS3_v2
instance_count: 1
environment_variables:
  STORAGE_ACCOUNT_NAME: "storage_place_holder"
  STORAGE_CONTAINER_NAME: "container_place_holder"
  FILE_NAME: "file_place_holder"

```

# [User-assigned (CLI)](#tab/user-identity-cli)

To deploy an online endpoint with the CLI, you need to define the configuration in a YAML file. For more information on the YAML schema, see [online endpoint YAML reference](reference-yaml-endpoint-online.md) document.

The YAML files in the following examples are used to create online endpoints. 

The following YAML example is located at `endpoints/online/managed/managed-identities/1-uai-create-endpoint`. The file, 

* Defines the name by which you want to refer to the endpoint, `my-uai-endpoint`.
* Specifies the type of authorization to use to access the endpoint, `auth-mode: key`.
* Indicates the identity type to use, `type: user_assigned`

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-uai-endpoint
auth_mode: key
identity:
  type: user_assigned
  user_assigned_identities:
    - resource_id: user_identity_ARM_id_place_holder

```

This YAML example, `2-sai-deployment.yml`,
