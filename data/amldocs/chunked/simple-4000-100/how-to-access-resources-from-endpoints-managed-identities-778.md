::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_user_identity_id" :::

Get the container registry associated with workspace.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_container_registry_id" :::

Retrieve the default storage of the workspace.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="get_workspace_storage_id" :::

Give permission of storage account to the user-assigned managed identity.  

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="give_permission_to_user_storage_account" :::

Give permission of container registry to user assigned managed identity.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="give_permission_to_container_registry" :::

Give permission of default workspace storage to user-assigned managed identity.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="give_permission_to_workspace_storage_account" :::

# [System-assigned (Python)](#tab/system-identity-python)

First, make an `AuthorizationManagementClient` to list Role Definitions: 

```python
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.v2018_01_01_preview.models import RoleDefinition
import uuid

role_definition_client = AuthorizationManagementClient(
    credential=credential,
    subscription_id=subscription_id,
    api_version="2018-01-01-preview",
)
```

Now, initialize one to make Role Assignments: 

```python
from azure.mgmt.authorization.v2020_10_01_preview.models import (
    RoleAssignment,
    RoleAssignmentCreateParameters,
)

role_assignment_client = AuthorizationManagementClient(
    credential=credential,
    subscription_id=subscription_id,
    api_version="2020-10-01-preview",
)
```


Then, get the Principal ID of the System-assigned managed identity: 

```python
endpoint = ml_client.online_endpoints.get(endpoint_name)
system_principal_id = endpoint.identity.principal_id
```

Next, give assign the `Storage Blob Data Reader` role to the endpoint. The Role Definition is retrieved by name and passed along with the Principal ID of the endpoint. The role is applied at the scope of the storage account created above and allows the endpoint to read the file. 

```python
role_name = "Storage Blob Data Reader"
scope = storage_account.id

role_defs = role_definition_client.role_definitions.list(scope=scope)
role_def = next((r for r in role_defs if r.role_name == role_name))

role_assignment_client.role_assignments.create(
    scope=scope,
    role_assignment_name=str(uuid.uuid4()),
    parameters=RoleAssignmentCreateParameters(
        role_definition_id=role_def.id, principal_id=system_principal_id
    ),
)
```


# [User-assigned (Python)](#tab/user-identity-python)

First, make an `AuthorizationManagementClient` to list Role Definitions: 

```python
from azure.mgmt.authorization import AuthorizationManagementClient
from azure.mgmt.authorization.v2018_01_01_preview.models import RoleDefinition
import uuid

role_definition_client = AuthorizationManagementClient(
    credential=credential,
    subscription_id=subscription_id,
    api_version="2018-01-01-preview",
)
```

Now, initialize one to make Role Assignments: 

```python
from azure.mgmt.authorization.v2020_10_01_preview.models import (
    RoleAssignment,
    RoleAssignmentCreateParameters,
)

role_assignment_client = AuthorizationManagementClient(
    credential=credential,
    subscription_id=subscription_id,
    api_version="2020-10-01-preview",
)
```

Then, get the Principal ID and Client ID of the User-assigned managed identity. To assign roles, we only need the Principal ID. However, we will use the Client ID to fill the `UAI_CLIENT_ID` placeholder environment variable before creating the deployment.
