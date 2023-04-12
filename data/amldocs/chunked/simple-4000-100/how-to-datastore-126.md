
# [Python SDK: SAS](#tab/sdk-SAS)

```python
from azure.ai.ml.entities import AzureBlobDatastore
from azure.ai.ml.entities import SasTokenConfiguration 
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

store = AzureBlobDatastore(
    name="blob_sas_example",
    description="Datastore pointing to a blob container using SAS token.",
    account_name="mytestblobstore",
    container_name="data-container",
    credentials=SasTokenConfiguration(
        sas_token= "?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX"
    ),
)

ml_client.create_or_update(store)
```

## Create an Azure Data Lake Gen2 datastore

# [CLI: Identity-based access](#tab/cli-adls-identity-based-access)
Create the following YAML file (updating the values):

```yaml
# my_adls_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureDataLakeGen2.schema.json
name: adls_gen2_credless_example
type: azure_data_lake_gen2
description: Credential-less datastore pointing to an Azure Data Lake Storage Gen2.
account_name: mytestdatalakegen2
filesystem: my-gen2-container
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_adls_datastore.yml
```

# [CLI: Service principal](#tab/cli-adls-sp)
Create the following YAML file (updating the values):

```yaml
# my_adls_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureDataLakeGen2.schema.json
name: adls_gen2_example
type: azure_data_lake_gen2
description: Datastore pointing to an Azure Data Lake Storage Gen2.
account_name: mytestdatalakegen2
filesystem: my-gen2-container
credentials:
  tenant_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  client_id: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
  client_secret: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_adls_datastore.yml
```

# [Python SDK: Identity-based access](#tab/sdk-adls-identity-access)

```python
from azure.ai.ml.entities import AzureDataLakeGen2Datastore
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

store = AzureDataLakeGen2Datastore(
    name="",
    description="",
    account_name="",
    filesystem=""
)

ml_client.create_or_update(store)
```

# [Python SDK: Service principal](#tab/sdk-adls-sp)

```python
from azure.ai.ml.entities import AzureDataLakeGen2Datastore
from azure.ai.ml.entities._datastore.credentials import ServicePrincipalCredentials

from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

store = AzureDataLakeGen2Datastore(
    name="adls_gen2_example",
    description="Datastore pointing to an Azure Data Lake Storage Gen2.",
    account_name="mytestdatalakegen2",
    filesystem="my-gen2-container",
     credentials=ServicePrincipalCredentials(
        tenant_id= "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        client_id= "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
        client_secret= "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    ),
)

ml_client.create_or_update(store)
```

## Create an Azure Files datastore

# [CLI: Account key](#tab/cli-azfiles-account-key)
Create the following YAML file (updating the values):

```yaml
# my_files_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureFile.schema.json
name: file_example
type: azure_file
description: Datastore pointing to an Azure File Share.
account_name: mytestfilestore
file_share_name: my-share
credentials:
  account_key: XxXxXxXXXXXXXxXxXxxXxxXXXXXXXXxXxxXXxXXXXXXXxxxXxXXxXXXXXxXXxXXXxXxXxxxXXxXXxXXXXXxXxxXX
```

Create the Azure Machine Learning datastore in the CLI:

```azurecli
az ml datastore create --file my_files_datastore.yml
```

# [CLI: SAS](#tab/cli-azfiles-sas)
Create the following YAML file (updating the values):

```yaml
# my_files_datastore.yml
$schema: https://azuremlschemas.azureedge.net/latest/azureFile.schema.json
name: file_sas_example
type: azure_file
description: Datastore pointing to an Azure File Share using SAS token.
account_name: mytestfilestore
file_share_name: my-share
credentials:
  sas_token: ?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX
```
