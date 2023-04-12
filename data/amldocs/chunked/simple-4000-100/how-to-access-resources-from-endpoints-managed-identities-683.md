If you encounter any issues, see [Troubleshooting online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md).

# [User-assigned (CLI)](#tab/user-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="create_endpoint" :::

Check the status of the endpoint with the following.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="check_endpoint_Status" :::

If you encounter any issues, see [Troubleshooting online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md).

# [System-assigned (Python)](#tab/system-identity-python)

When you create an online endpoint, a system-assigned managed identity is created for the endpoint by default.

```python
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```

Check the status of the endpoint via the details of the deployed endpoint object with the following code:  

```python
endpoint = ml_client.online_endpoints.get(endpoint_name)
print(endpoint.identity.type)
print(endpoint.identity.principal_id)
```

If you encounter any issues, see [Troubleshooting online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md).


# [User-assigned (Python)](#tab/user-identity-python)

The following Python endpoint object: 

* Assigns the name by which you want to refer to the endpoint to the variable `endpoint_name. 
* Specifies the type of authorization to use to access the endpoint `auth-mode="key"`.
* Defines its identity as a ManagedServiceIdentity and specifies the Managed Identity created above as user-assigned. 

Define and deploy the endpoint: 

```python
from azure.ai.ml.entities import ManagedIdentityConfiguration, IdentityConfiguration

endpoint = ManagedOnlineEndpoint(
    name=endpoint_name,
    auth_mode="key",
    identity=IdentityConfiguration(
        type="user_assigned",
        user_assigned_identities=[
            ManagedIdentityConfiguration(resource_id=uai_identity.id)
        ],
    ),
)

ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```


Check the status of the endpoint via the details of the deployed endpoint object with the following code:  

```python
endpoint = ml_client.online_endpoints.get(endpoint_name)
print(endpoint.identity.type)
print(endpoint.identity.user_assigned_identities)
```

If you encounter any issues, see [Troubleshooting online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md).


## Give access permission to the managed identity

>[!IMPORTANT] 
> Online endpoints require Azure Container Registry pull permission, AcrPull permission, to the container registry and Storage Blob Data Reader permission to the default datastore of the workspace.

You can allow the online endpoint permission to access your storage via its system-assigned managed identity or give permission to the user-assigned managed identity to access the storage account created in the previous section.

# [System-assigned (CLI)](#tab/system-identity-cli)

Retrieve the system-assigned managed identity that was created for your endpoint.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="get_system_identity" :::

From here, you can give the system-assigned managed identity permission to access your storage.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="give_permission_to_user_storage_account" :::

# [User-assigned (CLI)](#tab/user-identity-cli)

Retrieve user-assigned managed identity client ID.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_user_identity_client_id" :::

Retrieve the user-assigned managed identity ID.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_user_identity_id" :::
