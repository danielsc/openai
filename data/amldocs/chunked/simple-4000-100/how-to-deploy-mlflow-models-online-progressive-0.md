
# Progressive rollout of MLflow models to Online Endpoints

In this article, you'll learn how you can progressively update and deploy MLflow models to Online Endpoints without causing service disruption. You'll use blue-green deployment, also known as a safe rollout strategy, to introduce a new version of a web service to production. This strategy will allow you to roll out your new version of the web service to a small subset of users or requests before rolling it out completely.

## About this example

Online Endpoints have the concept of __Endpoint__ and __Deployment__. An endpoint represents the API that customers use to consume the model, while the deployment indicates the specific implementation of that API. This distinction allows users to decouple the API from the implementation and to change the underlying implementation without affecting the consumer. This example will use such concepts to update the deployed model in endpoints without introducing service disruption. 

The model we will deploy is based on the [UCI Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). The database contains 76 attributes, but we are using a subset of 14 of them. The model tries to predict the presence of heart disease in a patient. It is integer valued from 0 (no presence) to 1 (presence). It has been trained using an `XGBBoost` classifier and all the required preprocessing has been packaged as a `scikit-learn` pipeline, making this model an end-to-end pipeline that goes from raw data to predictions.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste files, clone the repo, and then change directories to `sdk/using-mlflow/deploy`.

### Follow along in Jupyter Notebooks

You can follow along this sample in the following notebooks. In the cloned repository, open the notebook: [mlflow_sdk_online_endpoints_progresive.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_online_endpoints_progresive.ipynb).

## Prerequisites

Before following the steps in this article, make sure you have the following prerequisites:

- An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
- Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the owner or contributor role for the Azure Machine Learning workspace, or a custom role allowing Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

Additionally, you will need to:

# [Azure CLI](#tab/cli)

- Install the Azure CLI and the ml extension to the Azure CLI. For more information, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

# [Python (Azure ML SDK)](#tab/sdk)

- Install the Azure Machine Learning SDK for Python
    
    ```bash
    pip install azure-ai-ml
    ```
    
# [Python (MLflow SDK)](#tab/mlflow)

- Install the Mlflow SDK package `mlflow` and the Azure Machine Learning plug-in for MLflow `azureml-mlflow`.

    ```bash
    pip install mlflow azureml-mlflow
    ```

- If you are not running in Azure Machine Learning compute, configure the MLflow tracking URI or MLflow's registry URI to point to the workspace you are working on. See [Configure MLflow for Azure Machine Learning](how-to-use-mlflow-configure-tracking.md) for more details.


### Connect to your workspace

First, let's connect to Azure Machine Learning workspace where we are going to work on.

# [Azure CLI](#tab/cli)

```azurecli
az account set --subscription <subscription>
az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
```
