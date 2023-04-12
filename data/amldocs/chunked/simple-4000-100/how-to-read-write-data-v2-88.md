1. The `type`; whether the data is a specific file (`uri_file`), a folder location (`uri_folder`), or an `mltable`.
1. The `path` of your data location; any of the paths outlined in the [Supported Paths](#supported-paths) section will work.

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Data
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

# Possible Asset Types for Data:
# AssetTypes.URI_FILE
# AssetTypes.URI_FOLDER
# AssetTypes.MLTABLE

# Possible Paths for Data:
# Blob: https://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
# Datastore: azureml://datastores/paths/<folder>/<file>
# Data Asset: azureml:<my_data>:<version>

my_job_inputs = {
    "input_data": Input(type=AssetTypes.URI_FOLDER, path="<path>")
}

job = command(
    code="./src",  # local path where the code is stored
    command="ls ${{inputs.input_data}}",
    inputs=my_job_inputs,
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:latest",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.jobs.create_or_update(job)
# get a URL for the status of the job
returned_job.services["Studio"].endpoint
```


### Read V1 data assets
This section explains how to read V1 `FileDataset` and `TabularDataset` data entities in a V2 job.

#### Read a `FileDataset`

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`), with the type set to `mltable` and the mode set to `eval_mount`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

command: |
  ls ${{inputs.my_data}}
code: <folder where code is located>
inputs:
  my_data:
    type: mltable
    mode: eval_mount
    path: azureml:<filedataset_name>@latest
environment: azureml:<environment_name>@latest
compute: azureml:cpu-cluster
```

Next, run in the CLI

```azurecli
az ml job create -f <file-name>.yml
```

# [Python SDK](#tab/python)

In the `Input` object, specify the `type` as `AssetTypes.MLTABLE` and `mode` as `InputOutputModes.EVAL_MOUNT`:

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Data
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

filedataset_asset = ml_client.data.get(name="<filedataset_name>", version="<version>")

my_job_inputs = {
    "input_data": Input(
            type=AssetTypes.MLTABLE, 
            path=filedataset_asset,
            mode=InputOutputModes.EVAL_MOUNT
    )
}

job = command(
    code="./src",  # local path where the code is stored
    command="ls ${{inputs.input_data}}",
    inputs=my_job_inputs,
    environment="<environment_name>:<version>",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.jobs.create_or_update(job)
# get a URL for the job status
returned_job.services["Studio"].endpoint
```


#### Read a `TabularDataset`

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`), with the type set to `mltable` and the mode set to `direct`:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

command: |
  ls ${{inputs.my_data}}
code: <folder where code is located>
inputs:
  my_data:
    type: mltable
    mode: direct
    path: azureml:<tabulardataset_name>@latest
environment: azureml:<environment_name>@latest
compute: azureml:cpu-cluster
```

Next, run in the CLI

```azurecli
az ml job create -f <file-name>.yml
```

# [Python SDK](#tab/python)

In the `Input` object, specify the `type` as `AssetTypes.MLTABLE`, and `mode` as `InputOutputModes.DIRECT`:

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Data
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml import MLClient

ml_client = MLClient.from_config()

filedataset_asset = ml_client.data.get(name="<tabulardataset_name>", version="<version>")

my_job_inputs = {
    "input_data": Input(
            type=AssetTypes.MLTABLE, 
            path=filedataset_asset,
            mode=InputOutputModes.DIRECT
    )
}

job = command(
    code="./src",  # local path where the code is stored
    command="python train.py --inputs ${{inputs.input_data}}",
    inputs=my_job_inputs,
    environment="<environment_name>:<version>",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.jobs.create_or_update(job)
# get a URL for the status of the job
returned_job.services["Studio"].endpoint
```
