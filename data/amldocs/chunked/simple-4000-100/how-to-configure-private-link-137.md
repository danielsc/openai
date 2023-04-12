
# [Portal](#tab/azure-portal)

The __Networking__ tab in Azure Machine Learning portal allows you to configure a private endpoint. However, it requires an existing virtual network. For more information, see [Create workspaces in the portal](how-to-manage-workspace.md).


## Add a private endpoint to a workspace

Use one of the following methods to add a private endpoint to an existing workspace:

> [!WARNING]
>
> If you have any existing compute targets associated with this workspace, and they are not behind the same virtual network tha the private endpoint is created in, they will not work.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

When using the Azure CLI [extension 2.0 CLI for machine learning](how-to-configure-cli.md), use the [Azure networking CLI commands](/cli/azure/network/private-endpoint#az-network-private-endpoint-create) to create a private link endpoint for the workspace.

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

# [Portal](#tab/azure-portal)

From the Azure Machine Learning workspace in the portal, select __Private endpoint connections__ and then select __+ Private endpoint__. Use the fields to create a new private endpoint.

* When selecting the __Region__, select the same region as your virtual network. 
* When selecting __Resource type__, use __Microsoft.MachineLearningServices/workspaces__. 
* Set the __Resource__ to your workspace name.

Finally, select __Create__ to create the private endpoint.


## Remove a private endpoint

You can remove one or all private endpoints for a workspace. Removing a private endpoint removes the workspace from the VNet that the endpoint was associated with. Removing the private endpoint may prevent the workspace from accessing resources in that VNet, or resources in the VNet from accessing the workspace. For example, if the VNet doesn't allow access to or from the public internet.

> [!WARNING]
> Removing the private endpoints for a workspace __doesn't make it publicly accessible__. To make the workspace publicly accessible, use the steps in the [Enable public access](#enable-public-access) section.

To remove a private endpoint, use the following information:

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
