
## Get workspace information

To retrieve a list of workspaces, use the following command:

```azurepowershell-interactive
Get-AzMLWorkspace
```

To retrieve information on a specific workspace, provide the name and resource group information:

```azurepowershell-interactive
Get-AzMLWorkspace -Name $Workspace -ResourceGroupName $ResourceGroup
```

## Delete a workspace

[!INCLUDE [machine-learning-delete-workspace](../../includes/machine-learning-delete-workspace.md)]

To delete a workspace after it's no longer needed, use the following command:

```azurepowershell-interactive
Remove-AzMLWorkspace -Name $Workspace -ResourceGroupName $ResourceGroup
```

> [!IMPORTANT]
> Deleting a workspace does not delete the application insight, storage account, key vault, or container registry used by the workspace.

You can also delete the resource group, which deletes the workspace and all other Azure resources in the resource group. To delete the resource group, use the following command:

```azurepowershell-interactive
Remove-AzResourceGroup -Name $ResourceGroup
```

## Next steps

To check for problems with your workspace, see [How to use workspace diagnostics](how-to-workspace-diagnostic-api.md).

To learn how to move a workspace to a new Azure subscription, see [How to move a workspace](how-to-move-workspace.md).

For information on how to keep your Azure ML up to date with the latest security updates, see [Vulnerability management](concept-vulnerability-management.md).

To learn how to train an ML model with your workspace, see the [Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md) tutorial.