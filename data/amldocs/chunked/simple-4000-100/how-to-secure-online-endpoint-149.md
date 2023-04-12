* The Azure Storage blob that is the default storage for the workspace
* The Azure Container Registry for the workspace

When you configure the `egress_public_network_access` to `disabled`, a new private endpoint is created per deployment, per service. For example, if you set the flag to `disabled` for three deployments to an online endpoint, nine private endpoints are created. Each deployment would have three private endpoints to communicate with the workspace, blob, and container registry.

## Scenarios

The following table lists the supported configurations when configuring inbound and outbound communications for an online endpoint:

| Configuration | Inbound </br> (Endpoint property) | Outbound </br> (Deployment property) | Supported? |
| -------- | -------------------------------- | --------------------------------- | --------- |
| secure inbound with secure outbound | `public_network_access` is disabled | `egress_public_network_access` is disabled   | Yes |
| secure inbound with public outbound | `public_network_access` is disabled</br>The workspace must also allow public access. | `egress_public_network_access` is enabled  | Yes |
| public inbound with secure outbound | `public_network_access` is enabled | `egress_public_network_access` is disabled    | Yes |
| public inbound with public outbound | `public_network_access` is enabled</br>The workspace must also allow public access. | `egress_public_network_access` is enabled  | Yes |

> [!IMPORTANT]
> Outbound communication from managed online endpoint deployment is to the _workspace API_. When the endpoint is configured to use __public outbound__, then the workspace must be able to accept that public communication (allow public access).

## End-to-end example

Use the information in this section to create an example configuration that uses private endpoints to secure online endpoints.

> [!TIP]
> In this example, and Azure Virtual Machine is created inside the VNet. You connect to the VM using SSH, and run the deployment from the VM. This configuration is used to simplify the steps in this example, and does not represent a typical secure configuration. For example, in a production environment you would most likely use a VPN client or Azure ExpressRoute to directly connect clients to the virtual network.

### Create workspace and secured resources

The steps in this section use an Azure Resource Manager template to create the following Azure resources:

* Azure Virtual Network
* Azure Machine Learning workspace
* Azure Container Registry
* Azure Key Vault
* Azure Storage account (blob & file storage)

Public access is disabled for all the services. While the Azure Machine Learning workspace is secured behind a vnet, it's configured to allow public network access. For more information, see [CLI 2.0 secure communications](how-to-configure-cli.md#secure-communications). A scoring subnet is created, along with outbound rules that allow communication with the following Azure services:

* Azure Active Directory
* Azure Resource Manager
* Azure Front Door
* Microsoft Container Registries

The following diagram shows the different components created in this architecture:

The following diagram shows the overall architecture of this example:

:::image type="content" source="./media/how-to-secure-online-endpoint/endpoint-network-isolation-diagram.png" alt-text="Diagram of the services created.":::

To create the resources, use the following Azure CLI commands. To create a resource group. Replace `<my-resource-group>` and `<my-location>` with the desierd values.  

```azurecli
# create resource group
az group create --name <my-resource-group> --location <my-location>
```

Clone the example files for the deployment, use the following command:

```azurecli
#Clone the example files
git clone https://github.com/Azure/azureml-examples
```

To create the resources, use the following Azure CLI commands. Replace `<UNIQUE_SUFFIX>` with a unique suffix for the resources that are created.

```azurecli
az deployment group create --template-file endpoints/online/managed/vnet/setup_ws/main.bicep --parameters suffix=$SUFFIX --resource-group <my-resource-group>
```
