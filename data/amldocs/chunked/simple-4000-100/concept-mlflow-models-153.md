> MLflow environments and Azure Machine Learning environments are different concepts. While the former opperates at the level of the model, the latter operates at the level of the workspace (for registered environments) or jobs/deployments (for annonymous environments). When you deploy MLflow models in Azure Machine Learning, the model's environment is built and used for deployment. Alternatively, you can override this behaviour with the [Azure ML CLI v2](concept-v2.md) and deploy MLflow models using a specific Azure Machine Learning environments.

### Model's predict function

All MLflow models contain a `predict` function. **This function is the one that is called when a model is deployed using a no-code-deployment experience**. What the `predict` function returns (classes, probabilities, a forecast, etc.) depend on the framework (i.e. flavor) used for training. Read the documentation of each flavor to know what they return.

In same cases, you may need to customize this function to change the way inference is executed. On those cases, you will need to [log models with a different behavior in the predict method](how-to-log-mlflow-models.md#logging-models-with-a-different-behavior-in-the-predict-method) or [log a custom model's flavor](how-to-log-mlflow-models.md#logging-custom-models).

## Loading MLflow models back

Models created as MLflow models can be loaded back directly from the run where they were logged, from the file system where they are saved or from the model registry where they are registered. MLflow provides a consistent way to load those models regardless of the location.

There are two workflows available for loading models:

* **Loading back the same object and types that were logged:** You can load models using MLflow SDK and obtain an instance of the model with types belonging to the training library. For instance, an ONNX model will return a `ModelProto` while a decision tree trained with Scikit-Learn model will return a `DecisionTreeClassifier` object. Use `mlflow.<flavor>.load_model()` to do so.
* **Loading back a model for running inference:** You can load models using MLflow SDK and obtain a wrapper where MLflow warranties there will be a `predict` function. It doesn't matter which flavor you are using, every MLflow model needs to implement this contract. Furthermore, MLflow warranties that this function can be called using arguments of type `pandas.DataFrame`, `numpy.ndarray` or `dict[string, numpyndarray]` (depending on the signature of the model). MLflow handles the type conversion to the input type the model actually expects. Use `mlflow.pyfunc.load_model()` to do so.

## Start logging models

We recommend starting taking advantage of MLflow models in Azure Machine Learning. There are different ways to start using the model's concept with MLflow. Read [How to log MLFlow models](how-to-log-mlflow-models.md) to a comprehensive guide.

