
# [Private network connectivity](#tab/privateworkspace)

The configuration below creates a workspace in an isolated network environment using Azure Private Link endpoints. [Private DNS zones](../dns/private-dns-privatednszone.md) are included so domain names can be resolved within the virtual network.

Some resources in Azure require globally unique names. Before deploying your resources using the following templates, set the `resourceprefix` variable to a value that is unique.

When using private link endpoints for both Azure Container Registry and Azure Machine Learning, Azure Container Registry tasks cannot be used for building [environment](/python/api/azure-ai-ml/azure.ai.ml.entities.environment) images. Instead you can build images using an Azure Machine Learning compute cluster. To configure the cluster name of use, set the [image_build_compute_name](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/machine_learning_workspace) argument. You can configure to [allow public access](./how-to-configure-private-link.md?tabs=python#enable-public-access) to a workspace that has a private link endpoint using the [public_network_access_enabled](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/machine_learning_workspace) argument.

**variables.tf**:
```terraform
variable "name" {
  type        = string
  description = "Name of the deployment"
}

variable "environment" {
  type        = string
  description = "Name of the environment"
  default     = "dev"
}

variable "location" {
  type        = string
  description = "Location of the resources"
  default     = "East US"
}

variable "vnet_address_space" {
  type        = list(string)
  description = "Address space of the virtual network"
  default     = ["10.0.0.0/16"]
}

variable "training_subnet_address_space" {
  type        = list(string)
  description = "Address space of the training subnet"
  default     = ["10.0.1.0/24"]
}

variable "aks_subnet_address_space" {
  type        = list(string)
  description = "Address space of the aks subnet"
  default     = ["10.0.2.0/23"]
}

variable "ml_subnet_address_space" {
  type        = list(string)
  description = "Address space of the ML workspace subnet"
  default     = ["10.0.0.0/24"]
}
variable "dsvm_subnet_address_space" {
  type        = list(string)
  description = "Address space of the DSVM subnet"
  default     = ["10.0.4.0/24"]
}

variable "bastion_subnet_address_space" {
  type        = list(string)
  description = "Address space of the bastion subnet"
  default     = ["10.0.5.0/24"]
}

variable "image_build_compute_name" {
  type        = string
  description = "Name of the compute cluster to be created and set to build docker images"
  default     = "image-builder"
}

# DSVM Variables
variable "dsvm_name" {
  type        = string
  description = "Name of the Data Science VM"
  default     = "vmdsvm01"
}
variable "dsvm_admin_username" {
  type        = string
  description = "Admin username of the Data Science VM"
  default     = "azureadmin"
}

variable "dsvm_host_password" {
  type        = string
  description = "Password for the admin username of the Data Science VM"
  sensitive   = true
}
```

**workspace.tf**:
```terraform
# Dependent resources for Azure Machine Learning
resource "azurerm_application_insights" "default" {
  name                = "appi-${var.name}-${var.environment}"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  application_type    = "web"
}

resource "azurerm_key_vault" "default" {
  name                     = "kv-${var.name}-${var.environment}"
  location                 = azurerm_resource_group.default.location
  resource_group_name      = azurerm_resource_group.default.name
  tenant_id                = data.azurerm_client_config.current.tenant_id
  sku_name                 = "premium"
  purge_protection_enabled = true

  network_acls {
    default_action = "Deny"
    bypass         = "AzureServices"
  }
}

resource "azurerm_storage_account" "default" {
  name                     = "st${var.name}${var.environment}"
  location                 = azurerm_resource_group.default.location
  resource_group_name      = azurerm_resource_group.default.name
  account_tier             = "Standard"
  account_replication_type = "GRS"

  network_rules {
    default_action = "Deny"
    bypass         = ["AzureServices"]
  }
}

resource "azurerm_container_registry" "default" {
  name                = "cr${var.name}${var.environment}"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  sku                 = "Premium"
  admin_enabled       = true

  network_rule_set {
    default_action = "Deny"
  }
  public_network_access_enabled = false
}

# Machine Learning workspace
resource "azurerm_machine_learning_workspace" "default" {
  name                    = "mlw-${var.name}-${var.environment}"
  location                = azurerm_resource_group.default.location
  resource_group_name     = azurerm_resource_group.default.name
  application_insights_id = azurerm_application_insights.default.id
  key_vault_id            = azurerm_key_vault.default.id
  storage_account_id      = azurerm_storage_account.default.id
  container_registry_id   = azurerm_container_registry.default.id

  identity {
    type = "SystemAssigned"
  }

  # Args of use when using an Azure Private Link configuration
  public_network_access_enabled = false
  image_build_compute_name      = var.image_build_compute_name
  depends_on = [
    azurerm_private_endpoint.kv_ple,
    azurerm_private_endpoint.st_ple_blob,
    azurerm_private_endpoint.storage_ple_file,
    azurerm_private_endpoint.cr_ple,
    azurerm_subnet.snet-training
  ]

}

# Private endpoints
resource "azurerm_private_endpoint" "kv_ple" {
  name                = "ple-${var.name}-${var.environment}-kv"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  subnet_id           = azurerm_subnet.snet-workspace.id

  private_dns_zone_group {
    name                 = "private-dns-zone-group"
    private_dns_zone_ids = [azurerm_private_dns_zone.dnsvault.id]
  }

  private_service_connection {
    name                           = "psc-${var.name}-kv"
    private_connection_resource_id = azurerm_key_vault.default.id
    subresource_names              = ["vault"]
    is_manual_connection           = false
  }
}

resource "azurerm_private_endpoint" "st_ple_blob" {
  name                = "ple-${var.name}-${var.environment}-st-blob"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  subnet_id           = azurerm_subnet.snet-workspace.id

  private_dns_zone_group {
    name                 = "private-dns-zone-group"
    private_dns_zone_ids = [azurerm_private_dns_zone.dnsstorageblob.id]
  }

  private_service_connection {
    name                           = "psc-${var.name}-st"
    private_connection_resource_id = azurerm_storage_account.default.id
    subresource_names              = ["blob"]
    is_manual_connection           = false
  }
}

resource "azurerm_private_endpoint" "storage_ple_file" {
  name                = "ple-${var.name}-${var.environment}-st-file"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  subnet_id           = azurerm_subnet.snet-workspace.id

  private_dns_zone_group {
    name                 = "private-dns-zone-group"
    private_dns_zone_ids = [azurerm_private_dns_zone.dnsstoragefile.id]
  }

  private_service_connection {
    name                           = "psc-${var.name}-st"
    private_connection_resource_id = azurerm_storage_account.default.id
    subresource_names              = ["file"]
    is_manual_connection           = false
  }
}

resource "azurerm_private_endpoint" "cr_ple" {
  name                = "ple-${var.name}-${var.environment}-cr"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  subnet_id           = azurerm_subnet.snet-workspace.id

  private_dns_zone_group {
    name                 = "private-dns-zone-group"
    private_dns_zone_ids = [azurerm_private_dns_zone.dnscontainerregistry.id]
  }

  private_service_connection {
    name                           = "psc-${var.name}-cr"
    private_connection_resource_id = azurerm_container_registry.default.id
    subresource_names              = ["registry"]
    is_manual_connection           = false
  }
}

resource "azurerm_private_endpoint" "mlw_ple" {
  name                = "ple-${var.name}-${var.environment}-mlw"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  subnet_id           = azurerm_subnet.snet-workspace.id

  private_dns_zone_group {
    name                 = "private-dns-zone-group"
    private_dns_zone_ids = [azurerm_private_dns_zone.dnsazureml.id, azurerm_private_dns_zone.dnsnotebooks.id]
  }

  private_service_connection {
    name                           = "psc-${var.name}-mlw"
    private_connection_resource_id = azurerm_machine_learning_workspace.default.id
    subresource_names              = ["amlworkspace"]
    is_manual_connection           = false
  }
}

# Compute cluster for image building required since the workspace is behind a vnet.
# For more details, see https://docs.microsoft.com/en-us/azure/machine-learning/tutorial-create-secure-workspace#configure-image-builds.
resource "azurerm_machine_learning_compute_cluster" "image-builder" {
  name                          = var.image_build_compute_name
  location                      = azurerm_resource_group.default.location
  vm_priority                   = "LowPriority"
  vm_size                       = "Standard_DS2_v2"
  machine_learning_workspace_id = azurerm_machine_learning_workspace.default.id
  subnet_resource_id            = azurerm_subnet.snet-training.id

  scale_settings {
    min_node_count                       = 0
    max_node_count                       = 3
    scale_down_nodes_after_idle_duration = "PT15M" # 15 minutes
  }

  identity {
    type = "SystemAssigned"
  }
}

```
