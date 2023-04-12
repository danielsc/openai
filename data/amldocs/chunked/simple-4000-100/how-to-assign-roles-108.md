
After deployment, this role becomes available in the specified workspace. Now you can add and assign this role in the Azure portal.

For more information on custom roles, see [Azure custom roles](../role-based-access-control/custom-roles.md). 

### Azure Machine Learning operations

For more information on the operations (actions and not actions) usable with custom roles, see [Resource provider operations](../role-based-access-control/resource-provider-operations.md#microsoftmachinelearningservices). You can also use the following Azure CLI command to list operations:

```azurecli-interactive
az provider operation show –n Microsoft.MachineLearningServices
```

## List custom roles

In the Azure CLI, run the following command:

```azurecli-interactive
az role definition list --subscription <sub-id> --custom-role-only true
```

To view the role definition for a specific custom role, use the following Azure CLI command. The `<role-name>` should be in the same format returned by the command above:

```azurecli-interactive
az role definition list -n <role-name> --subscription <sub-id>
```

## Update a custom role

In the Azure CLI, run the following command:

```azurecli-interactive
az role definition update --role-definition update_def.json --subscription <sub-id>
```

You need to have permissions on the entire scope of your new role definition. For example if this new role has a scope across three subscriptions, you need to have permissions on all three subscriptions. 

> [!NOTE]
> Role updates can take 15 minutes to an hour to apply across all role assignments in that scope.

## Use Azure Resource Manager templates for repeatability

If you anticipate that you'll need to recreate complex role assignments, an Azure Resource Manager template can be a significant help. The [machine-learning-dependencies-role-assignment template](https://github.com/Azure/azure-quickstart-templates/tree/master//quickstarts/microsoft.machinelearningservices/machine-learning-dependencies-role-assignment) shows how role assignments can be specified in source code for reuse. 

## Common scenarios

The following table is a summary of Azure Machine Learning activities and the permissions required to perform them at the least scope. For example, if an activity can be performed with a workspace scope (Column 4), then all higher scope with that permission will also work automatically. Note that for certain activities the permissions differ between V1 and V2 APIs.

> [!IMPORTANT]
> All paths in this table that start with `/` are **relative paths** to `Microsoft.MachineLearningServices/` :

| Activity | Subscription-level scope | Resource group-level scope | Workspace-level scope |
| ----- | ----- | ----- | ----- |
| Create new workspace <sub>1</sub> | Not required | Owner or contributor | N/A (becomes Owner or inherits higher scope role after creation) |
| Request subscription level Amlcompute quota or set workspace level quota | Owner, or contributor, or custom role </br>allowing `/locations/updateQuotas/action`</br> at subscription scope | Not Authorized | Not Authorized |
| Create new compute cluster | Not required | Not required | Owner, contributor, or custom role allowing: `/workspaces/computes/write` |
| Create new compute instance | Not required | Not required | Owner, contributor, or custom role allowing: `/workspaces/computes/write` |
| Submitting any type of run (V1) | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/*/read", "/workspaces/environments/write", "/workspaces/experiments/runs/write", "/workspaces/metadata/artifacts/write", "/workspaces/metadata/snapshots/write", "/workspaces/environments/build/action", "/workspaces/experiments/runs/submit/action", "/workspaces/environments/readSecrets/action"` |
| Submitting any type of run (V2) | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/*/read", "/workspaces/environments/write", "/workspaces/jobs/*", "/workspaces/metadata/artifacts/write", "/workspaces/metadata/codes/*/write", "/workspaces/environments/build/action", "/workspaces/environments/readSecrets/action"` |
