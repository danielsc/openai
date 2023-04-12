| `environment` | string or object | **Required.** The environment to use for the job. This can be either a reference to an existing versioned environment in the workspace or an inline environment specification. <br> <br> To reference an existing environment, use the `azureml:<environment-name>:<environment-version>` syntax. <br><br> To define an environment inline, follow the [Environment schema](reference-yaml-environment.md#yaml-syntax). Exclude the `name` and `version` properties as they aren't supported for inline environments. | |
| `environment_variables` | object | Dictionary of environment variable name-value pairs to set on the process where the command is executed. | |
| `distribution` | object | The distribution configuration for distributed training scenarios. One of [MpiConfiguration](#mpiconfiguration), [PyTorchConfiguration](#pytorchconfiguration), or [TensorFlowConfiguration](#tensorflowconfiguration). | |
| `resources.instance_count` | integer | The number of nodes to use for the job. | `1` |

#### Distribution configurations

##### MpiConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Distribution type.  | `mpi` |
| `process_count_per_instance` | integer | **Required.** The number of processes per node to launch for the job.  | |

##### PyTorchConfiguration

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** Distribution type.  | `pytorch` | |
| `process_count_per_instance` | integer | The number of processes per node to launch for the job. | |  `1` |

##### TensorFlowConfiguration

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** Distribution type.  | `tensorflow` |
| `worker_count` | integer | The number of workers to launch for the job. | | Defaults to `resources.instance_count`. |
| `parameter_server_count` | integer | The number of parameter servers to launch for the job. | | `0` |

### Job inputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job input. Specify `uri_file` for input data that points to a single file source, or `uri_folder` for input data that points to a folder source. [Learn more about data access.](concept-data.md)| `uri_file`, `uri_folder`, `mltable`, `mlflow_model` | `uri_folder` |
| `path` | string | The path to the data to use as input. This can be specified in a few ways: <br><br> - A local path to the data source file or folder, for example, `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. For more information on using the `azureml://` URI format, see [Core yaml syntax](reference-yaml-core-syntax.md). <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset, use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), for example, `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. In this case you're fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |
