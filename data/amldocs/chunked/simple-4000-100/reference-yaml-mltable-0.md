
# CLI (v2) mltable YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Find the source JSON schema at https://azuremlschemas.azureedge.net/latest/MLTable.schema.json.

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## How to author `MLTable` files

This article contains information relating to the `MLTable` YAML schema only. For more information on MLTable, including `MLTable` file authoring, MLTable *artifacts* creation, consuming in Pandas and Spark, and end-to-end examples, read [Working with tables in Azure Machine Learning](how-to-mltable.md).

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, you can invoke schema and resource completions if you include `$schema` at the top of your file. | | |
| `type` | const | `mltable` abstracts the schema definition for tabular data, to make it easier for data consumers to materialize the table into a Pandas/Dask/Spark dataframe | `mltable` | `mltable`|
| `paths` | array | Paths can be a `file` path, `folder` path, or `pattern` for paths. `pattern` supports *globbing* patterns that specify sets of filenames with wildcard characters (`*`, `?`, `[abc]`, `[a-z]`). Supported URI types: `azureml`, `https`, `wasbs`, `abfss`, and `adl`. See [Core yaml syntax](reference-yaml-core-syntax.md) for more information that explains how to use the `azureml://` URI format. |`file`<br>`folder`<br>`pattern`  | |
| `transformations`| array | A defined transformation sequence, applied to data loaded from defined paths. Read [Transformations](#transformations) for more information. |`read_delimited`<br>`read_parquet`<br>`read_json_lines`<br>`read_delta_lake`<br>`take`<br>`take_random_sample`<br>`drop_columns`<br>`keep_columns`<br>`convert_column_types`<br>`skip`<br>`filter`<br>`extract_columns_from_partition_format` || 

### Transformations

#### Read transformations

|Read Transformation  | Description | Parameters |
|---------|---------|---------|
|`read_delimited` | Adds a transformation step to read delimited text file(s) provided in `paths`. | `infer_column_types`: Boolean to infer column data types. Defaults to True. Type inference requires that the current compute can access the data source. Currently, type inference will only pull the first 200 rows.<br><br>`encoding`: Specify the file encoding. Supported encodings: `utf8`, `iso88591`, `latin1`, `ascii`, `utf16`, `utf32`, `utf8bom` and `windows1252`. Default encoding: `utf8`.<br><br>`header`: user can choose one of the following options: `no_header`, `from_first_file`, `all_files_different_headers`, `all_files_same_headers`. Defaults to `all_files_same_headers`.<br><br>`delimiter`: The separator used to split columns.<br><br>`empty_as_string`: Specify if empty field values should load as empty strings. The default (False) will read empty field values as nulls. Passing this setting as *True* will read empty field values as empty strings. If the values are converted to numeric or datetime, then this setting has no effect, as empty values will be converted to nulls.<br><Br>`include_path_column`: Boolean to keep path information as column in the table. Defaults to False. This setting is useful when reading multiple files, and you want to know from which file a specific record originated. Additionally, you can keep useful information in the file path.<br><br>`support_multi_line`: By default (`support_multi_line=False`), all line breaks, including line breaks in quoted field values, will be interpreted as a record break. This approach to data reading increases speed, and it offers optimization for parallel execution on multiple CPU cores. However, it may result in silent production of more records with misaligned field values. Set this value to True when the delimited files are known to contain quoted line breaks. |
