
# CLI (v2) model YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/model.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `$schema` | string | The YAML schema. | |
| `name` | string | **Required.** Name of the model. | |
| `version` | int | Version of the model. If omitted, Azure ML will autogenerate a version. | |
| `description` | string | Description of the model. | |
| `tags` | object | Dictionary of tags for the model. | |
| `path` | string | Either a local path to the model file(s), or the URI of a cloud path to the model file(s). This can point to either a file or a directory. | |
| `type` | string | Storage format type of the model. Applicable for no-code deployment scenarios. | `custom_model`, `mlflow_model`, `triton_model` |
| `flavors` | object | Flavors of the model. Each model storage format type may have one or more supported flavors. Applicable for no-code deployment scenarios. | |

## Remarks

The `az ml model` command can be used for managing Azure Machine Learning models.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/assets/model). Several are shown below.

## YAML: local file

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/model.schema.json
name: local-file-example
path: mlflow-model/model.pkl
description: Model created from local file.

```

## YAML: local folder in MLflow format

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/model.schema.json
name: local-mlflow-example
path: mlflow-model
type: mlflow_model
description: Model created from local MLflow model directory.

```

- [Install and use the CLI (v2)](how-to-configure-cli.md)
