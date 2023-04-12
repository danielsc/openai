
    
### Delta Lake

This example assumes that you have a data in an Azure Data Lake Delta format:

- `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/`

This folder will have the following structure

```Text
├── 📁 <folder>
│   ├── 📁 _change_data
│   ├── 📁 _delta_index
│   ├── 📁 _delta_log
│   ├── 📄 part-0000-XXX.parquet
│   ├── 📄 part-0001-XXX.parquet
```

Also, you'd like to read the data as of a specific timestamp: `2022-08-26T00:00:00Z`.

# [CLI](#tab/cli)

Create an `MLTable` file in the `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/` location:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable

paths:
- folder: ./

transformations:
 - read_delta_lake:
      timestamp_as_of: '2022-08-26T00:00:00Z'      
```

If you don't use [Option 1: Directly author `MLTable` in cloud storage with VSCode](#option-1-directly-author-mltable-in-cloud-storage-with-vscode), then you can upload your `MLTable` file with `azcopy`:

```bash
SOURCE=<local_path-to-mltable-file>
DEST=https://<account_name>.blob.core.windows.net/<filesystem>/<folder>
azcopy cp $SOURCE $DEST
```

# [Python](#tab/Python-SDK)

```python
import mltable
from mltable import MLTableHeaders, MLTableFileEncoding
from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential

# update the file name
my_path = {
    'folder': './'
}

tbl = mltable.from_delta_lake(
    paths=[my_path], 
    timestamp_as_of='2022-08-26T00:00:00Z'
)

# save the table to the local file system
local_folder = "local"
tbl.save(local_folder)

# upload the MLTable file to your storage account
storage_account_url = "https://<account_name>.blob.core.windows.net"
container_name = "<filesystem>"
data_folder_on_storage = '<folder>'

# get a blob client using default credential
blob_client = BlobClient(
    credential=DefaultAzureCredential(), 
    account_url=storage_account_url, 
    container_name=container_name,
    blob_name=f'{data_folder_on_storage}/MLTable'
)

# upload to cloud storage
with open(f'{local_folder}/MLTable', "rb") as mltable_file:
    blob_client.upload_blob(mltable_file)

```


Consumers of the data can load the MLTable artifact into Pandas or Spark with:

# [Pandas](#tab/pandas)

```python
import mltable

# the URI points to the folder containing the MLTable file.
uri = "abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>"
tbl = mltable.load(uri)
df = tbl.to_pandas_dataframe()
```

# [Spark](#tab/spark)
[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

You must ensure that the `mltable` package is installed on the Spark cluster. For more information, read:
- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Quickstart: Apache Spark jobs in Azure Machine Learning (preview)](quickstart-spark-jobs.md).

```python
# the URI points to the folder containing the MLTable file.
uri = "abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>"

df = spark.read.mltable(uri)
df.show()
```


## Interactive development with the `mltable` Python SDK 

To access your data during interactive development (for example, in a notebook) without creating an MLTable artifact, use the `mltable` Python SDK. This code sample shows the general format to read data into Pandas, using the `mltable` Python SDK:

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

The `mltable` library supports tabular data reads from different path types:
