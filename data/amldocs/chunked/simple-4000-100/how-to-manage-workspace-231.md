1. When you're finished configuring networking, you can select __Review + Create__, or advance to the optional __Advanced__ configuration.


### Advanced

By default, metadata for the workspace is stored in an Azure Cosmos DB instance that Microsoft maintains. This data is encrypted using Microsoft-managed keys.

To limit the data that Microsoft collects on your workspace, select __High business impact workspace__ in the portal, or set `hbi_workspace=true ` in Python. For more information on this setting, see [Encryption at rest](concept-data-encryption.md#encryption-at-rest).

> [!IMPORTANT]	
> Selecting high business impact can only be done when creating a workspace. You cannot change this setting after workspace creation.	

#### Use your own data encryption key

You can provide your own key for data encryption. Doing so creates the Azure Cosmos DB instance that stores metadata in your Azure subscription. For more information, see [Customer-managed keys](concept-customer-managed-keys.md).


Use the following steps to provide your own key:

> [!IMPORTANT]	
> Before following these steps, you must first perform the following actions:	
>
> Follow the steps in [Configure customer-managed keys](how-to-setup-customer-managed-keys.md) to:
> * Register the Azure Cosmos DB provider
> * Create and configure an Azure Key Vault
> * Generate a key

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python

from azure.ai.ml.entities import Workspace, CustomerManagedKey

# specify the workspace details
ws = Workspace(
    name="my_workspace",
    location="eastus",
    display_name="My workspace",
    description="This example shows how to create a workspace",
    customer_managed_key=CustomerManagedKey(
        key_vault="/subscriptions/<SUBSCRIPTION_ID>/resourcegroups/<RESOURCE_GROUP>/providers/microsoft.keyvault/vaults/<VAULT_NAME>"
        key_uri="<KEY-IDENTIFIER>"
    )
    tags=dict(purpose="demo")
)

ml_client.workspaces.begin_create(ws)
```

# [Portal](#tab/azure-portal)

1. Select __Customer-managed keys__, and then select __Click to select key__.

    :::image type="content" source="media/how-to-manage-workspace/advanced-workspace.png" alt-text="Customer-managed keys":::

1. On the __Select key from Azure Key Vault__ form, select an existing Azure Key Vault, a key that it contains, and the version of the key. This key is used to encrypt the data stored in Azure Cosmos DB. Finally, use the __Select__ button to use this key.

   :::image type="content" source="media/how-to-manage-workspace/select-key-vault.png" alt-text="Select the key":::


### Download a configuration file

If you'll be running your code on a [compute instance](quickstart-create-resources.md), skip this step.  The compute instance will create and store copy of this file for you.

If you plan to use code on your local environment that references this workspace, download the file:
1. Select your workspace in [Azure studio](https://ml.azure.com)
1. At the top right, select the workspace name, then select  **Download config.json**

   ![Download config.json](./media/how-to-manage-workspace/configure.png)

Place the file into  the directory structure with your Python scripts or Jupyter Notebooks. It can be in the same directory, a subdirectory named *.azureml*, or in a parent directory. When you create a compute instance, this file is added to the correct directory on the VM for you.

## Connect to a workspace

When running machine learning tasks using the SDK, you require a MLClient object that specifies the connection to your workspace. You can create an `MLClient` object from parameters, or with a configuration file.

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

* **With a configuration file:** This code will read the contents of the configuration file to find your workspace.  You'll get a prompt to sign in if you aren't already authenticated.

    ```python
    from azure.ai.ml import MLClient
    
    # read the config from the current directory
    ws_from_config = MLClient.from_config()
    ```
