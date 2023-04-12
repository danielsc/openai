| [privateaks.bicep](https://github.com/Azure/azure-quickstart-templates/blob/master/quickstarts/microsoft.machinelearningservices/machine-learning-end-to-end-secure/modules/privateaks.bicep) | Defines an Azure Kubernetes Services cluster instance. |

> [!IMPORTANT]
> The example templates may not always use the latest API version for Azure Machine Learning. Before using the template, we recommend modifying it to use the latest API versions. For information on the latest API versions for Azure Machine Learning, see the [Azure Machine Learning REST API](/rest/api/azureml/).
>
> Each Azure service has its own set of API versions. For information on the API for a specific service, check the service information in the [Azure REST API reference](/rest/api/azure/).
>
> To update the API version, find the `Microsoft.MachineLearningServices/<resource>` entry for the resource type and update it to the latest version. The following example is an entry for the Azure Machine Learning workspace that uses an API version of `2022-05-01`:
>
>```json
>resource machineLearning 'Microsoft.MachineLearningServices/workspaces@2022-05-01' = {
>```

# [Terraform](#tab/terraform)

The template consists of multiple files. The following table describes what each file is responsible for:

| File | Description |
| ----- | ----- |
| [variables.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/variables.tf) | Variables and default values used by the template.
| [main.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/main.tf) | Specifies the Azure Resource Manager provider and defines the resource group. |
| [network.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/network.tf) | Defines the Azure Virtual Network, subnets, and network security groups. |
| [bastion.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/bastion.tf) | Defines the Azure Bastion host and associated NSG. Azure Bastion allows you to easily access a VM inside a VNet using your web browser. |
| [dsvm.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/dsvm.tf) | Defines the Data Science Virtual Machine (DSVM). Azure Bastion is used to access this VM through your web browser. |
| [workspace.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/workspace.tf) | Defines the Azure Machine Learning workspace. Including dependency resources for Azure Storage, Key Vault, Application Insights, and Container Registry. |
| [compute.tf](https://github.com/Azure/terraform/blob/master/quickstart/201-machine-learning-moderately-secure/compute.tf) | Defines an Azure Machine Learning compute instance and cluster. |

> [!TIP]
> The [Terraform Azure provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs) supports additional arguments that are not used in this tutorial. For example, the [environment](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs#environment) argument allows you to target cloud regions such as Azure Government and Azure China 21ViaNet.


> [!IMPORTANT]
> The DSVM and Azure Bastion is used as an easy way to connect to the secured workspace for this tutorial. In a production environment, we recommend using an [Azure VPN gateway](../vpn-gateway/vpn-gateway-about-vpngateways.md) or [Azure ExpressRoute](../expressroute/expressroute-introduction.md) to access the resources inside the VNet directly from your on-premises network.

## Configure the template

# [Bicep](#tab/bicep)

To run the Bicep template, use the following commands from the `machine-learning-end-to-end-secure` where the `main.bicep` file is:

1. To create a new Azure Resource Group, use the following command. Replace `exampleRG` with your resource group name, and `eastus` with the Azure region you want to use:
