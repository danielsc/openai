
```azurecli-interactive
az ml workspace create -g <resource-group-name> --file privatelink.yml
```

After creating the workspace, use the [Azure networking CLI commands](/cli/azure/network/private-endpoint#az-network-private-endpoint-create) to create a private link endpoint for the workspace.

```azurecli-interactive
az network private-endpoint create \
    --name <private-endpoint-name> \
    --vnet-name <vnet-name> \
    --subnet <subnet-name> \
    --private-connection-resource-id "/subscriptions/<subscription>/resourceGroups/<resource-group-name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>" \
    --group-id amlworkspace \
    --connection-name workspace -l <location>
```

To create the private DNS zone entries for the workspace, use the following commands:

```azurecli-interactive
# Add privatelink.api.azureml.ms
az network private-dns zone create \
    -g <resource-group-name> \
    --name 'privatelink.api.azureml.ms'

az network private-dns link vnet create \
    -g <resource-group-name> \
    --zone-name 'privatelink.api.azureml.ms' \
    --name <link-name> \
    --virtual-network <vnet-name> \
    --registration-enabled false

az network private-endpoint dns-zone-group create \
    -g <resource-group-name> \
    --endpoint-name <private-endpoint-name> \
    --name myzonegroup \
    --private-dns-zone 'privatelink.api.azureml.ms' \
    --zone-name 'privatelink.api.azureml.ms'

# Add privatelink.notebooks.azure.net
az network private-dns zone create \
    -g <resource-group-name> \
    --name 'privatelink.notebooks.azure.net'

az network private-dns link vnet create \
    -g <resource-group-name> \
    --zone-name 'privatelink.notebooks.azure.net' \
    --name <link-name> \
    --virtual-network <vnet-name> \
    --registration-enabled false

az network private-endpoint dns-zone-group add \
    -g <resource-group-name> \
    --endpoint-name <private-endpoint-name> \
    --name myzonegroup \
    --private-dns-zone 'privatelink.notebooks.azure.net' \
    --zone-name 'privatelink.notebooks.azure.net'
```

### Customer-managed key and high business impact workspace

By default, metadata for the workspace is stored in an Azure Cosmos DB instance that Microsoft maintains. This data is encrypted using Microsoft-managed keys. Instead of using the Microsoft-managed key, you can also provide your own key. Doing so creates an extra set of resources in your Azure subscription to store your data.

To learn more about the resources that are created when you bring your own key for encryption, see [Data encryption with Azure Machine Learning](./concept-data-encryption.md#azure-cosmos-db).

Use the `customer_managed_key` parameter and containing `key_vault` and `key_uri` parameters, to specify the resource ID and uri of the key within the vault.

To [limit the data that Microsoft collects](./concept-data-encryption.md#encryption-at-rest) on your workspace, you can additionally specify the `hbi_workspace` property. 

```YAML
$schema: https://azuremlschemas.azureedge.net/latest/workspace.schema.json
name: mlw-cmkexample-prod
location: eastus
display_name: Customer managed key encryption-example
description: This configurations shows how to create a workspace that uses customer-managed keys for encryption.
customer_managed_key: 
  key_vault: /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<KEY_VAULT>
  key_uri: https://<KEY_VAULT>.vault.azure.net/keys/<KEY_NAME>/<KEY_VERSION>
tags:
  purpose: demonstration

```

Then, you can reference this configuration file as part of the workspace creation CLI command.

```azurecli-interactive
az ml workspace create -g <resource-group-name> --file cmk.yml
```

> [!NOTE]
> Authorize the __Machine Learning App__ (in Identity and Access Management) with contributor permissions on your subscription to manage the data encryption additional resources.

> [!NOTE]
> Azure Cosmos DB is __not__ used to store information such as model performance, information logged by experiments, or information logged from your model deployments.
