
# [Azure PowerShell](#tab/azpowershell)

```azurepowershell
New-AzResourceGroupDeployment `
  -Name "exampledeployment" `
  -ResourceGroupName "examplegroup" `
  -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" `
  -workspaceName "exampleworkspace" `
  -location "eastus" `
  -storageAccountOption "existing" `
  -storageAccountName "existingstorageaccountname"
```


## Deploy an encrypted workspace

The following example template demonstrates how to create a workspace with three settings:

* Enable high confidentiality settings for the workspace. This creates a new Azure Cosmos DB instance.
* Enable encryption for the workspace.
* Uses an existing Azure Key Vault to retrieve customer-managed keys. Customer-managed keys are used to create a new Azure Cosmos DB instance for the workspace.

> [!IMPORTANT]
> Once a workspace has been created, you cannot change the settings for confidential data, encryption, key vault ID, or key identifiers. To change these values, you must create a new workspace using the new values.

For more information, see [Customer-managed keys](concept-customer-managed-keys.md).

> [!IMPORTANT]
> There are some specific requirements your subscription must meet before using this template:
> * You must have an existing Azure Key Vault that contains an encryption key.
> * The Azure Key Vault must be in the same region where you plan to create the Azure Machine Learning workspace.
> * You must specify the ID of the Azure Key Vault and the URI of the encryption key.
> 
> For steps on creating the vault and key, see [Configure customer-managed keys](how-to-setup-customer-managed-keys.md).

__To get the values__ for the `cmk_keyvault` (ID of the Key Vault) and the `resource_cmk_uri` (key URI) parameters needed by this template, use the following steps:	

1. To get the Key Vault ID, use the following command:	

    # [Azure CLI](#tab/azcli)	
    
    ```azurecli	
    az keyvault show --name <keyvault-name> --query 'id' --output tsv	
    ```	
    
    # [Azure PowerShell](#tab/azpowershell)	
    
    ```azurepowershell	
    Get-AzureRMKeyVault -VaultName '<keyvault-name>'	
    ```	

    This command returns a value similar to `/subscriptions/{subscription-guid}/resourceGroups/<resource-group-name>/providers/Microsoft.KeyVault/vaults/<keyvault-name>`.	

1. To get the value for the URI for the customer managed key, use the following command:	

    # [Azure CLI](#tab/azcli)	
    
    ```azurecli	
    az keyvault key show --vault-name <keyvault-name> --name <key-name> --query 'key.kid' --output tsv	
    ```	
    
    # [Azure PowerShell](#tab/azpowershell)	
    
    ```azurepowershell	
    Get-AzureKeyVaultKey -VaultName '<keyvault-name>' -KeyName '<key-name>'	
    ```	

  This command returns a value similar to `https://mykeyvault.vault.azure.net/keys/mykey/{guid}`.	

> [!IMPORTANT]	
> Once a workspace has been created, you cannot change the settings for confidential data, encryption, key vault ID, or key identifiers. To change these values, you must create a new workspace using the new values.

To enable use of Customer Managed Keys, set the following parameters when deploying the template:

* **encryption_status** to **Enabled**.
* **cmk_keyvault** to the `cmk_keyvault` value obtained in previous steps.
* **resource_cmk_uri** to the `resource_cmk_uri` value obtained in previous steps.

# [Azure CLI](#tab/azcli)

```azurecli
az deployment group create \
    --name "exampledeployment" \
    --resource-group "examplegroup" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" \
    --parameters workspaceName="exampleworkspace" \
      location="eastus" \
      encryption_status="Enabled" \
      cmk_keyvault="/subscriptions/{subscription-guid}/resourceGroups/<resource-group-name>/providers/Microsoft.KeyVault/vaults/<keyvault-name>" \
      resource_cmk_uri="https://mykeyvault.vault.azure.net/keys/mykey/{guid}" \
```
