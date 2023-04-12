    * __Private DNS Zone__: Leave the two private DNS zones at the default values of __privatelink.api.azureml.ms__ and __privatelink.notebooks.azure.net__.

    Select __OK__ to create the private endpoint.

    :::image type="content" source="./media/tutorial-create-secure-workspace/machine-learning-workspace-private-endpoint.png" alt-text="Screenshot of workspace private network config":::

1. Select __Review + create__. Verify that the information is correct, and then select __Create__.
1. Once the workspace has been created, select __Go to resource__.
1. From the __Settings__ section on the left, select __Private endpoint connections__ and then select the link in the __Private endpoint__ column:

    :::image type="content" source="./media/tutorial-create-secure-workspace/workspace-private-endpoint-connections.png" alt-text="Screenshot of workspace private endpoint connections":::

1. Once the private endpoint information appears, select __DNS configuration__ from the left of the page. Save the IP address and fully qualified domain name (FQDN) information on this page, as it will be used later.

    :::image type="content" source="./media/tutorial-create-secure-workspace/workspace-private-endpoint-dns.png" alt-text="screenshot of IP and FQDN entries":::

> [!IMPORTANT]
> There are still some configuration steps needed before you can fully use the workspace. However, these require you to connect to the workspace.

## Enable studio

Azure Machine Learning studio is a web-based application that lets you easily manage your workspace. However, it needs some extra configuration before it can be used with resources secured inside a VNet. Use the following steps to enable studio:

1. When using an Azure Storage Account that has a private endpoint, add the service principal for the workspace as a __Reader__ for the storage private endpoint(s). From the Azure portal, select your storage account and then select __Networking__. Next, select __Private endpoint connections__.

    :::image type="content" source="./media/tutorial-create-secure-workspace/storage-private-endpoint-select.png" alt-text="Screenshot of storage private endpoints":::

1. For __each private endpoint listed__, use the following steps:

    1. Select the link in the __Private endpoint__ column.
    
        :::image type="content" source="./media/tutorial-create-secure-workspace/storage-private-endpoint-selected.png" alt-text="Screenshot of endpoints to select":::

    1. Select __Access control (IAM)__ from the left side.
    1. Select __+ Add__, and then __Add role assignment (Preview)__.

        ![Access control (IAM) page with Add role assignment menu open.](../../includes/role-based-access-control/media/add-role-assignment-menu-generic.png)

    1. On the __Role__ tab, select the __Reader__.

        ![Add role assignment page with Role tab selected.](../../includes/role-based-access-control/media/add-role-assignment-role-generic.png)

    1. On the __Members__ tab, select __User, group, or service principal__ in the __Assign access to__ area and then select __+ Select members__. In the __Select members__ dialog, enter the name as your Azure Machine Learning workspace. Select the service principal for the workspace, and then use the __Select__ button.

    1. On the **Review + assign** tab, select **Review + assign** to assign the role.

## Connect to the workspace

There are several ways that you can connect to the secured workspace. The steps in this article use a __jump box__, which is a virtual machine in the VNet. You can connect to it using your web browser and Azure Bastion. The following table lists several other ways that you might connect to the secure workspace:

| Method | Description |
| ----- | ----- |
| [Azure VPN gateway](../vpn-gateway/vpn-gateway-about-vpngateways.md) | Connects on-premises networks to the VNet over a private connection. Connection is made over the public internet. |
| [ExpressRoute](https://azure.microsoft.com/services/expressroute/) | Connects on-premises networks into the cloud over a private connection. Connection is made using a connectivity provider. |
