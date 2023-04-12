
# Access Azure resources from an online endpoint with a managed identity 

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to access Azure resources from your scoring script with an online endpoint and either a system-assigned managed identity or a user-assigned managed identity. 

Managed endpoints allow Azure Machine Learning to manage the burden of provisioning your compute resource and deploying your machine learning model. Typically your model needs to access Azure resources such as the Azure Container Registry or your blob storage for inferencing; with a managed identity you can access these resources without needing to manage credentials in your code. [Learn more about managed identities](../active-directory/managed-identities-azure-resources/overview.md).

This guide assumes you don't have a managed identity, a storage account or an online endpoint. If you already have these components, skip to the [give access permission to the managed identity](#give-access-permission-to-the-managed-identity) section. 

## Prerequisites

# [System-assigned (CLI)](#tab/system-identity-cli)

* To use Azure Machine Learning, you must have an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* Install and configure the Azure CLI and ML (v2) extension. For more information, see [Install, set up, and use the 2.0 CLI](how-to-configure-cli.md).

* An Azure Resource group, in which you (or the service principal you use) need to have `User Access Administrator` and  `Contributor` access. You'll have such a resource group if you configured your ML extension per the above article.

* An Azure Machine Learning workspace. You'll have a workspace if you configured your ML extension per the above article.

* A trained machine learning model ready for scoring and deployment. If you are following along with the sample, a model is provided.

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults gitworkspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

* To follow along with the sample, clone the samples repository

    ```azurecli
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/cli
    ```
    
# [User-assigned (CLI)](#tab/user-identity-cli)

* To use Azure Machine Learning, you must have an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* Install and configure the Azure CLI and ML (v2) extension. For more information, see [Install, set up, and use the 2.0 CLI](how-to-configure-cli.md).

* An Azure Resource group, in which you (or the service principal you use) need to have `User Access Administrator` and  `Contributor` access. You'll have such a resource group if you configured your ML extension per the above article.

* An Azure Machine Learning workspace. You'll have a workspace if you configured your ML extension per the above article.

* A trained machine learning model ready for scoring and deployment. If you are following along with the sample, a model is provided.

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults gitworkspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

* To follow along with the sample, clone the samples repository

    ```azurecli
    git clone https://github.com/Azure/azureml-examples --depth 1
    cd azureml-examples/cli
    ```
