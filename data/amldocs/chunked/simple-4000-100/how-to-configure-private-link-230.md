To remove a private endpoint, use the following information:

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


When using the Azure CLI [extension 2.0 CLI for machine learning](how-to-configure-cli.md), use the following command to remove the private endpoint:

```azurecli
az network private-endpoint delete \
    --name <private-endpoint-name> \
    --resource-group <resource-group-name> \
```

# [Portal](#tab/azure-portal)

1. From the [Azure portal](https://portal.azure.com), select your Azure Machine Learning workspace.
1. From the left side of the page, select __Networking__ and then select the __Private endpoint connections__ tab.
1. Select the endpoint to remove and then select __Remove__.

:::image type="content" source="./media/how-to-configure-private-link/remove-private-endpoint.png" alt-text="Screenshot of the UI to remove a private endpoint.":::


## Enable public access

In some situations, you may want to allow someone to connect to your secured workspace over a public endpoint, instead of through the VNet. Or you may want to remove the workspace from the VNet and re-enable public access.

> [!IMPORTANT]
> Enabling public access doesn't remove any private endpoints that exist. All communications between components behind the VNet that the private endpoint(s) connect to are still secured. It enables public access only to the workspace, in addition to the private access through any private endpoints.

> [!WARNING]
> When connecting over the public endpoint while the workspace uses a private endpoint to communicate with other resources:
> * __Some features of studio will fail to access your data__. This problem happens when the _data is stored on a service that is secured behind the VNet_. For example, an Azure Storage Account. 
> * Using Jupyter, JupyterLab, RStudio, or Posit Workbench (formerly RStudio Workbench) on a compute instance, including running notebooks, __is not supported__.

To enable public access, use the following steps:

> [!TIP]
> There are two possible properties that you can configure:
> * `allow_public_access_when_behind_vnet` - used by the Python SDK v1
> * `public_network_access` - used by the CLI and Python SDK v2
> Each property overrides the other. For example, setting `public_network_access` will override any previous setting to `allow_public_access_when_behind_vnet`.
>
> Microsoft recommends using `public_network_access` to enable or disable public access to a workspace.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


When using the Azure CLI [extension 2.0 CLI for machine learning](how-to-configure-cli.md), use the `az ml update` command to enable `public_network_access` for the workspace:

```azurecli
az ml workspace update \
    --set public_network_access=Enabled \
    -n <workspace-name> \
    -g <resource-group-name>
```

You can also enable public network access by using a YAML file. For more information, see the [workspace YAML reference](reference-yaml-workspace.md).

# [Portal](#tab/azure-portal)

1. From the [Azure portal](https://portal.azure.com), select your Azure Machine Learning workspace.
1. From the left side of the page, select __Networking__ and then select the __Public access__ tab.
1. Select __All networks__, and then select __Save__.

:::image type="content" source="./media/how-to-configure-private-link/workspace-public-access.png" alt-text="Screenshot of the UI to enable public endpoint.":::


## Securely connect to your workspace

[!INCLUDE [machine-learning-connect-secure-workspace](../../includes/machine-learning-connect-secure-workspace.md)]

## Multiple private endpoints

Azure Machine Learning supports multiple private endpoints for a workspace. Multiple private endpoints are often used when you want to keep different environments separate. The following are some scenarios that are enabled by using multiple private endpoints:

* Client development environments in a separate VNet.
