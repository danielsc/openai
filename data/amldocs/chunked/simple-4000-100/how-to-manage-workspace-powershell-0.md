
# Manage Azure Machine Learning workspaces using Azure PowerShell

Use the Azure PowerShell module for Azure Machine Learning to create and manage your Azure Machine Learning workspaces. For a full list of the Azure PowerShell cmdlets for Azure Machine Learning, see the [Az.MachineLearningServices](/powershell/module/az.machinelearningservices) reference documentation.

You can also manage workspaces [using the Azure CLI](how-to-manage-workspace-cli.md), [Azure portal and Python SDK](how-to-manage-workspace.md), or [via the VS Code extension](how-to-setup-vs-code.md).

## Prerequisites

- An **Azure subscription**. If you don't have one, try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
- The [Azure PowerShell module](https://www.powershellgallery.com/packages/Az). To make sure you have the latest version, see [Install the Azure PowerShell module](/powershell/azure/install-az-ps).

  > [!IMPORTANT]
  > While the **Az.MachineLearningServices** PowerShell module is in preview, you must install it
  > separately using the `Install-Module` cmdlet.

  ```azurepowershell-interactive
  Install-Module -Name Az.MachineLearningServices -Scope CurrentUser -Repository PSGallery -Force
## Sign in to Azure

Sign in to your Azure subscription with the `Connect-AzAccount` command and follow the on-screen directions.

```azurepowershell
Connect-AzAccount
```

If you don't know which location you want to use, you can list the available locations. Display the list of locations by using the following code example and find the one you want to use. This example uses **eastus**. Store the location in a variable and use the variable so you can change it in one place.

```azurepowershell-interactive
Get-AzLocation | Select-Object -Property Location
$Location = 'eastus'
```

## Create a resource group

Create an Azure resource group with [New-AzResourceGroup](/powershell/module/az.resources/new-azresourcegroup). A resource group is a logical container into which Azure resources are deployed and managed.

```azurepowershell-interactive
$ResourceGroup = 'MyResourceGroup'
New-AzResourceGroup -Name $ResourceGroup -Location $Location
```

## Create dependency resources

An Azure Machine Learning workspace depends on the following Azure resources:

* Application Insights
* Azure Key Vault
* Azure Storage Account

Use the following commands to create these resources and retrieve the Azure Resource Manager ID for each of them:

> [!NOTE]
> The Microsoft.Insights resource provider must be registered for your subscription prior to running
> the following commands. This is a one time registration. Use
> `Register-AzResourceProvider -ProviderNamespace Microsoft.Insights` to perform the registration.

1. Create the Application Insights instance:

   ```azurepowershell-interactive
   $AppInsights = 'MyAppInsights'
   New-AzApplicationInsights -Name $AppInsights -ResourceGroupName $ResourceGroup -Location $Location
   $appid = (Get-AzResource -Name $AppInsights -ResourceGroupName $ResourceGroup).ResourceId

1. Create the Azure Key Vault:

    > [!IMPORTANT]
    > Each key vault must have a unique name. Replace `MyKeyVault` with the name of your key vault in the following example.

   ```azurepowershell-interactive
   $KeyVault = 'MyKeyVault'
   New-AzKeyVault -Name $KeyVault -ResourceGroupName $ResourceGroup -Location $Location
   $kvid = (Get-AzResource -Name $KeyVault -ResourceGroupName $ResourceGroup).ResourceId

1. Create the Azure Storage Account:

    > [!IMPORTANT]
    > Each storage account must have a unique name. Replace `MyStorage` with the name of your storage account in the following example. You can use `Get-AzStorageAccountNameAvailability -Name 'YourUniqueName'` to verify the name before running the following example.

   ```azurepowershell-interactive
   $Storage = 'MyStorage'

   $storageParams = @{
     Name = $Storage
     ResourceGroupName = $ResourceGroup
     Location = $Location
     SkuName = 'Standard_LRS'
     Kind = 'StorageV2'
   }
   New-AzStorageAccount @storageParams

   $storeid = (Get-AzResource -Name $Storage -ResourceGroupName $ResourceGroup).ResourceId

## Create a workspace

> [!NOTE]
> The Microsoft.MachineLearningServices resource provider must be registered for your subscription
> prior to running the following commands. This is a one time registration. Use
> `Register-AzResourceProvider -ProviderNamespace Microsoft.MachineLearningServices` to perform the
> registration.

The following command creates the workspace and configures it to use the services created previously. It also configures the workspace to use a system-assigned managed identity, which is used to access these services. For more information on using managed identities with Azure Machine Learning, see the [Set up authentication to other services](how-to-identity-based-service-authentication.md) article.

```azurepowershell-interactive
$Workspace = 'MyWorkspace'
$mlWorkspaceParams = @{
  Name = $Workspace
  ResourceGroupName = $ResourceGroup
  Location = $Location
  ApplicationInsightID = $appid
  KeyVaultId = $kvid
  StorageAccountId = $storeid
  IdentityType = 'SystemAssigned'
}
New-AzMLWorkspace @mlWorkspaceParams
```
