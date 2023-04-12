

## Write data in a job

In your job, you can write data to your cloud-based storage with *outputs*. The [Supported modes](#supported-modes) section showed that only job *outputs* can write data, because the mode can be either `rw_mount` or `upload`.

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`), with the `outputs` section populated with the type and path where you'd like to write your data:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/CommandJob.schema.json

# Possible Paths for Data:
# Blob: https://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
# Datastore: azureml://datastores/paths/<folder>/<file>
# Data Asset: azureml:<my_data>:<version>

code: src
command: >-
  python prep.py 
  --raw_data ${{inputs.raw_data}} 
  --prep_data ${{outputs.prep_data}}
inputs:
  raw_data: 
    type: <type> # uri_file, uri_folder, mltable
    path: <path>
outputs:
  prep_data: 
    type: <type> # uri_file, uri_folder, mltable
    path: <path>
environment: azureml:<environment_name>@latest
compute: azureml:cpu-cluster
```

Next, create a job with the CLI:

```azurecli
az ml job create --file <file-name>.yml
```

# [Python SDK](#tab/python)

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Data
from azure.ai.ml import Input, Output
from azure.ai.ml.constants import AssetTypes

# Possible Asset Types for Data:
# AssetTypes.URI_FILE
# AssetTypes.URI_FOLDER
# AssetTypes.MLTABLE

# Possible Paths for Data:
# Blob: https://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
# Datastore: azureml://datastores/paths/<folder>/<file>
# Data Asset: azureml:<my_data>:<version>

my_job_inputs = {
    "raw_data": Input(type=AssetTypes.URI_FOLDER, path="<path>")
}

my_job_outputs = {
    "prep_data": Output(type=AssetTypes.URI_FOLDER, path="<path>")
}

job = command(
    code="./src",  # local path where the code is stored
    command="python process_data.py --raw_data ${{inputs.raw_data}} --prep_data ${{outputs.prep_data}}",
    inputs=my_job_inputs,
    outputs=my_job_outputs,
    environment="<environment_name>:<version>",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.create_or_update(job)
# get a URL for the status of the job
returned_job.services["Studio"].endpoint

```


## Data in pipelines

If you work with Azure Machine Learning pipelines, you can read data into and move data between pipeline components with the Azure Machine Learning CLI v2 extension, or the Python SDK v2.

### Azure Machine Learning CLI v2
This YAML file shows how to use the output data from one component as the input for another component of the pipeline, with the Azure Machine Learning CLI v2 extension:

[!INCLUDE [CLI v2](../../includes/machine-learning-CLI-v2.md)]

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

display_name: 3b_pipeline_with_data
description: Pipeline with 3 component jobs with data dependencies

settings:
  default_compute: azureml:cpu-cluster

outputs:
  final_pipeline_output:
    mode: rw_mount

jobs:
  component_a:
    type: command
    component: ./componentA.yml
    inputs:
      component_a_input: 
        type: uri_folder
        path: ./data

    outputs:
      component_a_output: 
        mode: rw_mount
  component_b:
    type: command
    component: ./componentB.yml
    inputs:
      component_b_input: ${{parent.jobs.component_a.outputs.component_a_output}}
    outputs:
      component_b_output: 
        mode: rw_mount
  component_c:
    type: command
    component: ./componentC.yml
    inputs:
      component_c_input: ${{parent.jobs.component_b.outputs.component_b_output}}
    outputs:
      component_c_output: ${{parent.outputs.final_pipeline_output}}
      #  mode: upload


```

### Python SDK v2

This example defines a pipeline that contains three nodes, and moves data between each node.

* `prepare_data_node` loads the image and labels from Fashion MNIST data set into `mnist_train.csv` and `mnist_test.csv`.
