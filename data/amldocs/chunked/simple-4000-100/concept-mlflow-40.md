* [Hyper-parameter optimization using Hyperopt and nested runs in MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_nested_runs.ipynb): Demonstrates how to use child runs in MLflow to do hyper-parameter optimization for models by using the popular library Hyperopt. It shows how to transfer metrics, parameters, and artifacts from child runs to parent runs.
* [Logging models with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/logging_and_customizing_models.ipynb): Demonstrates how to use the concept of models instead of artifacts with MLflow, including how to construct custom models.
* [Manage runs and experiments with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/runs-management/run_history.ipynb): Demonstrates how to query experiments, runs, metrics, parameters, and artifacts from Azure Machine Learning by using MLflow.

> [!IMPORTANT]
> - MLflow in R support is limited to tracking experiment's metrics, parameters and models on Azure Machine Learning jobs. Interactive training on RStudio, Posit (formerly RStudio Workbench) or Jupyter Notebooks with R kernels is not supported. Model management and registration is not supported using the MLflow R SDK. As an alternative, use Azure ML CLI or [Azure ML studio](https://ml.azure.com) for model registration and management. View the following [R example about using the MLflow tracking client with Azure Machine Learning](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/single-step/r).
> - MLflow in Java support is limited to tracking experiment's metrics and parameters on Azure Machine Learning jobs. Artifacts and models can't be tracked using the MLflow Java SDK. As an alternative, use the `Outputs` folder in jobs along with the method `mlflow.save_model` to save models (or artifacts) you want to capture. View the following [Java example about using the MLflow tracking client with the Azure Machine Learning](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/single-step/java/iris).

## Model registries with MLflow

Azure Machine Learning supports MLflow for model management. This support represents a convenient way to support the entire model lifecycle for users who are familiar with the MLflow client.

To learn more about how to manage models by using the MLflow API in Azure Machine Learning, view [Manage model registries in Azure Machine Learning with MLflow](how-to-manage-models-mlflow.md).

### Example notebooks

* [Manage model registries with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/model-management/model_management.ipynb): Demonstrates how to manage models in registries by using MLflow.

## Model deployment with MLflow

You can [deploy MLflow models to Azure Machine Learning](how-to-deploy-mlflow-models.md) and take advantage of the improved experience when you use this type of models. Azure Machine Learning supports deploying MLflow models to both real-time and batch endpoints without having to indicate and environment or a scoring script. Deployment is supported using either MLflow SDK, Azure Machine Learning CLI, Azure Machine Learning SDK for Python, or the [Azure Machine Learning studio](https://ml.azure.com) portal.

Learn more at [Guidelines for deploying MLflow models](how-to-deploy-mlflow-models.md).

### Example notebooks

* [Deploy MLflow to Online Endpoints](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_online_endpoints.ipynb): Demonstrates how to deploy models in MLflow format to online endpoints using MLflow SDK.
* [Deploy MLflow to Online Endpoints with safe rollout](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_online_endpoints_progresive.ipynb): Demonstrates how to deploy models in MLflow format to online endpoints using MLflow SDK with progressive rollout of models and the deployment of multiple model's versions in the same endpoint.
