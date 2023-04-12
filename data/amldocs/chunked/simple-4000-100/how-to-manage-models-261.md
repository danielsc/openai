This option is an `azureml job` reference URI format, which helps you register a model from artifacts in any of the job's outputs. This format is aligned with the existing `azureml` datastore reference URI format, and also supports referencing artifacts from named outputs of the job (not just the default artifact location). You can establish a lineage between a registered model and the job it was trained from, if you didn't directly register your model within the training script by using MLflow.

Format:
`azureml://jobs/<job-name>/outputs/<output-name>/paths/<path-to-model-relative-to-the-named-output-location>`

Examples:
- Default artifact location: `azureml://jobs/<run-id>/outputs/artifacts/paths/model/`
  * This is equivalent to `runs:/<run-id>/model/`.
  * *artifacts* is the reserved keyword to refer to the output that represents the default artifact location.
- From a named output directory: `azureml://jobs/<run-id>/outputs/trained-model`
- From a specific file or folder path within the named output directory:
  * `azureml://jobs/<run-id>/outputs/trained-model/paths/cifar.pt`
  * `azureml://jobs/<run-id>/outputs/checkpoints/paths/model/`

Saving model from a named output:

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

job_name = "<JOB_NAME>"

run_model = Model(
    path=f"azureml://jobs/{job_name}/outputs/artifacts/paths/model/",
    name="run-model-example",
    description="Model created from run.",
    type=AssetTypes.MLFLOW_MODEL,
)
# Uncomment after adding required details above
# ml_client.models.create_or_update(run_model)
```


For a complete example, see the [model notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/assets/model/model.ipynb).


### Register your model as an asset in Machine Learning by using the UI

To create a model in Machine Learning, from the UI, open the **Models** page. Select **Register model**, and select where your model is located. Fill out the required fields, and then select **Register**.

:::image type="content" source="./media/how-to-manage-models/register-model-local.png" alt-text="Screenshot of the UI to register a model." lightbox="./media/how-to-manage-models/register-model-local.png":::


## Manage models

The SDK and CLI (v2) also allow you to manage the lifecycle of your Azure ML model assets.

### List

List all the models in your workspace:

# [Azure CLI](#tab/cli)

```cli
az ml model list
```

# [Python SDK](#tab/python)

```python
models = ml_client.models.list()
for model in models:
    print(model.name)
```


List all the model versions under a given name:

# [Azure CLI](#tab/cli)

```cli
az ml model list --name run-model-example
```

# [Python SDK](#tab/python)

```python
models = ml_client.models.list(name="run-model-example")
for model in models:
    print(model.version)
```


### Show

Get the details of a specific model:

# [Azure CLI](#tab/cli)

```cli
az ml model show --name run-model-example --version 1
```

# [Python SDK](#tab/python)

```python
model_example = ml_client.models.get(name="run-model-example", version="1")
print(model_example)
```

### Update

Update mutable properties of a specific model:

# [Azure CLI](#tab/cli)

```cli
az ml model update --name  run-model-example --version 1 --set description="This is an updated description." --set tags.stage="Prod"
```

# [Python SDK](#tab/python)

```python
model_example.description="This is an updated description."
model_example.tags={"stage":"Prod"}
ml_client.models.create_or_update(model=model_example)
```

> [!IMPORTANT]
> For model, only `description` and `tags` can be updated. All other properties are immutable; if you need to change any of those properties you should create a new version of the model.

### Archive

Archiving a model will hide it by default from list queries (`az ml model list`). You can still continue to reference and use an archived model in your workflows. You can archive either all versions of a model or only a specific version.
