
# Deploy and run MLflow models in Spark jobs

In this article, learn how to deploy and run your [MLflow](https://www.mlflow.org) model in Spark jobs to perform inference over large amounts of data or as part of data wrangling jobs.


## About this example

This example shows how you can deploy an MLflow model registered in Azure Machine Learning to Spark jobs running in [managed Spark clusters (preview)](how-to-submit-spark-jobs.md), Azure Databricks, or Azure Synapse Analytics, to perform inference over large amounts of data. 

The model is based on the [UCI Heart Disease Data Set](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). The database contains 76 attributes, but we are using a subset of 14 of them. The model tries to predict the presence of heart disease in a patient. It is integer valued from 0 (no presence) to 1 (presence). It has been trained using an `XGBBoost` classifier and all the required preprocessing has been packaged as a `scikit-learn` pipeline, making this model an end-to-end pipeline that goes from raw data to predictions.

The information in this article is based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste files, clone the repo, and then change directories to `sdk/using-mlflow/deploy`.

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd sdk/python/using-mlflow/deploy
```

## Prerequisites

Before following the steps in this article, make sure you have the following prerequisites:

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]

- You must have a MLflow model registered in your workspace. Particularly, this example will register a model trained for the [Diabetes dataset](https://www4.stat.ncsu.edu/~boos/var.select/diabetes.html).


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


### Registering the model

We need a model registered in the Azure Machine Learning registry to perform inference. In this case, we already have a local copy of the model in the repository, so we only need to publish the model to the registry in the workspace. You can skip this step if the model you are trying to deploy is already registered.
   
```python
model_name = 'heart-classifier'
model_local_path = "model"

registered_model = mlflow_client.create_model_version(
    name=model_name, source=f"file://{model_local_path}"
)
version = registered_model.version
```

Alternatively, if your model was logged inside of a run, you can register it directly.

> [!TIP]
> To register the model, you'll need to know the location where the model has been stored. If you are using `autolog` feature of MLflow, the path will depend on the type and framework of the model being used. We recommend to check the jobs output to identify which is the name of this folder. You can look for the folder that contains a file named `MLModel`. If you are logging your models manually using `log_model`, then the path is the argument you pass to such method. As an example, if you log the model using `mlflow.sklearn.log_model(my_model, "classifier")`, then the path where the model is stored is `classifier`.
