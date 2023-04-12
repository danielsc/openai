* While most of the steps in this article use the Azure portal or the Azure Machine Learning studio, some steps use the Azure CLI extension for Machine Learning v2.

## Create a virtual network

To create a virtual network, use the following steps:

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Virtual Network__ in the search field. Select the __Virtual Network__ entry, and then select __Create__.


    :::image type="content" source="./media/tutorial-create-secure-workspace/create-resource-search-vnet.png" alt-text="The create resource UI search":::

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-resource-vnet.png" alt-text="Virtual network create":::

1. From the __Basics__ tab, select the Azure __subscription__ to use for this resource and then select or create a new __resource group__. Under __Instance details__, enter a friendly __name__ for your virtual network and select the __region__ to create it in.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-vnet-basics.png" alt-text="Image of the basic virtual network config":::

1. Select __Security__. Select to __Enable Azure Bastion__. [Azure Bastion](../bastion/bastion-overview.md) provides a secure way to access the VM jump box you'll create inside the VNet in a later step. Use the following values for the remaining fields:

    * __Bastion name__: A unique name for this Bastion instance
    * __Public IP address__: Create a new public IP address.

    Leave the other fields at the default values.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-bastion.png" alt-text="Screenshot of Bastion config.":::

1. Select __IP Addresses__. The default settings should be similar to the following image:

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-vnet-ip-address-default.png" alt-text="Default IP Address screen.":::

    Use the following steps to configure the IP address and configure a subnet for training and scoring resources:

    > [!TIP]
    > While you can use a single subnet for all Azure ML resources, the steps in this article show how to create two subnets to separate the training & scoring resources.
    >
    > The workspace and other dependency services will go into the training subnet. They can still be used by resources in other subnets, such as the scoring subnet.

    1. Look at the default __IPv4 address space__ value. In the screenshot, the value is __172.16.0.0/16__. __The value may be different for you__. While you can use a different value, the rest of the steps in this tutorial are based on the __172.16.0.0/16 value__.
    
        > [!IMPORTANT]
        > We do not recommend using the 172.17.0.0/16 IP address range for your VNet. This is the default subnet range used by the Docker bridge network. Other ranges may also conflict depending on what you want to connect to the virtual network. For example, if you plan to connect your on premises network to the VNet, and your on-premises network also uses the 172.16.0.0/16 range. Ultimately, it is up to __you__ to plan your network infrastructure.

    1. Select the __Default__ subnet and then select __Remove subnet__.
    
        :::image type="content" source="./media/tutorial-create-secure-workspace/delete-default-subnet.png" alt-text="Screenshot of deleting default subnet.":::

    1. To create a subnet to contain the workspace, dependency services, and resources used for _training_, select __+ Add subnet__ and set the subnet name, starting address, and subnet size. The following are the values used in this tutorial:
        * __Name__: Training
        * __Starting address__: 172.16.0.0
        * __Subnet size__: /24 (256 addresses)

        :::image type="content" source="./media/tutorial-create-secure-workspace/vnet-add-training-subnet.png" alt-text="Screenshot of Training subnet.":::
