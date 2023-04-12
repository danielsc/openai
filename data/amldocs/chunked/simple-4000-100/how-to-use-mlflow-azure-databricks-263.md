If you want to use Azure Machine Learning Model Registry instead of Azure Databricks, we recommend you to [set MLflow Tracking to only track in your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace). This will remove the ambiguity of where models are being registered and simplifies complexity.

However, if you want to continue using the dual-tracking capabilities but register models in Azure Machine Learning, you can instruct MLflow to use Azure ML for model registries by configuring the MLflow Model Registry URI. This URI has the exact same format and value that the MLflow tracking URI.

```python
mlflow.set_registry_uri(azureml_mlflow_uri)
```

> [!NOTE]
> The value of `azureml_mlflow_uri` was obtained in the same way it was demostrated in [Set MLflow Tracking to only track in your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace)

For a complete example about this scenario please check the example [Training models in Azure Databricks and deploying them on Azure ML](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/track_with_databricks_deploy_aml.ipynb).

## Deploying and consuming models registered in Azure Machine Learning

Models registered in Azure Machine Learning Service using MLflow can be consumed as: 

* An Azure Machine Learning endpoint (real-time and batch): This deployment allows you to leverage Azure Machine Learning deployment capabilities for both real-time and batch inference in Azure Container Instances (ACI), Azure Kubernetes (AKS) or our Managed Inference Endpoints. 

* MLFlow model objects or Pandas UDFs, which can be used in Azure Databricks notebooks in streaming or batch pipelines.

### Deploy models to Azure Machine Learning endpoints 
You can leverage the `azureml-mlflow` plugin to deploy a model to your Azure Machine Learning workspace. Check [How to deploy MLflow models](how-to-deploy-mlflow-models.md) page for a complete detail about how to deploy models to the different targets.

> [!IMPORTANT]
> Models need to be registered in Azure Machine Learning registry in order to deploy them. If your models happen to be registered in the MLflow instance inside Azure Databricks, you will have to register them again in Azure Machine Learning. If this is you case, please check the example [Training models in Azure Databricks and deploying them on Azure ML](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/track_with_databricks_deploy_aml.ipynb)

### Deploy models to ADB for batch scoring using UDFs

You can choose Azure Databricks clusters for batch scoring. By leveraging Mlflow, you can resolve any model from the registry you are connected to. You will typically use one of the following two methods:

- If your model was trained and built with Spark libraries (like `MLLib`), use `mlflow.pyfunc.spark_udf` to load a model and used it as a Spark Pandas UDF to score new data.
- If your model wasn't trained or built with Spark libraries, either use `mlflow.pyfunc.load_model` or `mlflow.<flavor>.load_model` to load the model in the cluster driver. Notice that in this way, any parallelization or work distribution you want to happen in the cluster needs to be orchestrated by you. Also, notice that MLflow doesn't install any library your model requires to run. Those libraries need to be installed in the cluster before running it.

The following example shows how to load a model from the registry named `uci-heart-classifier` and used it as a Spark Pandas UDF to score new data.

```python
from pyspark.sql.types import ArrayType, FloatType 

model_name = "uci-heart-classifier"
model_uri = "models:/"+model_name+"/latest"

#Create a Spark UDF for the MLFlow model 
pyfunc_udf = mlflow.pyfunc.spark_udf(spark, model_uri) 
```

> [!TIP]
> Check [Loading models from registry](how-to-manage-models-mlflow.md#loading-models-from-registry) for more ways to reference models from the registry. 
