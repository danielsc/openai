> Azure Cosmos DB is __not__ used to store information such as model performance, information logged by experiments, or information logged from your model deployments.

> [!IMPORTANT]
> Selecting high business impact can only be done when creating a workspace. You cannot change this setting after workspace creation.

For more information on customer-managed keys and high business impact workspace, see [Enterprise security for Azure Machine Learning](concept-data-encryption.md#encryption-at-rest).

## Using the CLI to manage workspaces

### Get workspace information

To get information about a workspace, use the following command:

```azurecli-interactive
az ml workspace show -n <workspace-name> -g <resource-group-name>
```

For more information, see the [az ml workspace show](/cli/azure/ml/workspace#az-ml-workspace-show) documentation.

### Update a workspace

To update a workspace, use the following command:

```azurecli-interactive
az ml workspace update -n <workspace-name> -g <resource-group-name>
```

For more information, see the [az ml workspace update](/cli/azure/ml/workspace#az-ml-workspace-update) documentation.

### Sync keys for dependent resources

If you change access keys for one of the resources used by your workspace, it takes around an hour for the workspace to synchronize to the new key. To force the workspace to sync the new keys immediately, use the following command:

```azurecli-interactive
az ml workspace sync-keys -n <workspace-name> -g <resource-group-name>
```

For more information on changing keys, see [Regenerate storage access keys](how-to-change-storage-access-key.md).

For more information on the sync-keys command, see [az ml workspace sync-keys](/cli/azure/ml/workspace#az-ml-workspace-sync-keys).

### Delete a workspace

[!INCLUDE [machine-learning-delete-workspace](../../includes/machine-learning-delete-workspace.md)]

To delete a workspace after it's no longer needed, use the following command:

```azurecli-interactive
az ml workspace delete -n <workspace-name> -g <resource-group-name>
```

> [!IMPORTANT]
> Deleting a workspace does not delete the application insight, storage account, key vault, or container registry used by the workspace.

You can also delete the resource group, which deletes the workspace and all other Azure resources in the resource group. To delete the resource group, use the following command:

```azurecli-interactive
az group delete -g <resource-group-name>
```

For more information, see the [az ml workspace delete](/cli/azure/ml/workspace#az-ml-workspace-delete) documentation.

If you accidentally deleted your workspace, are still able to retrieve your notebooks. For more information, see the [workspace deletion](./how-to-high-availability-machine-learning.md#workspace-deletion) section of the disaster recovery article.

## Troubleshooting

### Resource provider errors

[!INCLUDE [machine-learning-resource-provider](../../includes/machine-learning-resource-provider.md)]

### Moving the workspace

> [!WARNING]
> Moving your Azure Machine Learning workspace to a different subscription, or moving the owning subscription to a new tenant, is not supported. Doing so may cause errors.

### Deleting the Azure Container Registry

The Azure Machine Learning workspace uses Azure Container Registry (ACR) for some operations. It will automatically create an ACR instance when it first needs one.

[!INCLUDE [machine-learning-delete-acr](../../includes/machine-learning-delete-acr.md)]

## Next steps

For more information on the Azure CLI extension for machine learning, see the [az ml](/cli/azure/ml) documentation.

To check for problems with your workspace, see [How to use workspace diagnostics](how-to-workspace-diagnostic-api.md).

To learn how to move a workspace to a new Azure subscription, see [How to move a workspace](how-to-move-workspace.md).

For information on how to keep your Azure ML up to date with the latest security updates, see [Vulnerability management](concept-vulnerability-management.md).
