
## Materialize data into Pandas using `mltable` library

Another method for accessing data in cloud storage is to use the `mltable` library. The general format for reading data into pandas using `mltable` is:

```python
import mltable

# define a path or folder or pattern
path = {
    'file': '<supported_path>'
    # alternatives
    # 'folder': '<supported_path>'
    # 'pattern': '<supported_path>'
}

# create an mltable from paths
tbl = mltable.from_delimited_files(paths=[path])
# alternatives
# tbl = mltable.from_parquet_files(paths=[path])
# tbl = mltable.from_json_lines_files(paths=[path])
# tbl = mltable.from_delta_lake(paths=[path])

# materialize to pandas
df = tbl.to_pandas_dataframe()
df.head()
```

### Supported paths

You'll notice the `mltable` library supports reading tabular data from different path types:

|Location  | Examples  |
|---------|---------|
|A path on your local computer     | `./home/username/data/my_data`         |
|A path on a public http(s) server    |  `https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv`    |
|A path on Azure Storage     |   `wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>` <br> `abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>`    |
|A long-form Azure ML datastore  |   `azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<wsname>/datastores/<name>/paths/<path>`      |

> [!NOTE]
> `mltable` does user credential passthrough for paths on Azure Storage and Azure ML datastores. If you do not have permission to the data on the underlying storage then you will not be able to access the data.

### Files, folders and globs

`mltable` supports reading from:

- file(s), for example: `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-csv.csv`
- folder(s), for example `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-folder/`
- [glob](https://wikipedia.org/wiki/Glob_(programming)) pattern(s), for example `abfss://<file_system>@<account_name>.dfs.core.windows.net/my-folder/*.csv`
- Or, a combination of files, folders, globbing patterns

The flexibility of `mltable` allows you to materialize data into a single dataframe from a combination of local/cloud storage and combinations of files/folder/globs. For example:

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

Update the placeholders (`<>`) in the code snippet with your details.

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

Update the placeholders (`<>`) in the code snippet with your details.

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

Update the placeholders (`<>`) in the code snippet with your details.

```python
import mltable

path = {
    'file': 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<wsname>/datastores/<name>/paths/<folder>/<file>.csv'
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```
