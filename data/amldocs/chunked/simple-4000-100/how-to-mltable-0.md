
# Working with tables in Azure Machine Learning

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning developer platform you use:"]
> * [v2 (current version)](how-to-mltable.md)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Azure ML supports a Table type (`mltable`) that allows for a *blueprint* that defines *how* you would like data files to *materialize* into a Pandas or Spark data frame (rows and columns). Azure ML Tables have these two key features:

1. **An `MLTable` file.** A YAML-based file that defines the materialization blueprint. In the `MLTable`, you can specify:
    - The storage location(s) of the data - local, in the cloud, or on a public http(s) server. Azure ML supports *Globbing* patterns. These locations can specify sets of filenames, with wildcard characters (`*`, `?`, `[abc]`, `[a-z]`).
    - *read transformation* - for example, the file format type (delimited text, Parquet, Delta, json), delimiters, headers, etc.
    - Column type conversions (enforce schema).
    - New column creation, using folder structure information - for example, creation of a year and month column, using the `{year}/{month}` folder structure in the path.
    - *Subsets of data* to materialize - for example, filter rows, keep/drop columns, take random samples.
1. **A fast and efficient engine** to materialize the data into a Pandas or Spark dataframe, according to the blueprint defined in the `MLTable` file. The engine relies on [Rust](https://www.rust-lang.org/). The Rust language is known for high speed and high memory efficiency.

In this article you'll learn:

> [!div class="checklist"]
> - When to use Tables instead of Files or Folders.
> - How to install the MLTable SDK.
> - How to define the materialization blueprint using an `MLTable` file.
> - Examples that show use of Tables in Azure ML.
> - How to use Tables during interactive development (for example, in a notebook).

## Prerequisites

- An Azure subscription. Create a free account before you begin if you don't already have an Azure subscription. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

- The [Azure Machine Learning SDK for Python](https://aka.ms/sdk-v2-install).

- An Azure Machine Learning workspace.


## When to use tables instead of files or folders
Tabular data *doesn't* require Azure ML Tables (`mltable`). You can use Azure ML File (`uri_file`) and Folder (`uri_folder`) types, and provide your own parsing logic, to materialize the data into a Pandas or Spark data frame. In cases where you have a simple CSV file or Parquet folder, you'll find it **easier** to use Azure ML Files/Folders rather than Tables.

### An example of when *not* to use Azure ML tables

Let's assume you have a single CSV file on a public http server, and you'd like to read into Pandas. Two lines of Python code can read the data:

```python
import pandas as pd

pd.read_csv("https://azuremlexamples.blob.core.windows.net/datasets/iris.csv")
```

With Azure ML Tables, you would need to first define the `MLTable` file:

```yml
# /data/iris/MLTable
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable
paths:
    - file: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv

transformations:
    - read_delimited:
        delimiter: ','
        header: all_files_same_headers
```

Before reading into Pandas:

```python
import mltable

# load the folder containing MLTable file
tbl =  mltable.load("/data/iris")
tbl.to_pandas_dataframe()
```

For a simple CSV file, definition of the `MLTable` creates unnecessary extra work. Instead, you'll find Azure ML Tables (`mltable`) much more useful to deal with these scenarios:

- The schema of your data is complex and/or that schema frequently changes.
- You only need a subset of data (for example: a sample of rows or files, specific columns, etc.).
- AutoML jobs that require tabular data.
