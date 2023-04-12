

Then, create a storage account: 

```python
storage_account_parameters = StorageAccountCreateParameters(
    sku=Sku(name="Standard_LRS"), kind="Storage", location=workspace_location
)

storage_account = storage_client.storage_accounts.begin_create(
    resource_group_name=resource_group,
    account_name=storage_account_name,
    parameters=storage_account_parameters,
).result()
```

Next, create the blob container in the storage account:

```python
blob_container = storage_client.blob_containers.create(
    resource_group_name=resource_group,
    account_name=storage_account_name,
    container_name=storage_container_name,
    blob_container=BlobContainer(),
)
```

Retrieve the storage account key and create a handle to the container with `ContainerClient`: 

```python
res = storage_client.storage_accounts.list_keys(
    resource_group_name=resource_group,
    account_name=storage_account_name,
)
key = res.keys[0].value

container_client = ContainerClient(
    account_url=storage_account.primary_endpoints.blob,
    container_name=storage_container_name,
    credential=key,
)
```

Then, upload a blob to the container with the `ContainerClient`:

```python
with open(file_name, "rb") as f:
    container_client.upload_blob(name=file_name, data=f.read())
```

# [User-assigned (Python)](#tab/user-identity-python)

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

Then, create a storage account: 

```python
storage_account_parameters = StorageAccountCreateParameters(
    sku=Sku(name="Standard_LRS"), kind="Storage", location=workspace_location
)

storage_account = storage_client.storage_accounts.begin_create(
    resource_group_name=resource_group,
    account_name=storage_account_name,
    parameters=storage_account_parameters,
).result()
```

Next, create the blob container in the storage account:

```python
blob_container = storage_client.blob_containers.create(
    resource_group_name=resource_group,
    account_name=storage_account_name,
    container_name=storage_container_name,
    blob_container=BlobContainer(),
)
```

Retrieve the storage account key and create a handle to the container with `ContainerClient`: 

```python
res = storage_client.storage_accounts.list_keys(
    resource_group_name=resource_group,
    account_name=storage_account_name,
)
key = res.keys[0].value

container_client = ContainerClient(
    account_url=storage_account.primary_endpoints.blob,
    container_name=storage_container_name,
    credential=key,
)
```

Then, upload a blob to the container with the `ContainerClient`:

```python
with open(file_name, "rb") as f:
    container_client.upload_blob(name=file_name, data=f.read())
```


## Create an online endpoint

The following code creates an online endpoint without specifying a deployment. 

> [!WARNING]
> The identity for an endpoint is immutable. During endpoint creation, you can associate it with a system-assigned identity (default) or a user-assigned identity. You can't change the identity after the endpoint has been created.

# [System-assigned (CLI)](#tab/system-identity-cli)
When you create an online endpoint, a system-assigned managed identity is created for the endpoint by default.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="create_endpoint" :::

Check the status of the endpoint with the following.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="check_endpoint_Status" :::

If you encounter any issues, see [Troubleshooting online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md).
