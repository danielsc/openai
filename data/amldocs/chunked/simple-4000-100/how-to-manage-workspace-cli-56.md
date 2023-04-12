> If you are using the Azure Cloud Shell, you can skip this section. The cloud shell automatically authenticates you using the account you log into your Azure subscription.

There are several ways that you can authenticate to your Azure subscription from the CLI. The most simple is to interactively authenticate using a browser. To authenticate interactively, open a command line or terminal and use the following command:

```azurecli-interactive
az login
```

If the CLI can open your default browser, it will do so and load a sign-in page. Otherwise, you need to open a browser and follow the instructions on the command line. The instructions involve browsing to [https://aka.ms/devicelogin](https://aka.ms/devicelogin) and entering an authorization code.

[!INCLUDE [select-subscription](../../includes/machine-learning-cli-subscription.md)] 

For other methods of authenticating, see [Sign in with Azure CLI](/cli/azure/authenticate-azure-cli).

## Create a resource group

The Azure Machine Learning workspace must be created inside a resource group. You can use an existing resource group or create a new one. To __create a new resource group__, use the following command. Replace `<resource-group-name>` with the name to use for this resource group. Replace `<location>` with the Azure region to use for this resource group:

> [!NOTE]
> You should select a region where Azure Machine Learning is available. For information, see [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=machine-learning-service).

```azurecli-interactive
az group create --name <resource-group-name> --location <location>
```

The response from this command is similar to the following JSON. You can use the output values to locate the created resources or parse them as input to subsequent CLI steps for automation.

```json
{
  "id": "/subscriptions/<subscription-GUID>/resourceGroups/<resourcegroupname>",
  "location": "<location>",
  "managedBy": null,
  "name": "<resource-group-name>",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null,
  "type": null
}
```

For more information on working with resource groups, see [az group](/cli/azure/group).

## Create a workspace

When you deploy an Azure Machine Learning workspace, various other services are [required as dependent associated resources](./concept-workspace.md#associated-resources). When you use the CLI to create the workspace, the CLI can either create new associated resources on your behalf or you could attach existing resources.

> [!IMPORTANT]
> When attaching your own storage account, make sure that it meets the following criteria:
>
> * The storage account is _not_ a premium account (Premium_LRS and Premium_GRS)
> * Both Azure Blob and Azure File capabilities enabled
> * Hierarchical Namespace (ADLS Gen 2) is disabled
> These requirements are only for the _default_ storage account used by the workspace.
>
> When attaching Azure container registry, you must have the [admin account](../container-registry/container-registry-authentication.md#admin-account) enabled before it can be used with an Azure Machine Learning workspace.

# [Create with new resources](#tab/createnewresources)

To create a new workspace where the __services are automatically created__, use the following command:

```azurecli-interactive
az ml workspace create -n <workspace-name> -g <resource-group-name>
```

# [Bring existing resources](#tab/bringexistingresources)

To create a new workspace while bringing existing associated resources using the CLI, you'll first have to define how your workspace should be configured in a configuration file.

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-basicex-prod
location: eastus
display_name: Bring your own dependent resources-example
description: This configuration specifies a workspace configuration with existing dependent resources
storage_account: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>
container_registry: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ContainerRegistry/registries/<CONTAINER_REGISTRY>
key_vault: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<KEY_VAULT>
application_insights: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.insights/components/<APP_INSIGHTS>
tags:
  purpose: demonstration
```
