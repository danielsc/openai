Configure the variable names for the workspace, workspace location, and the endpoint you want to create for use with your deployment.

# [System-assigned (CLI)](#tab/system-identity-cli)

The following code exports these values as environment variables in your endpoint:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="set_variables" :::

Next, specify what you want to name your blob storage account, blob container, and file. These variable names are defined here, and are referred to in `az storage account create` and `az storage container create` commands in the next section.

The following code exports those values as environment variables:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="configure_storage_names" :::

After these variables are exported, create a text file locally. When the endpoint is deployed, the scoring script will access this text file using the system-assigned managed identity that's generated upon endpoint creation.

# [User-assigned (CLI)](#tab/user-identity-cli)

Decide on the name of your endpoint, workspace, workspace location and export that value as an environment variable:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="set_variables" :::

Next, specify what you want to name your blob storage account, blob container, and file. These variable names are defined here, and are referred to in `az storage account create` and `az storage container create` commands in the next section.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="configure_storage_names" :::

After these variables are exported, create a text file locally. When the endpoint is deployed, the scoring script will access this text file using the user-assigned managed identity used in the endpoint. 

Decide on the name of your user identity name, and export that value as an environment variable:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="set_user_identity_name" :::

# [System-assigned (Python)](#tab/system-identity-python)

Assign values for the workspace and deployment-related variables:

```python
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"
endpoint_name = "<ENDPOINT_NAME>"
```

Next, specify what you want to name your blob storage account, blob container, and file. These variable names are defined here, and are referred to in the storage account and container creation code by the `StorageManagementClient` and `ContainerClient`. 

```python
storage_account_name = "<STORAGE_ACCOUNT_NAME>"
storage_container_name = "<CONTAINER_TO_ACCESS>"
file_name = "<FILE_TO_ACCESS>"
```

After these variables are assigned, create a text file locally. When the endpoint is deployed, the scoring script will access this text file using the system-assigned managed identity that's generated upon endpoint creation.

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


# [User-assigned (Python)](#tab/user-identity-python)


Assign values for the workspace and deployment-related variables:

```python
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"
endpoint_name = "<ENDPOINT_NAME>"
```
