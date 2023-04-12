
# MLflow and Azure Machine Learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of the Azure Machine Learning developer platform that you're using:"]
> * [v1](v1/concept-mlflow-v1.md)
> * [v2 (current version)](concept-mlflow.md)

[MLflow](https://www.mlflow.org) is an open-source framework that's designed to manage the complete machine learning lifecycle. Its ability to train and serve models on different platforms allows you to use a consistent set of tools regardless of where your experiments are running: locally on your computer, on a remote compute target, on a virtual machine, or on an Azure Machine Learning compute instance.

> [!TIP]
> Azure Machine Learning workspaces are MLflow-compatible, which means you can use Azure Machine Learning workspaces in the same way that you use an MLflow tracking server. Such compatibility has the following advantages:
> * We don't host MLflow server instances under the hood. The workspace can talk the MLflow standard.
> * You can use Azure Machine Learning workspaces as your tracking server for any MLflow code, whether it runs on Azure Machine Learning or not. You only need to configure MLflow to point to the workspace where the tracking should happen.
> * You can run any training routine that uses MLflow in Azure Machine Learning without any change.

> [!NOTE]
> Unlike the Azure Machine Learning SDK v1, there's no logging functionality in the SDK v2 and we recommend using MLflow for logging. Such strategy allows your training routines to become cloud-agnostic and portable, removing any dependency in your code with Azure Machine Learning.

## Tracking with MLflow

Azure Machine Learning uses MLflow Tracking for metric logging and artifact storage for your experiments. When connected to Azure Machine Learning, all tracking performed using MLflow is materialized in the workspace you are working on. To learn more about how to instrument your experiments for tracking experiments and training routines, see [Log metrics, parameters, and files with MLflow](how-to-log-view-metrics.md). You can also use MLflow to [Query & compare experiments and runs with MLflow](how-to-track-experiments-mlflow.md).


### Centralize tracking

You can connect MLflow to Azure Machine Learning workspaces even when you are running locally or in a different cloud. The workspace provides a centralized, secure, and scalable location to store training metrics and models.

Capabilities include:

* [Track machine learning experiments and models running locally or in the cloud](how-to-use-mlflow-cli-runs.md) with MLflow in Azure Machine Learning.
* [Track Azure Databricks machine learning experiments](how-to-use-mlflow-azure-databricks.md) with MLflow in Azure Machine Learning.
* [Track Azure Synapse Analytics machine learning experiments](how-to-use-mlflow-azure-synapse.md) with MLflow in Azure Machine Learning.

### Example notebooks

* [Training and tracking an XGBoost classifier with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_classification_mlflow.ipynb): Demonstrates how to track experiments by using MLflow, log models, and combine multiple flavors into pipelines.
* [Training and tracking an XGBoost classifier with MLflow using service principal authentication](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_service_principal.ipynb): Demonstrates how to track experiments by using MLflow from compute that's running outside Azure Machine Learning. It shows how to authenticate against Azure Machine Learning services by using a service principal.
* [Hyper-parameter optimization using Hyperopt and nested runs in MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_nested_runs.ipynb): Demonstrates how to use child runs in MLflow to do hyper-parameter optimization for models by using the popular library Hyperopt. It shows how to transfer metrics, parameters, and artifacts from child runs to parent runs.
