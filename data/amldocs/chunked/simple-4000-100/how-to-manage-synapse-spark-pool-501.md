> The parameter `--user-assigned-identities` can take a list of resource IDs and assign multiple user-defined identities to an attached Synapse Spark pool. The first user-assigned identity in the list will be used for submitting a job by default.

# [Python SDK](#tab/sdk)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
To use system-assigned identity, pass `IdentityConfiguration`, with type set to `SystemAssigned`, as the `identity` parameter of the `SynapseSparkCompute` class. This code snippet updates a Synapse Spark pool to use a system-assigned identity:

```python
# import required libraries 
from azure.ai.ml import MLClient
from azure.ai.ml.entities import SynapseSparkCompute, IdentityConfiguration 
from azure.identity import DefaultAzureCredential
    
subscription_id = "<SUBSCRIPTION_ID>" 
resource_group_name = "<RESOURCE_GROUP>" 
workspace_name = "<AML_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace 
) 

synapse_name = "<ATTACHED_SPARK_POOL_NAME>" 
synapse_resource ="/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>" 
synapse_identity = IdentityConfiguration(type="SystemAssigned") 

synapse_comp = SynapseSparkCompute(name=synapse_name, resource_id=synapse_resource,identity=synapse_identity) ml_client.begin_create_or_update(synapse_comp) 
```

A Synapse Spark pool can also use a user-assigned identity. For a user-assigned identity, you can pass a managed identity definition, using the [IdentityConfiguration](/python/api/azure-ai-ml/azure.ai.ml.entities.identityconfiguration) class, as the `identity` parameter of the `SynapseSparkCompute` class. For the managed identity definition used in this way, set the `type` to `UserAssigned`. In addition, pass a `user_assigned_identities` parameter. The parameter `user_assigned_identities` is a list of objects of the [UserAssignedIdentity](/python/api/azure-ai-ml/azure.ai.ml.entities.userassignedidentity) class. The `resource_id`of the user-assigned identity populates each `UserAssignedIdentity` class object. This code snippet updates a Synapse Spark pool to use a user-assigned identity:

```python
# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    SynapseSparkCompute,
    IdentityConfiguration,
    UserAssignedIdentity,
)
from azure.identity import DefaultAzureCredential

subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

synapse_name = "<ATTACHED_SPARK_POOL_NAME>"
synapse_resource = "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>"
synapse_identity = IdentityConfiguration(
    type="UserAssigned",
    user_assigned_identities=[
        UserAssignedIdentity(
            resource_id="/subscriptions/<SUBSCRIPTION_ID/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID>"
        )
    ],
)

synapse_comp = SynapseSparkCompute(
    name=synapse_name, resource_id=synapse_resource, identity=synapse_identity
)
ml_client.begin_create_or_update(synapse_comp)
```

> [!NOTE]
> If a pool with the specified name does not already exist in the workspace, the `azure.ai.ml.MLClient.begin_create_or_update()` function will attach a new Synapse Spark pool. However, if a Synapse Spark pool, with the specified name, is already attached to the workspace, an `azure.ai.ml.MLClient.begin_create_or_update()` function call will update the existing attached pool, with the new identity or identities.


## Detach the Synapse Spark pool

We might want to detach an attached Synapse Spark pool, to clean up a workspace.


# [Studio UI](#tab/studio-ui)
