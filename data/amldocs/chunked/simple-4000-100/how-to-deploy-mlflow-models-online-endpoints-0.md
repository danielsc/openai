
# Deploy MLflow models to online endpoints

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](./v1/how-to-deploy-mlflow-models.md)
> * [v2 (current version)](how-to-deploy-mlflow-models-online-endpoints.md)

In this article, learn how to deploy your [MLflow](https://www.mlflow.org) model to an [online endpoint](concept-endpoints.md) for real-time inference. When you deploy your MLflow model to an online endpoint, you don't need to indicate a scoring script or an environment. This characteristic is usually referred as __no-code deployment__. 

For no-code-deployment, Azure Machine Learning 

* Dynamically installs Python packages provided in the `conda.yaml` file, this means the dependencies are installed during container runtime.
* Provides a MLflow base image/curated environment that contains the following items:
    * [`azureml-inference-server-http`](how-to-inference-server-http.md) 
    * [`mlflow-skinny`](https://github.com/mlflow/mlflow/blob/master/README_SKINNY.rst)
    * A scoring script to perform inference.

> [!WARNING]
> __Workspaces without public network access:__ Azure Machine Learning performs dynamic installation of packages when deploying MLflow models with no-code deployment. As a consequence, deploying MLflow models to online endpoints with no-code deployment in a private network without egress connectivity is not supported by the moment. If that's your case, either enable egress connectivity or indicate the environment to use in the deployment as explained in [Customizing MLflow model deployments](#customizing-mlflow-model-deployments).


## About this example

This example shows how you can deploy an MLflow model to an online endpoint to perform predictions. This example uses an MLflow model based on the [Diabetes dataset](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html). This dataset contains ten baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements obtained from n = 442 diabetes patients, as well as the response of interest, a quantitative measure of disease progression one year after baseline (regression).

The model has been trained using an `scikit-learn` regressor and all the required preprocessing has been packaged as a pipeline, making this model an end-to-end pipeline that goes from raw data to predictions.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo and then change directories to the `cli/endpoints/online` if you are using the Azure CLI or `sdk/endpoints/online` if you are using our SDK for Python.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples/cli/endpoints/online
```

### Follow along in Jupyter Notebooks

You can follow along this sample in the following notebooks. In the cloned repository, open the notebook: [mlflow_sdk_online_endpoints_progresive.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_online_endpoints.ipynb).

## Prerequisites

Before following the steps in this article, make sure you have the following prerequisites:

- An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
- Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the owner or contributor role for the Azure Machine Learning workspace, or a custom role allowing Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
