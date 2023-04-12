| [ExpressRoute](https://azure.microsoft.com/services/expressroute/) | Connects on-premises networks into the cloud over a private connection. Connection is made using a connectivity provider. |

> [!IMPORTANT]
> When using a __VPN gateway__ or __ExpressRoute__, you will need to plan how name resolution works between your on-premises resources and those in the VNet. For more information, see [Use a custom DNS server](how-to-custom-dns.md).

### Create a jump box (VM)

Use the following steps to create an Azure Virtual Machine to use as a jump box. Azure Bastion enables you to connect to the VM desktop through your browser. From the VM desktop, you can then use the browser on the VM to connect to resources inside the VNet, such as Azure Machine Learning studio. Or you can install development tools on the VM. 

> [!TIP]
> The steps below create a Windows 11 enterprise VM. Depending on your requirements, you may want to select a different VM image. The Windows 11 (or 10) enterprise image is useful if you need to join the VM to your organization's domain.

1. In the [Azure portal](https://portal.azure.com), select the portal menu in the upper left corner. From the menu, select __+ Create a resource__ and then enter __Virtual Machine__. Select the __Virtual Machine__ entry, and then select __Create__.

1. From the __Basics__ tab, select the __subscription__, __resource group__, and __Region__ you previously used for the virtual network. Provide values for the following fields:

    * __Virtual machine name__: A unique name for the VM.
    * __Username__: The username you'll use to log in to the VM.
    * __Password__: The password for the username.
    * __Security type__: Standard.
    * __Image__: Windows 11 Enterprise.

        > [!TIP]
        > If Windows 11 Enterprise isn't in the list for image selection, use _See all images__. Find the __Windows 11__ entry from Microsoft, and use the __Select__ drop-down to select the enterprise image.


    You can leave other fields at the default values.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-virtual-machine-basic.png" alt-text="Image of VM basic configuration":::

1. Select __Networking__, and then select the __Virtual network__ you created earlier. Use the following information to set the remaining fields:

    * Select the __Training__ subnet.
    * Set the __Public IP__ to __None__.
    * Leave the other fields at the default value.

    :::image type="content" source="./media/tutorial-create-secure-workspace/create-virtual-machine-network.png" alt-text="Image of VM network configuration":::

1. Select __Review + create__. Verify that the information is correct, and then select __Create__.


### Connect to the jump box

1. Once the virtual machine has been created, select __Go to resource__.
1. From the top of the page, select __Connect__ and then __Bastion__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/virtual-machine-connect.png" alt-text="Image of the connect/bastion UI":::

1. Select __Use Bastion__, and then provide your authentication information for the virtual machine, and a connection will be established in your browser.

    :::image type="content" source="./media/tutorial-create-secure-workspace/use-bastion.png" alt-text="Image of use bastion dialog":::

## Create a compute cluster and compute instance

A compute cluster is used by your training jobs. A compute instance provides a Jupyter Notebook experience on a shared compute resource attached to your workspace.

1. From an Azure Bastion connection to the jump box, open the __Microsoft Edge__ browser on the remote desktop.
1. In the remote browser session, go to __https://ml.azure.com__. When prompted, authenticate using your Azure AD account.
1. From the __Welcome to studio!__ screen, select the __Machine Learning workspace__ you created earlier and then select __Get started__.

    > [!TIP]
    > If your Azure AD account has access to multiple subscriptions or directories, use the __Directory and Subscription__ dropdown to select the one that contains the workspace.
