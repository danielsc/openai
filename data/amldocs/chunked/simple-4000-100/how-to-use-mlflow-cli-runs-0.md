
# Track ML experiments and models with MLflow

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning developer platform you are using:"]
> * [v1](./v1/how-to-use-mlflow.md)
> * [v2 (current version)](how-to-use-mlflow-cli-runs.md)

In this article, learn how to enable [MLflow Tracking](https://mlflow.org/docs/latest/quickstart.html#using-the-tracking-api) to connect Azure Machine Learning as the backend of your MLflow experiments.

[MLflow](https://www.mlflow.org) is an open-source library for managing the lifecycle of your machine learning experiments. MLflow Tracking is a component of MLflow that logs and tracks your training job metrics and model artifacts, no matter your experiment's environment--locally on your computer, on a remote compute target, a virtual machine, or an [Azure Databricks cluster](how-to-use-mlflow-azure-databricks.md).

See [MLflow and Azure Machine Learning](concept-mlflow.md) for all supported MLflow and Azure Machine Learning functionality including MLflow Project support (preview) and model deployment.

> [!Tip] 
> If you want to track experiments running on Azure Databricks or Azure Synapse Analytics, see the dedicated articles [Track Azure Databricks ML experiments with MLflow and Azure Machine Learning](how-to-use-mlflow-azure-databricks.md) or [Track Azure Synapse Analytics ML experiments with MLflow and Azure Machine Learning](how-to-use-mlflow-azure-synapse.md).

> [!NOTE]
> The information in this document is primarily for data scientists and developers who want to monitor the model training process. If you are an administrator interested in monitoring resource usage and events from Azure Machine Learning, such as quotas, completed training jobs, or completed model deployments, see [Monitoring Azure Machine Learning](monitor-azure-machine-learning.md).

## Prerequisites

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]

* (Optional) Install and [set up Azure ML CLI (v2)](how-to-configure-cli.md#prerequisites) and make sure you install the ml extension.
* (Optional) Install and set up Azure ML SDK(v2) for Python.


### Connect to your workspace

First, let's connect to Azure Machine Learning workspace where your model is registered.

# [Azure Machine Learning compute](#tab/aml)

Tracking is already configured for you. Your default credentials will also be used when working with MLflow.

# [Remote compute](#tab/remote)

**Configure tracking URI**

[!INCLUDE [configure-mlflow-tracking](../../includes/machine-learning-mlflow-configure-tracking.md)]

**Configure authentication**

Once the tracking is configured, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials. Refer to [Configure MLflow for Azure Machine Learning: Configure authentication](how-to-use-mlflow-configure-tracking.md#configure-authentication) to additional ways to configure authentication for MLflow in Azure Machine Learning workspaces.

[!INCLUDE [configure-mlflow-auth](../../includes/machine-learning-mlflow-configure-auth.md)]


### Set experiment name

All MLflow runs are logged to the active experiment. By default, runs are logged to an experiment named `Default` that is automatically created for you. You can configure the experiment where tracking is happening.

> [!TIP]
> When submitting jobs using Azure ML CLI v2, you can set the experiment name using the property `experiment_name` in the YAML definition of the job. You don't have to configure it on your training script. See [YAML: display name, experiment name, description, and tags](reference-yaml-job-command.md#yaml-display-name-experiment-name-description-and-tags) for details.

# [MLflow SDK](#tab/mlflow)

To configure the experiment you want to work on use MLflow command [`mlflow.set_experiment()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_experiment).
