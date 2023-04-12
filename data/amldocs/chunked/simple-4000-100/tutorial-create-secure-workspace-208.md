    :::image type="content" source="./media/tutorial-create-secure-workspace/create-container-registry.png" alt-text="Create a container registry":::

1. From the __Networking__ tab, select __Private endpoint__ and then select __+ Add__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/container-registry-networking.png" alt-text="Container registry networking":::

1. On the __Create private endpoint__ form, use the following values:
    * __Subscription__: The same Azure subscription that contains the previous resources you've created.
    * __Resource group__: The same Azure resource group that contains the previous resources you've created.
    * __Location__: The same Azure region that contains the previous resources you've created.
    * __Name__: A unique name for this private endpoint.
    * __Target sub-resource__: registry
    * __Virtual network__: The virtual network you created earlier.
    * __Subnet__: Training (172.16.0.0/24)
    * __Private DNS integration__: Yes
    * __Private DNS Zone__: privatelink.azurecr.io

    Select __OK__ to create the private endpoint.

    :::image type="content" source="./media/tutorial-create-secure-workspace/container-registry-private-endpoint.png" alt-text="Configure container registry private endpoint":::

1. Select __Review + create__. Verify that the information is correct, and then select __Create__.
1. After the container registry has been created, select __Go to resource__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/container-registry-go-to-resource.png" alt-text="Select 'go to resource'":::

1. From the left of the page, select __Access keys__, and then enable __Admin user__. This setting is required when using Azure Container Registry inside a virtual network with Azure Machine Learning.

    :::image type="content" source="./media/tutorial-create-secure-workspace/container-registry-admin-user.png" alt-text="Screenshot of admin user toggle":::

## Create a workspace

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Machine Learning__. Select the __Machine Learning__ entry, and then select __Create__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/machine-learning-create.png" alt-text="{alt-text}":::

1. From the __Basics__ tab, select the __subscription__, __resource group__, and __Region__ you previously used for the virtual network. Use the following values for the other fields:
    * __Workspace name__: A unique name for your workspace.
    * __Storage account__: Select the storage account you created previously.
    * __Key vault__: Select the key vault you created previously.
    * __Application insights__: Use the default value.
    * __Container registry__: Use the container registry you created previously.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-machine-learning-workspace.png" alt-text="Basic workspace configuration":::

1. From the __Networking__ tab, select __Private endpoint__ and then select __+ add__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/machine-learning-workspace-networking.png" alt-text="Workspace networking":::

1. On the __Create private endpoint__ form, use the following values: 
    * __Subscription__: The same Azure subscription that contains the previous resources you've created.
    * __Resource group__: The same Azure resource group that contains the previous resources you've created.
    * __Location__: The same Azure region that contains the previous resources you've created.
    * __Name__: A unique name for this private endpoint.
    * __Target sub-resource__: amlworkspace
    * __Virtual network__: The virtual network you created earlier.
    * __Subnet__: Training (172.16.0.0/24)
    * __Private DNS integration__: Yes
    * __Private DNS Zone__: Leave the two private DNS zones at the default values of __privatelink.api.azureml.ms__ and __privatelink.notebooks.azure.net__.
