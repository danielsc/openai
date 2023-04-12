
# Train with MLflow Projects in Azure Machine Learning (Preview)

In this article, learn how to submit training jobs with [MLflow Projects](https://www.mlflow.org/docs/latest/projects.html) that uses Azure Machine Learning workspaces for tracking. You can submit jobs and only track them with Azure Machine Learning or migrate your runs to the cloud to run completely on [Azure Machine Learning Compute](./how-to-create-attach-compute-cluster.md).

[MLflow Projects](https://mlflow.org/docs/latest/projects.html) allow for you to organize and describe your code to let other data scientists (or automated tools) run it. MLflow Projects with Azure Machine Learning enable you to track and manage your training runs in your workspace.

[Learn more about the MLflow and Azure Machine Learning integration.](concept-mlflow.md)

## Prerequisites

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]

* Using Azure Machine Learning as backend for MLflow projects requires the package `azureml-core`:

  ```bash
  pip install azureml-core
  ```

### Connect to your workspace

If you're working outside Azure Machine Learning, you need to configure MLflow to point to your Azure Machine Learning workspace's tracking URI. You can find the instructions at [Configure MLflow for Azure Machine Learning](how-to-use-mlflow-configure-tracking.md).


## Track MLflow Projects in Azure Machine Learning workspaces

This example shows how to submit MLflow projects and track them Azure Machine Learning.

1. Add the `azureml-mlflow` package as a pip dependency to your environment configuration file in order to track metrics and key artifacts in your workspace. 

    __conda.yaml__

    ```yaml
    name: mlflow-example
    channels:
      - defaults
    dependencies:
      - numpy>=1.14.3
      - pandas>=1.0.0
      - scikit-learn
      - pip:
        - mlflow
        - azureml-mlflow
    ```

1. Submit the local run and ensure you set the parameter `backend = "azureml"`, which adds support of automatic tracking, model's capture, log files, snapshots, and printed errors in your workspace. In this example we assume the MLflow project you are trying to run is in the same folder you currently are, `uri="."`.
  
    # [MLflow CLI](#tab/cli)
    
    ```bash
    mlflow run . --experiment-name  --backend azureml --env-manager=local -P alpha=0.3
    ```
  
    # [Python](#tab/sdk)

    ```python
    local_env_run = mlflow.projects.run(
        uri=".", 
        parameters={"alpha":0.3},
        backend = "azureml",
        env_manager="local",
        backend_config = backend_config, 
    )
    ```
    
  
    View your runs and metrics in the [Azure Machine Learning studio](https://ml.azure.com).

## Train MLflow projects in Azure Machine Learning jobs

This example shows how to submit MLflow projects as a job running on Azure Machine Learning compute.

1. Create the backend configuration object, in this case we are going to indicate `COMPUTE`. This parameter references the name of your remote compute cluster you want to use for running your project. If `COMPUTE` is present, the project will be automatically submitted as an Azure Machine Learning job to the indicated compute. 

    # [MLflow CLI](#tab/cli)
  
    __backend_config.json__
  
    ```json
    {
        "COMPUTE": "cpu-cluster"
    }
    
    ```
  
    # [Python](#tab/sdk)
  
    ```python
    backend_config = {"COMPUTE": "cpu-cluster"}
    ```

1. Add the `azureml-mlflow` package as a pip dependency to your environment configuration file in order to track metrics and key artifacts in your workspace. 

    __conda.yaml__

    ```yaml
    name: mlflow-example
    channels:
      - defaults
    dependencies:
      - numpy>=1.14.3
      - pandas>=1.0.0
      - scikit-learn
      - pip:
        - mlflow
        - azureml-mlflow
    ```

1. Submit the local run and ensure you set the parameter `backend = "azureml"`, which adds support of automatic tracking, model's capture, log files, snapshots, and printed errors in your workspace. In this example we assume the MLflow project you are trying to run is in the same folder you currently are, `uri="."`.
