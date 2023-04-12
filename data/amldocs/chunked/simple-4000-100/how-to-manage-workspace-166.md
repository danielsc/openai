   Resource group | Use an existing resource group in your subscription or enter a name to create a new resource group. A resource group holds related resources for an Azure solution. In this example, we use **docs-aml**. You need *contributor* or *owner* role to use an existing resource group.  For more information about access, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
   Region | Select the Azure region closest to your users and the data resources to create your workspace.
   | Storage account | The default storage account for the workspace. By default, a new one is created. |
   | Key Vault | The Azure Key Vault used by the workspace. By default, a new one is created. |
   | Application Insights | The application insights instance for the workspace. By default, a new one is created. |
   | Container Registry | The Azure Container Registry for the workspace. By default, a new one isn't_ initially created for the workspace. Instead, it's created once you need it when creating a Docker image during training or deployment. |

   :::image type="content" source="media/how-to-manage-workspace/create-workspace-form.png" alt-text="Configure your workspace.":::

1. When you're finished configuring the workspace, select **Review + Create**. Optionally, use the [Networking](#networking) and [Advanced](#advanced) sections to configure more settings for the workspace.

1. Review the settings and make any other changes or corrections. When you're satisfied with the settings, select **Create**.

   > [!Warning] 
   > It can take several minutes to create your workspace in the cloud.

   When the process is finished, a deployment success message appears. 
 
 1. To view the new workspace, select **Go to resource**.
 

### Networking	

> [!IMPORTANT]	
> For more information on using a private endpoint and virtual network with your workspace, see [Network isolation and privacy](how-to-network-security-overview.md).


# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# Creating a unique workspace name with current datetime to avoid conflicts
import datetime
from azure.ai.ml.entities import Workspace

basic_private_link_workspace_name = (
    "mlw-privatelink-prod-" + datetime.datetime.now().strftime("%Y%m%d%H%M")
)

ws_private = Workspace(
    name=basic_private_link_workspace_name,
    location="eastus",
    display_name="Private Link endpoint workspace-example",
    description="When using private link, you must set the image_build_compute property to a cluster name to use for Docker image environment building. You can also specify whether the workspace should be accessible over the internet.",
    image_build_compute="cpu-compute",
    public_network_access="Disabled",
    tags=dict(purpose="demonstration"),
)

ml_client.workspaces.begin_create(ws_private).result()
```
 
This class requires an existing virtual network.

# [Portal](#tab/azure-portal)

1. The default network configuration is to use a __Public endpoint__, which is accessible on the public internet. To limit access to your workspace to an Azure Virtual Network you've created, you can instead select __Private endpoint__ as the __Connectivity method__, and then use __+ Add__ to configure the endpoint.	

   :::image type="content" source="media/how-to-manage-workspace/select-private-endpoint.png" alt-text="Private endpoint selection":::	

1. On the __Create private endpoint__ form, set the location, name, and virtual network to use. If you'd like to use the endpoint with a Private DNS Zone, select __Integrate with private DNS zone__ and select the zone using the __Private DNS Zone__ field. Select __OK__ to create the endpoint. 	

   :::image type="content" source="media/how-to-manage-workspace/create-private-endpoint.png" alt-text="Private endpoint creation":::	

1. When you're finished configuring networking, you can select __Review + Create__, or advance to the optional __Advanced__ configuration.
