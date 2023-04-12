| `append_row_to` | string | Aggregate all returns from each run of mini-batch and output it into this file. May reference to one of the outputs of parallel job by using the expression \${{outputs.<output_name>}} |||

### Job inputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job input. Specify `mltable` for input data that points to a location where has the mltable meta file, or `uri_folder` for input data that points to a folder source. | `mltable`, `uri_folder` | `uri_folder` |
| `path` | string | The path to the data to use as input. The value can be specified in a few ways: <br><br> - A local path to the data source file or folder, for example, `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. For more information, see [Core yaml syntax](reference-yaml-core-syntax.md) on how to use the `azureml://` URI format. <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset, use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), for example, `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. It will pass in the URL of the storage location as the job input. In this case, you're fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |

### Job outputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job output. For the default `uri_folder` type, the output will correspond to a folder. | `uri_folder` | `uri_folder` |
| `mode` | string | Mode of how output file(s) will get delivered to the destination storage. For read-write mount mode (`rw_mount`) the output directory will be a mounted directory. For upload mode the file(s) written will get uploaded at the end of the job. | `rw_mount`, `upload` | `rw_mount` |

### Predefined arguments for parallel job
| Key  | Description | Allowed values | Default value |
| ---  | ----------- | -------------- | ------------- |
| `--error_threshold`  | The threshold of **failed items**. Failed items are counted by the number gap between inputs and returns from each mini-batch. If the sum of failed items is higher than this threshold, the parallel job will be marked as failed.<br><br>Note: "-1" is the default number, which means to ignore all failures during parallel job.| [-1, int.max] | -1 |
| `--allowed_failed_percent`  | Similar to `mini_batch_error_threshold` but uses the percent of failed mini-batches instead of the count. | [0, 100] | 100 |
| `--task_overhead_timeout`  | The timeout in second for initialization of each mini-batch. For example, load mini-batch data and pass it to run() function. | (0, 259200] | 30 |
| `--progress_update_timeout`  | The timeout in second for monitoring the progress of mini-batch execution. If no progress updates receive within this timeout setting, the parallel job will be marked as failed. | (0, 259200] | Dynamically calculated by other settings. |
| `--first_task_creation_timeout`  | The timeout in second for monitoring the time between the job start to the run of first mini-batch. | (0, 259200] | 600 |
