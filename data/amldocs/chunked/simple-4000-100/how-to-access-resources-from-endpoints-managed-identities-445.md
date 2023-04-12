


## Create the managed identity 
To access Azure resources, create a system-assigned or user-assigned managed identity for your online endpoint. 

# [System-assigned (CLI)](#tab/system-identity-cli)

When you [create an online endpoint](#create-an-online-endpoint), a system-assigned managed identity is automatically generated for you, so no need to create a separate one. 

# [User-assigned (CLI)](#tab/user-identity-cli)

To create a user-assigned managed identity, use the following:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="create_user_identity" :::

# [System-assigned (Python)](#tab/system-identity-python)

When you [create an online endpoint](#create-an-online-endpoint), a system-assigned managed identity is automatically generated for you, so no need to create a separate one. 

# [User-assigned (Python)](#tab/user-identity-python)

To create a user-assigned managed identity, first get a handle to the `ManagedServiceIdentityClient`: 

```python
from azure.mgmt.msi import ManagedServiceIdentityClient
from azure.mgmt.msi.models import Identity

credential = AzureCliCredential()
msi_client = ManagedServiceIdentityClient(
    subscription_id=subscription_id,
    credential=credential,
)
```

Then, create the identity:

```python
msi_client.user_assigned_identities.create_or_update(
    resource_group_name=resource_group,
    resource_name=uai_name,
    parameters=Identity(location=workspace_location),
)
```

Now, retrieve the identity object, which contains details we will use below: 

```python
uai_identity = msi_client.user_assigned_identities.get(
    resource_group_name=resource_group,
    resource_name=uai_name,
)
uai_identity.as_dict()
```


## Create storage account and container

For this example, create a blob storage account and blob container, and then upload the previously created text file to the blob container. 
This is the storage account and blob container that you'll give the online endpoint and managed identity access to. 

# [System-assigned (CLI)](#tab/system-identity-cli)

First, create a storage account.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="create_storage_account" :::

Next, create the blob container in the storage account.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="create_storage_container" :::

Then, upload your text file to the blob container.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="upload_file_to_storage" :::

# [User-assigned (CLI)](#tab/user-identity-cli)

First, create a storage account.  

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="create_storage_account" :::

You can also retrieve an existing storage account ID with the following. 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_storage_account_id" :::

Next, create the blob container in the storage account. 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="create_storage_container" :::

Then, upload file in container. 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="upload_file_to_storage" :::

# [System-assigned (Python)](#tab/system-identity-python)

First, get a handle to the `StorageManagementclient`:

```python
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import ContainerClient
from azure.mgmt.storage.models import Sku, StorageAccountCreateParameters, BlobContainer

credential = AzureCliCredential()
storage_client = StorageManagementClient(
    credential=credential, subscription_id=subscription_id
)
```
