
# CLI (v2) batch endpoint YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/batchEndpoint.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `name` | string | **Required.** Name of the endpoint. Needs to be unique at the Azure region level. | | |
| `description` | string | Description of the endpoint. | | |
| `tags` | object | Dictionary of tags for the endpoint. | | |
| `auth_mode` | string | The authentication method for the endpoint. Currently only Azure Active Directory (Azure AD) token-based authentication is supported. | `aad_token` | `aad_token` |
| `defaults` | object | Default settings for the endpoint. | | |
| `defaults.deployment_name` | string | Name of the deployment that will serve as the default deployment for the endpoint. | | |

## Remarks

The `az ml batch-endpoint` commands can be used for managing Azure Machine Learning endpoints.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch). Several are shown below.

## YAML: basic

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/batchEndpoint.schema.json
name: mnist-batch
description: A batch endpoint for scoring images from the MNIST dataset.
auth_mode: aad_token
```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
