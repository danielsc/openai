* You only need to enable the parameter if you're using a private endpoint with the workspace _and_ don't want to allow operations with ARM over public networks.

Once we implement the parameter, it will be retroactively applied to existing workspaces using the following logic:

* If you have __an existing workspace with a private endpoint__, the flag will be __true__.

* If you have __an existing workspace without a private endpoint__ (public workspace), the flag will be __false__.

After the parameter has been implemented, the default value of the flag depends on the underlying REST API version used when you create a workspace (with a private endpoint):

* If the API version is __older__ than `2022-05-01`, then the flag is __true__ by default. 
* If the API version is `2022-05-01` or __newer__, then the flag is __false__ by default.

> [!IMPORTANT]
> If you want to use the v2 API with your workspace, you must set the v1_legacy_mode parameter to __false__.

## How to update v1_legacy_mode parameter

> [!WARNING]
> The *v1_legacy_mode* parameter is available now, but the v2 API blocking functionality will be enforced starting the week of May 15th, 2022.

To update v1_legacy_mode, use the following steps:

# [Python SDK](#tab/python)

To disable v1_legacy_mode, use [Workspace.update](/python/api/azureml-core/azureml.core.workspace(class)#update-friendly-name-none--description-none--tags-none--image-build-compute-none--service-managed-resources-settings-none--primary-user-assigned-identity-none--allow-public-access-when-behind-vnet-none-) and set `v1_legacy_mode=false`.

```python
from azureml.core import Workspace

ws = Workspace.from_config()
ws.update(v1_legacy_mode=False)
```

# [Azure CLI extension v1](#tab/azurecliextensionv1)

The Azure CLI [extension v1 for machine learning](reference-azure-machine-learning-cli.md) provides the [az ml workspace update](/cli/azure/ml(v1)/workspace#az-ml(v1)-workspace-update) command. To disable the parameter for a workspace, add the parameter `--v1-legacy-mode False`.

> [!IMPORTANT]
> The `v1-legacy-mode` parameter is only available in version 1.41.0 or newer of the Azure CLI extension for machine learning v1 (`azure-cli-ml`). Use the `az version` command to view version information.

```azurecli
az ml workspace update -g <myresourcegroup> -w <myworkspace> --v1-legacy-mode False
```

The return value of the `az ml workspace update` command may not show the updated value. To view the current state of the parameter, use the following command:
 
```azurecli
az ml workspace show -g <myresourcegroup> -w <myworkspace> --query v1LegacyMode
```

    
> [!IMPORTANT]
> Note that it takes about 30 minutes to an hour or more for changing v1_legacy_mode parameter from __true__ to __false__ to be reflected in the workspace. Therefore, if you set the parameter to __false__ but receive an error that the parameter is __true__ in a subsequent operation, please try after a few more minutes.

## Next steps

* [Use a private endpoint with Azure Machine Learning workspace](how-to-configure-private-link.md).
* [Create private link for managing Azure resources](../azure-resource-manager/management/create-private-link-access-portal.md).
