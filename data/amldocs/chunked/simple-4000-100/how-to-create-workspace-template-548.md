
    After these changes, you can specify the ID of the existing Key Vault resource when running the template. The template will then reuse the Key Vault by setting the `keyVault` property of the workspace to its ID.

    To get the ID of the Key Vault, you can reference the output of the original template job or use the Azure CLI. The following command is an example of using the Azure CLI to get the Key Vault resource ID:

    ```azurecli
    az keyvault show --name mykeyvault --resource-group myresourcegroup --query id
    ```

    This command returns a value similar to the following text:

    ```text
    /subscriptions/{subscription-guid}/resourceGroups/myresourcegroup/providers/Microsoft.KeyVault/vaults/mykeyvault
    ```

## Next steps

* [Deploy resources with Resource Manager templates and Resource Manager REST API](../azure-resource-manager/templates/deploy-rest.md).
* [Creating and deploying Azure resource groups through Visual Studio](../azure-resource-manager/templates/create-visual-studio-deployment-project.md).
* [For other templates related to Azure Machine Learning, see the Azure Quickstart Templates repository](https://github.com/Azure/azure-quickstart-templates).
* [How to use workspace diagnostics](how-to-workspace-diagnostic-api.md).
* [Move an Azure Machine Learning workspace to another subscription](how-to-move-workspace.md).
