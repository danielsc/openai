
You can inspect the model signature of your model by opening the MLmodel file associated with your MLflow model. For more details about how signatures work in MLflow, see [Signatures in MLflow](concept-mlflow-models.md#signatures).

> [!TIP]
> Signatures in MLflow models are optional but they are highly encouraged as they provide a convenient way to early detect data compatibility issues. For more information about how to log models with signatures read [Logging models with a custom signature, environment or samples](how-to-log-mlflow-models.md#logging-models-with-a-custom-signature-environment-or-samples).

## Deployment tools

Azure Machine Learning offers many ways to deploy MLflow models into Online and Batch endpoints. You can deploy models using the following tools:

> [!div class="checklist"]
> - MLflow SDK
> - Azure ML CLI and Azure ML SDK for Python
> - Azure Machine Learning studio

Each workflow has different capabilities, particularly around which type of compute they can target. The following table shows them.

| Scenario | MLflow SDK | Azure ML CLI/SDK | Azure ML studio |
| :- | :-: | :-: | :-: |
| Deploy to managed online endpoints | [See example](how-to-deploy-mlflow-models-online-progressive.md)<sup>1</sup> | [See example](how-to-deploy-mlflow-models-online-endpoints.md)<sup>1</sup> | [See example](how-to-deploy-mlflow-models-online-endpoints.md?tabs=studio)<sup>1</sup> |
| Deploy to managed online endpoints (with a scoring script) |  | [See example](how-to-deploy-mlflow-models-online-endpoints.md#customizing-mlflow-model-deployments) |  |
| Deploy to batch endpoints |  | [See example](how-to-mlflow-batch.md) | [See example](how-to-mlflow-batch.md?tab=studio) |
| Deploy to batch endpoints (with a scoring script) |  | [See example](how-to-mlflow-batch.md#customizing-mlflow-models-deployments-with-a-scoring-script) |   |
| Deploy to web services (ACI/AKS) | Legacy support<sup>2</sup> | <sup>2</sup> | <sup>2</sup> |
| Deploy to web services (ACI/AKS - with a scoring script) | <sup>2</sup> | <sup>2</sup> | Legacy support<sup>2</sup> |

> [!NOTE]
> - <sup>1</sup> Deployment to online endpoints in private link-enabled workspaces is not supported as public network access is required for package installation. We suggest to deploy with a scoring script on those scenarios.
> - <sup>2</sup> We recommend switching to our [managed online endpoints](concept-endpoints.md) instead.

### Which option to use?

If you are familiar with MLflow or your platform support MLflow natively (like Azure Databricks) and you wish to continue using the same set of methods, use the MLflow SDK. On the other hand, if you are more familiar with the [Azure ML CLI v2](concept-v2.md), you want to automate deployments using automation pipelines, or you want to keep deployments configuration in a git repository; we recommend you to use the [Azure ML CLI v2](concept-v2.md). If you want to quickly deploy and test models trained with MLflow, you can use [Azure Machine Learning studio](https://ml.azure.com) UI deployment.


## Differences between models deployed in Azure Machine Learning and MLflow built-in server

MLflow includes built-in deployment tools that model developers can use to test models locally. For instance, you can run a local instance of a model registered in MLflow server registry with `mlflow models serve -m my_model` or you can use the MLflow CLI `mlflow models predict`. Azure Machine Learning online and batch endpoints run different inferencing technologies which may have different features. Read this section to understand their differences.

### Batch vs Online endpoints

Azure Machine Learning supports deploying models to both online and batch endpoints. Online Endpoints compare to [MLflow built-in server](https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools) and they provide a scalable, synchronous, and lightweight way to run models for inference. Batch Endpoints, on the other hand, provide a way to run asynchronous inference over long running inferencing processes that can scale to big amounts of data. This capability is not present by the moment in MLflow server although similar capability can be achieved [using Spark jobs](how-to-deploy-mlflow-model-spark-jobs.md). 
