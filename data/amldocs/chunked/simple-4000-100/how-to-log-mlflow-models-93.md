
> [!NOTE]
> * `log_models=False` is configured in `autolog`. This prevents MLflow to automatically log the model, as it is done manually later.
> * `infer_signature` is a convenient method to try to infer the signature directly from inputs and outputs.
> * `mlflow.utils.environment._mlflow_conda_env` is a private method in MLflow SDK and it may change in the future. This example uses it just for sake of simplicity, but it must be used with caution or generate the YAML definition manually as a Python dictionary. 

## Logging models with a different behavior in the predict method

When you log a model using either `mlflow.autolog` or using `mlflow.<flavor>.log_model`, the flavor used for the model decides how inference should be executed and what gets returned by the model. MLflow doesn't enforce any specific behavior in how the `predict` generate results. There are scenarios where you probably want to do some pre-processing or post-processing before and after your model is executed.

A solution to this scenario is to implement machine learning pipelines that moves from inputs to outputs directly. Although this is possible (and sometimes encourageable for performance considerations), it may be challenging to achieve. For those cases, you probably want to [customize how your model does inference using a  custom models](#logging-custom-models) as explained in the following section.

## Logging custom models

MLflow provides support for a variety of [machine learning frameworks](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) including FastAI, MXNet Gluon, PyTorch, TensorFlow, XGBoost, CatBoost, h2o, Keras, LightGBM, MLeap, ONNX, Prophet, spaCy, Spark MLLib, Scikit-Learn, and statsmodels. However, there may be times where you need to change how a flavor works, log a model not natively supported by MLflow or even log a model that uses multiple elements from different frameworks. For those cases, you may need to create a custom model flavor.

For this type of models, MLflow introduces a flavor called `pyfunc` (standing from Python function). Basically this flavor allows you to log any object you want as a model, as long as it satisfies two conditions:

* You implement the method `predict` (at least).
* The Python object inherits from `mlflow.pyfunc.PythonModel`.

> [!TIP]
> Serializable models that implements the Scikit-learn API can use the Scikit-learn flavor to log the model, regardless of whether the model was built with Scikit-learn. If your model can be persisted in Pickle format and the object has methods `predict()` and `predict_proba()` (at least), then you can use `mlflow.sklearn.log_model()` to log it inside a MLflow run.

# [Using a model wrapper](#tab/wrapper)

The simplest way of creating your custom model's flavor is by creating a wrapper around your existing model object. MLflow will serialize it and package it for you. Python objects are serializable when the object can be stored in the file system as a file (generally in Pickle format). During runtime, the object can be materialized from such file and all the values, properties and methods available when it was saved will be restored.

Use this method when:
> [!div class="checklist"]
> * Your model can be serialized in Pickle format.
> * You want to retain the models state as it was just after training.
> * You want to customize the way the `predict` function works.

The following sample wraps a model created with XGBoost to make it behaves in a different way to the default implementation of the XGBoost flavor (it returns the probabilities instead of the classes):

```python
from mlflow.pyfunc import PythonModel, PythonModelContext

class ModelWrapper(PythonModel):
    def __init__(self, model):
        self._model = model

    def predict(self, context: PythonModelContext, data):
        # You don't have to keep the semantic meaning of `predict`. You can use here model.recommend(), model.forecast(), etc
        return self._model.predict_proba(data)

    # You can even add extra functions if you need to. Since the model is serialized,
    # all of them will be available when you load your model back.
    def predict_batch(self, data):
        pass
```
