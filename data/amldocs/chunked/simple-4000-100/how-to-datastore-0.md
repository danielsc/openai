
# Create datastores

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning developer platform you are using:"]
> * [v1](v1/how-to-access-data.md)
> * [v2 (current version)](how-to-datastore.md)

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

In this article, learn how to connect to Azure data storage services with Azure Machine Learning datastores.

## Prerequisites

- An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

- The [Azure Machine Learning SDK for Python](https://aka.ms/sdk-v2-install).

- An Azure Machine Learning workspace.

> [!NOTE]
> Azure Machine Learning datastores do **not** create the underlying storage account resources. Instead, they link an **existing** storage account for Azure Machine Learning use. Azure Machine Learning datastores are not required for this. If you have access to the underlying data, you can use storage URIs directly.


## Create an Azure Blob datastore

# [CLI: Identity-based access](#tab/cli-identity-based-access)
Create the following YAML file (be sure to update the appropriate values):

```yaml
# my_blob_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureBlob.schema.json
name: my_blob_ds # add your datastore name here
type: azure_blob
description: here is a description # add a datastore description here
account_name: my_account_name # add the storage account name here
container_name: my_container_name # add the storage container name here
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_blob_datastore.yml
```

# [CLI: Account key](#tab/cli-account-key)
Create the following YAML file (be sure to update the appropriate values):

```yaml
# my_blob_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureBlob.schema.json
name: blob_example
type: azure_blob
description: Datastore pointing to a blob container.
account_name: mytestblobstore
container_name: data-container
credentials:
  account_key: XXXxxxXXXxXXXXxxXXXXXxXXXXXxXxxXxXXXxXXXxXXxxxXXxxXXXxXxXXXxxXxxXXXXxxxxxXXxxxxxxXXXxXXX
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_blob_datastore.yml
```

# [CLI: SAS](#tab/cli-sas)
Create the following YAML file (be sure to update the appropriate values):

```yaml
# my_blob_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureBlob.schema.json
name: blob_sas_example
type: azure_blob
description: Datastore pointing to a blob container using SAS token.
account_name: mytestblobstore
container_name: data-container
credentials:
  sas_token: ?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_blob_datastore.yml
```

# [Python SDK: Identity-based access](#tab/sdk-identity-based-access)

```python
from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

store = AzureBlobDatastore(
    name="",
    description="",
    account_name="",
    container_name=""
)

ml_client.create_or_update(store)
```

# [Python SDK: Account key](#tab/sdk-account-key)

```python
from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml.entities import AccountKeyConfiguration
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

store = AzureBlobDatastore(
    name="blob_protocol_example",
    description="Datastore pointing to a blob container using https protocol.",
    account_name="mytestblobstore",
    container_name="data-container",
    protocol="https",
    credentials=AccountKeyConfiguration(
        account_key="XXXxxxXXXxXXXXxxXXXXXxXXXXXxXxxXxXXXxXXXxXXxxxXXxxXXXxXxXXXxxXxxXXXXxxxxxXXxxxxxxXXXxXXX"
    ),
)

ml_client.create_or_update(store)
```
