
# Regenerate storage account access keys
[!INCLUDE [cli v1](../../includes/machine-learning-dev-v1.md)]

Learn how to change the access keys for Azure Storage accounts used by Azure Machine Learning. Azure Machine Learning can use storage accounts to store data or trained models.

For security purposes, you may need to change the access keys for an Azure Storage account. When you regenerate the access key, Azure Machine Learning must be updated to use the new key. Azure Machine Learning may be using the storage account for both model storage and as a datastore.

> [!IMPORTANT]
> Credentials registered with datastores are saved in your Azure Key Vault associated with the workspace. If you have [soft-delete](../key-vault/general/soft-delete-overview.md) enabled for your Key Vault, this article provides instructions for updating credentials. If you unregister the datastore and try to re-register it under the same name, this action will fail. See [Turn on Soft Delete for an existing key vault](../key-vault/general/soft-delete-change.md#turn-on-soft-delete-for-an-existing-key-vault) for how to enable soft delete in this scenario.

## Prerequisites

* An Azure Machine Learning workspace. For more information, see the [Create workspace resources](quickstart-create-resources.md) article.

* The [Azure Machine Learning SDK](/python/api/overview/azure/ml/install).

* The [Azure Machine Learning CLI extension v1](v1/reference-azure-machine-learning-cli.md).

> [!NOTE]
> The code snippets in this document were tested with version 1.0.83 of the Python SDK.

<a id="whattoupdate"></a> 

## What needs to be updated

Storage accounts can be used by the Azure Machine Learning workspace (storing logs, models, snapshots, etc.) and as a datastore. The process to update the workspace is a single Azure CLI command, and can be ran after updating the storage key. The process of updating datastores is more involved, and requires discovering what datastores are currently using the storage account and then re-registering them.

> [!IMPORTANT]
> Update the workspace using the Azure CLI, and the datastores using Python, at the same time. Updating only one or the other is not sufficient, and may cause errors until both are updated.

To discover the storage accounts that are used by your datastores, use the following code:

```python
import azureml.core
from azureml.core import Workspace, Datastore

ws = Workspace.from_config()

default_ds = ws.get_default_datastore()
print("Default datstore: " + default_ds.name + ", storage account name: " +
      default_ds.account_name + ", container name: " + default_ds.container_name)

datastores = ws.datastores
for name, ds in datastores.items():
    if ds.datastore_type == "AzureBlob":
        print("Blob store - datastore name: " + name + ", storage account name: " +
              ds.account_name + ", container name: " + ds.container_name)
    if ds.datastore_type == "AzureFile":
        print("File share - datastore name: " + name + ", storage account name: " +
              ds.account_name + ", container name: " + ds.container_name)
```

This code looks for any registered datastores that use Azure Storage and lists the following information:

* Datastore name: The name of the datastore that the storage account is registered under.
* Storage account name: The name of the Azure Storage account.
* Container: The container in the storage account that is used by this registration.

It also indicates whether the datastore is for an Azure Blob or an Azure File share, as there are different methods to re-register each type of datastore.

If an entry exists for the storage account that you plan on regenerating access keys for, save the datastore name, storage account name, and container name.

## Update the access key

To update Azure Machine Learning to use the new key, use the following steps:

> [!IMPORTANT]
> Perform all steps, updating both the workspace using the CLI, and datastores using Python. Updating only one or the other may cause errors until both are updated.
