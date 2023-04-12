
> [!NOTE]
> If you use tabular `mltable` as your major input data, you need to have the MLTABLE specification file with `transformations - read_delimited` section filled under your specific path. For more examples, see [Create a mltable data asset](how-to-create-register-data-assets.md#create-a-mltable-data-asset)

### Implement predefined functions in entry script

Entry script is a single Python file where user needs to implement three predefined functions with custom code. Azure ML parallel job follows the diagram below to execute them in each processor.

:::image type="content" source="./media/how-to-use-parallel-job-in-pipeline/how-entry-script-works-in-parallel-job.png" alt-text="Diagram showing how entry script works in parallel job." lightbox ="./media/how-to-use-parallel-job-in-pipeline/how-entry-script-works-in-parallel-job.png":::

| Function name | Required | Description | Input | Return |
| :------------ | -------- | :---------- | :---- | :----- |
| Init() | Y | Use this function for common preparation before starting to run mini-batches. For example, use it to load the model into a global object. | -- | -- |
| Run(mini_batch) | Y | Implement main execution logic for mini_batches. | mini_batch: <br>Pandas dataframe if input data is a tabular data.<br> List of file path if input data is a directory. | Dataframe, List, or Tuple. |
| Shutdown() | N | Optional function to do custom cleans up before returning the compute back to pool. | -- | -- |

Check the following entry script examples to get more details:

- [Image identification for a list of image files](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/Code/digit_identification.py)
- [Iris classification for a tabular iris data](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/machine-learning-pipelines/parallel-run/Code/iris_score.py)

Once you have entry script ready, you can set following two attributes to use it in your parallel job:

| Attribute name | Type | Description | Default value |
|: ------------- | ---- |: ---------- | ------------- |
| `code` | string | Local path to the source code directory to be uploaded and used for the job. | |
| `entry_script` | string | The Python file that contains the implementation of pre-defined parallel functions. | |

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
