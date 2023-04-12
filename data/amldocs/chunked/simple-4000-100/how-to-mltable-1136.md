

#### Read parquet files in a folder
This example code shows how `mltable` can use [glob](https://wikipedia.org/wiki/Glob_(programming)) patterns - such as wildcards - to ensure that only the parquet files are read.

##### [ADLS gen2](#tab/adls)

Update the placeholders (`<>`) in the code snippet with your specific information.

```python
import mltable

path = {
    'pattern': 'abfss://<filesystem>@<account>.dfs.core.windows.net/<folder>/*.parquet'
}

tbl = mltable.from_parquet_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

##### [Blob storage](#tab/blob)

Update the placeholders (`<>`) in the code snippet with your specific information.

```python
import mltable

path = {
    'pattern': 'wasbs://<container>@<account>.blob.core.windows.net/<folder>/*.parquet'
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

##### [Azure ML Datastore](#tab/datastore)

Update the placeholders (`<>`) in the code snippet with your specific information.

```python
import mltable

path = {
    'pattern': 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<wsname>/datastores/<name>/paths/<folder>/*.parquet'
}

tbl = mltable.from_parquet_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

> [!TIP]
> To avoid the need to remember the datastore URI format, copy-and-paste the datastore URI from the Studio UI with these steps:
> 1. Select **Data** from the left-hand menu, then the **Datastores** tab.
> 1. Select your datastore name, and then **Browse**.
> 1. Find the file/folder you want to read into Pandas, and select the ellipsis (**...**) next to it. Select from the **Copy URI** menu. You can select the **Datastore URI** to copy into your notebook/script.
> :::image type="content" source="media/how-to-access-data-ci/datastore_uri_copy.png" alt-text="Screenshot highlighting the copy of the datastore URI.":::

##### [HTTP Server](#tab/http)

Update the placeholders (`<>`) in the code snippet with your specific information.

> [!IMPORTANT]
> Access at the **folder** level is required to glob the pattern on a public HTTP server.

```python
import mltable

path = {
    'pattern': '<https_address>/<folder>/*.parquet'
}

tbl = mltable.from_parquet_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```


### Reading data assets
In this section, you'll learn how to access your Azure ML data assets into Pandas.

#### Table asset

Earlier, if you created a Table asset in Azure ML (an `mltable`, or a V1 `TabularDataset`), you can load that asset into Pandas with:

```python
import mltable
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset = ml_client.data.get(name="<name_of_asset>", version="<version>")

tbl = mltable.load(f'azureml:/{data_asset.id}')
df = tbl.to_pandas_dataframe()
df.head()
```

#### File asset

If you registered a File asset that you want to read into Pandas data frame - for example, a CSV file - use this code:

```python
import mltable
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset = ml_client.data.get(name="<name_of_asset>", version="<version>")

path = {
    'file': data_asset.path
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

#### Folder asset

If you registered a Folder asset (`uri_folder` or a V1 `FileDataset`) that you want to read into Pandas data frame - for example, a folder containing CSV file - use this code:

```python
import mltable
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset = ml_client.data.get(name="<name_of_asset>", version="<version>")

path = {
    'folder': data_asset.path
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```
