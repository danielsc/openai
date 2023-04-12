|**Table**<br> Reference a data table    |   `mltable`      |     `TabularDataset`     | In V1 APIs, the Azure ML back-end stored the data materialization blueprint. This storage location meant that `TabularDataset` only worked if you had an Azure ML workspace. `mltable` stores the data materialization blueprint in *your* storage. This storage location means you can use it *disconnected to Azure ML* - for example, local, on-premises. In V2 APIs, you'll find it easier to transition from local to remote jobs. Read [Working with tables in Azure Machine Learning](how-to-mltable.md) for more information. |    You have a complex schema subject to frequent changes, or you need a subset of large tabular data.<br><br>AutoML with Tables. |

## Supported paths

When you create an Azure Machine Learning data asset, you must specify a `path` parameter that points to the data asset location. Supported paths include:

|Location  | Examples  |
|---------|---------|
|A path on your local computer    | `./home/username/data/my_data`         |
|A path on a Datastore  |   `azureml://datastores/<data_store_name>/paths/<path>`      |
|A path on a public http(s) server   |  `https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv`    |
|A path on Azure Storage    |(Blob) `wasbs://<containername>@<accountname>.blob.core.windows.net/<path_to_data>/`<br>(ADLS gen2) `abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>` <br>(ADLS gen1) `adl://<accountname>.azuredatalakestore.net/<path_to_data>/` |


> [!NOTE]
> When you create a data asset from a local path, it will automatically upload to the default Azure Machine Learning cloud  datastore.

## Create a File asset

# [Azure CLI](#tab/cli)

Create a `YAML` file `<file-name>.yml`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json

# Supported paths include:
# local: ./<path>/<file>
# blob:  https://<account_name>.blob.core.windows.net/<container_name>/<path>/<file>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/<file>
# Datastore: azureml://datastores/<data_store_name>/paths/<path>/<file>

type: uri_file
name: <name>
description: <description>
path: <uri>
```

Next, execute the following command in the CLI:

```cli
> az ml data create -f <file-name>.yml
```

# [Python SDK](#tab/Python-SDK)
```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Supported paths include:
# local: './<path>/<file>'
# blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>/<file>'
# ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/<file>'
# Datastore: 'azureml://datastores/<data_store_name>/paths/<path>/<file>'
my_path = '<path>'

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FILE,
    description="<description>",
    name="<name>",
    version="<version>"
)

ml_client.data.create_or_update(my_data)
```
# [Studio](#tab/Studio)

These steps explain how to create a File data asset in the Azure Machine Learning studio:

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com)

1. Under **Assets** in the left navigation, select **Data**. On the Data assets tab, select **Create**
:::image type="content" source="./media/how-to-create-data-assets/data-assets-create.png" alt-text="Screenshot highlights Create in the Data assets tab.":::

1. Give your data asset a name and an optional description. Then, select the **File (uri_file)** option under Type.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset-file-type.png" alt-text="In this screenshot, choose File (uri folder) in the Type dropdown.":::

1. You have a few options for your data source. If you already have the path to the file you want to upload, choose **From a URI**. For a file already stored in Azure, choose **From Azure storage**. To upload your file from your local drive, choose **From local files**.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset.png" alt-text="This screenshot shows data asset source choices.":::
