
# Manage Azure Machine Learning workspaces in the portal or with the Python SDK (v2)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK you are using:"]
> * [v1](v1/how-to-manage-workspace.md)
> * [v2 (current)](how-to-manage-workspace.md)

In this article, you create, view, and delete [**Azure Machine Learning workspaces**](concept-workspace.md) for [Azure Machine Learning](overview-what-is-azure-machine-learning.md), using the [Azure portal](https://portal.azure.com) or the [SDK for Python](https://aka.ms/sdk-v2-install).  

As your needs change or requirements for automation increase you can also manage workspaces [using the CLI](how-to-manage-workspace-cli.md), [Azure PowerShell](how-to-manage-workspace-powershell.md),  or [via the VS Code extension](how-to-setup-vs-code.md).

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.
* If using the Python SDK: 
   1. [Install the SDK v2](https://aka.ms/sdk-v2-install).
   1. Provide your subscription details

```python
# Enter details of your subscription
subscription_id = "<SUBSCRIPTION_ID>"
resource_group = "<RESOURCE_GROUP>"
```

   1. Get a handle to the subscription.  `ml_client` will be used in all the Python code in this article.

```python
# get a handle to the subscription

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group)
```
      
        * (Optional) If you have multiple accounts, add the tenant ID of the Azure Active Directory you wish to use into the `DefaultAzureCredential`. Find your tenant ID from the [Azure portal](https://portal.azure.com) under **Azure Active Directory, External Identities**.
                
            ```python
            DefaultAzureCredential(interactive_browser_tenant_id="<TENANT_ID>")
            ```
                
        * (Optional) If you're working on a [sovereign cloud](reference-machine-learning-cloud-parity.md)**, specify the sovereign cloud to authenticate with into the `DefaultAzureCredential`..
                
            ```python
            from azure.identity import AzureAuthorityHosts
            DefaultAzureCredential(authority=AzureAuthorityHosts.AZURE_GOVERNMENT))
            ```

## Limitations

[!INCLUDE [register-namespace](../../includes/machine-learning-register-namespace.md)]

* By default, creating a workspace also creates an Azure Container Registry (ACR).  Since ACR doesn't currently support unicode characters in resource group names, use a resource group that doesn't contain these characters.

* Azure Machine Learning doesn't support hierarchical namespace (Azure Data Lake Storage Gen2 feature) for the workspace's default storage account.

[!INCLUDE [application-insight](../../includes/machine-learning-application-insight.md)]

## Create a workspace

You can create a workspace [directly in Azure Machine Learning studio](./quickstart-create-resources.md#create-the-workspace), with limited options available. Or use one of the methods below for more control of options.

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

* **Default specification.** By default, dependent resources and the resource group will be created automatically. This code creates a workspace named `myworkspace` and a resource group named `myresourcegroup` in `eastus2`.
    
```python
# Creating a unique workspace name with current datetime to avoid conflicts
from azure.ai.ml.entities import Workspace
import datetime

basic_workspace_name = "mlw-basic-prod-" + datetime.datetime.now().strftime(
    "%Y%m%d%H%M"
)

ws_basic = Workspace(
    name=basic_workspace_name,
    location="eastus",
    display_name="Basic workspace-example",
    description="This example shows how to create a basic workspace",
    hbi_workspace=False,
    tags=dict(purpose="demo"),
)

ws_basic = ml_client.workspaces.begin_create(ws_basic).result()
print(ws_basic)
```
