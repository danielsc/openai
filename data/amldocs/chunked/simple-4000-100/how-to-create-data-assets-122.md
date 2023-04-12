:::image type="content" source="./media/how-to-create-data-assets/create-data-asset.png" alt-text="This screenshot shows data asset source choices.":::

1. Follow the steps; once you reach the Review step, select **Create** on the last page

## Create a Folder asset

# [Azure CLI](#tab/cli)

Create a `YAML` file (`<file-name>.yml`):

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json

# Supported paths include:
# local: ./<path>
# blob:  https://<account_name>.blob.core.windows.net/<container_name>/<path>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/
# Datastore: azureml://datastores/<data_store_name>/paths/<path>
type: uri_folder
name: <name_of_data>
description: <description goes here>
path: <path>
```

Next, use the CLI to create the data asset:

```azurecli
az ml data create -f <file-name>.yml
```

# [Python SDK](#tab/Python-SDK)

Use this Python Code to create a data asset in Azure Machine Learning:

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Supported paths include:
# local: './<path>'
# blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>'
# ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/'
# Datastore: 'azureml://datastores/<data_store_name>/paths/<path>'

my_path = '<path>'

my_data = Data(
    path=my_path,
    type=AssetTypes.URI_FOLDER,
    description="<description>",
    name="<name>",
    version='<version>'
)

ml_client.data.create_or_update(my_data)
```

# [Studio](#tab/Studio)

Use these steps to create a Folder data asset in the Azure Machine Learning studio:

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com)

1. Under **Assets** in the left navigation, select **Data**. On the Data assets tab, select **Create**
:::image type="content" source="./media/how-to-create-data-assets/data-assets-create.png" alt-text="Screenshot highlights Create in the Data assets tab.":::

1. Give your data asset a name and optional description. Then, select the **Folder (uri_folder)** option under Type, if it isn't already selected.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset-folder-type.png" alt-text="In this screenshot, choose Folder (uri folder) in the Type dropdown.":::

1. You have a few options for your data source. If you already have the path to the folder you want to upload, choose **From a URI**. For a folder already stored in Azure, choose **From Azure storage**. To upload a folder from your local drive, choose **From local files**.
:::image type="content" source="./media/how-to-create-data-assets/create-data-asset.png" alt-text="This screenshot shows data asset source choices.":::

1. Follow the steps, once you reach the Review step, select **Create** on the last page.

## Create a Table asset

You must create a valid `MLTable` file before you create the asset. Read [Authoring `MLTable` files](how-to-mltable.md#authoring-mltable-files) to learn more about `MLTable` file and artifact creation.

> [!IMPORTANT]
> The `path` should be a *folder* that contains a valid `MLTable` file.

# [Azure CLI](#tab/cli)

Create a `YAML` file (`<file-name>.yml`):

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json

# path must point to **folder** containing MLTable artifact (MLTable file + data
# Supported paths include:
# local: ./<path>
# blob:  https://<account_name>.blob.core.windows.net/<container_name>/<path>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/
# Datastore: azureml://datastores/<data_store_name>/paths/<path>

type: mltable
name: <name_of_data>
description: <description goes here>
path: <path>
```

Next, create the data asset using the CLI:

```azurecli
az ml data create -f <file-name>.yml
```

# [Python SDK](#tab/Python-SDK)

You can create a data asset in Azure Machine Learning using the following Python Code:

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# my_path must point to folder containing MLTable artifact (MLTable file + data
# Supported paths include:
# local: './<path>'
# blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>'
# ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/'
# Datastore: 'azureml://datastores/<data_store_name>/paths/<path>'

my_path = '<path>'

my_data = Data(
    path=my_path,
    type=AssetTypes.MLTABLE,
    description="<description>",
    name="<name>",
    version='<version>'
)

ml_client.data.create_or_update(my_data)
```
