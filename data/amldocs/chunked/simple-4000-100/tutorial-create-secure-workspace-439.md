1. To update the workspace to use the compute cluster to build Docker images. Replace `docs-ml-rg` with your resource group. Replace `docs-ml-ws` with your workspace. Replace `cpu-cluster` with the compute cluster to use:
    
    ```azurecli-interactive
    az ml workspace update \
      -n myworkspace \
      -g myresourcegroup \
      -i mycomputecluster
    ```

    > [!NOTE]
    > You can use the same compute cluster to train models and build Docker images for the workspace.

## Use the workspace

> [!IMPORTANT]
> The steps in this article put Azure Container Registry behind the VNet. In this configuration, you cannot deploy a model to Azure Container Instances inside the VNet. We do not recommend using Azure Container Instances with Azure Machine Learning in a virtual network. For more information, see [Secure the inference environment (SDK/CLI v1)](./v1/how-to-secure-inferencing-vnet.md).
>
> As an alternative to Azure Container Instances, try Azure Machine Learning managed online endpoints. For more information, see [Enable network isolation for managed online endpoints](how-to-secure-online-endpoint.md).

At this point, you can use the studio to interactively work with notebooks on the compute instance and run training jobs on the compute cluster. For a tutorial on using the compute instance and compute cluster, see [Tutorial: Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md).

## Stop compute instance and jump box

> [!WARNING]
> While it is running (started), the compute instance and jump box will continue charging your subscription. To avoid excess cost, __stop__ them when they are not in use.

The compute cluster dynamically scales between the minimum and maximum node count set when you created it. If you accepted the defaults, the minimum is 0, which effectively turns off the cluster when not in use.
### Stop the compute instance

From studio, select __Compute__, __Compute clusters__, and then select the compute instance. Finally, select __Stop__ from the top of the page.

:::image type="content" source="./media/tutorial-create-secure-workspace/compute-instance-stop.png" alt-text="Screenshot of stop button for compute instance":::
### Stop the jump box

Once it has been created, select the virtual machine in the Azure portal and then use the __Stop__ button. When you're ready to use it again, use the __Start__ button to start it.

:::image type="content" source="./media/tutorial-create-secure-workspace/virtual-machine-stop.png" alt-text="Screenshot of stop button for the VM":::

You can also configure the jump box to automatically shut down at a specific time. To do so, select __Auto-shutdown__, __Enable__, set a time, and then select __Save__.

:::image type="content" source="./media/tutorial-create-secure-workspace/virtual-machine-auto-shutdown.png" alt-text="Screenshot of auto-shutdown option":::

## Clean up resources

If you plan to continue using the secured workspace and other resources, skip this section.

To delete all resources created in this tutorial, use the following steps:

1. In the Azure portal, select __Resource groups__ on the far left.
1. From the list, select the resource group that you created in this tutorial.
1. Select __Delete resource group__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/delete-resources.png" alt-text="Screenshot of delete resource group button":::

1. Enter the resource group name, then select __Delete__.
## Next steps

Now that you've created a secure workspace and can access studio, learn how to [deploy a model to an online endpoint with network isolation](how-to-secure-online-endpoint.md).
