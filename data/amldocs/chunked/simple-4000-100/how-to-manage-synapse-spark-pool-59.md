1. Enter a **Name**, which will refer to the attached Synapse Spark Pool inside the Azure Machine Learning.

1. Select an Azure **Subscription** from the dropdown menu.

1. Select a **Synapse workspace** from the dropdown menu.

1. Select a **Spark Pool** from the dropdown menu.

1. Toggle the **Assign a managed identity** option, to enable it.

1. Select a managed **Identity type** to use with this attached Synapse Spark Pool.

1. Select **Update**, to complete the Synapse Spark Pool attach process.

# [CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

With the Azure Machine Learning CLI, we can attach and manage a Synapse Spark pool from the command line interface, using intuitive YAML syntax and commands.

To define an attached Synapse Spark pool using YAML syntax, the YAML file should cover these properties: 

- `name` – name of the attached Synapse Spark pool.

- `type` – set this property to `synapsespark`.

- `resource_id` – this property should provide the resource ID value of the Synapse Spark pool created in the Azure Synapse Analytics workspace. The Azure resource ID includes

  - Azure Subscription ID, 

  - resource Group Name, 

  - Azure Synapse Analytics Workspace Name, and

  - name of the Synapse Spark Pool.

    ```YAML
    name: <ATTACHED_SPARK_POOL_NAME>
  
    type: synapsespark

    resource_id: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>
    ```

- `identity` – this property defines the identity type to assign to the attached Synapse Spark pool. It can take one of these values:

    - `system_assigned`
    - `user_assigned`

        ```YAML
        name: <ATTACHED_SPARK_POOL_NAME>
    
        type: synapsespark

        resource_id: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>

        identity:
        type: system_assigned
        ```

- For the `identity` type `user_assigned`, you should also provide a list of `user_assigned_identities` values. Each user-assigned identity should be declared as an element of the list, by using the `resource_id` value of the user-assigned identity. The first user-assigned identity in the list will be used for submitting a job by default.

    ```YAML
    name: <ATTACHED_SPARK_POOL_NAME>
  
    type: synapsespark

    resource_id: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Synapse/workspaces/<SYNAPSE_WORKSPACE_NAME>/bigDataPools/<SPARK_POOL_NAME>

    identity:
      type: user_assigned
      user_assigned_identities:
        - resource_id: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID>
    ```

The YAML files above can be used in the `az ml compute attach` command as the `--file` parameter. A Synapse Spark pool can be attached to an Azure Machine Learning workspace, in a specified resource group of a subscription, with the `az ml compute attach` command as shown here:

```azurecli
az ml compute attach --file <YAML_SPECIFICATION_FILE_NAME>.yaml --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --workspace-name <AML_WORKSPACE_NAME>
```

This sample shows the expected output of the above command:

```azurecli
Class SynapseSparkCompute: This is an experimental class, and may change at any time. Please see https://aka.ms/azuremlexperimental for more information.

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
