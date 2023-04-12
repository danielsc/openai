
If the attached Synapse Spark pool, with the name specified in the YAML specification file, already exists in the workspace, then `az ml compute attach` command execution will update the existing pool with the information provided in the YAML specification file. You can update the

- identity type
- user assigned identities
- tags

values through YAML specification file.

To display details of an attached Synapse Spark pool, execute the `az ml compute show` command. Pass the name of the attached Synapse Spark pool with the `--name` parameter, as shown: 

```azurecli
az ml compute show --name <ATTACHED_SPARK_POOL_NAME> --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

This sample shows the expected output of the above command:

```azurecli
<ATTACHED_SPARK_POOL_NAME>
{
    "auto_pause_settings": {
    "auto_pause_enabled": true,
    "delay_in_minutes": 15
    },
    "created_on": "2022-09-13 19:01:05.109840+00:00",
    "id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<AML_WORKSPACE_NAME>/computes/<ATTACHED_SPARK_POOL_NAME>",
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

To see a list of all computes, including the attached Synapse Spark pools in a workspace, use the `az ml compute list` command. Use the name parameter to pass the name of the workspace, as shown: 

```azurecli
az ml compute list --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

This sample shows the expected output of the above command:

```azurecli
[
    {
    "auto_pause_settings": {
        "auto_pause_enabled": true,
        "delay_in_minutes": 15
    },
    "created_on": "2022-09-09 21:28:54.871251+00:00",
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
    "resource_id": "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>",
    "scale_settings": {
        "auto_scale_enabled": false,
        "max_node_count": 0,
        "min_node_count": 0
    },
    "spark_version": "3.2",
    "type": "synapsespark"
    },
    ...
]
```

# [Python SDK](#tab/sdk)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Azure Machine Learning Python SDK (preview) provides convenient functions for attaching and managing Synapse Spark pool, using Python code in Azure Machine Learning Notebooks.

To attach a Synapse Compute using Python SDK, first create an instance of [azure.ai.ml.MLClient class](/python/api/azure-ai-ml/azure.ai.ml.mlclient). This provides convenient functions for interaction with Azure Machine Learning services. The following code sample uses `azure.identity.DefaultAzureCredential` for connecting to a workspace in resource group of a specified Azure subscription. In the following code sample, define the `SynapseSparkCompute` with the parameters:
