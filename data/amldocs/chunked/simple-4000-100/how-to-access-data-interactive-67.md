
> [!TIP]
> Rather than remember the datastore URI format, you can copy-and-paste the datastore URI from the Studio UI by following these steps:
> 1. Select **Data** from the left-hand menu followed by the **Datastores** tab. 
> 1. Select your datastore name and then **Browse**. 
> 1. Find the file/folder you want to read into pandas, select the elipsis (**...**) next to it. Select from the menu **Copy URI**. You can select the **Datastore URI** to copy into your notebook/script.
> :::image type="content" source="media/how-to-access-data-ci/datastore_uri_copy.png" alt-text="Screenshot highlighting the copy of the datastore URI.":::

You can also instantiate an Azure ML filesystem and do filesystem-like commands like `ls`, `glob`, `exists`, `open`, etc. The `open()` method will return a file-like object, which can be passed to any other library that expects to work with python files, or used by your own code as you would a normal python file object. These file-like objects respect the use of `with` contexts, for example:

```python
from azureml.fsspec import AzureMachineLearningFileSystem

# instantiate file system using datastore URI
fs = AzureMachineLearningFileSystem('azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>')

# list files in the path
fs.ls()
# output example:
# /datastore_name/folder/file1.csv
# /datastore_name/folder/file2.csv

# use an open context
with fs.open('/datastore_name/folder/file1.csv') as f:
    # do some process
    process_file(f)
```

### Examples

In this section we provide some examples of how to use Filesystem spec, for some common scenarios.

#### Read a single CSV file into pandas

If you have a *single* CSV file, then as outlined above you can read that into pandas with:

```python
import pandas as pd

df = pd.read_csv("azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/<filename>.csv")
```

#### Read a folder of CSV files into pandas

The Pandas `read_csv()` method doesn't support reading a folder of CSV files. You need to glob csv paths and concatenate them to a data frame using Pandas `concat()` method. The code below demonstrates how to achieve this concatenation with the Azure ML filesystem:

```python
import pandas as pd
from azureml.fsspec import AzureMachineLearningFileSystem

# define the URI - update <> placeholders
uri = 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/*.csv'

# create the filesystem
fs = AzureMachineLearningFileSystem(uri)

# append csv files in folder to a list
dflist = []
for path in fs.ls():
    with fs.open(path) as f:
        dflist.append(pd.read_csv(f))

# concatenate data frames
df = pd.concat(dflist)
df.head()
```

#### Reading CSV files into Dask

Below is an example of reading a CSV file into a Dask data frame:

```python
import dask.dd as dd

df = dd.read_csv("azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/<filename>.csv")
df.head()
``` 

#### Read a folder of parquet files into pandas
Parquet files are typically written to a folder as part of an ETL process, which can emit files pertaining to the ETL such as progress, commits, etc. Below is an example of files created from an ETL process (files beginning with `_`) to produce a parquet file of data.

:::image type="content" source="media/how-to-access-data-ci/parquet-auxillary.png" alt-text="Screenshot showing the parquet etl process.":::

In these scenarios, you'll only want to read the parquet files in the folder and ignore the ETL process files. The code below shows how you can use glob patterns to read only parquet files in a folder:

```python
import pandas as pd
from azureml.fsspec import AzureMachineLearningFileSystem

# define the URI - update <> placeholders
uri = 'azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/*.parquet'

# create the filesystem
fs = AzureMachineLearningFileSystem(uri)

# append csv files in folder to a list
dflist = []
for path in fs.ls():
    with fs.open(path) as f:
        dflist.append(pd.read_parquet(f))

# concatenate data frames
df = pd.concat(dflist)
df.head()
```
