| `path` | string | The path to the data to use as input. This can be specified in a few ways: <br><br> - A local path to the data source file or folder, e.g. `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. See [Core yaml syntax](reference-yaml-core-syntax.md) for more information on how to use the `azureml://` URI format. <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), e.g. `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. Note that in this case you are fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |

### Job outputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job output. For the default `uri_folder` type, the output will correspond to a folder. | `uri_file`, `uri_folder`, `mltable`, `mlflow_model` | `uri_folder` |
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

The `az ml job` commands can be used for managing Azure Machine Learning pipeline jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Several are shown below.

## YAML: hello pipeline

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
display_name: hello_pipeline
jobs:
  hello_job:
    command: echo "hello"
    environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
    compute: azureml:cpu-cluster
  world_job:
    command: echo "world"
    environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
    compute: azureml:cpu-cluster
 
```

## YAML: input/output dependency

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
display_name: hello_pipeline_io
jobs:
  hello_job:
    command: echo "hello" && echo "world" > ${{outputs.world_output}}/world.txt
    environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
    compute: azureml:cpu-cluster
    outputs:
      world_output:
  world_job:
    command: cat ${{inputs.world_input}}/world.txt
    environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1
    compute: azureml:cpu-cluster
    inputs:
      world_input: ${{parent.jobs.hello_job.outputs.world_output}}
 
```
