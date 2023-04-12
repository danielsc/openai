
# Logging MLflow models

The following article explains how to start logging your trained models (or artifacts) as MLflow models. It explores the different methods to customize the way MLflow packages your models and hence how it runs them. 

## Why logging models instead of artifacts?

If you are not familiar with MLflow, you may not be aware of the difference between logging artifacts or files vs. logging MLflow models. We recommend reading the article [From artifacts to models in MLflow](concept-mlflow-models.md) for an introduction to the topic.

A model in MLflow is also an artifact, but with a specific structure that serves as a contract between the person that created the model and the person that intends to use it. Such contract helps build the bridge about the artifacts themselves and what they mean.

Logging models has the following advantages:
> [!div class="checklist"]
> * Models can be directly loaded for inference using `mlflow.<flavor>.load_model` and use the `predict` function.
> * Models can be used as pipelines inputs directly.
> * Models can be deployed without indicating a scoring script nor an environment.
> * Swagger is enabled in deployed endpoints automatically and the __Test__ feature can be used in Azure ML studio.
> * You can use the Responsible AI dashboard.

There are different ways to start using the model's concept in Azure Machine Learning with MLflow, as explained in the following sections:

## Logging models using autolog

One of the simplest ways to start using this approach is by using MLflow autolog functionality. Autolog allows MLflow to instruct the framework associated to with the framework you are using to log all the metrics, parameters, artifacts and models that the framework considers relevant. By default, most models will be log if autolog is enabled. Some flavors may decide not to do that in specific situations. For instance, the flavor PySpark won't log models if they exceed a certain size.

You can turn on autologging by using either `mlflow.autolog()` or `mlflow.<flavor>.autolog()`. The following example uses `autolog()` for logging a classifier model trained with XGBoost:

```python
import mlflow
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

mlflow.autolog()

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
```

> [!TIP]
> If you are using Machine Learning pipelines, like for instance [Scikit-Learn pipelines](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html), use the `autolog` functionality of that flavor for logging models. Models are automatically logged when the `fit()` method is called on the pipeline object. The notebook [Training and tracking an XGBoost classifier with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_classification_mlflow.ipynb) demonstrates how to log a model with preprocessing using pipelines.

## Logging models with a custom signature, environment or samples

You can log models manually using the method `mlflow.<flavor>.log_model` in MLflow. Such workflow has the advantages of retaining control of different aspects of how the model is logged. 

Use this method when:
> [!div class="checklist"]
> * You want to indicate pip packages or a conda environment different from the ones that are automatically detected.
> * You want to include input examples.
> * You want to include specific artifacts into the package that will be needed.
> * Your signature is not correctly inferred by `autolog`. This is specifically important when you deal with inputs that are tensors where the signature needs specific shapes.
> * Somehow the default behavior of autolog doesn't fill your purpose.

The following example code logs a model for an XGBoost classifier:

```python
import mlflow
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from mlflow.models import infer_signature
from mlflow.utils.environment import _mlflow_conda_env

mlflow.autolog(log_models=False)

model = XGBClassifier(use_label_encoder=False, eval_metric="logloss")
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=False)
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

# Signature
signature = infer_signature(X_test, y_test)

# Conda environment
custom_env =_mlflow_conda_env(
    additional_conda_deps=None,
    additional_pip_deps=["xgboost==1.5.2"],
    additional_conda_channels=None,
)

# Sample
input_example = X_train.sample(n=1)

# Log the model manually
mlflow.xgboost.log_model(model, 
                         artifact_path="classifier", 
                         conda_env=custom_env,
                         signature=signature,
                         input_example=input_example)
```
