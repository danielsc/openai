
# Manage Azure Machine Learning workspaces using Azure CLI

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK or CLI extension you are using:"]
> * [v1](v1/how-to-manage-workspace-cli.md)
> * [v2 (current version)](how-to-manage-workspace-cli.md)

In this article, you learn how to create and manage Azure Machine Learning workspaces using the Azure CLI. The Azure CLI provides commands for managing Azure resources and is designed to get you working quickly with Azure, with an emphasis on automation. The machine learning extension to the CLI provides commands for working with Azure Machine Learning resources.

You can also manage workspaces the [Azure portal and Python SDK](how-to-manage-workspace.md), [Azure PowerShell](how-to-manage-workspace-powershell.md), or [via the VS Code extension](how-to-setup-vs-code.md).

## Prerequisites

* An **Azure subscription**. If you don't have one, try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

* To use the CLI commands in this document from your **local environment**, you need the [Azure CLI](/cli/azure/install-azure-cli).

    If you use the [Azure Cloud Shell](https://azure.microsoft.com//features/cloud-shell/), the CLI is accessed through the browser and lives in the cloud.

## Limitations

[!INCLUDE [register-namespace](../../includes/machine-learning-register-namespace.md)]

[!INCLUDE [application-insight](../../includes/machine-learning-application-insight.md)]

### Secure CLI communications

Some of the Azure CLI commands communicate with Azure Resource Manager over the internet. This communication is secured using HTTPS/TLS 1.2.

With the Azure Machine Learning CLI extension v2 ('ml'), all of the commands communicate with the Azure Resource Manager. This includes operational data such as YAML parameters and metadata. If your Azure Machine Learning workspace is public (that is, not behind a virtual network), then there's no extra configuration required. Communications are secured using HTTPS/TLS 1.2.

If your Azure Machine Learning workspace uses a private endpoint and virtual network and you're using CLI v2, choose one of the following configurations to use:

* If you're __OK__ with the CLI v2 communication over the public internet, use the following `--public-network-access` parameter for the `az ml workspace update` command to enable public network access. For example, the following command updates a workspace for public network access:

    ```azurecli
    az ml workspace update --name myworkspace --public-network-access enabled
    ```

* If you are __not OK__ with the CLI v2 communication over the public internet, you can use an Azure Private Link to increase security of the communication. Use the following links to secure communications with Azure Resource Manager by using Azure Private Link.

    1. [Secure your Azure Machine Learning workspace inside a virtual network using a private endpoint](how-to-configure-private-link.md).
    2. [Create a Private Link for managing Azure resources](../azure-resource-manager/management/create-private-link-access-portal.md). 
    3. [Create a private endpoint](../azure-resource-manager/management/create-private-link-access-portal.md#create-private-endpoint) for the Private Link created in the previous step.

    > [!IMPORTANT]
    > To configure the private link for Azure Resource Manager, you must be the _subscription owner_ for the Azure subscription, and an _owner_ or _contributor_ of the root management group. For more information, see [Create a private link for managing Azure resources](../azure-resource-manager/management/create-private-link-access-portal.md).

For more information on CLI v2 communication, see [Install and set up the CLI](how-to-configure-cli.md#secure-communications).

## Connect the CLI to your Azure subscription

> [!IMPORTANT]
> If you are using the Azure Cloud Shell, you can skip this section. The cloud shell automatically authenticates you using the account you log into your Azure subscription.
