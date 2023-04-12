
# [Azure PowerShell](#tab/azpowershell)

```azurepowershell
New-AzResourceGroupDeployment `
  -Name "exampledeployment" `
  -ResourceGroupName "examplegroup" `
  -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" `
  -workspaceName "exampleworkspace" `
  -location "eastus" `
  -encryption_status "Enabled" `
  -cmk_keyvault "/subscriptions/{subscription-guid}/resourceGroups/<resource-group-name>/providers/Microsoft.KeyVault/vaults/<keyvault-name>" `
  -resource_cmk_uri "https://mykeyvault.vault.azure.net/keys/mykey/{guid}"
```

When using a customer-managed key, Azure Machine Learning creates a secondary resource group which contains the Azure Cosmos DB instance. For more information, see [Encryption at rest in Azure Cosmos DB](concept-data-encryption.md#encryption-at-rest).

An additional configuration you can provide for your data is to set the **confidential_data** parameter to **true**. Doing so, does the following:

* Starts encrypting the local scratch disk for Azure Machine Learning compute clusters, providing you have not created any previous clusters in your subscription. If you have previously created a cluster in the subscription, open a support ticket to have encryption of the scratch disk enabled for your compute clusters.
* Cleans up the local scratch disk between jobs.
* Securely passes credentials for the storage account, container registry, and SSH account from the execution layer to your compute clusters by using key vault.
* Enables IP filtering to ensure the underlying batch pools cannot be called by any external services other than AzureMachineLearningService.

    > [!IMPORTANT]
    > Once a workspace has been created, you cannot change the settings for confidential data, encryption, key vault ID, or key identifiers. To change these values, you must create a new workspace using the new values.

  For more information, see [encryption at rest](concept-data-encryption.md#encryption-at-rest).

## Deploy workspace behind a virtual network

By setting the `vnetOption` parameter value to either `new` or `existing`, you are able to create the resources used by a workspace behind a virtual network.

> [!IMPORTANT]
> For container registry, only the 'Premium' sku is supported.

> [!IMPORTANT]
> Application Insights does not support deployment behind a virtual network.

### Only deploy workspace behind private endpoint

If your associated resources are not behind a virtual network, you can set the **privateEndpointType** parameter to `AutoAproval` or `ManualApproval` to deploy the workspace behind a private endpoint. This can be done for both new and existing workspaces. When updating an existing workspace, fill in the template parameters with the information from the existing workspace.

# [Azure CLI](#tab/azcli)

```azurecli
az deployment group create \
    --name "exampledeployment" \
    --resource-group "examplegroup" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" \
    --parameters workspaceName="exampleworkspace" \
      location="eastus" \
      privateEndpointType="AutoApproval"
```

# [Azure PowerShell](#tab/azpowershell)

```azurepowershell
New-AzResourceGroupDeployment `
  -Name "exampledeployment" `
  -ResourceGroupName "examplegroup" `
  -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" `
  -workspaceName "exampleworkspace" `
  -location "eastus" `
  -privateEndpointType "AutoApproval"
```


### Use a new virtual network

To deploy a resource behind a new virtual network, set the **vnetOption** to **new** along with the virtual network settings for the respective resource. The deployment below shows how to deploy a workspace with the storage account resource behind a new virtual network.
