> Perform all steps, updating both the workspace using the CLI, and datastores using Python. Updating only one or the other may cause errors until both are updated.

1. Regenerate the key. For information on regenerating an access key, see [Manage storage account access keys](../storage/common/storage-account-keys-manage.md). Save the new key.

1. The Azure Machine Learning workspace will automatically synchronize the new key and begin using it after an hour. To force the workspace to synch to the new key immediately, use the following steps:

    1. To sign in to the Azure subscription that contains your workspace by using the following Azure CLI command:

        ```azurecli-interactive
        az login
        ```

        [!INCLUDE [select-subscription](../../includes/machine-learning-cli-subscription.md)]

    1. To update the workspace to use the new key, use the following command. Replace `myworkspace` with your Azure Machine Learning workspace name, and replace `myresourcegroup` with the name of the Azure resource group that contains the workspace.

        ```azurecli-interactive
        az ml workspace sync-keys -w myworkspace -g myresourcegroup
        ```

        [!INCLUDE [install extension](../../includes/machine-learning-service-install-extension.md)]

        This command automatically syncs the new keys for the Azure storage account used by the workspace.

1. You can re-register datastore(s) that use the storage account via the SDK or [the Azure Machine Learning studio](https://ml.azure.com).
    1. **To re-register datastores via the Python SDK**, use the values from the [What needs to be updated](#whattoupdate) section and the key from step 1 with the following code. 
    
        Since `overwrite=True` is specified, this code overwrites the existing registration and updates it to use the new key.
    
        ```python
        # Re-register the blob container
        ds_blob = Datastore.register_azure_blob_container(workspace=ws,
                                                  datastore_name='your datastore name',
                                                  container_name='your container name',
                                                  account_name='your storage account name',
                                                  account_key='new storage account key',
                                                  overwrite=True)
        # Re-register file shares
        ds_file = Datastore.register_azure_file_share(workspace=ws,
                                              datastore_name='your datastore name',
                                              file_share_name='your container name',
                                              account_name='your storage account name',
                                              account_key='new storage account key',
                                              overwrite=True)
        
        ```
    
    1. **To re-register datastores via the studio**
        1. In the studio, select **Data** on the left pane under **Assets**.
        1. At the top, select **Datastores**.
        1. Select which datastore you want to update.
        1. Select the **Update credentials** button on the top left. 
        1. Use your new access key from step 1 to populate the form and click **Save**.
        
            If you are updating credentials for your **default datastore**, complete this step and repeat step 2b to resync your new key with the default datastore of the workspace. 

## Next steps

For more information on registering datastores, see the [`Datastore`](/python/api/azureml-core/azureml.core.datastore%28class%29) class reference.
