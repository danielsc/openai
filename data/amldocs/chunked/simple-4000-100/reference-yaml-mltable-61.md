
Next, add the following contents to the `MLTable` file:

```yml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable
paths:
    - file: https://azuremlexamples.blob.core.windows.net/datasets/iris.csv

transformations:
    - read_delimited:
        delimiter: ','
        header: all_files_same_headers
        include_path_column: true
```

You can then materialize into Pandas using:

> [!IMPORTANT]
> You must have the `mltable` Python SDK installed. Install it with:<br>
> `pip install mltable`.

```python
import mltable

tbl = mltable.load("./iris")
df = tbl.to_pandas_dataframe()
```

You should see that the data includes a new column named `Path`. This column contains the data path, which is `https://azuremlexamples.blob.core.windows.net/datasets/iris.csv`.

You can create a data asset using the CLI:

```azurecli
az ml data create --name iris-from-https --version 1 --type mltable --path ./iris
```

The folder containing the `MLTable` will automatically upload to cloud storage (the default Azure ML datastore).

> [!TIP]
> An Azure ML data asset is similar to web browser bookmarks (favorites). Instead of remembering long URIs (storage paths) that point to your most frequently used data, you can create a data asset, and then access that asset with a friendly name.

### Delimited text files

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json
type: mltable

# Supported paths include:
# local: ./<path>
# blob: wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>
# Public http(s) server: https://<url>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/
# Datastore: azureml://subscriptions/<subid>/resourcegroups/<rg>/workspaces/<ws>/datastores/<datastore_name>/paths/<path>

paths:
  - file: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/ # a specific file on ADLS
  # additional options
  # - folder: ./<folder> a specific folder
  # - pattern: ./*.csv # glob all the csv files in a folder

transformations:
    - read_delimited:
        encoding: ascii
        header: all_files_same_headers
        delimiter: ","
        include_path_column: true
        empty_as_string: false
    - keep_columns: [col1, col2, col3, col4, col5, col6, col7]
    # or you can drop_columns...
    # - drop_columns: [col1, col2, col3, col4, col5, col6, col7]
    - convert_column_types:
        - columns: col1
          column_type: int
        - columns: col2
          column_type:
            datetime:
                formats:
                    - "%d/%m/%Y"
        - columns: [col1, col2, col3] 
          column_type:
            boolean:
                mismatch_as: error
                true_values: ["yes", "true", "1"]
                false_values: ["no", "false", "0"]
      - filter: 'col("col1") > 32 and col("col7") == "a_string"'
      # create a column called timestamp with the values extracted from the folder information
      - extract_columns_from_partition_format: {timestamp:yyyy/MM/dd}
      - skip: 10
      - take_random_sample:
          probability: 0.50
          seed: 1394
      # or you can take the first n records
      # - take: 200
```

### Parquet

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json
type: mltable

# Supported paths include:
# local: ./<path>
# blob: wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>
# Public http(s) server: https://<url>
# ADLS gen2: abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/
# Datastore: azureml://subscriptions/<subid>/resourcegroups/<rg>/workspaces/<ws>/datastores/<datastore_name>/paths/<path>


paths:
  - pattern: azureml://subscriptions/<subid>/resourcegroups/<rg>/workspaces/<ws>/datastores/<datastore_name>/paths/<path>/*.parquet
  
transformations:
  - read_parquet:
        include_path_column: false
  - filter: 'col("temperature") > 32 and col("location") == "UK"'
  - skip: 1000 # skip first 1000 rows
  # create a column called timestamp with the values extracted from the folder information
  - extract_columns_from_partition_format: {timestamp:yyyy/MM/dd}
```
