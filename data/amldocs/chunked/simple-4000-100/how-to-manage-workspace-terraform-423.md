
**network.tf**:
```terraform
# Virtual Network
resource "azurerm_virtual_network" "default" {
  name                = "vnet-${var.name}-${var.environment}"
  address_space       = var.vnet_address_space
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
}

resource "azurerm_subnet" "snet-training" {
  name                                           = "snet-training"
  resource_group_name                            = azurerm_resource_group.default.name
  virtual_network_name                           = azurerm_virtual_network.default.name
  address_prefixes                               = var.training_subnet_address_space
  enforce_private_link_endpoint_network_policies = true
}

resource "azurerm_subnet" "snet-aks" {
  name                                           = "snet-aks"
  resource_group_name                            = azurerm_resource_group.default.name
  virtual_network_name                           = azurerm_virtual_network.default.name
  address_prefixes                               = var.aks_subnet_address_space
  enforce_private_link_endpoint_network_policies = true
}

resource "azurerm_subnet" "snet-workspace" {
  name                                           = "snet-workspace"
  resource_group_name                            = azurerm_resource_group.default.name
  virtual_network_name                           = azurerm_virtual_network.default.name
  address_prefixes                               = var.ml_subnet_address_space
  enforce_private_link_endpoint_network_policies = true
}

# ...
# For full reference, see: https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/network.tf
```

There are several options to connect to your private link endpoint workspace. To learn more about these options, refer to [Securely connect to your workspace](./how-to-secure-workspace-vnet.md#securely-connect-to-your-workspace).


## Troubleshooting

### Resource provider errors

[!INCLUDE [machine-learning-resource-provider](../../includes/machine-learning-resource-provider.md)]

## Next steps

* To learn more about Terraform support on Azure, see [Terraform on Azure documentation](/azure/developer/terraform/).
* For details on the Terraform Azure provider and Machine Learning module, see [Terraform Registry Azure Resource Manager Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/machine_learning_workspace).
* To find "quick start" template examples for Terraform, see [Azure Terraform QuickStart Templates](https://github.com/Azure/terraform/tree/master/quickstart):
  
  * [101: Machine learning workspace and compute](https://github.com/Azure/terraform/tree/master/quickstart/101-machine-learning) – the minimal set of resources needed to get started with Azure ML.
  * [201: Machine learning workspace, compute, and a set of network components for network isolation](https://github.com/Azure/terraform/tree/master/quickstart/201-machine-learning-moderately-secure) – all resources that are needed to create a production-pilot environment for use with HBI data.
  * [202: Similar to 201, but with the option to bring existing network components.](https://github.com/Azure/terraform/tree/master/quickstart/202-machine-learning-moderately-secure-existing-VNet).
  * [301:  Machine Learning workspace (Secure Hub and Spoke with Firewall)](https://github.com/azure/terraform/tree/master/quickstart/301-machine-learning-hub-spoke-secure).
  
* To learn more about network configuration options, see [Secure Azure Machine Learning workspace resources using virtual networks (VNets)](./how-to-network-security-overview.md).
* For alternative Azure Resource Manager template-based deployments, see [Deploy resources with Resource Manager templates and Resource Manager REST API](../azure-resource-manager/templates/deploy-rest.md).
* For information on how to keep your Azure ML up to date with the latest security updates, see [Vulnerability management](concept-vulnerability-management.md).