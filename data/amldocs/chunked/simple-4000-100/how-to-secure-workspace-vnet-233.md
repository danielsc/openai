
    This code returns a value similar to `"/subscriptions/{GUID}/resourceGroups/{resourcegroupname}/providers/Microsoft.ContainerRegistry/registries/{ACRname}"`. The last part of the string is the name of the Azure Container Registry for the workspace.

    # [Portal](#tab/portal)

    From the overview section of your workspace, the __Registry__ value links to the Azure Container Registry.

    :::image type="content" source="./media/how-to-enable-virtual-network/azure-machine-learning-container-registry.png" alt-text="Azure Container Registry for the workspace" border="true":::


1. Limit access to your virtual network using the steps in [Connect privately to an Azure Container Registry](../container-registry/container-registry-private-link.md). When adding the virtual network, select the virtual network and subnet for your Azure Machine Learning resources.

1. Configure the ACR for the workspace to [Allow access by trusted services](../container-registry/allow-access-trusted-services.md).

1. Create an Azure Machine Learning compute cluster. This cluster is used to build Docker images when ACR is behind a VNet. For more information, see [Create a compute cluster](how-to-create-attach-compute-cluster.md).

1. Use one of the following methods to configure the workspace to build Docker images using the compute cluster.

    > [!IMPORTANT]
    > The following limitations apply When using a compute cluster for image builds:
    > * Only a CPU SKU is supported.
    > * If you use a compute cluster configured for no public IP address, you must provide some way for the cluster to access the public internet. Internet access is required when accessing images stored on the Microsoft Container Registry, packages installed on Pypi, Conda, etc. You need to configure User Defined Routing (UDR) to reach to a public IP to access the internet. For example, you can use the public IP of your firewall, or you can use [Virtual Network NAT](../virtual-network/nat-gateway/nat-overview.md) with a public IP. For more information, see [How to securely train in a VNet](how-to-secure-training-vnet.md).

    # [Azure CLI](#tab/cli)

    You can use the `az ml workspace update` command to set a build compute. The command is the same for both the v1 and v2 Azure CLI extensions for machine learning. In the following command, replace `myworkspace` with your workspace name, `myresourcegroup` with the resource group that contains the workspace, and `mycomputecluster` with the compute cluster name:

    ```azurecli
    az ml workspace update --name myworkspace --resource-group myresourcegroup --image-build-compute mycomputecluster
    ```

    # [Python SDK](#tab/python)

    The following code snippet demonstrates how to update the workspace to set a build compute using the [Azure Machine Learning SDK](/python/api/overview/azure/ai-ml-readme). Replace `mycomputecluster` with the name of the cluster to use:

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    ```python
    # import required libraries
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    subscription_id = "<your subscription ID>"
    resource_group = "<your resource group name>"
    workspace = "<your workspace name>"

    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
    
    # Get workspace info
    ws=ml_client.workspaces.get(name=workspace)
    # Update to use cpu-cluster for image builds
    ws.image_build_compute="cpu-cluster"
    ml_client.workspaces.begin_update(ws)
    # To switch back to using ACR to build (if ACR is not in the VNet):
    # ws.image_build_compute = ''
    # ml_client.workspaces.begin_update(ws)
    ```

    
    For more information, see the [begin_update](/python/api/azure-ai-ml/azure.ai.ml.operations.workspaceoperations#azure-ai-ml-operations-workspaceoperations-begin-update) method reference.

    # [Portal](#tab/portal)

    Currently there isn't a way to set the image build compute from the Azure portal.
