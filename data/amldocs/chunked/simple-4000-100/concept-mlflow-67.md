* [Deploy MLflow to Online Endpoints with safe rollout](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_online_endpoints_progresive.ipynb): Demonstrates how to deploy models in MLflow format to online endpoints using MLflow SDK with progressive rollout of models and the deployment of multiple model's versions in the same endpoint.
* [Deploy MLflow to web services (V1)](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/mlflow_sdk_web_service.ipynb): Demonstrates how to deploy models in MLflow format to web services (ACI/AKS v1) using MLflow SDK.
* [Deploying models trained in Azure Databricks to Azure Machine Learning with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/deploy/track_with_databricks_deploy_aml.ipynb): Demonstrates how to train models in Azure Databricks and deploy them in Azure ML. It also includes how to handle cases where you also want to track the experiments with the MLflow instance in Azure Databricks.

## Training MLflow projects (preview)

You can submit training jobs to Azure Machine Learning by using [MLflow projects](https://www.mlflow.org/docs/latest/projects.html) (preview). You can submit jobs locally with Azure Machine Learning tracking or migrate your jobs to the cloud via [Azure Machine Learning compute](./how-to-create-attach-compute-cluster.md).

Learn more at [Train machine learning models with MLflow projects and Azure Machine Learning](how-to-train-mlflow-projects.md).

### Example notebooks

* [Track an MLflow project in Azure Machine Learning workspaces](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/track-and-monitor-experiments/using-mlflow/train-projects-local/train-projects-local.ipynb)
* [Train and run an MLflow project on Azure Machine Learning jobs](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/track-and-monitor-experiments/using-mlflow/train-projects-remote/train-projects-remote.ipynb).

## MLflow SDK, Azure Machine Learning v2, and Azure Machine Learning studio capabilities

The following table shows which operations are supported by each of the tools available in the machine learning lifecycle.

| Feature | MLflow SDK | Azure Machine Learning CLI/SDK | Azure Machine Learning studio |
| :- | :-: | :-: | :-: |
| Track and log metrics, parameters, and models | **&check;** | | |
| Retrieve metrics, parameters, and models | **&check;** | <sup>1</sup> | **&check;** |
| Submit training jobs | **&check;** <sup>2</sup> | **&check;** | **&check;** |
| Submit training jobs with Azure Machine learning data assets |  | **&check;** | **&check;** |
| Submit training jobs with machine learning pipelines | | **&check;** | **&check;** |
| Manage experiments and runs | **&check;** | **&check;** | **&check;** |
| Manage MLflow models | **&check;**<sup>3</sup> | **&check;** | **&check;** |
| Manage non-MLflow models | | **&check;** | **&check;** |
| Deploy MLflow models to Azure Machine Learning (Online & Batch) | **&check;**<sup>4</sup> | **&check;** | **&check;** |
| Deploy non-MLflow models to Azure Machine Learning | | **&check;** | **&check;** |

> [!NOTE]
> - <sup>1</sup> Only artifacts and models can be downloaded.
> - <sup>2</sup> Using MLflow projects (preview).
> - <sup>3</sup> Some operations may not be supported. View [Manage model registries in Azure Machine Learning with MLflow](how-to-manage-models-mlflow.md) for details.
> - <sup>4</sup> Deployment of MLflow models to batch inference by using the MLflow SDK is not possible at the moment. As an alternative, see [Deploy and run MLflow models in Spark jobs](how-to-deploy-mlflow-model-spark-jobs.md).


## Next steps

* [Concept: From artifacts to models in MLflow](concept-mlflow-models.md).
* [How-to: Configure MLflow for Azure Machine Learning](how-to-use-mlflow-configure-tracking.md).
* [How-to: Migrate logging from SDK v1 to MLflow](reference-migrate-sdk-v1-mlflow-tracking.md)
