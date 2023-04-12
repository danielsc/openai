
Then, you can reference this configuration file as part of the workspace creation CLI command.

```azurecli-interactive
az ml workspace create -g <resource-group-name> --file workspace.yml
```

If attaching existing resources, you must provide the ID for the resources. You can get this ID either via the 'properties'  tab on each resource in the Azure portal, or by running the following commands using the Azure CLI.

* **Azure Storage Account**: 
      `az storage account show --name <storage-account-name> --query "id"`
* **Azure Application Insights**: 
      `az monitor app-insights component show --app <application-insight-name> -g <resource-group-name> --query "id"`
* **Azure Key Vault**:
      `az keyvault show --name <key-vault-name> --query "ID"`
* **Azure Container Registry**:
      `az acr show --name <acr-name> -g <resource-group-name> --query "id"`

The Resource ID value looks similar to the following text: `"/subscriptions/<service-GUID>/resourceGroups/<resource-group-name>/providers/<provider>/<subresource>/<resource-name>"`.


> [!IMPORTANT]
> When you attaching existing resources, you don't have to specify all. You can specify one or more. For example, you can specify an existing storage account and the workspace will create the other resources.

The output of the workspace creation command is similar to the following JSON. You can use the output values to locate the created resources or parse them as input to subsequent CLI steps.

```json
{
  "applicationInsights": "/subscriptions/<service-GUID>/resourcegroups/<resource-group-name>/providers/microsoft.insights/components/<application-insight-name>",
  "containerRegistry": "/subscriptions/<service-GUID>/resourcegroups/<resource-group-name>/providers/microsoft.containerregistry/registries/<acr-name>",
  "creationTime": "2019-08-30T20:24:19.6984254+00:00",
  "description": "",
  "friendlyName": "<workspace-name>",
  "id": "/subscriptions/<service-GUID>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>",
  "identityPrincipalId": "<GUID>",
  "identityTenantId": "<GUID>",
  "identityType": "SystemAssigned",
  "keyVault": "/subscriptions/<service-GUID>/resourcegroups/<resource-group-name>/providers/microsoft.keyvault/vaults/<key-vault-name>",
  "location": "<location>",
  "name": "<workspace-name>",
  "resourceGroup": "<resource-group-name>",
  "storageAccount": "/subscriptions/<service-GUID>/resourcegroups/<resource-group-name>/providers/microsoft.storage/storageaccounts/<storage-account-name>",
  "type": "Microsoft.MachineLearningServices/workspaces",
  "workspaceid": "<GUID>"
}

```

## Advanced configurations
### Configure workspace for private network connectivity

Dependent on your use case and organizational requirements, you can choose to configure Azure Machine Learning using private network connectivity. You can use the Azure CLI to deploy a workspace and a Private link endpoint for the workspace resource. For more information on using a private endpoint and virtual network (VNet) with your workspace, see [Virtual network isolation and privacy overview](how-to-network-security-overview.md). For complex resource configurations, also refer to template based deployment options including [Azure Resource Manager](how-to-create-workspace-template.md).

When using private link, your workspace can't use Azure Container Registry to build docker images. Hence, you must set the image_build_compute property to a CPU compute cluster name to use for Docker image environment building. You can also specify whether the private link workspace should be accessible over the internet using the public_network_access property.

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-privatelink-prod
location: eastus
display_name: Private Link endpoint workspace-example
description: When using private link, you must set the image_build_compute property to a cluster name to use for Docker image environment building. You can also specify whether the workspace should be accessible over the internet.
image_build_compute: cpu-compute
public_network_access: Disabled
tags:
  purpose: demonstration
```
