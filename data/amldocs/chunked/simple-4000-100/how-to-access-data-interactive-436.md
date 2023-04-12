
> [!TIP]
> Rather than remember the datastore URI format, you can copy-and-paste the datastore URI from the Studio UI by following these steps:
> 1. Select **Data** from the left-hand menu followed by the **Datastores** tab. 
> 1. Select your datastore name and then **Browse**. 
> 1. Find the file/folder you want to read into pandas, select the elipsis (**...**) next to it. Select from the menu **Copy URI**. You can select the **Datastore URI** to copy into your notebook/script.
> :::image type="content" source="media/how-to-access-data-ci/datastore_uri_copy.png" alt-text="Screenshot highlighting the copy of the datastore URI.":::

##### [HTTP Server](#tab/http)
```python
import mltable

path = {
    'file': 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv'
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```


#### Read parquet files in a folder
The example code below shows how `mltable` can use [glob](https://wikipedia.org/wiki/Glob_(programming)) patterns - such as wildcards - to ensure only the parquet files are read. 

##### [ADLS gen2](#tab/adls)

Update the placeholders (`<>`) in the code snippet with your details.

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

Update the placeholders (`<>`) in the code snippet with your details.

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

Update the placeholders (`<>`) in the code snippet with your details.

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
> Rather than remember the datastore URI format, you can copy-and-paste the datastore URI from the Studio UI by following these steps:
> 1. Select **Data** from the left-hand menu followed by the **Datastores** tab. 
> 1. Select your datastore name and then **Browse**. 
> 1. Find the file/folder you want to read into pandas, select the elipsis (**...**) next to it. Select from the menu **Copy URI**. You can select the **Datastore URI** to copy into your notebook/script.
> :::image type="content" source="media/how-to-access-data-ci/datastore_uri_copy.png" alt-text="Screenshot highlighting the copy of the datastore URI.":::

##### [HTTP Server](#tab/http)

Update the placeholders (`<>`) in the code snippet with your details.

> [!IMPORTANT]
> To glob the pattern on a public HTTP server, there must be access at the **folder** level.

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
In this section, you'll learn how to access your Azure ML data assets into pandas.

#### Table asset

If you've previously created a Table asset in Azure ML (an `mltable`, or a V1 `TabularDataset`), you can load that into pandas using:

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

If you've registered a File asset that you want to read into Pandas data frame - for example, a CSV file - you can achieve this using:

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
