# Use customer-managed keys with Azure Machine Learning

In the [customer-managed keys concepts article](concept-customer-managed-keys.md), you learned about the encryption capabilities that Azure Machine Learning provides. Now learn how to use customer-managed keys with Azure Machine Learning.

[!INCLUDE [machine-learning-customer-managed-keys.md](../../includes/machine-learning-customer-managed-keys.md)]

## Prerequisites

* An Azure subscription.

* The following Azure resource providers must be registered:

    | Resource provider | Why it's needed |
    | ----- | ----- |
    | Microsoft.MachineLearningServices | Creating the Azure Machine Learning workspace.
    | Microsoft.Storage	Azure | Storage Account is used as the default storage for the workspace.
    | Microsoft.KeyVault |Azure Key Vault is used by the workspace to store secrets.
    | Microsoft.DocumentDB/databaseAccounts | Azure Cosmos DB instance that logs metadata for the workspace.
    | Microsoft.Search/searchServices | Azure Search provides indexing capabilities for the workspace.

    For information on registering resource providers, see [Resolve errors for resource provider registration](/azure/azure-resource-manager/templates/error-register-resource-provider).


## Limitations

* The customer-managed key for resources the workspace depends on can’t be updated after workspace creation.
* Resources managed by Microsoft in your subscription can’t transfer ownership to you.
* You can't delete Microsoft-managed resources used for customer-managed keys without also deleting your workspace.
* The key vault that contains your customer-managed key must be in the same Azure subscription as the Azure Machine Learning workspace.
* Workspace with customer-managed key doesn't currently support v2 online endpoint and batch endpoint.

> [!IMPORTANT]
> When using a customer-managed key, the costs for your subscription will be higher because of the additional resources in your subscription. To estimate the cost, use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/).

## Create Azure Key Vault

To create the key vault, see [Create a key vault](../key-vault/general/quick-create-portal.md). When creating Azure Key Vault, you must enable __soft delete__ and __purge protection__.

> [!IMPORTANT]
> The key vault must be in the same Azure subscription that will contain your Azure Machine Learning workspace.

### Create a key

> [!TIP]
> If you have problems creating the key, it may be caused by Azure role-based access controls that have been applied in your subscription. Make sure that the security principal (user, managed identity, service principal, etc.) you are using to create the key has been assigned the __Contributor__ role for the key vault instance. You must also configure an __Access policy__ in key vault that grants the security principal __Create__, __Get__, __Delete__, and __Purge__ authorization.
>
> If you plan to use a user-assigned managed identity for your workspace, the managed identity must also be assigned these roles and access policies.
>
> For more information, see the following articles:
> * [Provide access to key vault keys, certificates, and secrets](../key-vault/general/rbac-guide.md)
> * [Assign a key vault access policy](../key-vault/general/assign-access-policy.md)
> * [Use managed identities with Azure Machine Learning](how-to-identity-based-service-authentication.md)

1. From the [Azure portal](https://portal.azure.com), select the key vault instance. Then select __Keys__ from the left.
1. Select __+ Generate/import__ from the top of the page. Use the following values to create a key:

    * Set __Options__ to __Generate__.
    * Enter a __Name__ for the key. The name should be something that identifies what the planned use is. For example, `my-cosmos-key`.
    * Set __Key type__ to __RSA__.
    * We recommend selecting at least __3072__ for the __RSA key size__.
    * Leave __Enabled__ set to yes.

    Optionally you can set an activation date, expiration date, and tags.
