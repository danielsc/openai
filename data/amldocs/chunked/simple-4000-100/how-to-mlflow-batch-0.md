
# Use MLflow models in batch deployments

[!INCLUDE [cli v2](../../includes/machine-learning-dev-v2.md)]

In this article, learn how to deploy your [MLflow](https://www.mlflow.org) model to Azure ML for both batch inference using batch endpoints. Azure Machine Learning supports no-code deployment of models created and logged with MLflow. This means that you don't have to provide a scoring script or an environment.

For no-code-deployment, Azure Machine Learning 

* Provides a MLflow base image/curated environment that contains the required dependencies to run an Azure Machine Learning Batch job.
* Creates a batch job pipeline with a scoring script for you that can be used to process data using parallelization.

> [!NOTE]
> For more information about the supported file types in batch endpoints with MLflow, view [Considerations when deploying to batch inference](#considerations-when-deploying-to-batch-inference).

## About this example

This example shows how you can deploy an MLflow model to a batch endpoint to perform batch predictions. This example uses an MLflow model based on the [UCI Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). The database contains 76 attributes, but we are using a subset of 14 of them. The model tries to predict the presence of heart disease in a patient. It is integer valued from 0 (no presence) to 1 (presence).

The model has been trained using an `XGBBoost` classifier and all the required preprocessing has been packaged as a `scikit-learn` pipeline, making this model an end-to-end pipeline that goes from raw data to predictions.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo and then change directories to the `cli/endpoints/batch` if you are using the Azure CLI or `sdk/endpoints/batch` if you are using our SDK for Python.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/batch
```

### Follow along in Jupyter Notebooks

You can follow along this sample in the following notebooks. In the cloned repository, open the notebook: [mlflow-for-batch-tabular.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/batch/mlflow-for-batch-tabular.ipynb).

## Prerequisites

[!INCLUDE [basic cli prereqs](../../includes/machine-learning-cli-prereqs.md)]

* You must have a MLflow model. If your model is not in MLflow format and you want to use this feature, you can [convert your custom ML model to MLflow format](how-to-convert-custom-model-to-mlflow.md).

## Steps

Follow these steps to deploy an MLflow model to a batch endpoint for running batch inference over new data:

1. First, let's connect to Azure Machine Learning workspace where we are going to work on.

   # [Azure CLI](#tab/cli)
   
   ```azurecli
   az account set --subscription <subscription>
   az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
   ```
   
   # [Python](#tab/sdk)
   
   The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace in which you'll perform deployment tasks.
   
   1. Import the required libraries:
   
   ```python
   from azure.ai.ml import MLClient, Input
   from azure.ai.ml.entities import BatchEndpoint, BatchDeployment, Model, AmlCompute, Data, BatchRetrySettings
   from azure.ai.ml.constants import AssetTypes, BatchDeploymentOutputAction
   from azure.identity import DefaultAzureCredential
   ```
   
   2. Configure workspace details and get a handle to the workspace:
   
   ```python
   subscription_id = "<subscription>"
   resource_group = "<resource-group>"
   workspace = "<workspace>"
   
   ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
   ```
