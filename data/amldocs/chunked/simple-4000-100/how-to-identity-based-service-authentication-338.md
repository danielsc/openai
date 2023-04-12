* If your storage is ADLS Gen 2 or Blob and has virtual network settings, customers can use either user identity or workspace MSI depending on the datastore settings defined during creation. 

* If the virtual network setting is “Allow Azure services on the trusted services list to access this storage account”, then Workspace MSI is used. 

## Scenario: Azure Container Registry without admin user

When you disable the admin user for ACR, Azure ML uses a managed identity to build and pull Docker images. There are two workflows when configuring Azure ML to use an ACR with the admin user disabled:

* Allow Azure ML to create the ACR instance and then disable the admin user afterwards.
* Bring an existing ACR with the admin user already disabled.

### Azure ML with auto-created ACR instance

1. Create a new Azure Machine Learning workspace.
1. Perform an action that requires Azure Container Registry. For example, the [Tutorial: Train your first model](tutorial-1st-experiment-sdk-train.md).
1. Get the name of the ACR created by the cluster.

    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

    ```azurecli-interactive
    az ml workspace show -w <my workspace> \
    -g <my resource group>
    --query containerRegistry
    ```

    This command returns a value similar to the following text. You only want the last portion of the text, which is the ACR instance name:

    ```output
    /subscriptions/<subscription id>/resourceGroups/<my resource group>/providers/MicrosoftContainerReggistry/registries/<ACR instance name>
    ```

1. Update the ACR to disable the admin user:

    ```azurecli-interactive
    az acr update --name <ACR instance name> --admin-enabled false
    ```

### Bring your own ACR

If ACR admin user is disallowed by subscription policy, you should first create ACR without admin user, and then associate it with the workspace. Also, if you have existing ACR with admin user disabled, you can attach it to the workspace.

[Create ACR from Azure CLI](../container-registry/container-registry-get-started-azure-cli.md) without setting ```--admin-enabled``` argument, or from Azure portal without enabling admin user. Then, when creating Azure Machine Learning workspace, specify the Azure resource ID of the ACR. The following example demonstrates creating a new Azure ML workspace that uses an existing ACR:

> [!TIP]
> To get the value for the `--container-registry` parameter, use the [az acr show](/cli/azure/acr#az-acr-show) command to show information for your ACR. The `id` field contains the resource ID for your ACR.

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli-interactive
az ml workspace create -w <workspace name> \
-g <workspace resource group> \
-l <region> \
--container-registry /subscriptions/<subscription id>/resourceGroups/<acr resource group>/providers/Microsoft.ContainerRegistry/registries/<acr name>
```

### Create compute with managed identity to access Docker images for training

To access the workspace ACR, create machine learning compute cluster with system-assigned managed identity enabled. You can enable the identity from Azure portal or Studio when creating compute, or from Azure CLI using the below. For more information, see [using managed identity with compute clusters](how-to-create-attach-compute-cluster.md#set-up-managed-identity).

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli-interaction
az ml compute create --name cpu-cluster --type <cluster name>  --identity-type systemassigned
```

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.entities import IdentityConfiguration, AmlCompute
from azure.ai.ml.constants import ManagedServiceIdentityType

# Create an identity configuration for a system-assigned managed identity
identity_config = IdentityConfiguration(type = ManagedServiceIdentityType.SYSTEM_ASSIGNED)

# specify aml compute name.
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    # Pass the identity configuration
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4, identity=identity_config
    )
    ml_client.compute.begin_create_or_update(compute)
```
