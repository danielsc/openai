Once the tracking is configured, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials. Refer to [Configure MLflow for Azure Machine Learning: Configure authentication](how-to-use-mlflow-configure-tracking.md#configure-authentication) to additional ways to configure authentication for MLflow in Azure Machine Learning workspaces.

[!INCLUDE [configure-mlflow-auth](../../includes/machine-learning-mlflow-configure-auth.md)]

#### Experiment's names in Azure Machine Learning

When MLflow is configured to exclusively track experiments in Azure Machine Learning workspace, the experiment's naming convention has to follow the one used by Azure Machine Learning. In Azure Databricks, experiments are named with the path to where the experiment is saved like `/Users/alice@contoso.com/iris-classifier`. However, in Azure Machine Learning, you have to provide the experiment name directly. As in the previous example, the same experiment would be named `iris-classifier` directly:

```python
mlflow.set_experiment(experiment_name="experiment-name")
```

### Tracking parameters, metrics and artifacts

You can use then MLflow in Azure Databricks in the same way as you're used to. For details see [Log & view metrics and log files](how-to-log-view-metrics.md).

## Logging models with MLflow

After your model is trained, you can log it to the tracking server with the `mlflow.<model_flavor>.log_model()` method. `<model_flavor>`, refers to the framework associated with the model. [Learn what model flavors are supported](https://mlflow.org/docs/latest/models.html#model-api). In the following example, a model created with the Spark library MLLib is being registered:


```python
mlflow.spark.log_model(model, artifact_path = "model")
```

It's worth to mention that the flavor `spark` doesn't correspond to the fact that we are training a model in a Spark cluster but because of the training framework it was used (you can perfectly train a model using TensorFlow with Spark and hence the flavor to use would be `tensorflow`).

Models are logged inside of the run being tracked. That means that models are available in either both Azure Databricks and Azure Machine Learning (default) or exclusively in Azure Machine Learning if you configured the tracking URI to point to it.

> [!IMPORTANT]
> Notice that here the parameter `registered_model_name` has not been specified. Read the section [Registering models in the registry with MLflow](#registering-models-in-the-registry-with-mlflow) for more details about the implications of such parameter and how the registry works.

## Registering models in the registry with MLflow

As opposite to tracking, **model registries can't operate** at the same time in Azure Databricks and Azure Machine Learning. Either one or the other has to be used. By default, the Azure Databricks workspace is used for model registries; unless you chose to [set MLflow Tracking to only track in your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace), then the model registry is the Azure Machine Learning workspace.

Then, considering you're using the default configuration, the following line will log a model inside the corresponding runs of both Azure Databricks and Azure Machine Learning, but it will register it only on Azure Databricks:

```python
mlflow.spark.log_model(model, artifact_path = "model", 
                       registered_model_name = 'model_name')  
```

* **If a registered model with the name doesn’t exist**, the method registers a new model, creates version 1, and returns a ModelVersion MLflow object. 

* **If a registered model with the name already exists**, the method creates a new model version and returns the version object. 

### Using Azure Machine Learning Registry with MLflow

If you want to use Azure Machine Learning Model Registry instead of Azure Databricks, we recommend you to [set MLflow Tracking to only track in your Azure Machine Learning workspace](#tracking-exclusively-on-azure-machine-learning-workspace). This will remove the ambiguity of where models are being registered and simplifies complexity.
