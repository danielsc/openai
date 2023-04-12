
# Track Azure Synapse Analytics ML experiments with MLflow and Azure Machine Learning

In this article, learn how to enable MLflow to connect to Azure Machine Learning while working in an Azure Synapse Analytics workspace. You can leverage this configuration for tracking, model management and model deployment.

[MLflow](https://www.mlflow.org) is an open-source library for managing the life cycle of your machine learning experiments. MLFlow Tracking is a component of MLflow that logs and tracks your training run metrics and model artifacts. Learn more about [MLflow](concept-mlflow.md). 

If you have an MLflow Project to train with Azure Machine Learning, see [Train ML models with MLflow Projects and Azure Machine Learning (preview)](how-to-train-mlflow-projects.md).

## Prerequisites

* An [Azure Synapse Analytics workspace and cluster](../synapse-analytics/quickstart-create-workspace.md).
* An [Azure Machine Learning Workspace](quickstart-create-resources.md).

## Install libraries

To install libraries on your dedicated cluster in Azure Synapse Analytics:

1. Create a `requirements.txt` file with the packages your experiments requires, but making sure it also includes the following packages:

    __requirements.txt__

    ```pip
    mlflow
    azureml-mlflow
    azure-ai-ml
    ```

3. Navigate to Azure Analytics Workspace portal.

4. Navigate to the **Manage** tab and select **Apache Spark Pools**.

5. Click the three dots next to the cluster name, and select **Packages**.

    ![install mlflow packages in Azure Synapse Analytics](media/how-to-use-mlflow-azure/install-packages.png)

6. On the **Requirements files** section, click on **Upload**.

7. Upload the `requirements.txt` file.

8. Wait for your cluster to restart.

## Track experiments with MLflow

Azure Synapse Analytics can be configured to track experiments using MLflow to Azure Machine Learning workspace. Azure Machine Learning provides a centralized repository to manage the entire lifecycle of experiments, models and deployments. It also has the advantage of enabling easier path to deployment using Azure Machine Learning deployment options.

### Configuring your notebooks to use MLflow connected to Azure Machine Learning

To use Azure Machine Learning as your centralized repository for experiments, you can leverage MLflow. On each notebook where you are working on, you have to configure the tracking URI to point to the workspace you will be using. The following example shows how it can be done:

__Configure tracking URI__

[!INCLUDE [configure-mlflow-tracking](../../includes/machine-learning-mlflow-configure-tracking.md)]

__Configure authentication__

Once the tracking is configured, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials. Refer to [Configure MLflow for Azure Machine Learning: Configure authentication](how-to-use-mlflow-configure-tracking.md#configure-authentication) to additional ways to configure authentication for MLflow in Azure Machine Learning workspaces.

[!INCLUDE [configure-mlflow-auth](../../includes/machine-learning-mlflow-configure-auth.md)]

### Experiment's names in Azure Machine Learning

By default, Azure Machine Learning tracks runs in a default experiment called `Default`. It is usually a good idea to set the experiment you will be going to work on. Use the following syntax to set the experiment's name:

```python
mlflow.set_experiment(experiment_name="experiment-name")
```

### Tracking parameters, metrics and artifacts

You can use then MLflow in Azure Synapse Analytics in the same way as you're used to. For details see [Log & view metrics and log files](how-to-log-view-metrics.md).

## Registering models in the registry with MLflow

Models can be registered in Azure Machine Learning workspace, which offers a centralized repository to manage their lifecycle. The following example logs a model trained with Spark MLLib and also registers it in the registry.
