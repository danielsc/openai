
### Supported paths

The `mltable` library supports tabular data reads from different path types:

|Location  | Examples  |
|---------|---------|
|A path on your local computer     | `./home/username/data/my_data`         |
|A path on a public http(s) server    |  `https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv`    |
|A path on Azure Storage    |   `wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>` <br> `abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>`    |
|A long-form Azure ML datastore  |   `azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<wsname>/datastores/<name>/paths/<path>`      |

> [!NOTE]
> `mltable` handles user credential passthrough for paths on Azure Storage and Azure ML datastores. If you do not have permission to the data on the underlying storage, you can't access the data.

### Files, folders and globs

`mltable` supports reading from:

- file(s), for example: `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-csv.csv`
- folder(s), for example `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-folder/`
- [glob](https://wikipedia.org/wiki/Glob_(programming)) pattern(s), for example `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-folder/*.csv`
- Or, a combination of files, folders, globbing patterns

The `mltable` flexibility allows for data materialization into a single dataframe, from a combination of local/cloud storage and combinations of files/folder/globs. For example:

```python
path1 = {
    'file': 'abfss://filesystem@account1.dfs.core.windows.net/my-csv.csv'
}

path2 = {
    'folder': './home/username/data/my_data'
}

path3 = {
    'pattern': 'abfss://filesystem@account2.dfs.core.windows.net/folder/*.csv'
}

tbl = mltable.from_delimited_files(paths=[path1, path2, path3])
```

### Supported file formats
`mltable` supports the following file formats:

- Delimited Text (for example: CSV files): `mltable.from_delimited_files(paths=[path])`
- Parquet: `mltable.from_parquet_files(paths=[path])`
- Delta: `mltable.from_delta_lake(paths=[path])`
- JSON lines format: `mltable.from_json_lines_files(paths=[path])`

### Examples


#### Read a CSV file

##### [ADLS gen2](#tab/adls)

Update the placeholders (`<>`) in the code snippet with your specific information.

```python
import mltable

path = {
    'file': 'abfss://<filesystem>@<account>.dfs.core.windows.net/<folder>/<file_name>.csv'
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

##### [Blob storage](#tab/blob)

Update the placeholders (`<>`) in the code snippet with your specific information.

```python
import mltable

path = {
    'file': 'wasbs://<container>@<account>.blob.core.windows.net/<folder>/<file_name>.csv'
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
    'file': 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<wsname>/datastores/<name>/paths/<folder>/<file>.csv'
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

> [!TIP]
> To avoid the need to remember the datastore URI format, copy-and-paste the datastore URI from the Studio UI with these steps:
> 1. Select **Data** from the left-hand menu, followed by the **Datastores** tab.
> 1. Select your datastore name, and then **Browse**.
> 1. Find the file/folder you want to read into Pandas, and select the ellipsis (**...**) next to it. Select from the menu **Copy URI**. Select the **Datastore URI** to copy into your notebook/script.
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
