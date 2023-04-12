

# [Studio](#tab/azure-studio)

For information on configuring managed identity when creating a compute cluster in studio, see [Set up managed identity](how-to-create-attach-compute-cluster.md#set-up-managed-identity).


A managed identity is automatically granted ACRPull role on workspace ACR to enable pulling Docker images for training.

> [!NOTE]
> If you create compute first, before workspace ACR has been created, you have to assign the ACRPull role manually.

### Use Docker images for inference

Once you've configured ACR without admin user as described earlier, you can access Docker images for inference without admin keys from your Azure Kubernetes service (AKS). When you create or attach AKS to workspace, the cluster's service principal is automatically assigned ACRPull access to workspace ACR.

> [!NOTE]
> If you bring your own AKS cluster, the cluster must have service principal enabled instead of managed identity.

## Scenario: Use a private Azure Container Registry

By default, Azure Machine Learning uses Docker base images that come from a public repository managed by Microsoft. It then builds your training or inference environment on those images. For more information, see [What are ML environments?](concept-environments.md).

To use a custom base image internal to your enterprise, you can use managed identities to access your private ACR. There are two use cases:

 * Use base image for training as is.
 * Build Azure Machine Learning managed image with custom image as a base.

### Pull Docker base image to machine learning compute cluster for training as is

Create machine learning compute cluster with system-assigned managed identity enabled as described earlier. Then, determine the principal ID of the managed identity.

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli-interactive
az ml compute show --name <cluster name> -w <workspace> -g <resource group>
```

Optionally, you can update the compute cluster to assign a user-assigned managed identity:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli-interactive
az ml compute update --name <cluster name> --user-assigned-identities <my-identity-id>
```

To allow the compute cluster to pull the base images, grant the managed service identity ACRPull role on the private ACR

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli-interactive
az role assignment create --assignee <principal ID> \
--role acrpull \
--scope "/subscriptions/<subscription ID>/resourceGroups/<private ACR resource group>/providers/Microsoft.ContainerRegistry/registries/<private ACR name>"
```

Finally, create an environment and specify the base image location in the [environment YAML file](reference-yaml-environment.md).

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/environment.schema.json
name: docker-image-example
image: pytorch/pytorch:latest
description: Environment created from a Docker image.

```

```azurecli
az ml environment create --file <yaml file>
```

You can now use the environment in a [training job](how-to-train-cli.md).

### Build Azure Machine Learning managed environment into base image from private ACR for training or inference

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

In this scenario, Azure Machine Learning service builds the training or inference environment on top of a base image you supply from a private ACR. Because the image build task happens on the workspace ACR using ACR Tasks, you must perform more steps to allow access.

1. Create __user-assigned managed identity__ and grant the identity ACRPull access to the __private ACR__.  
1. Grant the workspace __managed identity__ a __Managed Identity Operator__ role on the __user-assigned managed identity__ from the previous step. This role allows the workspace to assign the user-assigned managed identity to ACR Task for building the managed environment. 
