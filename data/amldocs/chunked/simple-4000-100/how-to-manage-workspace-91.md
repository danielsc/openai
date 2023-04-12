
* **Use existing Azure resources**.  You can also create a workspace that uses existing Azure resources with the Azure resource ID format. Find the specific Azure resource IDs in the Azure portal or with the SDK. This example assumes that the resource group, storage account, key vault, App Insights, and container registry already exist.

```python
# Creating a unique workspace name with current datetime to avoid conflicts
import datetime
from azure.ai.ml.entities import Workspace

basic_ex_workspace_name = "mlw-basicex-prod-" + datetime.datetime.now().strftime(
    "%Y%m%d%H%M"
)

# Change the following variables to resource ids of your existing storage account, key vault, application insights
# and container registry. Here we reuse the ones we just created for the basic workspace
existing_storage_account = (
    # e.g. "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.Storage/storageAccounts/<STORAGE_ACCOUNT>"
    ws_basic.storage_account
)
existing_container_registry = (
    # e.g. "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ContainerRegistry/registries/<CONTAINER_REGISTRY>"
    ws_basic.container_registry
)
existing_key_vault = (
    # e.g. "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.KeyVault/vaults/<KEY_VAULT>"
    ws_basic.key_vault
)
existing_application_insights = (
    # e.g. "/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.insights/components/<APP_INSIGHTS>"
    ws_basic.application_insights
)

ws_with_existing_resources = Workspace(
    name=basic_ex_workspace_name,
    location="eastus",
    display_name="Bring your own dependent resources-example",
    description="This sample specifies a workspace configuration with existing dependent resources",
    storage_account=existing_storage_account,
    container_registry=existing_container_registry,
    key_vault=existing_key_vault,
    application_insights=existing_application_insights,
    tags=dict(purpose="demonstration"),
)

ws_with_existing_resources = ml_client.begin_create_or_update(
    ws_with_existing_resources
).result()

print(ws_with_existing_resources)
```

For more information, see [Workspace SDK reference](/python/api/azure-ai-ml/azure.ai.ml.entities.workspace).

If you have problems in accessing your subscription, see [Set up authentication for Azure Machine Learning resources and workflows](how-to-setup-authentication.md), and the [Authentication in Azure Machine Learning](https://aka.ms/aml-notebook-auth) notebook.

# [Portal](#tab/azure-portal)

1. Sign in to the [Azure portal](https://portal.azure.com/) by using the credentials for your Azure subscription. 

1. In the upper-left corner of Azure portal, select **+ Create a resource**.

    :::image type="content" source="media/how-to-manage-workspace/create-workspace.gif" alt-text="Screenshot show how to create a  workspace in Azure portal.":::

1. Use the search bar to find **Machine Learning**.

1. Select **Machine Learning**.

1. In the **Machine Learning** pane, select **Create** to begin.

1. Provide the following information to configure your new workspace:

   Field|Description 
   ---|---
   Workspace name |Enter a unique name that identifies your workspace. In this example, we use **docs-ws**. Names must be unique across the resource group. Use a name that's easy to recall and to differentiate from workspaces created by others. The workspace name is case-insensitive.
   Subscription |Select the Azure subscription that you want to use.
   Resource group | Use an existing resource group in your subscription or enter a name to create a new resource group. A resource group holds related resources for an Azure solution. In this example, we use **docs-aml**. You need *contributor* or *owner* role to use an existing resource group.  For more information about access, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
