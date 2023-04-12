| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. In this case, you're fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |

### Job outputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job output. For the default `uri_folder` type, the output will correspond to a folder. | `uri_folder` | `uri_folder` |
| `path` | string | The path to the data to use as input. This can be specified in a few ways: <br><br> - A local path to the data source file or folder, for example, `path: ./iris.csv`. The data will get uploaded during job submission. <br><br> - A URI of a cloud path to the file or folder to use as the input. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, `adl`. For more information on how to use the `azureml://` URI format, see [Core yaml syntax](reference-yaml-core-syntax.md). <br><br> - An existing registered Azure ML data asset to use as the input. To reference a registered data asset, use the `azureml:<data_name>:<data_version>` syntax or `azureml:<data_name>@latest` (to reference the latest version of that data asset), for example, `path: azureml:cifar10-data:1` or `path: azureml:cifar10-data@latest`. | | |
| `mode` | string | Mode of how output file(s) will get delivered to the destination storage. For read-write mount mode (`rw_mount`) the output directory will be a mounted directory. For upload mode the file(s) written will get uploaded at the end of the job. | `rw_mount`, `upload` | `rw_mount` |

## Remarks

The `az ml schedule` command can be used for managing Azure Machine Learning models.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/schedules). A couple are shown below.

## YAML: Schedule with recurrence pattern

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/schedule.schema.json
name: simple_recurrence_job_schedule
display_name: Simple recurrence job schedule
description: a simple hourly recurrence job schedule

trigger:
  type: recurrence
  frequency: day #can be minute, hour, day, week, month
  interval: 1 #every day
  schedule:
    hours: [4,5,10,11,12]
    minutes: [0,30]
  start_time: "2022-07-10T10:00:00" # optional - default will be schedule creation time
  time_zone: "Pacific Standard Time" # optional - default will be UTC

create_job: ./simple-pipeline-job.yml
# create_job: azureml:simple-pipeline-job

```

## YAML: Schedule with cron expression

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/schedule.schema.json
name: simple_cron_job_schedule
display_name: Simple cron job schedule
description: a simple hourly cron job schedule

trigger:
  type: cron
  expression: "0 * * * *"
  start_time: "2022-07-10T10:00:00" # optional - default will be schedule creation time
  time_zone: "Pacific Standard Time" # optional - default will be UTC

# create_job: azureml:simple-pipeline-job
create_job: ./simple-pipeline-job.yml
```

## Appendix

### Timezone

Current schedule supports the following timezones. The key can be used directly in the Python SDK, while the value can be used in the YAML job. The table is organized by UTC(Coordinated Universal Time).
