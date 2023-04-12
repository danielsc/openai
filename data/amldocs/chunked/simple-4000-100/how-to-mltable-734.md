

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


### Parquet

This example assumes that you have a folder of parquet files stored in the following Azure Data Lake location:

- `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/`

You'd like to take a 20% random sample of rows from all the parquet files in the folder.


# [CLI](#tab/cli)
Create an `MLTable` file in the `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/` location:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable

paths:
  - pattern: ./*.parquet

transformations:
  - read_parquet:
        include_path_column: false 
  - take_random_sample:
        probability: 0.20
        seed: 132
```

If you don't already use [Option 1: Directly author `MLTable` in cloud storage with VSCode](#option-1-directly-author-mltable-in-cloud-storage-with-vscode), then you can upload your `MLTable` file with `azcopy`:

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
    'pattern': './*.parquet'
}

tbl = mltable.from_parquet_files(paths=[my_path])
tbl = tbl.take_random_sample(probability=0.20, seed=132)

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

You'll need to ensure the `mltable` package is installed on the Spark cluster. For more information, read:
- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Quickstart: Apache Spark jobs in Azure Machine Learning (preview)](quickstart-spark-jobs.md).

```python
# the URI points to the folder containing the MLTable file.
uri = "abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>"

df = spark.read.mltable(uri)
df.show()
```
