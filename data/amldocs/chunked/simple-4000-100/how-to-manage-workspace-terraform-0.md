
# Manage Azure Machine Learning workspaces using Terraform

In this article, you learn how to create and manage an Azure Machine Learning workspace using Terraform configuration files. [Terraform](/azure/developer/terraform/)'s template-based configuration files enable you to define, create, and configure Azure resources in a repeatable and predictable manner. Terraform tracks resource state and is able to clean up and destroy resources. 

A Terraform configuration is a document that defines the resources that are needed for a deployment. It may also specify deployment variables. Variables are used to provide input values when using the configuration.

## Prerequisites

* An **Azure subscription**. If you don't have one, try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
* An installed version of the [Azure CLI](/cli/azure/).
* Configure Terraform: follow the directions in this article and the [Terraform and configure access to Azure](/azure/developer/terraform/get-started-cloud-shell) article.

## Limitations

[!INCLUDE [register-namespace](../../includes/machine-learning-register-namespace.md)]

[!INCLUDE [application-insight](../../includes/machine-learning-application-insight.md)]

## Declare the Azure provider

Create the Terraform configuration file that declares the Azure provider:

1. Create a new file named `main.tf`. If working with Azure Cloud Shell, use bash:

    ```bash
    code main.tf
    ```

1. Paste the following code into the editor:

    **main.tf**:
```terraform
terraform {
  required_version = ">=1.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.76.0"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_client_config" "current" {}

resource "azurerm_resource_group" "default" {
  name     = "rg-${var.name}-${var.environment}"
  location = var.location
}
```

1. Save the file (**&lt;Ctrl>S**) and exit the editor (**&lt;Ctrl>Q**).

## Deploy a workspace

The following Terraform configurations can be used to create an Azure Machine Learning workspace. When you create an Azure Machine Learning workspace, various other services are required as dependencies. The template also specifies these [associated resources to the workspace](./concept-workspace.md#associated-resources). Depending on your needs, you can choose to use the template that creates resources with either public or private network connectivity.

# [Public network connectivity](#tab/publicworkspace)

Some resources in Azure require globally unique names. Before deploying your resources using the following templates, set the `name` variable to a value that is unique.

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
  purge_protection_enabled = false
}

resource "azurerm_storage_account" "default" {
  name                            = "st${var.name}${var.environment}"
  location                        = azurerm_resource_group.default.location
  resource_group_name             = azurerm_resource_group.default.name
  account_tier                    = "Standard"
  account_replication_type        = "GRS"
  allow_nested_items_to_be_public = false
}

resource "azurerm_container_registry" "default" {
  name                = "cr${var.name}${var.environment}"
  location            = azurerm_resource_group.default.location
  resource_group_name = azurerm_resource_group.default.name
  sku                 = "Premium"
  admin_enabled       = true
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
}



```
