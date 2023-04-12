
# Use network isolation with managed online endpoints

[!INCLUDE [SDK/CLI v2](../../includes/machine-learning-dev-v2.md)]

When deploying a machine learning model to a managed online endpoint, you can secure communication with the online endpoint by using [private endpoints](../private-link/private-endpoint-overview.md).

You can secure the inbound scoring requests from clients to an _online endpoint_. You can also secure the outbound communications between a _deployment_ and the Azure resources it uses. Security for inbound and outbound communication are configured separately. For more information on endpoints and deployments, see [What are endpoints and deployments](concept-endpoints.md#what-are-endpoints-and-deployments).

The following diagram shows how communications flow through private endpoints to the managed online endpoint. Incoming scoring requests from clients are received through the workspace private endpoint from your virtual network. Outbound communication with services is handled through private endpoints to those service instances from the deployment:

:::image type="content" source="./media/how-to-secure-online-endpoint/endpoint-network-isolation-ingress-egress.png" alt-text="Diagram of overall ingress/egress communication.":::

## Prerequisites

* To use Azure machine learning, you must have an Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

* You must install and configure the Azure CLI and `ml` extension or the AzureML Python SDK v2. For more information, see the following articles:

    * [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).
    * [Install the Python SDK v2](https://aka.ms/sdk-v2-install).

* You must have an Azure Resource Group, in which you (or the service principal you use) need to have `Contributor` access. You'll have such a resource group if you configured your `ml` extension per the above article.

* You must have an Azure Machine Learning workspace, and the workspace must use a private endpoint. If you don't have one, the steps in this article create an example workspace, VNet, and VM. For more information, see [Configure a private endpoint for Azure Machine Learning workspace](./how-to-configure-private-link.md).

    The workspace configuration can either allow or disallow public network access. If you plan on using managed online endpoint deployments that use __public outbound__, then you must also [configure the workspace to allow public access](how-to-configure-private-link.md#enable-public-access).

    Outbound communication from managed online endpoint deployment is to the _workspace API_. When the endpoint is configured to use __public outbound__, then the workspace must be able to accept that public communication (allow public access).

* When the workspace is configured with a private endpoint, the Azure Container Registry for the workspace must be configured for __Premium__ tier. For more information, see [Azure Container Registry service tiers](../container-registry/container-registry-skus.md).

* The Azure Container Registry and Azure Storage Account must be in the same Azure Resource Group as the workspace.

* If you want to use a [user-assigned managed identity](../active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities.md?pivots=identity-mi-methods-azp) to create and manage online endpoints and online deployments, the identity should have the proper permissions. For details about the required permissions, see [Set up service authentication](./how-to-identity-based-service-authentication.md#workspace). For example, you need to assign the proper RBAC permission for Azure Key Vault on the identity.

> [!IMPORTANT]
> The end-to-end example in this article comes from the files in the __azureml-examples__ GitHub repository. To clone the samples repository and switch to the repository's `cli/` directory, use the following commands: 
