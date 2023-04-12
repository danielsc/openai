    > If your Azure AD account has access to multiple subscriptions or directories, use the __Directory and Subscription__ dropdown to select the one that contains the workspace.

    :::image type="content" source="./media/tutorial-create-secure-workspace/studio-select-workspace.png" alt-text="Screenshot of the select workspace dialog":::

1. From studio, select __Compute__, __Compute clusters__, and then __+ New__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/studio-new-compute-cluster.png" alt-text="Screenshot of new compute cluster workflow":::

1. From the __Virtual Machine__ dialog, select __Next__ to accept the default virtual machine configuration.

    :::image type="content" source="./media/tutorial-create-secure-workspace/studio-new-compute-vm.png" alt-text="Screenshot of compute cluster vm settings":::
    
1. From the __Configure Settings__ dialog, enter __cpu-cluster__ as the __Compute name__. Set the __Subnet__ to __Training__ and then select __Create__ to create the cluster.

    > [!TIP]
    > Compute clusters dynamically scale the nodes in the cluster as needed. We recommend leaving the minimum number of nodes at 0 to reduce costs when the cluster is not in use.

    :::image type="content" source="./media/tutorial-create-secure-workspace/studio-new-compute-settings.png" alt-text="Screenshot of new compute cluster settings":::

1. From studio, select __Compute__, __Compute instance__, and then __+ New__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-compute-instance.png" alt-text="Screenshot of new compute instance workflow":::

1. From the __Virtual Machine__ dialog, enter a unique __Computer name__ and select __Next: Advanced Settings__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-compute-instance-vm.png" alt-text="Screenshot of compute instance vm settings":::

1. From the __Advanced Settings__ dialog, set the __Subnet__ to __Training__, and then select __Create__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-compute-instance-settings.png" alt-text="Screenshot of compute instance settings":::

> [!TIP]
> When you create a compute cluster or compute instance, Azure Machine Learning dynamically adds a Network Security Group (NSG). This NSG contains the following rules, which are specific to compute cluster and compute instance:
> 
> * Allow inbound TCP traffic on ports 29876-29877 from the `BatchNodeManagement` service tag.
> * Allow inbound TCP traffic on port 44224 from the `AzureMachineLearning` service tag.
>
> The following screenshot shows an example of these rules:
>
> :::image type="content" source="./media/how-to-secure-training-vnet/compute-instance-cluster-network-security-group.png" alt-text="Screenshot of NSG":::

For more information on creating a compute cluster and compute cluster, including how to do so with Python and the CLI, see the following articles:

* [Create a compute cluster](how-to-create-attach-compute-cluster.md)
* [Create a compute instance](how-to-create-manage-compute-instance.md)

## Configure image builds

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

When Azure Container Registry is behind the virtual network, Azure Machine Learning can't use it to directly build Docker images (used for training and deployment). Instead, configure the workspace to use the compute cluster you created earlier. Use the following steps to create a compute cluster and configure the workspace to use it to build images:

1. Navigate to [https://shell.azure.com/](https://shell.azure.com/) to open the Azure Cloud Shell.
1. From the Cloud Shell, use the following command to install the 2.0 CLI for Azure Machine Learning:
 
    ```azurecli-interactive
    az extension add -n ml
    ```

1. To update the workspace to use the compute cluster to build Docker images. Replace `docs-ml-rg` with your resource group. Replace `docs-ml-ws` with your workspace. Replace `cpu-cluster` with the compute cluster to use:
