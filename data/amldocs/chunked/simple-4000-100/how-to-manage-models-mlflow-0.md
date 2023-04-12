
# Manage models registries in Azure Machine Learning with MLflow

Azure Machine Learning supports MLflow for model management. This represents a convenient way to support the entire model lifecycle for users familiar with the MLFlow client. The following article describes the different capabilities and how it compares with other options.

### Prerequisites

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]

* Some operations may be executed directly using the MLflow fluent API (`mlflow.<method>`). However, others may require to create an MLflow client, which allows to communicate with Azure Machine Learning in the MLflow protocol. You can create an `MlflowClient` object as follows. This tutorial will use the object `client` to refer to such MLflow client.

    ```python
    using mlflow

    client = mlflow.tracking.MlflowClient()
    ```

## Registering new models in the registry

### Creating models from an existing run 

If you have an MLflow model logged inside of a run and you want to register it in a registry, you can do that by using the run ID and the path where the model was logged. See [Manage experiments and runs with MLflow](how-to-track-experiments-mlflow.md) to know how to query this information if you don't have it.

```python
mlflow.register_model(f"runs:/{run_id}/{artifact_path}", model_name)
```

> [!NOTE]
> Models can only be registered to the registry in the same workspace where the run was tracked. Cross-workspace operations are not supported by the moment in Azure Machine Learning.

> [!TIP]
> We recommend to register models from runs or using the method `mlflow.<flavor>.log_model` from inside the run as it keeps lineage from the job that generated the asset.

### Creating models from assets

If you have a folder with an MLModel MLflow model, then you can register it directly. There's no need for the model to be always in the context of a run. To do that you can use the URI schema `file://path/to/model` to register MLflow models stored in the local file system. Let's create a simple model using `Scikit-Learn` and save it in MLflow format in the local storage:

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

mlflow.sklearn.save_model(reg, "./regressor")
```

> [!TIP]
> The method `save_model()` works in the same way as `log_model()`. While `log_model()` saves the model inside on an active run, `save_model()` uses the local file system for saving the model.

You can now register the model from the local path:

```python
import os

model_local_path = os.path.abspath("./regressor")
mlflow.register_model(f"file://{model_local_path}", "local-model-test")
```

## Querying model registries

### Querying all the models in the registry

You can query all the registered models in the registry using the MLflow client. The following sample prints all the model's names:

```python
for model in client.search_registered_models():
    print(f"{model.name}")
```

> [!NOTE]
> __MLflow 2.0 advisory:__ In older versions of Mlflow (<2.0), use method `MlflowClient.list_registered_models()` instead.

### Getting specific versions of the model

The command above will retrieve the model object which contains all the model versions. However, if you want to get the last registered model version of a given model, you can use `get_registered_model`:

```python
client.get_registered_model(model_name)
```

If you need a specific version of the model, you can indicate so:

```python
client.get_model_version(model_name, version=2)
```

## Loading models from registry

You can load models directly from the registry to restore the models objects that were logged. Use the functions `mlflow.<flavor>.load_model()` or `mlflow.pyfunc.load_model()` indicating the URI of the model you want to load using the following syntax:

* `models:/<model-name>/latest`, to load the last version of the model.
* `models:/<model-name>/<version-number>`, to load a specific version of the model.
