| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. Note that in this case you are fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |

### Job outputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job output. For the default `uri_folder` type, the output will correspond to a folder. | `uri_folder` , `mlflow_model`, `custom_model`| `uri_folder` |
| `mode` | string | Mode of how output file(s) will get delivered to the destination storage. For read-write mount mode (`rw_mount`) the output directory will be a mounted directory. For upload mode the file(s) written will get uploaded at the end of the job. | `rw_mount`, `upload` | `rw_mount` |

### Identity configurations

#### UserIdentityConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Identity type.  | `user_identity` |

#### ManagedIdentityConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Identity type.  | `managed` or `managed_identity` |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Several are shown below.

## YAML: hello world

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: echo "hello world"
environment:
  image: library/python:latest
compute: azureml:cpu-cluster

```

## YAML: display name, experiment name, description, and tags

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: echo "hello world"
environment:
  image: library/python:latest
compute: azureml:cpu-cluster
tags:
  hello: world
display_name: hello-world-example
experiment_name: hello-world-example
description: |
  # Azure Machine Learning "hello world" job

  This is a "hello world" job running in the cloud via Azure Machine Learning!

  ## Description

  Markdown is supported in the studio for job descriptions! You can edit the description there or via CLI.

```

## YAML: environment variables

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: echo $hello_env_var
environment:
  image: library/python:latest
compute: azureml:cpu-cluster
environment_variables:
  hello_env_var: "hello world"

```

## YAML: source code

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: ls
code: src
environment:
  image: library/python:latest
compute: azureml:cpu-cluster

```

## YAML: literal inputs

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: |
  echo ${{inputs.hello_string}}
  echo ${{inputs.hello_number}}
environment:
  image: library/python:latest
inputs:
  hello_string: "hello world"
  hello_number: 42
compute: azureml:cpu-cluster

```

## YAML: write to default outputs

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: echo "hello world" > ./outputs/helloworld.txt
environment:
  image: library/python:latest
compute: azureml:cpu-cluster

```
