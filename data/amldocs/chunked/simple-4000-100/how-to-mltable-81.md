- You only need a subset of data (for example: a sample of rows or files, specific columns, etc.).
- AutoML jobs that require tabular data.

### A motivating example for using Azure ML tables

We explained when to *avoid* Azure ML Tables. Here, we'll see a motivating example of when Azure ML Tables can help your workflow. Imagine a scenario where you have many text files in a folder:

```text
├── my_data
│   ├── file1.txt
│   ├── file1_use_this.txt
│   ├── file2.txt
│   ├── file2_use_this.txt
.
.
.
│   ├── file1000.txt
│   ├── file1000_use_this.txt
```

Each text file has this structure:

```text
store_location date zip_code amount x y z staticvar1 stasticvar2 
Seattle 20/04/2022 12324 123.4 true no 0 2 4 
.
.
.
London 20/04/2022 XX358YY 156 true yes 1 2 4
```

The data has these important characteristics:

- Only files with this suffix `_use_this.txt` have the relevant data. We can ignore other file names that don't have that suffix.
- Date data will have this format `DD/MM/YYYY`. It will not have a string format.
- The x, y, z columns are booleans, not strings. Values in the data can be either `yes`/`no`, `1`/`0`, `true`/`false`.
- The store location is an index that is useful for generation of data subsets.
- The file is encoded in `ascii` format.
- Every file in the folder contains the same header.
- The first million records for zip_code are numeric, but later on, they'll become alphanumeric.
- Some static variables in the data aren't useful for machine learning.

You can materialize the above text files into a data frame using Pandas and an Azure ML Folder (`uri_folder`):

```python
import glob
import datetime
import os
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input_folder", type=str)
args = parser.parse_args()

path = os.path.join(args.input_folder, "*_use_this.txt")
files = glob.glob(path)

# create empty list
dfl = []

# dict of column types
col_types = {
    "zip": str,
    "date": datetime.date,
    "x": bool,
    "y": bool,
    "z": bool
}

# enumerate files into a list of dfs
for f in files:
    csv = pd.read_table(
        path=f,
        delimiter=" ",
        header=0,
        usecols=["store_location", "zip_code", "date", "amount", "x", "y", "z"],
        dtype=col_types,
        encoding='ascii',
        true_values=['yes', '1', 'true'],
        false_values=['no', '0', 'false']
    )
    dfl.append(csv)

# concatenate the list of dataframes
df = pd.concat(dfl)
# set the index column
df.index_columns("store_location")
```

However, problems can occur when

- **The schema changes (for example, a column name changes):** All consumers of the data must independently update their Python code. Other examples can involve type changes, added / removed columns, encoding change, etc.
- **The data size increases** - If the data becomes too large for Pandas to process, all the consumers of the data will need to switch to a more scalable library (PySpark/Dask).

Azure ML Tables allow the data asset creator to define the materialization blueprint in a single file. Then, consumers can then easily materialize the data into a data frame. The consumers can avoid the need to write their own Python parsing logic. The creator of the data asset defines an `MLTable` file:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable

# paths are relative to the location of the MLTable file
paths:
    - pattern: ./*_use_this.txt

traits:
    index_columns:
        - "store_location"

transformations:
    - read_delimited:
        encoding: ascii
        header: all_files_same_headers
        delimiter: " "
    - keep_columns: ["store_location", "zip_code", "date", "amount", "x", "y", "z"]
    - convert_column_types:
        - columns: date
          column_type:
            datetime:
                formats:
                    - "%d/%m/%Y"
        - columns: ["x","y","z"] 
          column_type:
            boolean:
                mismatch_as: error
                true_values:
                    - "yes"
                    - "true"
                    - "1"
                false_values:
                    - "no"
                    - "false"
                    - "0"
```
