
# Use authentication credential secrets in Azure Machine Learning jobs

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the version of the Azure Machine Learning Python SDK you are using:"]
> * [v1](v1/how-to-use-secrets-in-runs.md)
> * [v2 (current version)](how-to-use-secrets-in-runs.md)

Authentication information such as your user name and password are secrets. For example, if you connect to an external database in order to query training data, you would need to pass your username and password to the remote job context. Coding such values into training scripts in clear text is insecure as it would potentially expose the secret.

The Azure Key Vault allows you to securely store and retrieve secrets. In this article, learn how you can retrieve secrets stored in a key vault from a training job running on a compute cluster.

> [!IMPORTANT]
> The Azure Machine Learning Python SDK v2 and Azure CLI extension v2 for machine learning do not provide the capability to set or get secrets. Instead, the information in this article uses the [Azure Key Vault Secrets client library for Python](/python/api/overview/azure/keyvault-secrets-readme).

## Prerequisites

Before following the steps in this article, make sure you have the following prerequisites:

> [!TIP]
> Many of the prerequisites in this section require __Contributor__, __Owner__, or equivalent access to your Azure subscription, or the Azure Resource Group that contains the resources. You may need to contact your Azure administrator and have them perform these actions.

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
 
* An Azure Machine Learning workspace. If you don't have one, use the steps in the [Quickstart: Create workspace resources](quickstart-create-resources.md) article to create one.

* An Azure Key Vault. If you used the [Quickstart: Create workspace resources](quickstart-create-resources.md) article to create your workspace, a key vault was created for you. You can also create a separate key vault instance using the information in the [Quickstart: Create a key vault](../key-vault/general/quick-create-portal.md) article.

    > [!TIP]
    > You do not have to use same key vault as the workspace.

* An Azure Machine Learning compute cluster configured to use a [managed identity](how-to-create-attach-compute-cluster.md?tabs=azure-studio#set-up-managed-identity). The cluster can be configured for either a system-assigned or user-assigned managed identity.

* Grant the managed identity for the compute cluster access to the secrets stored in key vault. The method used to grant access depends on how your key vault is configured:

    * [Azure role-based access control (Azure RBAC)](../key-vault/general/rbac-guide.md): When configured for Azure RBAC, add the managed identity to the __Key Vault Secrets User__ role on your key vault.
    * [Azure Key Vault access policy](../key-vault/general/assign-access-policy.md): When configured to use access policies, add a new policy that grants the __get__ operation for secrets and assign it to the managed identity.

* A stored secret value in the key vault. This value can then be retrieved using a key. For more information, see [Quickstart: Set and retrieve a secret from Azure Key Vault](../key-vault/secrets/quick-create-python.md).

    > [!TIP]
    > The quickstart link is to the steps for using the Azure Key Vault Python SDK. In the table of contents in the left navigation area are links to other ways to set a key.

## Getting secrets

1. Add the `azure-keyvault-secrets` and `azure-identity` packages to the [Azure Machine Learning environment](concept-environments.md) used when training the model. For example, by adding them to the conda file used to build the environment.

    The environment is used to build the Docker image that the training job runs in on the compute cluster.
