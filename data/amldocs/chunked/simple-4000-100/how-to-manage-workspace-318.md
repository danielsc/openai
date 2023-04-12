* **From parameters**: There's no need to have a config.json file available if you use this approach.
    
```python
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Workspace
from azure.identity import DefaultAzureCredential

ws = MLClient(
    DefaultAzureCredential(),
    subscription_id="<SUBSCRIPTION_ID>",
    resource_group_name="<RESOURCE_GROUP>",
    workspace_name="<AML_WORKSPACE_NAME>",
)
print(ws)
```

If you have problems in accessing your subscription, see [Set up authentication for Azure Machine Learning resources and workflows](how-to-setup-authentication.md), and the [Authentication in Azure Machine Learning](https://aka.ms/aml-notebook-auth) notebook.

## Find a workspace

See a list of all the workspaces you can use.  
You can also search for workspace inside studio.  See [Search for Azure Machine Learning assets (preview)](how-to-search-assets.md).


# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml import MLClient
from azure.ai.ml.entities import Workspace
from azure.identity import DefaultAzureCredential

# Enter details of your subscription
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"

my_ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group)
```
```python
for ws in my_ml_client.workspaces.list():
    print(ws.name, ":", ws.location, ":", ws.description)
```

To get details of a specific workspace:

```python
ws = my_ml_client.workspaces.get("<AML_WORKSPACE_NAME>")
# uncomment this line after providing a workspace name above
# print(ws.location,":", ws.resource_group)
```


# [Portal](#tab/azure-portal)

1. Sign in to the [Azure portal](https://portal.azure.com/).

1. In the top search field, type **Machine Learning**.  

1. Select **Machine Learning**.

   ![Search for Azure Machine Learning workspace](./media/how-to-manage-workspace/find-workspaces.png)

1. Look through the list of workspaces found. You can filter based on subscription, resource groups, and locations.  

1. Select a workspace to display its properties.



## Delete a workspace

When you no longer need a workspace, delete it.  

[!INCLUDE [machine-learning-delete-workspace](../../includes/machine-learning-delete-workspace.md)]

If you accidentally deleted your workspace, you may still be able to retrieve your notebooks. For details, see [Failover for business continuity and disaster recovery](./how-to-high-availability-machine-learning.md#workspace-deletion).

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
ml_client.workspaces.begin_delete(name=ws_basic.name, delete_dependent_resources=True)
```

The default action isn't to delete resources associated with the workspace, that is, container registry, storage account, key vault, and application insights.  Set `delete_dependent_resources` to True to delete these resources as well.

# [Portal](#tab/azure-portal)

In the [Azure portal](https://portal.azure.com/), select **Delete**  at the top of the workspace you wish to delete.

:::image type="content" source="./media/how-to-manage-workspace/delete-workspace.png" alt-text="Delete workspace":::


## Clean up resources

[!INCLUDE [aml-delete-resource-group](../../includes/aml-delete-resource-group.md)]

## Troubleshooting

* **Supported browsers in Azure Machine Learning studio**: We recommend that you use the most up-to-date browser that's compatible with your operating system. The following browsers are supported:
  * Microsoft Edge (The new Microsoft Edge, latest version. Not Microsoft Edge legacy)
  * Safari (latest version, Mac only)
  * Chrome (latest version)
  * Firefox (latest version)

* **Azure portal**: 
  * If you go directly to your workspace from a share link from the SDK or the Azure portal, you can't view the standard **Overview** page that has subscription information in the extension. In this scenario, you also can't switch to another workspace. To view another workspace, go directly to [Azure Machine Learning studio](https://ml.azure.com) and search for the workspace name.
