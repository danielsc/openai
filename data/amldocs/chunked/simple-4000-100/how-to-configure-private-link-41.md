* When attaching an Azure Kubernetes Service cluster to a workspace with a private endpoint, the cluster must be in the same region as the workspace.
* When using a workspace with multiple private endpoints, one of the private endpoints must be in the same VNet as the following dependency services:

    * Azure Storage Account that provides the default storage for the workspace
    * Azure Key Vault for the workspace
    * Azure Container Registry for the workspace.

    For example, one VNet ('services' VNet) would contain a private endpoint for the dependency services and the workspace. This configuration allows the workspace to communicate with the services. Another VNet ('clients') might only contain a private endpoint for the workspace, and be used only for communication between client development machines and the workspace.

## Create a workspace that uses a private endpoint

Use one of the following methods to create a workspace with a private endpoint. Each of these methods __requires an existing virtual network__:

> [!TIP]
> If you'd like to create a workspace, private endpoint, and virtual network at the same time, see [Use an Azure Resource Manager template to create a workspace for Azure Machine Learning](how-to-create-workspace-template.md).

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

When using the Azure CLI [extension 2.0 CLI for machine learning](how-to-configure-cli.md), a YAML document is used to configure the workspace. The following example demonstrates creating a new workspace using a YAML configuration:

> [!TIP]
> When using private link, your workspace cannot use Azure Container Registry tasks compute for image building. The `image_build_compute` property in this configuration specifies a CPU compute cluster name to use for Docker image environment building. You can also specify whether the private link workspace should be accessible over the internet using the `public_network_access` property.
>
> In this example, the compute referenced by `image_build_compute` will need to be created before building images.

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

```azurecli-interactive
az ml workspace create \
    -g <resource-group-name> \
    --file privatelink.yml
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
    --name privatelink.api.azureml.ms

az network private-dns link vnet create \
    -g <resource-group-name> \
    --zone-name privatelink.api.azureml.ms \
    --name <link-name> \
    --virtual-network <vnet-name> \
    --registration-enabled false

az network private-endpoint dns-zone-group create \
    -g <resource-group-name> \
    --endpoint-name <private-endpoint-name> \
    --name myzonegroup \
    --private-dns-zone privatelink.api.azureml.ms \
    --zone-name privatelink.api.azureml.ms

# Add privatelink.notebooks.azure.net
az network private-dns zone create \
    -g <resource-group-name> \
    --name privatelink.notebooks.azure.net

az network private-dns link vnet create \
    -g <resource-group-name> \
    --zone-name privatelink.notebooks.azure.net \
    --name <link-name> \
    --virtual-network <vnet-name> \
    --registration-enabled false

az network private-endpoint dns-zone-group add \
    -g <resource-group-name> \
    --endpoint-name <private-endpoint-name> \
    --name myzonegroup \
    --private-dns-zone privatelink.notebooks.azure.net \
    --zone-name privatelink.notebooks.azure.net
```
