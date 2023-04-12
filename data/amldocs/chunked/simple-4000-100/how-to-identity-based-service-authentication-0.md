
# Set up authentication between Azure ML and other services

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK or CLI extension you are using:"]
> * [v1](./v1/how-to-use-managed-identities.md)
> * [v2 (current version)](./how-to-identity-based-service-authentication.md)

Azure Machine Learning is composed of multiple Azure services. There are multiple ways that authentication can happen between Azure Machine Learning and the services it relies on.


* The Azure Machine Learning workspace uses a __managed identity__ to communicate with other services. By default, this is a system-assigned managed identity. You can also use a user-assigned managed identity instead.
* Azure Machine Learning uses Azure Container Registry (ACR) to store Docker images used to train and deploy models. If you allow Azure ML to automatically create ACR, it will enable the __admin account__.
* The Azure ML compute cluster uses a __managed identity__ to retrieve connection information for datastores from Azure Key Vault and to pull Docker images from ACR. You can also configure identity-based access to datastores, which will instead use the managed identity of the compute cluster.
* Data access can happen along multiple paths depending on the data storage service and your configuration. For example, authentication to the datastore may use an account key, token, security principal, managed identity, or user identity.
* Managed online endpoints can use a managed identity to access Azure resources when performing inference. For more information, see [Access Azure resources from an online endpoint](how-to-access-resources-from-endpoints-managed-identities.md).

## Prerequisites

[!INCLUDE [cli & sdk v2](../../includes/machine-learning-cli-sdk-v2-prereqs.md)]

* To assign roles, the login for your Azure subscription must have the [Managed Identity Operator](../role-based-access-control/built-in-roles.md#managed-identity-operator) role, or other role that grants the required actions (such as __Owner__).

* You must be familiar with creating and working with [Managed Identities](../active-directory/managed-identities-azure-resources/overview.md).

## User-assigned managed identity

### Workspace

You can add a user-assigned managed identity when creating an Azure Machine Learning workspace from the [Azure portal](https://portal.azure.com). Use the following steps while creating the workspace:

1. From the __Basics__ page, select the Azure Storage Account, Azure Container Registry, and Azure Key Vault you want to use with the workspace.
1. From the __Advanced__ page, select __User-assigned identity__ and then select the managed identity to use.

The following [Azure RBAC role assignments](../role-based-access-control/role-assignments.md) are required on your user-assigned managed identity for your Azure Machine Learning workspace to access data on the workspace-associated resources.

|Resource|Permission|
|---|---|
|Azure Storage|Contributor (control plane) + Storage Blob Data Contributor (data plane, optional, to enable data preview in the Azure Machine Learning studio)|
|Azure Key Vault (when using [RBAC permission model](../key-vault/general/rbac-guide.md))|Contributor (control plane) + Key Vault Administrator (data plane)|
|Azure Key Vault (when using [access policies permission model](../key-vault/general/assign-access-policy.md))|Contributor + any access policy permissions besides **purge** operations|
|Azure Container Registry|Contributor|
|Azure Application Insights|Contributor|

For automated creation of role assignments on your user-assigned managed identity, you may use [this ARM template](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-dependencies-role-assignment).

> [!TIP]
> For a workspace with [customer-managed keys for encryption](concept-data-encryption.md), you can pass in a user-assigned managed identity to authenticate from storage to Key Vault. Use the `user-assigned-identity-for-cmk-encryption` (CLI) or `user_assigned_identity_for_cmk_encryption` (SDK) parameters to pass in the managed identity. This managed identity can be the same or different as the workspace primary user assigned managed identity.
