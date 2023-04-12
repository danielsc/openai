
# How to use parallel job in pipeline (V2)

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Parallel job lets users accelerate their job execution by distributing repeated tasks on powerful multi-nodes compute clusters. For example, take the scenario where you're running an object detection model on large set of images. With Azure ML Parallel job, you can easily distribute your images to run custom code in parallel on a specific compute cluster. Parallelization could significantly reduce the time cost. Also by using Azure ML parallel job you can simplify and automate your process to make it more efficient.

## Prerequisite

Azure ML parallel job can only be used as one of steps in a pipeline job. Thus, it's important to be familiar with using pipelines. To learn more about Azure ML pipelines, see the following articles.

- Understand what is a [Azure Machine Learning pipeline](concept-ml-pipelines.md)
- Understand how to use Azure ML pipeline with [CLI v2](how-to-create-component-pipelines-cli.md) and [SDK v2](how-to-create-component-pipeline-python.md).

## Why are parallel jobs needed?

In the real world, ML engineers always have scale requirements on their training or inferencing tasks. For example, when a data scientist provides a single script to train a sales prediction model, ML engineers need to apply this training task to each individual store. During this scale out process, some challenges are:

- Delay pressure caused by long execution time.
- Manual intervention to handle unexpected issues to keep the task proceeding.

The core value of Azure ML parallel job is to split a single serial task into mini-batches and dispatch those mini-batches to multiple computes to execute in parallel. By using parallel jobs, we can:

 - Significantly reduce end-to-end execution time.
 - Use Azure ML parallel job's automatic error handling settings.

You should consider using Azure ML Parallel job if:

 - You plan to train many models on top of your partitioned data.
 - You want to accelerate your large scale batch inferencing task.

## Prepare for parallel job

Unlike other types of jobs, a parallel job requires preparation. Follow the next sections to prepare for creating your parallel job.

### Declare the inputs to be distributed and partition setting

Parallel job requires only one **major input data** to be split and processed with parallel. The major input data can be either tabular data or a set of files. Different input types can have a different partition method.

The following table illustrates the relation between input data and partition setting:

| Data format | AML input type | AML input mode | Partition method |
|: ---------- |: ------------- |: ------------- |: --------------- |
| File list | `mltable` or<br>`uri_folder` | ro_mount or<br>download | By size (number of files) |
| Tabular data | `mltable` | direct | By size (estimated physical size) |

You can declare your major input data with `input_data` attribute in parallel job YAML or Python SDK. And you can bind it with one of your defined `inputs` of your parallel job by using `${{inputs.<input name>}}`. Then to define the partition method for your major input.

For example, you could set numbers to `mini_batch_size` to partition your data **by size**.

- When using file list input, this value defines the number of files for each mini-batch.
- When using tabular input, this value defines the estimated physical size for each mini-batch.

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
