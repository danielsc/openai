Archiving a model will hide it by default from list queries (`az ml model list`). You can still continue to reference and use an archived model in your workflows. You can archive either all versions of a model or only a specific version.

If you don't specify a version, all versions of the model under that given name will be archived. If you create a new model version under an archived model container, that new version will automatically be set as archived as well.

Archive all versions of a model:

# [Azure CLI](#tab/cli)

```cli
az ml model archive --name run-model-example
```

# [Python SDK](#tab/python)

```python
ml_client.models.archive(name="run-model-example")
```

            
Archive a specific model version:

# [Azure CLI](#tab/cli)

```cli
az ml model archive --name run-model-example --version 1
```

# [Python SDK](#tab/python)

```python
ml_client.models.archive(name="run-model-example", version="1")
```


## Use model for training

The SDK and CLI (v2) also allow you to use a model in a training job as an input or output.

## Use model as input in a job

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`). Specify in the `inputs` section of the job:

1. The `type`; whether the model is a `mlflow_model`,`custom_model` or `triton_model`. 
1. The `path` of where your data is located; can be any of the paths outlined in the [Supported Paths](#supported-paths) section. 

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

# Possible Paths for models:
# AzureML Datastore: azureml://datastores/<datastore-name>/paths/<path_on_datastore>
# MLflow run: runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>
# Job: azureml://jobs/<job-name>/outputs/<output-name>/paths/<path-to-model-relative-to-the-named-output-location>
# Model Asset: azureml:<my_model>:<version>

command: |
  ls ${{inputs.my_model}}
inputs:
  my_model:
    type: mlflow_model # List of all model types here: https://learn.microsoft.com/azure/machine-learning/reference-yaml-model#yaml-syntax
    path: ../../assets/model/mlflow-model
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

Next, run in the CLI

```azurecli
az ml job create -f <file-name>.yml
```

For a complete example, see the [model GitHub repo](https://github.com/Azure/azureml-examples/tree/main/cli/assets/model).


# [Python SDK](#tab/python)

The `Input` class allows you to define:

1. The `type`; whether the model is a `mlflow_model`,`custom_model` or `triton_model`. 
1. The `path` of where your data is located; can be any of the paths outlined in the [Supported Paths](#supported-paths) section. 

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Model
from azure.ai.ml import Input
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import MLClient

# Possible Asset Types for Data:
# AssetTypes.MLFLOW_MODEL
# AssetTypes.CUSTOM_MODEL
# AssetTypes.TRITON_MODEL

# Possible Paths for Model:
# Local path: mlflow-model/model.pkl
# AzureML Datastore: azureml://datastores/<datastore-name>/paths/<path_on_datastore>
# MLflow run: runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>
# Job: azureml://jobs/<job-name>/outputs/<output-name>/paths/<path-to-model-relative-to-the-named-output-location>
# Model Asset: azureml:<my_model>:<version>

my_job_inputs = {
    "input_model": Input(type=AssetTypes.MLFLOW_MODEL, path="mlflowmodel")
}

job = command(
    code="./src",  # local path where the code is stored
    command="ls ${{inputs.input_model}}",
    inputs=my_job_inputs,
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:9",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.jobs.create_or_update(job)
# get a URL for the status of the job
returned_job.services["Studio"].endpoint
```

## Use model as output in a job

In your job you can write model to your cloud-based storage using *outputs*. 
