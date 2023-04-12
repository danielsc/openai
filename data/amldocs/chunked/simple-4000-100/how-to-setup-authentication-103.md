The easiest way to create an SP and grant access to your workspace is by using the [Azure CLI](/cli/azure/install-azure-cli). To create a service principal and grant it access to your workspace, use the following steps:

> [!NOTE]
> You must be an admin on the subscription to perform all of these steps.

1. Authenticate to your Azure subscription:

    ```azurecli-interactive
    az login
    ```

    If the CLI can open your default browser, it will do so and load a sign-in page. Otherwise, you need to open a browser and follow the instructions on the command line. The instructions involve browsing to [https://aka.ms/devicelogin](https://aka.ms/devicelogin) and entering an authorization code.

    If you have multiple Azure subscriptions, you can use the `az account set -s <subscription name or ID>` command to set the subscription. For more information, see [Use multiple Azure subscriptions](/cli/azure/manage-azure-subscriptions-azure-cli).

    For other methods of authenticating, see [Sign in with Azure CLI](/cli/azure/authenticate-azure-cli).

1. Create the service principal. In the following example, an SP named **ml-auth** is created:

    ```azurecli-interactive
    az ad sp create-for-rbac --sdk-auth --name ml-auth --role Contributor --scopes /subscriptions/<subscription id>
    ```

    The output will be a JSON similar to the following. Take note of the `clientId`, `clientSecret`, and `tenantId` fields, as you'll need them for other steps in this article.

    ```json
    {
        "clientId": "your-client-id",
        "clientSecret": "your-client-secret",
        "subscriptionId": "your-sub-id",
        "tenantId": "your-tenant-id",
        "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
        "resourceManagerEndpointUrl": "https://management.azure.com",
        "activeDirectoryGraphResourceId": "https://graph.windows.net",
        "sqlManagementEndpointUrl": "https://management.core.windows.net:5555",
        "galleryEndpointUrl": "https://gallery.azure.com/",
        "managementEndpointUrl": "https://management.core.windows.net"
    }
    ```

1. Retrieve the details for the service principal by using the `clientId` value returned in the previous step:

    ```azurecli-interactive
    az ad sp show --id your-client-id
    ```

    The following JSON is a simplified example of the output from the command. Take note of the `objectId` field, as you'll need its value for the next step.

    ```json
    {
        "accountEnabled": "True",
        "addIns": [],
        "appDisplayName": "ml-auth",
        ...
        ...
        ...
        "objectId": "your-sp-object-id",
        "objectType": "ServicePrincipal"
    }
    ```

1. To grant access to the workspace and other resources used by Azure Machine Learning, use the information in the following articles:
    * [How to assign roles and actions in AzureML](how-to-assign-roles.md)
    * [How to assign roles in the CLI](../role-based-access-control/role-assignments-cli.md)

    > [!IMPORTANT]
    > Owner access allows the service principal to do virtually any operation in your workspace. It is used in this document to demonstrate how to grant access; in a production environment Microsoft recommends granting the service principal the minimum access needed to perform the role you intend it for. For information on creating a custom role with the access needed for your scenario, see [Manage access to Azure Machine Learning workspace](how-to-assign-roles.md).


## Configure a managed identity

> [!IMPORTANT]
> Managed identity is only supported when using the Azure Machine Learning SDK from an Azure Virtual Machine or with an Azure Machine Learning compute cluster.

### Managed identity with a VM

1. Enable a [system-assigned managed identity for Azure resources on the VM](../active-directory/managed-identities-azure-resources/qs-configure-portal-windows-vm.md#system-assigned-managed-identity).

1. From the [Azure portal](https://portal.azure.com), select your workspace and then select __Access Control (IAM)__.
