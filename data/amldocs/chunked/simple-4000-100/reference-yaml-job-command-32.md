| `inputs` | object | Dictionary of inputs to the job. The key is a name for the input within the context of the job and the value is the input value. <br><br> Inputs can be referenced in the `command` using the `${{ inputs.<input_name> }}` expression. | | |
| `inputs.<input_name>` | number, integer, boolean, string or object | One of a literal value (of type number, integer, boolean, or string) or an object containing a [job input data specification](#job-inputs). | | |
| `outputs` | object | Dictionary of output configurations of the job. The key is a name for the output within the context of the job and the value is the output configuration. <br><br> Outputs can be referenced in the `command` using the `${{ outputs.<output_name> }}` expression. | |
| `outputs.<output_name>` | object | You can leave the object empty, in which case by default the output will be of type `uri_folder` and Azure ML will system-generate an output location for the output. File(s) to the output directory will be written via read-write mount. If you want to specify a different mode for the output, provide an object containing the [job output specification](#job-outputs). | |
| `identity` | object | The identity is used for data accessing. It can be [UserIdentityConfiguration](#useridentityconfiguration), [ManagedIdentityConfiguration](#managedidentityconfiguration) or None. If it's UserIdentityConfiguration the identity of job submitter will be used to access input data and write result to output folder, otherwise, the managed identity of the compute target will be used. | |

### Distribution configurations

#### MpiConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Distribution type.  | `mpi` |
| `process_count_per_instance` | integer | **Required.** The number of processes per node to launch for the job.  | |

#### PyTorchConfiguration

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** Distribution type.  | `pytorch` | |
| `process_count_per_instance` | integer | The number of processes per node to launch for the job. | |  `1` |

#### TensorFlowConfiguration

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** Distribution type.  | `tensorflow` |
| `worker_count` | integer | The number of workers to launch for the job. | | Defaults to `resources.instance_count`. |
| `parameter_server_count` | integer | The number of parameter servers to launch for the job. | | `0` |

### Job inputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job input. Specify `uri_file` for input data that points to a single file source, or `uri_folder` for input data that points to a folder source. | `uri_file`, `uri_folder`, `mlflow_model`, `custom_model`| `uri_folder` |
| `path` | string | The path to the data to use as input. This can be specified in a few ways: <br><br> - A local path to the data source file or folder, e.g. `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. See [Core yaml syntax](reference-yaml-core-syntax.md) for more information on how to use the `azureml://` URI format. <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), e.g. `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. Note that in this case you are fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |
