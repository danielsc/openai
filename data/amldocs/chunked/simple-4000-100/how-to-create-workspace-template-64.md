> While the template associated with this document creates a new Azure Container Registry, you can also create a new workspace without creating a container registry. One will be created when you perform an operation that requires a container registry. For example, training or deploying a model.
>
> You can also reference an existing container registry or storage account in the Azure Resource Manager template, instead of creating a new one. When doing so, you must either [use a managed identity](how-to-identity-based-service-authentication.md) (preview), or [enable the admin account](../container-registry/container-registry-authentication.md#admin-account) for the container registry.

[!INCLUDE [machine-learning-delete-acr](../../includes/machine-learning-delete-acr.md)]

For more information on templates, see the following articles:

* [Author Azure Resource Manager templates](../azure-resource-manager/templates/syntax.md)
* [Deploy an application with Azure Resource Manager templates](../azure-resource-manager/templates/deploy-powershell.md)
* [Microsoft.MachineLearningServices resource types](/azure/templates/microsoft.machinelearningservices/allversions)

## Deploy template

To deploy your template you have to create a resource group.

See the [Azure portal](#use-the-azure-portal) section if you prefer using the graphical user interface.

# [Azure CLI](#tab/azcli)


```azurecli
az group create --name "examplegroup" --location "eastus"
```

# [Azure PowerShell](#tab/azpowershell)

```azurepowershell
New-AzResourceGroup -Name "examplegroup" -Location "eastus"
```


Once your resource group is successfully created, deploy the template with the following command:

# [Azure CLI](#tab/azcli)

```azurecli
az deployment group create \
    --name "exampledeployment" \
    --resource-group "examplegroup" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" \
    --parameters workspaceName="exampleworkspace" location="eastus"
```

# [Azure PowerShell](#tab/azpowershell)

```azurepowershell
New-AzResourceGroupDeployment `
  -Name "exampledeployment" `
  -ResourceGroupName "examplegroup" `
  -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" `
  -workspaceName "exampleworkspace" `
  -location "eastus"
```


By default, all of the resources created as part of the template are new. However, you also have the option of using existing resources. By providing additional parameters to the template, you can use existing resources. For example, if you want to use an existing storage account set the **storageAccountOption** value to **existing** and provide the name of your storage account in the **storageAccountName** parameter.

> [!IMPORTANT]
> If you want to use an existing Azure Storage account, it cannot be a premium account (Premium_LRS and Premium_GRS). It also cannot have a hierarchical namespace (used with Azure Data Lake Storage Gen2). Neither premium storage or hierarchical namespace are supported with the default storage account of the workspace. Neither premium storage or hierarchical namespaces are supported with the _default_ storage account of the workspace. You can use premium storage or hierarchical namespace with _non-default_ storage accounts.

# [Azure CLI](#tab/azcli)

```azurecli
az deployment group create \
    --name "exampledeployment" \
    --resource-group "examplegroup" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" \
    --parameters workspaceName="exampleworkspace" \
      location="eastus" \
      storageAccountOption="existing" \
      storageAccountName="existingstorageaccountname"
```

# [Azure PowerShell](#tab/azpowershell)
