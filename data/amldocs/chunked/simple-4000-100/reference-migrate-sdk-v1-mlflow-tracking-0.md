
# Migrate logging from SDK v1 to SDK v2

Azure Machine Learning uses MLflow Tracking for metric logging and artifact storage for your experiments, whether you created the experiments via the Azure Machine Learning Python SDK, the Azure Machine Learning CLI, or Azure Machine Learning studio. We recommend using MLflow for tracking experiments. 

If you're migrating from SDK v1 to SDK v2, use the information in this section to understand the MLflow equivalents of SDK v1 logging APIs.

## Why MLflow?

MLflow, with over 13 million monthly downloads, has become the standard platform for end-to-end MLOps, enabling teams of all sizes to track, share, package and deploy any model for batch or real-time inference. By integrating with MLflow, your training code will not need to hold any specific code related to Azure Machine Learning, achieving true portability and seamless integration with other open-source platforms.

## Prepare for migrating to MLflow

To use MLflow tracking, you will need to install `mlflow` and `azureml-mlflow` Python packages. All Azure Machine Learning environments have these packages already available for you but you will need to include them if creating your own environment.

```bash
pip install mlflow azureml-mlflow
```

> [!TIP]
> You can use the [`mlflow-skinny`](https://github.com/mlflow/mlflow/blob/master/README_SKINNY.rst) which is a lightweight MLflow package without SQL storage, server, UI, or data science dependencies. This is recommended for users who primarily need the tracking and logging capabilities without importing the full suite of MLflow features including deployments.

## Connect to your workspace

Azure Machine Learning allows users to perform tracking in training jobs running on your workspace or running remotely (tracking experiments running outside Azure Machine Learning). If performing remote tracking, you will need to indicate the workspace you want to connect MLflow to.

# [Azure Machine Learning compute](#tab/aml)

You are already connected to your workspace when running on Azure Machine Learning compute.

# [Remote compute](#tab/remote)

**Configure tracking URI**

[!INCLUDE [configure-mlflow-tracking](../../includes/machine-learning-mlflow-configure-tracking.md)]

**Configure authentication**

Once the tracking is configured, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials. Refer to [Configure MLflow for Azure Machine Learning: Configure authentication](how-to-use-mlflow-configure-tracking.md#configure-authentication) for more ways to configure authentication for MLflow in Azure Machine Learning workspaces.

[!INCLUDE [configure-mlflow-auth](../../includes/machine-learning-mlflow-configure-auth.md)]


## Experiments and runs

__SDK v1__

```python
from azureml.core import Experiment

# create an AzureML experiment and start a run
experiment = Experiment(ws, "create-experiment-sdk-v1")
azureml_run = experiment.start_logging()
```

__SDK v2 with MLflow__

```python
# Set the MLflow experiment and start a run
mlflow.set_experiment("logging-with-mlflow")
mlflow_run = mlflow.start_run()
```

## Logging API comparison

### Log an integer or float metric

__SDK v1__

```python
azureml_run.log("sample_int_metric", 1)
```

__SDK v2 with MLflow__

```python
mlflow.log_metric("sample_int_metric", 1)
```

### Log a boolean metric

__SDK v1__

```python
azureml_run.log("sample_boolean_metric", True)
```

__SDK v2 with MLflow__

```python
mlflow.log_metric("sample_boolean_metric", 1)
```

### Log a string metric

__SDK v1__

```python
azureml_run.log("sample_string_metric", "a_metric")
```

__SDK v2 with MLflow__

```python
mlflow.log_text("sample_string_text", "string.txt")
```

* The string will be logged as an _artifact_, not as a metric. In Azure Machine Learning studio, the value will be displayed in the __Outputs + logs__ tab.
