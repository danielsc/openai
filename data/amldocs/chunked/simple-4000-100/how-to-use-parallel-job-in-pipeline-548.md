
## Create parallel job in pipeline

# [Azure CLI](#tab/cliv2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

You can create your parallel job inline with your pipeline job:
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

First, you need to import the required libraries, initiate your ml_client with proper credential, and create/retrieve your computes:

```python
# import required libraries
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.ai.ml import MLClient, Input, Output, load_component
from azure.ai.ml.dsl import pipeline
from azure.ai.ml.entities import Environment
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml.parallel import parallel_run_function, RunFunction
```

```python
try:
    credential = DefaultAzureCredential()
    # Check if given credential can get token successfully.
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:
    # Fall back to InteractiveBrowserCredential in case DefaultAzureCredential not work
    credential = InteractiveBrowserCredential()
```

```python
# Get a handle to workspace
ml_client = MLClient.from_config(credential=credential)

# Retrieve an already attached Azure Machine Learning Compute.
cpu_compute_target = "cpu-cluster"
print(ml_client.compute.get(cpu_compute_target))
gpu_compute_target = "gpu-cluster"
print(ml_client.compute.get(gpu_compute_target))
```

Then implement your parallel job by filling `parallel_run_function`:

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
