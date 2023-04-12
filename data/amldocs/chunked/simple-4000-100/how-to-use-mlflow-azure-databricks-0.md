
# Track Azure Databricks ML experiments with MLflow and Azure Machine Learning

[MLflow](https://www.mlflow.org) is an open-source library for managing the life cycle of your machine learning experiments. You can use MLflow to integrate Azure Databricks with Azure Machine Learning to ensure you get the best from both of the products.

In this article, you will learn:
> [!div class="checklist"]
> - The required libraries needed to use MLflow with Azure Databricks and Azure Machine Learning.
> - How to [track Azure Databricks runs with MLflow in Azure Machine Learning](#track-azure-databricks-runs-with-mlflow).
> - How to [log models with MLflow](#registering-models-in-the-registry-with-mlflow) to get them registered in Azure Machine Learning.
> - How to [deploy and consume models registered in Azure Machine Learning](#deploying-and-consuming-models-registered-in-azure-machine-learning).

## Prerequisites

* Install the `azureml-mlflow` package, which handles the connectivity with Azure Machine Learning, including authentication.
* An [Azure Databricks workspace and cluster](/azure/databricks/scenarios/quickstart-create-databricks-workspace-portal).
* [Create an Azure Machine Learning Workspace](quickstart-create-resources.md).
    * See which [access permissions you need to perform your MLflow operations with your workspace](how-to-assign-roles.md#mlflow-operations).

### Example notebooks

The [Training models in Azure Databricks and deploying them on Azure ML](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/track_with_databricks_deploy_aml.ipynb) demonstrates how to train models in Azure Databricks and deploy them in Azure ML. It also includes how to handle cases where you also want to track the experiments and models with the MLflow instance in Azure Databricks and leverage Azure ML for deployment.

## Install libraries

To install libraries on your cluster, navigate to the **Libraries** tab and select **Install New**

 ![mlflow with azure databricks](./media/how-to-use-mlflow-azure-databricks/azure-databricks-cluster-libraries.png)

In the **Package** field, type azureml-mlflow and then select install. Repeat this step as necessary to install other additional packages to your cluster for your experiment.

 ![Azure DB install mlflow library](./media/how-to-use-mlflow-azure-databricks/install-libraries.png)

## Track Azure Databricks runs with MLflow

Azure Databricks can be configured to track experiments using MLflow in two ways:

- [Track in both Azure Databricks workspace and Azure Machine Learning workspace (dual-tracking)](#dual-tracking-on-azure-databricks-and-azure-machine-learning)
- [Track exclusively on Azure Machine Learning](#tracking-exclusively-on-azure-machine-learning-workspace)

By default, dual-tracking is configured for you when you linked your Azure Databricks workspace.

### Dual-tracking on Azure Databricks and Azure Machine Learning

Linking your ADB workspace to your Azure Machine Learning workspace enables you to track your experiment data in the Azure Machine Learning workspace and Azure Databricks workspace at the same time. This is referred as Dual-tracking.

> [!WARNING]
> Dual-tracking in a [private link enabled Azure Machine Learning workspace](how-to-configure-private-link.md) is not supported by the moment. Configure [exclusive tracking with your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace) instead.
> 
> [!WARNING]
> Dual-tracking in not supported in Azure China by the moment. Configure [exclusive tracking with your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace) instead.

To link your ADB workspace to a new or existing Azure Machine Learning workspace, 
1. Sign in to [Azure portal](https://portal.azure.com).
1. Navigate to your ADB workspace's **Overview** page.
1. Select the **Link Azure Machine Learning workspace** button on the bottom right. 

 ![Link Azure DB and Azure Machine Learning workspaces](./media/how-to-use-mlflow-azure-databricks/link-workspaces.png)
