# Customer-managed keys for Azure Machine Learning

Azure Machine Learning is built on top of multiple Azure services. While the data is stored securely using encryption keys that Microsoft provides, you can enhance security by also providing your own (customer-managed) keys. The keys you provide are stored securely using Azure Key Vault.

[!INCLUDE [machine-learning-customer-managed-keys.md](../../includes/machine-learning-customer-managed-keys.md)]

In addition to customer-managed keys, Azure Machine Learning also provides a [hbi_workspace flag](/python/api/azure-ai-ml/azure.ai.ml.entities.workspace). Enabling this flag reduces the amount of data Microsoft collects for diagnostic purposes and enables [extra encryption in Microsoft-managed environments](../security/fundamentals/encryption-atrest.md). This flag also enables the following behaviors:

* Starts encrypting the local scratch disk in your Azure Machine Learning compute cluster, provided you haven’t created any previous clusters in that subscription. Else, you need to raise a support ticket to enable encryption of the scratch disk of your compute clusters.
* Cleans up your local scratch disk between jobs.
* Securely passes credentials for your storage account, container registry, and SSH account from the execution layer to your compute clusters using your key vault.

> [!TIP]
> The `hbi_workspace` flag does not impact encryption in transit, only encryption at rest.

## Prerequisites

* An Azure subscription.
* An Azure Key Vault instance. The key vault contains the key(s) used to encrypt your services.

    * The key vault instance must enable soft delete and purge protection.
    * The managed identity for the services secured by a customer-managed key must have the following permissions in key vault:

        * wrap key
        * unwrap key
        * get

        For example, the managed identity for Azure Cosmos DB would need to have those permissions to the key vault.

## Limitations

* The customer-managed key for resources the workspace depends on can’t be updated after workspace creation.
* Resources managed by Microsoft in your subscription can’t transfer ownership to you.
* You can't delete Microsoft-managed resources used for customer-managed keys without also deleting your workspace.

## How workspace metadata is stored

The following resources store metadata for your workspace:

| Service | How it’s used |
| ----- | ----- |
| Azure Cosmos DB | Stores job history data. |
| Azure Cognitive Search | Stores indices that are used to help query your machine learning content. |
| Azure Storage Account | Stores other metadata such as Azure Machine Learning pipelines data. |

Your Azure Machine Learning workspace reads and writes data using its managed identity. This identity is granted access to the resources using a role assignment (Azure role-based access control) on the data resources. The encryption key you provide is used to encrypt data that is stored on Microsoft-managed resources. It's also used to create indices for Azure Cognitive Search, which are created at runtime.

## Customer-managed keys

When you __don't use a customer-managed key__, Microsoft creates and manages these resources in a Microsoft owned Azure subscription and uses a Microsoft-managed key to encrypt the data. 

When you __use a customer-managed key__, these resources are _in your Azure subscription_ and encrypted with your key. While they exist in your subscription, these resources are __managed by Microsoft__. They're automatically created and configured when you create your Azure Machine Learning workspace.

> [!IMPORTANT]
> When using a customer-managed key, the costs for your subscription will be higher because these resources are in your subscription. To estimate the cost, use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/).

These Microsoft-managed resources are located in a new Azure resource group is created in your subscription. This group is in addition to the resource group for your workspace. This resource group will contain the Microsoft-managed resources that your key is used with. The resource group will be named using the formula of `<Azure Machine Learning workspace resource group name><GUID>`.
