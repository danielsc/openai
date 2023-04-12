* The workspace mustn't be in use during the move operation. Verify that all experiment jobs, data profiling jobs, and labeling projects have completed. Also verify that inference endpoints aren't being invoked.
* The workspace will become unavailable during the move.
* Before to the move, you must delete or detach computes and inference endpoints from the workspace.
* Datastores may still show the old subscription information after the move.

## Prepare and validate the move

1. In Azure CLI, set the subscription to that of your origin workspace

    ```azurecli-interactive
    az account set -s origin-sub-id
    ```

2. Verify that the origin workspace isn't being used. Check that any experiment jobs, data profiling jobs, or labeling projects have completed. Also verify that inferencing endpoints aren't being invoked. 

3. Delete or detach any computes from the workspace, and delete any inferencing endpoints. Moving computes and endpoints isn't supported. Also note that the workspace will become unavailable during the move.

4. Create a destination resource group in the new subscription. This resource group will contain the workspace after the move. The destination must be in the same region as the origin.

    ```azurecli-interactive
    az group create -g destination-rg -l my-region --subscription destination-sub-id                  
    ```

5. The following command demonstrates how to validate the move operation for workspace. You can include associated resources such as storage account, container registry, key vault, and application insights into the move by adding them to the ```resources``` list. The validation may take several minutes. In this command, `origin-rg` is the origin resource group, while `destination-rg` is the destination. The subscription IDs are represented by `origin-sub-id` and `destination-sub-id`, while the workspace is `origin-workspace-name`:

    ```azurecli-interactive
    az resource invoke-action --action validateMoveResources --ids "/subscriptions/origin-sub-id/resourceGroups/origin-rg" --request-body "{  \"resources\": [\"/subscriptions/origin-sub-id/resourceGroups/origin-rg/providers/Microsoft.MachineLearningServices/workspaces/origin-workspace-name\"],\"targetResourceGroup\":\"/subscriptions/destination-sub-id/resourceGroups/destination-rg\" }"
    ```

## Move the workspace

Once the validation has succeeded, move the workspace. You may also include any associated resources into move operation by adding them to the ```ids``` parameter. This operation may take several minutes.

```azurecli-interactive
az resource move --destination-group destination-rg --destination-subscription-id destination-sub-id --ids "/subscriptions/origin-sub-id/resourceGroups/origin-rg/providers/Microsoft.MachineLearningServices/workspaces/origin-workspace-name"
```

After the move has completed, recreate any computes and redeploy any web service endpoints at the new location.

## Next steps

* Learn about [resource move](../azure-resource-manager/management/move-resource-group-and-subscription.md)
