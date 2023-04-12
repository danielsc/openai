
# Use an Azure Resource Manager template to create a workspace for Azure Machine Learning

In this article, you learn several ways to create an Azure Machine Learning workspace using Azure Resource Manager templates. A Resource Manager template makes it easy to create resources as a single, coordinated operation. A template is a JSON document that defines the resources that are needed for a deployment. It may also specify deployment parameters. Parameters are used to provide input values when using the template.

For more information, see [Deploy an application with Azure Resource Manager template](../azure-resource-manager/templates/deploy-powershell.md).

## Prerequisites

* An **Azure subscription**. If you do not have one, try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

* To use a template from a CLI, you need either [Azure PowerShell](/powershell/azure/) or the [Azure CLI](/cli/azure/install-azure-cli).

## Limitations

[!INCLUDE [register-namespace](../../includes/machine-learning-register-namespace.md)]

* The example template may not always use the latest API version for Azure Machine Learning. Before using the template, we recommend modifying it to use the latest API versions. For information on the latest API versions for Azure Machine Learning, see the [Azure Machine Learning REST API](/rest/api/azureml/).

    > [!TIP]
    > Each Azure service has its own set of API versions. For information on the API for a specific service, check the service information in the [Azure REST API reference](/rest/api/azure/).

    To update the API version, find the `"apiVersion": "YYYY-MM-DD"` entry for the resource type and update it to the latest version. The following example is an entry for Azure Machine Learning:

    ```json
    "type": "Microsoft.MachineLearningServices/workspaces",
    "apiVersion": "2020-03-01",
    ```

### Multiple workspaces in the same VNet

The template doesn't support multiple Azure Machine Learning workspaces deployed in the same VNet. This is because the template creates new DNS zones during deployment.

If you want to create a template that deploys multiple workspaces in the same VNet, set this up manually (using the Azure Portal or CLI) and then [use the Azure portal to generate a template](../azure-resource-manager/templates/export-template-portal.md).

## Workspace Resource Manager template

The Azure Resource Manager template used throughout this document can be found in the [microsoft.machineleaerningservices/machine-learning-workspace-vnet](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.machinelearningservices/machine-learning-workspace-vnet/azuredeploy.json) directory of the Azure quickstart templates GitHub repository.

This template creates the following Azure services:

* Azure Storage Account
* Azure Key Vault
* Azure Application Insights
* Azure Container Registry
* Azure Machine Learning workspace

The resource group is the container that holds the services. The various services are required by the Azure Machine Learning workspace.

The example template has two **required** parameters:

* The **location** where the resources will be created.

    The template will use the location you select for most resources. The exception is the Application Insights service, which is not available in all of the locations that the other services are. If you select a location where it is not available, the service will be created in the South Central US location.

* The **workspaceName**, which is the friendly name of the Azure Machine Learning workspace.

    > [!NOTE]
    > The workspace name is case-insensitive.

    The names of the other services are generated randomly.

> [!TIP]
> While the template associated with this document creates a new Azure Container Registry, you can also create a new workspace without creating a container registry. One will be created when you perform an operation that requires a container registry. For example, training or deploying a model.
