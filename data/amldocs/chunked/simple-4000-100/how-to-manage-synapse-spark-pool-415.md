Execute the `az ml compute update` command, with appropriate parameters, to update the identity associated with an attached Synapse Spark pool. To assign a system-assigned identity, set the `--identity` parameter in the command to `SystemAssigned`, as shown:

```azurecli
az ml compute update --identity SystemAssigned --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME> --name <ATTACHED_SPARK_POOL_NAME>
```

This sample shows the expected output of the above command:

```azurecli
Class SynapseSparkCompute: This is an experimental class, and may change at any time. Please see https://aka.ms/azuremlexperimental for more information.
{
    "auto_pause_settings": {
    "auto_pause_enabled": true,
    "delay_in_minutes": 15
    },
    "created_on": "2022-09-13 20:02:15.746490+00:00",
    "id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<AML_WORKSPACE_NAME>/computes/<ATTACHED_SPARK_POOL_NAME>",
    "identity": {
    "principal_id": "<PRINCIPAL_ID>",
    "tenant_id": "<TENANT_ID>",
    "type": "system_assigned"
    },
    "location": "eastus2",
    "name": "<ATTACHED_SPARK_POOL_NAME>",
    "node_count": 5,
    "node_family": "MemoryOptimized",
    "node_size": "Small",
    "provisioning_state": "Succeeded",
    "resourceGroup": "<RESOURCE_GROUP>",
    "resource_id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<AML_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>",
    "scale_settings": {
    "auto_scale_enabled": false,
    "max_node_count": 0,
    "min_node_count": 0
    },
    "spark_version": "3.2",
    "type": "synapsespark"
}
```

To assign a user-assigned identity, set the parameter `--identity` in the command to `UserAssigned`. Additionally, you should pass the resource ID, for the user-assigned identity, using the `--user-assigned-identities` parameter as shown:

```azurecli
az ml compute update --identity UserAssigned --user-assigned-identities /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID> --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME> --name <ATTACHED_SPARK_POOL_NAME>
```

This sample shows the expected output of the above command:

```azurecli
Class SynapseSparkCompute: This is an experimental class, and may change at any time. Please see https://aka.ms/azuremlexperimental for more information.
{
  "auto_pause_settings": {
    "auto_pause_enabled": true,
    "delay_in_minutes": 15
  },
  "created_on": "2022-09-13 20:02:15.746490+00:00",
  "id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<AML_WORKSPACE_NAME>/computes/<ATTACHED_SPARK_POOL_NAME>",
  "identity": {
    "type": "user_assigned",
    "user_assigned_identities": [
      {
        "client_id": "<CLIENT_ID>",
        "principal_id": "<PRINCIPAL_ID>",
        "resource_id": "/subscriptions/<SUBSCRIPTION_ID>/resourcegroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID>"
      }
    ]
  },
  "location": "eastus2",
  "name": "<ATTACHED_SPARK_POOL_NAME>",
  "node_count": 5,
  "node_family": "MemoryOptimized",
  "node_size": "Small",
  "provisioning_state": "Succeeded",
  "resourceGroup": "<RESOURCE_GROUP>",
  "resource_id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>",
  "scale_settings": {
    "auto_scale_enabled": false,
    "max_node_count": 0,
    "min_node_count": 0
  },
  "spark_version": "3.2",
  "type": "synapsespark"
}
```

> [!NOTE]
> The parameter `--user-assigned-identities` can take a list of resource IDs and assign multiple user-defined identities to an attached Synapse Spark pool. The first user-assigned identity in the list will be used for submitting a job by default.
