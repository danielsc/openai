| overhead timeout | integer | The timeout in second for initialization of each mini-batch. For example, load mini-batch data and pass it to run() function. | (0, 259200] | 600 | N/A | --task_overhead_timeout |
| progress update timeout | integer | The timeout in second for monitoring the progress of mini-batch execution. If no progress updates receive within this timeout setting, the parallel job will be marked as failed. | (0, 259200] | Dynamically calculated by other settings. | N/A | --progress_update_timeout |
| first task creation timeout | integer | The timeout in second for monitoring the time between the job start to the run of first mini-batch. | (0, 259200] | 600 | N/A | --first_task_creation_timeout |
| logging level | string | Define which level of logs will be dumped to user log files. | INFO, WARNING, or DEBUG | INFO | logging_level | N/A |
| append row to | string | Aggregate all returns from each run of mini-batch and output it into this file. May reference to one of the outputs of parallel job by using the expression ${{outputs.<output_name>}} |  |  | task.append_row_to | N/A |
| copy logs to parent | string | Boolean option to whether copy the job progress, overview, and logs to the parent pipeline job. | True or False | False | N/A | --copy_logs_to_parent |
| resource monitor interval | integer | The time interval in seconds to dump node resource usage(for example, cpu, memory) to log folder under "logs/sys/perf" path.<br><br>Note: Frequent dump resource logs will slightly slow down the execution speed of your mini-batch. Set this value to "0" to stop dumping resource usage. | [0, int.max] | 600 | N/A | --resource_monitor_interval |

Sample code to update these settings:

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

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

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# parallel task to process tabular data
tabular_batch_inference = parallel_run_function(
    name="batch_score_with_tabular_input",
    display_name="Batch Score with Tabular Dataset",
    description="parallel component for batch score",
    inputs=dict(
        job_data_path=Input(
            type=AssetTypes.MLTABLE,
            description="The data to be split and scored in parallel",
        ),
        score_model=Input(
            type=AssetTypes.URI_FOLDER, description="The model for batch score."
        ),
    ),
    outputs=dict(job_output_path=Output(type=AssetTypes.MLTABLE)),
    input_data="${{inputs.job_data_path}}",
    instance_count=2,
    max_concurrency_per_instance=2,
    mini_batch_size="100",
    mini_batch_error_threshold=5,
    logging_level="DEBUG",
    retry_settings=dict(max_retries=2, timeout=60),
    task=RunFunction(
        code="./src",
        entry_script="tabular_batch_inference.py",
        environment=Environment(
            image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
            conda_file="./src/environment_parallel.yml",
        ),
        program_arguments="--model ${{inputs.score_model}} "
        "--job_output_path ${{outputs.job_output_path}} "
        "--error_threshold 5 "
        "--allowed_failed_percent 30 "
        "--task_overhead_timeout 1200 "
        "--progress_update_timeout 600 "
        "--first_task_creation_timeout 600 "
        "--copy_logs_to_parent True "
        "--resource_monitor_interva 20 ",
        append_row_to="${{outputs.job_output_path}}",
    ),
)
```
