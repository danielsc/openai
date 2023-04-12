        
    # [Azure PowerShell](#tab/azpowershell)
      
    ```azurepowershell
    Get-AzVirtualNetwork -ResourceGroupName "examplegroup" -Name "examplevnet" | Set-AzVirtualNetworkSubnetConfig -Name "examplesubnet" -AddressPrefix "<subnet prefix>" -ServiceEndpoint "Microsoft.Storage" | Set-AzVirtualNetwork
    Get-AzVirtualNetwork -ResourceGroupName "examplegroup" -Name "examplevnet" | Set-AzVirtualNetworkSubnetConfig -Name "examplesubnet" -AddressPrefix "<subnet prefix>" -ServiceEndpoint "Microsoft.KeyVault" | Set-AzVirtualNetwork
    Get-AzVirtualNetwork -ResourceGroupName "examplegroup" -Name "examplevnet" | Set-AzVirtualNetworkSubnetConfig -Name "examplesubnet" -AddressPrefix "<subnet prefix>" -ServiceEndpoint "Microsoft.ContainerRegistry" | Set-AzVirtualNetwork
    ```
    

1. Deploy the workspace

    # [Azure CLI](#tab/azcli)
    
    ```azurecli
    az deployment group create \
    --name "exampledeployment" \
    --resource-group "examplegroup" \
    --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json" \
    --parameters workspaceName="exampleworkspace" \
      location="eastus" \
      vnetOption="existing" \
      vnetName="examplevnet" \
      vnetResourceGroupName="examplegroup" \
      storageAccountBehindVNet="true" \
      keyVaultBehindVNet="true" \
      containerRegistryBehindVNet="true" \
      containerRegistryOption="new" \
      containerRegistrySku="Premium" \
      subnetName="examplesubnet" \
      subnetOption="existing"
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
      -vnetOption "existing" `
      -vnetName "examplevnet" `
      -vnetResourceGroupName "examplegroup" `
      -storageAccountBehindVNet "true"
      -keyVaultBehindVNet "true" `
      -containerRegistryBehindVNet "true" `
      -containerRegistryOption "new" `
      -containerRegistrySku "Premium" `
      -subnetName "examplesubnet" `
      -subnetOption "existing"
      -privateEndpointType "AutoApproval"
    ```

## Use the Azure portal

1. Follow the steps in [Deploy resources from custom template](../azure-resource-manager/templates/deploy-portal.md#deploy-resources-from-custom-template). When you arrive at the __Select a template__ screen, choose the **quickstarts** entry. When it appears, select the link labeled "Click here to open template repository". This link takes you to the `quickstarts` directory in the Azure quickstart templates repository.
1. In the list of quickstart templates, select `microsoft.machinelearningservices`. Finally, select `Deploy to Azure`.
1. When the template appears, provide the following required information and any other parameters depending on your deployment scenario.

   * Subscription: Select the Azure subscription to use for these resources.
   * Resource group: Select or create a resource group to contain the services.
   * Region: Select the Azure region where the resources will be created.
   * Workspace name: The name to use for the Azure Machine Learning workspace that will be created. The workspace name must be between 3 and 33 characters. It may only contain alphanumeric characters and '-'.
   * Location: Select the location where the resources will be created.
1. Select __Review + create__.
1. In the __Review + create__ screen, agree to the listed terms and conditions and select __Create__.

For more information, see [Deploy resources from custom template](../azure-resource-manager/templates/deploy-portal.md#deploy-resources-from-custom-template).
