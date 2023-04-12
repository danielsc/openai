
# CLI (v2) data YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/data.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `name` | string | **Required.** Name of the data asset. | | |
| `version` | string | Version of the dataset. If omitted, Azure ML will autogenerate a version. | | |
| `description` | string | Description of the data asset. | | |
| `tags` | object | Dictionary of tags for the data asset. | | |
| `type` | string | The data asset type. Specify `uri_file` for data that points to a single file source, or `uri_folder` for data that points to a folder source. | `uri_file`, `uri_folder` | `uri_folder` |
| `path` | string | Either a local path to the data source file or folder, or the URI of a cloud path to the data source file or folder. Please ensure that the source provided here is compatible with the `type` specified. <br><br> Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, and `adl`. See [Core yaml syntax](reference-yaml-core-syntax.md) for more information on how to use the `azureml://` URI format. | | |

## Remarks

The `az ml data` commands can be used for managing Azure Machine Learning data assets.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/assets/data). Several are shown below.

## YAML: datastore file

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-file-example
description: Data asset created from file in cloud.
type: uri_file
path: azureml://datastores/workspaceblobstore/paths/example-data/titanic.csv
```

## YAML: datastore folder

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-folder-example
description: Data asset created from folder in cloud.
type: uri_folder
path: azureml://datastores/workspaceblobstore/paths/example-data/
```

## YAML: https file

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-file-https-example
description: Data asset created from a file in cloud using https URL.
type: uri_file
path: https://account-name.blob.core.windows.net/container-name/example-data/titanic.csv
```

## YAML: https folder

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-folder-https-example
description: Dataset created from folder in cloud using https URL.
type: uri_folder
path: https://account-name.blob.core.windows.net/container-name/example-data/
```

## YAML: wasbs file

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-file-wasbs-example
description: Data asset created from a file in cloud using wasbs URL.
type: uri_file
path: wasbs://account-name.blob.core.windows.net/container-name/example-data/titanic.csv
```

## YAML: wasbs folder

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: cloud-folder-wasbs-example
description: Data asset created from folder in cloud using wasbs URL.
type: uri_folder
path: wasbs://account-name.blob.core.windows.net/container-name/example-data/
```

## YAML: local file

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: local-file-example-titanic
description: Data asset created from local file.
type: uri_file
path: sample-data/titanic.csv

```

## YAML: local folder

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: local-folder-example-titanic
description: Dataset created from local folder.
type: uri_folder
path: sample-data/

```
