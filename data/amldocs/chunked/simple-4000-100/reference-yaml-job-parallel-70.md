| `--first_task_creation_timeout`  | The timeout in second for monitoring the time between the job start to the run of first mini-batch. | (0, 259200] | 600 |
| `--copy_logs_to_parent`  | Boolean option to whether copy the job progress, overview, and logs to the parent pipeline job. | True, False | False |
| `--metrics_name_prefix`  | Provide the custom prefix of your metrics in this parallel job. |  |  |
| `--push_metrics_to_parent`  | Boolean option to whether push metrics to the parent pipeline job. | True, False | False |
| `--resource_monitor_interval`  | The time interval in seconds to dump node resource usage(for example, cpu, memory) to log folder under "logs/sys/perf" path. <br><br> Note: Frequent dump resource logs will slightly slow down the execution speed of your mini-batch. Set this value to "0" to stop dumping resource usage. | [0, int.max] | 600 |

## Remarks

The `az ml job` commands can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Several are shown below.

## YAML: Using parallel job in pipeline

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

display_name: iris-batch-prediction-using-parallel
description: The hello world pipeline job with inline parallel job
tags:
  tag: tagvalue
  owner: sdkteam

settings:
  default_compute: azureml:cpu-cluster

jobs:
  batch_prediction:
    type: parallel
    compute: azureml:cpu-cluster
    inputs:
      input_data: 
        type: mltable
        path: ./neural-iris-mltable
        mode: direct
      score_model: 
        type: uri_folder
        path: ./iris-model
        mode: download
    outputs:
      job_output_file:
        type: uri_file
        mode: rw_mount

    input_data: ${{inputs.input_data}}
    mini_batch_size: "10kb"
    resources:
        instance_count: 2
    max_concurrency_per_instance: 2

    logging_level: "DEBUG"
    mini_batch_error_threshold: 5
    retry_settings:
      max_retries: 2
      timeout: 60

    task:
      type: run_function
      code: "./script"
      entry_script: iris_prediction.py
      environment:
        name: "prs-env"
        version: 1
        image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
        conda_file: ./environment/environment_parallel.yml
      program_arguments: >-
        --model ${{inputs.score_model}}
        --error_threshold 5
        --allowed_failed_percent 30
        --task_overhead_timeout 1200
        --progress_update_timeout 600
        --first_task_creation_timeout 600
        --copy_logs_to_parent True
        --resource_monitor_interva 20
      append_row_to: ${{outputs.job_output_file}}

```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
