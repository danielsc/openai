To attach a Synapse Compute using Python SDK, first create an instance of [azure.ai.ml.MLClient class](/python/api/azure-ai-ml/azure.ai.ml.mlclient). This provides convenient functions for interaction with Azure Machine Learning services. The following code sample uses `azure.identity.DefaultAzureCredential` for connecting to a workspace in resource group of a specified Azure subscription. In the following code sample, define the `SynapseSparkCompute` with the parameters:
- `name` - user-defined name of the new attached Synapse Spark pool. 
- `resource_id` - resource ID of the Synapse Spark pool created earlier in the Azure Synapse Analytics workspace.

An [azure.ai.ml.MLClient.begin_create_or_update()](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-begin-create-or-update) function call attaches the defined Synapse Spark pool to the Azure Machine Learning workspace.

```python
from azure.ai.ml import MLClient
from azure.ai.ml.entities import SynapseSparkCompute
from azure.identity import DefaultAzureCredential

subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

synapse_name = "<ATTACHED_SPARK_POOL_NAME>"
synapse_resource = "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>"

synapse_comp = SynapseSparkCompute(name=synapse_name, resource_id=synapse_resource)
ml_client.begin_create_or_update(synapse_comp)
```

To attach a Synapse Spark pool that uses system-assigned identity, pass [IdentityConfiguration](/python/api/azure-ai-ml/azure.ai.ml.entities.identityconfiguration), with type set to `SystemAssigned`, as the `identity` parameter of the `SynapseSparkCompute` class. This code snippet attaches a Synapse Spark pool that uses system-assigned identity.

```python
# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import SynapseSparkCompute, IdentityConfiguration
from azure.identity import DefaultAzureCredential

subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
workspace_name = "<AML_WORKSPACE_NAME>"

ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

synapse_name = "<ATTACHED_SPARK_POOL_NAME>"
synapse_resource = "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>"
synapse_identity = IdentityConfiguration(type="SystemAssigned")

synapse_comp = SynapseSparkCompute(
    name=synapse_name, resource_id=synapse_resource, identity=synapse_identity
)
ml_client.begin_create_or_update(synapse_comp)
```

A Synapse Spark pool can also use a user-assigned identity. For a user-assigned identity, you can pass a managed identity definition, using the [IdentityConfiguration](/python/api/azure-ai-ml/azure.ai.ml.entities.identityconfiguration) class, as the `identity` parameter of the `SynapseSparkCompute` class. For the managed identity definition used in this way, set the `type` to `UserAssigned`. In addition, pass a `user_assigned_identities` parameter. The parameter `user_assigned_identities` is a list of objects of the [UserAssignedIdentity](/python/api/azure-ai-ml/azure.ai.ml.entities.userassignedidentity) class. The `resource_id`of the user-assigned identity populates each `UserAssignedIdentity` class object. This code snippet attaches a Synapse Spark pool that uses a user-assigned identity:

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
