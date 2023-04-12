
The consumers can materialize the data into data frame with three lines of Python code:

```python
import mltable

tbl = mltable.load("./my_data")
df = tbl.to_pandas_dataframe()
```

In this scenario, Azure ML Tables, instead of Files or Folders, offers these key benefits:

- Consumers don't need to create their own Python parsing logic to materialize the data into Pandas or Spark.
- One location (the MLTable file) can handle schema changes, to avoid required code changes in multiple locations.

## What is the difference between V2 and V1 APIs?

|Type  |V2 API  |V1 API  |Canonical Scenarios | V2/V1 API Difference
|---------|---------|---------|---------|---------|
|**File**<br>Reference a single file     |    `uri_file`     |   `FileDataset`      |       Read/write a single file - the file can have any format.   |  A type new to V2 APIs. In V1 APIs, files always mapped to a folder on the compute target filesystem; this mapping required an `os.path.join`. In V2 APIs, the single file is mapped. This way, you can refer to that location in your code.   |
|**Folder**<br> Reference a single folder     |     `uri_folder`    |   `FileDataset`      |  You must read/write a folder of parquet/CSV files into Pandas/Spark.<br><br>Deep-learning with images, text, audio, video files located in a folder.       | In V1 APIs, `FileDataset` had an associated engine that could take a file sample from a folder. In V2 APIs, a Folder is a simple mapping to the compute target filesystem. |
|**Table**<br> Reference a data table    |   `mltable`      |     `TabularDataset`    |    You have a complex schema subject to frequent changes, or you need a subset of large tabular data.<br><br>AutoML with Tables.     | In V1 APIs, the Azure ML back-end stored the data materialization blueprint. This storage location meant that `TabularDataset` only worked if you had an Azure ML workspace. `mltable` stores the data materialization blueprint in *your* storage. This storage location means you can use it *disconnected to Azure ML* - for example, local, on-premises. In V2 APIs, you'll find it easier to transition from local to remote jobs. |

## Installing the `mltable` library
MLTable is pre-installed on Compute Instance, AzureML Spark, and DSVM. You can install `mltable` Python library with this code:

```bash
pip install mltable
```

> [!NOTE]
> - MLTable is a separate library from `azure-ai-ml`.
> - If you use a Compute Instance/Spark/DSVM, we recommend that you keep the package up-to-date with `pip install -U mltable`
> - MLTable can be used totally ‘disconnected’ to Azure ML (and the cloud). You can use MLTable anywhere you can get a Python session – for example: locally, Cloud VM, Databricks, Synapse, On-prem server, etc.

## The `MLTable` file

The `MLTable` file is a YAML-based file that defines the materialization blueprint. In the `MLTable` file, you can specify:

- The data storage location(s), which can be local, in the cloud, or on a public http(s) server. *Globbing* patterns are also supported. This way, wildcard characters (`*`, `?`, `[abc]`, `[a-z]`) can specify sets of filenames.
- *read transformation* - for example, the file format type (delimited text, Parquet, Delta, json), delimiters, headers, etc.
- Column type conversions (enforce schema).
- New columns, using folder structure information - for example, create a year and month column using the `{year}/{month}` folder structure in the path.
- *Subsets of data* to materialize - for example, filter rows, keep/drop columns, take random samples.

### File Naming
While the `MLTable` file contains YAML, it needs the **exact** `MLTable` name (no filename extensions).

> [!CAUTION]
> Filename extensions of **yaml** or **yml**, as seen in `MLTable.yaml` or `MLTable.yml`, will cause an `MLTable file not found` error when loading. The MLTable file needs the exact `MLTable` name.

### Authoring `MLTable` files

You can author `MLTable` files with the Python SDK. You can also directly author the MLTable file in an IDE (like VSCode). This example shows an MLTable file authored with the SDK:
