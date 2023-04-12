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

```cli
az ml model create --name my-model --version 1 --path azureml://jobs/<run-id>/outputs/trained-model
```

For a complete example, see the [CLI reference](/cli/azure/ml/model).


### Register your model as an asset in Machine Learning by using the SDK

Use the following tabs to select where your model is located.

# [Local model](#tab/use-local)

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

file_model = Model(
    path="mlflow-model/model.pkl",
    type=AssetTypes.CUSTOM_MODEL,
    name="local-file-example",
    description="Model created from local file.",
)
ml_client.models.create_or_update(file_model)
```

# [Datastore](#tab/use-datastore)

You can create a model from a cloud path by using any one of the following supported URI formats.

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

cloud_model = Model(
    path=file_model.path,
    # The above line basically provides a path in the format "azureml://subscriptions/XXXXXXXXXXXXXXXX/resourceGroups/XXXXXXXXXXX/workspaces/XXXXXXXXXXX/datastores/workspaceblobstore/paths/model.pkl"
    # Users could also use,"azureml://datastores/workspaceblobstore/paths/model.pkl" as a shorthand to the same location
    name="cloud-path-example",
    type=AssetTypes.CUSTOM_MODEL,
    description="Model created from cloud path.",
)
ml_client.models.create_or_update(cloud_model)
```


The examples use the shorthand `azureml` scheme for pointing to a path on the `datastore` by using the syntax `azureml://datastores/${{datastore-name}}/paths/${{path_on_datastore}}`.

# [Job output](#tab/use-job-output)

You have two options here. You can use the MLflow run URI format, or you can use the `azureml job` URI format.

### MLflow

This option is optimized for MLflow users, who are likely already familiar with the MLflow run URI format. This option helps you create a model from artifacts in the default artifact location (where all MLflow-logged models and artifacts are located). This establishes a lineage between a registered model and the run the model came from.

Format:
`runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>`

Example:
`runs:/<run-id>/model/`

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import ModelType

run_model = Model(
    path="runs:/<run-id>/model/"
    name="run-model-example",
    description="Model created from run.",
    type=ModelType.MLFLOW
)

ml_client.models.create_or_update(run_model) 
```

### azureml job

This option is an `azureml job` reference URI format, which helps you register a model from artifacts in any of the job's outputs. This format is aligned with the existing `azureml` datastore reference URI format, and also supports referencing artifacts from named outputs of the job (not just the default artifact location). You can establish a lineage between a registered model and the job it was trained from, if you didn't directly register your model within the training script by using MLflow.
