* `models:/<model-name>/latest`, to load the last version of the model.
* `models:/<model-name>/<version-number>`, to load a specific version of the model.
* `models:/<model-name>/<stage-name>`, to load a specific version in a given stage for a model. View [Model stages](#model-stages) for details.

> [!TIP]
> For learning about the difference between `mlflow.<flavor>.load_model()` and `mlflow.pyfunc.load_model()`, view [Loading MLflow models back](concept-mlflow-models.md#loading-mlflow-models-back) article.

## Model stages

MLflow supports model's stages to manage model's lifecycle. Model's version can transition from one stage to another. Stages are assigned to a model's version (instead of models) which means that a given model can have multiple versions on different stages.

> [!IMPORTANT]
> Stages can only be accessed using the MLflow SDK. They don't show up in the [Azure ML Studio portal](https://ml.azure.com) and can't be retrieved using neither Azure ML SDK, Azure ML CLI, or Azure ML REST API. Creating deployment from a given model's stage is not supported by the moment.

### Querying model stages

You can use the MLflow client to check all the possible stages a model can be:

```python
client.get_model_version_stages(model_name, version="latest")
```

You can see what model's version is on each stage by getting the model from the registry. The following example gets the model's version currently in the stage `Staging`.

```python
client.get_latest_versions(model_name, stages=["Staging"])
```

> [!NOTE]
> Multiple versions can be in the same stage at the same time in Mlflow, however, this method returns the latest version (greater version) among all of them.

> [!WARNING]
> Stage names are case sensitive.

### Transitioning models

Transitioning a model's version to a particular stage can be done using the MLflow client. 

```python
client.transition_model_version_stage(model_name, version=3, stage="Staging")
```

By default, if there were an existing model version in that particular stage, it will remain there. Hence, it won't be replaced as multiple model's versions can be in the same stage at the same time. Alternatively, you can indicate `archive_existing_versions=True` to tell MLflow to move the existing model's version to the stage `Archived`.

```python
client.transition_model_version_stage(
    model_name, version=3, stage="Staging", archive_existing_versions=True
)
```

### Loading models from stages

ou can load a model in a particular stage directly from Python using the `load_model` function and the following URI format. Notice that for this method to success, you need to have all the libraries and dependencies already installed in the environment you're working at.

```python
model = mlflow.pyfunc.load_model(f"models:/{model_name}/Staging")
```

## Editing and deleting models

Editing registered models is supported in both Mlflow and Azure ML. However, there are some differences important to be noticed:

> [!WARNING]
> Renaming models is not supported in Azure Machine Learning as model objects are immmutable.

### Editing models

You can edit model's description and tags from a model using Mlflow:

```python
client.update_model_version(model_name, version=1, description="My classifier description")
```

To edit tags, you have to use the method `set_model_version_tag` and `remove_model_version_tag`:

```python
client.set_model_version_tag(model_name, version="1", key="type", value="classification")
```

Removing a tag:

```python
client.delete_model_version_tag(model_name, version="1", key="type")
```

### Deleting a model's version

You can delete any model version in the registry using the MLflow client, as demonstrated in the following example:

```python
client.delete_model_version(model_name, version="2")
```

> [!NOTE]
> Azure Machine Learning doesn't support deleting the entire model container. To achieve the same thing, you will need to delete all the model versions from a given model.

## Support matrix for managing models with MLflow
