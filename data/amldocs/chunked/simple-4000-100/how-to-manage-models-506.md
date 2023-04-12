## Use model as output in a job

In your job you can write model to your cloud-based storage using *outputs*. 

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`), with the `outputs` section populated with the type and path of where you would like to write your data to:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

# Possible Paths for Model:
# Local path: mlflow-model/model.pkl
# AzureML Datastore: azureml://datastores/<datastore-name>/paths/<path_on_datastore>
# MLflow run: runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>
# Job: azureml://jobs/<job-name>/outputs/<output-name>/paths/<path-to-model-relative-to-the-named-output-location>
# Model Asset: azureml:<my_model>:<version>

code: src
command: >-
  python hello-model-as-output.py 
  --input_model ${{inputs.input_model}} 
  --custom_model_output ${{outputs.output_folder}}
inputs:
  input_model: 
    type: mlflow_model # mlflow_model,custom_model, triton_model
    path: ../../assets/model/mlflow-model
outputs:
  output_folder: 
    type: custom_model # mlflow_model,custom_model, triton_model
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster
```

Next create a job using the CLI:

```azurecli
az ml job create --file <file-name>.yml
```
For a complete example, see the [model GitHub repo](https://github.com/Azure/azureml-examples/tree/main/cli/assets/model).

# [Python SDK](#tab/python)

```python
from azure.ai.ml import command
from azure.ai.ml.entities import Model
from azure.ai.ml import Input, Output
from azure.ai.ml.constants import AssetTypes

# Possible Asset Types for Model:
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
    "input_model": Input(type=AssetTypes.MLFLOW_MODEL, path="mlflow-model"),
    "input_data": Input(type=AssetTypes.URI_FILE, path="./mlflow-model/input_example.json"),
}

my_job_outputs = {
    "output_folder": Output(type=AssetTypes.CUSTOM_MODEL)
}

job = command(
    code="./src",  # local path where the code is stored
    command="python load_write_model.py --input_model ${{inputs.input_model}} --output_folder ${{outputs.output_folder}}",
    inputs=my_job_inputs,
    outputs=my_job_outputs,
    environment="AzureML-sklearn-0.24-ubuntu18.04-py37-cpu:9",
    compute="cpu-cluster",
)

# submit the command
returned_job = ml_client.create_or_update(job)
# get a URL for the status of the job
returned_job.services["Studio"].endpoint

```

## Next steps

* [Install and set up Python SDK v2](https://aka.ms/sdk-v2-install)
* [No-code deployment for MLflow models](how-to-deploy-mlflow-models-online-endpoints.md)
* Learn more about [MLflow and Azure Machine Learning](concept-mlflow.md)
