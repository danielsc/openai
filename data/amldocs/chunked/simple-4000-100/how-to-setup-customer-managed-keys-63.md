    * Leave __Enabled__ set to yes.

    Optionally you can set an activation date, expiration date, and tags.

1. Select __Create__ to create the key.

### Allow Azure Cosmos DB to access the key

1. To configure the key vault, select it in the [Azure portal](https://portal.azure.com) and then select __Access polices__ from the left menu.
1. To create permissions for Azure Cosmos DB, select __+ Create__ at the top of the page. Under __Key permissions__, select __Get__, __Unwrap Key__, and __Wrap key__ permissions.
1. Under __Principal__, search for __Azure Cosmos DB__ and then select it. The principal ID for this entry is `a232010e-820c-4083-83bb-3ace5fc29d0b` for all regions other than Azure Government. For Azure Government, the principal ID is `57506a73-e302-42a9-b869-6f12d9ec29e9`.
1. Select __Review + Create__, and then select __Create__.

## Create a workspace that uses a customer-managed key

Create an Azure Machine Learning workspace. When creating the workspace, you must select the __Azure Key Vault__ and the __key__. Depending on how you create the workspace, you specify these resources in different ways:

> [!WARNING]
> The key vault that contains your customer-managed key must be in the same Azure subscription as the workspace.

* __Azure portal__: Select the key vault and key from a dropdown input box when configuring the workspace.
* __SDK, REST API, and Azure Resource Manager templates__: Provide the Azure Resource Manager ID of the key vault and the URL for the key. To get these values, use the [Azure CLI](/cli/azure/install-azure-cli) and the following commands:

    ```azurecli
    # Replace `mykv` with your key vault name.
    # Replace `mykey` with the name of your key.

    # Get the Azure Resource Manager ID of the key vault
    az keyvault show --name mykv --query id
    # Get the URL for the key
    az keyvault key show --vault-name mykv -n mykey --query key.kid
    ```

    The key vault ID value will be similar to `/subscriptions/{GUID}/resourceGroups/{resource-group-name}/providers/Microsoft.KeyVault/vaults/mykv`. The URL for the key will be similar to `https://mykv.vault.azure.net/keys/mykey/{GUID}`.

For examples of creating the workspace with a customer-managed key, see the following articles:

| Creation method | Article |
| ----- | ----- |
| CLI | [Create a workspace with Azure CLI](how-to-manage-workspace-cli.md#customer-managed-key-and-high-business-impact-workspace) |
| Azure portal/</br>Python SDK | [Create and manage a workspace](how-to-manage-workspace.md#use-your-own-data-encryption-key) |
| Azure Resource Manager</br>template | [Create a workspace with a template](how-to-create-workspace-template.md#deploy-an-encrypted-workspace) |
| REST API | [Create, run, and delete Azure ML resources with REST](how-to-manage-rest.md#create-a-workspace-using-customer-managed-encryption-keys) |

Once the workspace has been created, you'll notice that Azure resource group is created in your subscription. This group is in addition to the resource group for your workspace. This resource group will contain the Microsoft-managed resources that your key is used with. The resource group will be named using the formula of `<Azure Machine Learning workspace resource group name><GUID>`. It will contain an Azure Cosmos DB instance, Azure Storage Account, and Azure Cognitive Search.

> [!TIP]
> * The [__Request Units__](../cosmos-db/request-units.md) for the Azure Cosmos DB instance automatically scale as needed.
> * If your Azure Machine Learning workspace uses a private endpoint, this resource group will also contain a Microsoft-managed Azure Virtual Network. This VNet is used to secure communications between the managed services and the workspace. You __cannot provide your own VNet for use with the Microsoft-managed resources__. You also __cannot modify the virtual network__. For example, you cannot change the IP address range that it uses.

> [!IMPORTANT]
> If your subscription does not have enough quota for these services, a failure will occur.
