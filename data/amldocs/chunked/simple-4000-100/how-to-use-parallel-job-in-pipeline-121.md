
# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Declare `job_data_path` as one of the inputs. Bind it to `input_data` attribute.

```python
# parallel task to process file data
file_batch_inference = parallel_run_function(
    name="file_batch_score",
    display_name="Batch Score with File Dataset",
    description="parallel component for batch score",
    inputs=dict(
        job_data_path=Input(
            type=AssetTypes.MLTABLE,
            description="The data to be split and scored in parallel",
        )
    ),
    outputs=dict(job_output_path=Output(type=AssetTypes.MLTABLE)),
    input_data="${{inputs.job_data_path}}",
    instance_count=2,
    max_concurrency_per_instance=1,
    mini_batch_size="1",
    mini_batch_error_threshold=1,
    retry_settings=dict(max_retries=2, timeout=60),
    logging_level="DEBUG",
    task=RunFunction(
        code="./src",
        entry_script="file_batch_inference.py",
        program_arguments="--job_output_path ${{outputs.job_output_path}}",
        environment="azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1",
    ),
)
```


Once you have the partition setting defined, you can configure parallel setting by using two attributes below:

| Attribute name | Type | Description | Default value |
|:-|--|:-|--|
| `instance_count` | integer | The number of nodes to use for the job. | 1 |
| `max_concurrency_per_instance` | integer | The number of processors on each node. | For a GPU compute, the default value is 1.<br> For a CPU compute, the default value is the number of cores. |

These two attributes work together with your specified compute cluster.

:::image type="content" source="./media/how-to-use-parallel-job-in-pipeline/how-distributed-data-works-in-parallel-job.png" alt-text="Diagram showing how distributed data works in parallel job." lightbox ="./media/how-to-use-parallel-job-in-pipeline/how-distributed-data-works-in-parallel-job.png":::

Sample code to set two attributes:

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
# parallel task to process file data
file_batch_inference = parallel_run_function(
    name="file_batch_score",
    display_name="Batch Score with File Dataset",
    description="parallel component for batch score",
    inputs=dict(
        job_data_path=Input(
            type=AssetTypes.MLTABLE,
            description="The data to be split and scored in parallel",
        )
    ),
    outputs=dict(job_output_path=Output(type=AssetTypes.MLTABLE)),
    input_data="${{inputs.job_data_path}}",
    instance_count=2,
    max_concurrency_per_instance=1,
    mini_batch_size="1",
    mini_batch_error_threshold=1,
    retry_settings=dict(max_retries=2, timeout=60),
    logging_level="DEBUG",
    task=RunFunction(
        code="./src",
        entry_script="file_batch_inference.py",
        program_arguments="--job_output_path ${{outputs.job_output_path}}",
        environment="azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1",
    ),
)
```
