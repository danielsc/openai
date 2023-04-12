|`timezone`| string |Specifies the time zone of the recurrence. If omitted, by default is UTC. |See [appendix for timezone values](#timezone)|

### Job definition

Customer can directly use `create_job: azureml:<job_name>` or can use the following properties to define the job.

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
|`type`| string | **Required.** Specifies the job type. Only pipeline job is supported.|`pipeline`|
|`job`| string | **Required.** Define how to reference a job, it can be `azureml:<job_name>` or a local pipeline job yaml such as `file:hello-pipeline.yml`.| |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, we'll take schedule name as default value. | |
|`inputs`| object | Dictionary of inputs to the job. The key is a name for the input within the context of the job and the value is the input value.| |
|`outputs`|object | Dictionary of output configurations of the job. The key is a name for the output within the context of the job and the value is the output configuration.| |
| `settings` | object | Default settings for the pipeline job. See [Attributes of the `settings` key](#attributes-of-the-settings-key) for the set of configurable properties. | |

### Attributes of the `settings` key

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `default_datastore` | string | Name of the datastore to use as the default datastore for the pipeline job. This value must be a reference to an existing datastore in the workspace using the `azureml:<datastore-name>` syntax. Any outputs defined in the `outputs` property of the parent pipeline job or child step jobs will be stored in this datastore. If omitted, outputs will be stored in the workspace blob datastore. | |
| `default_compute` | string | Name of the compute target to use as the default compute for all steps in the pipeline. If compute is defined at the step level, it will override this default compute for that specific step. This value must be a reference to an existing compute in the workspace using the `azureml:<compute-name>` syntax. | |
| `continue_on_step_failure` | boolean | Whether the execution of steps in the pipeline should continue if one step fails. The default value is `False`, which means that if one step fails, the pipeline execution will be stopped, canceling any running steps. | `False` |

### Job inputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job input. Specify `uri_file` for input data that points to a single file source, or `uri_folder` for input data that points to a folder source. | `uri_file`, `uri_folder` | `uri_folder` |
| `path` | string | The path to the data to use as input. This can be specified in a few ways: <br><br> - A local path to the data source file or folder, for example, `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. For more information on how to use the `azureml://` URI format, see [Core yaml syntax](reference-yaml-core-syntax.md). <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset, use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), for example, `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. In this case, you're fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |
