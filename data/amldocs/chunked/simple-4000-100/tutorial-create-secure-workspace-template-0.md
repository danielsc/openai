# How to create a secure workspace by using template

Templates provide a convenient way to create reproducible service deployments. The template defines what will be created, with some information provided by you when you use the template. For example, specifying a unique name for the Azure Machine Learning workspace.

In this tutorial, you learn how to use a [Microsoft Bicep](../azure-resource-manager/bicep/overview.md) and [Hashicorp Terraform](https://www.terraform.io/) template to create the following Azure resources:

* Azure Virtual Network. The following resources are secured behind this VNet:
    * Azure Machine Learning workspace
        * Azure Machine Learning compute instance
        * Azure Machine Learning compute cluster
    * Azure Storage Account
    * Azure Key Vault
    * Azure Application Insights
    * Azure Container Registry
    * Azure Bastion host
    * Azure Machine Learning Virtual Machine (Data Science Virtual Machine)
    * The __Bicep__ template also creates an Azure Kubernetes Service cluster, and a separate resource group for it.

## Prerequisites

Before using the steps in this article, you must have an Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/).

You must also have either a Bash or Azure PowerShell command line.

> [!TIP]
> When reading this article, use the tabs in each section to select whether to view information on using Bicep or Terraform templates.

# [Bicep](#tab/bicep)

1. To install the command-line tools, see [Set up Bicep development and deployment environments](../azure-resource-manager/bicep/install.md).

1. The Bicep template used in this article is located at [https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure). Use the following commands to clone the GitHub repo to your development environment:

    > [!TIP]
    > If you do not have the `git` command on your development environment, you can install it from [https://git-scm.com/](https://git-scm.com/).

    ```azurecli
    git clone https://github.com/Azure/azure-quickstart-templates
    cd azure-quickstart-templates/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure
    ```  

# [Terraform](#tab/terraform)

1. To install, configure, and authenticate Terraform to your Azure subscription, use the steps in one of the following articles:

    * [Azure Cloud Shell](/azure/developer/terraform/get-started-cloud-shell-bash)
    * [Windows with Bash](/azure/developer/terraform/get-started-windows-bash)
    * [Windows with Azure PowerShell](/azure/developer/terraform/get-started-windows-powershell)

1. The Terraform template files used in this article are located at [https://github.com/Azure/terraform/tree/master/quickstart/201-machine-learning-moderately-secure](https://github.com/Azure/terraform/tree/master/quickstart/201-machine-learning-moderately-secure). To clone the repo locally and change directory to where the template files are located, use the following commands from the command line:

    > [!TIP]
    > If you do not have the `git` command on your development environment, you can install it from [https://git-scm.com/](https://git-scm.com/).

    ```azurecli
    git clone https://github.com/Azure/terraform
    cd terraform/quickstart/201-machine-learning-moderately-secure
    ```

## Understanding the template

# [Bicep](#tab/bicep)

The Bicep template is made up of the [main.bicep](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure/main.bicep) and the `.bicep` files in the [modules](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure/modules) subdirectory. The following table describes what each file is responsible for:
