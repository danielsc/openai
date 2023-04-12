For metrics that contain multiple values (for instance, a loss curve, or a PR curve), only the last logged value of the metric is returned. If you want to retrieve all the values of a given metric, uses `mlflow.get_metric_history` method. This method requires you to use the `MlflowClient`:

```python
client = mlflow.tracking.MlflowClient()
client.get_metric_history("1234-5678-90AB-CDEFG", "log_loss")
```

### Getting artifacts from a run

Any artifact logged by a run can be queried by MLflow. Artifacts can't be access using the run object itself and the MLflow client should be used instead:

```python
client = mlflow.tracking.MlflowClient()
client.list_artifacts("1234-5678-90AB-CDEFG")
```

The method above will list all the artifacts logged in the run, but they will remain stored in the artifacts store (Azure ML storage). To download any of them, use the method `download_artifact`:

```python
file_path = mlflow.artifacts.download_artifacts(
    run_id="1234-5678-90AB-CDEFG", artifact_path="feature_importance_weight.png"
)
```

> [!NOTE]
> __MLflow 2.0 advisory:__ In legacy versions of MLflow (<2.0), use the method `MlflowClient.download_artifacts()` instead.

### Getting models from a run

Models can also be logged in the run and then retrieved directly from it. To retrieve it, you need to know the artifact's path where it is stored. The method `list_artifacats` can be used to find artifacts that are representing a model since MLflow models are always folders. You can download a model by indicating the path where the model is stored using the `download_artifact` method:

```python
artifact_path="classifier"
model_local_path = mlflow.artifacts.download_artifacts(
  run_id="1234-5678-90AB-CDEFG", artifact_path=artifact_path
)
```
  
You can then load the model back from the downloaded artifacts using the typical function `load_model`:

```python
model = mlflow.xgboost.load_model(model_local_path)
```

> [!NOTE]
> The previous example assumes the model was created using `xgboost`. Change it to the flavor applies to your case.

MLflow also allows you to both operations at once and download and load the model in a single instruction. MLflow will download the model to a temporary folder and load it from there. The method `load_model` uses an URI format to indicate from where the model has to be retrieved. In the case of loading a model from a run, the URI structure is as follows:

```python
model = mlflow.xgboost.load_model(f"runs:/{last_run.info.run_id}/{artifact_path}")
```

> [!TIP]
> You can also load models from the registry using MLflow. View [loading MLflow models with MLflow](how-to-manage-models-mlflow.md#loading-models-from-registry) for details.

## Getting child (nested) runs

MLflow supports the concept of child (nested) runs. They are useful when you need to spin off training routines requiring being tracked independently from the main training process. Hyper-parameter tuning optimization processes or Azure Machine Learning pipelines are typical examples of jobs that generate multiple child runs. You can query all the child runs of a specific run using the property tag `mlflow.parentRunId`, which contains the run ID of the parent run.

```python
hyperopt_run = mlflow.last_active_run()
child_runs = mlflow.search_runs(
    filter_string=f"tags.mlflow.parentRunId='{hyperopt_run.info.run_id}'"
)
```

## Compare jobs and models in AzureML studio (preview)

To compare and evaluate the quality of your jobs and models in AzureML Studio, use the [preview panel](./how-to-enable-preview-features.md) to enable the feature. Once enabled, you can compare the parameters, metrics, and tags between the jobs and/or models you selected.

:::image type="content" source="media/how-to-track-experiments-mlflow/compare.gif" alt-text="Screenshot of the preview panel showing how to compare jobs and models in AzureML studio.":::


The [MLflow with Azure ML notebooks](https://github.com/Azure/azureml-examples/tree/main/sdk/python/using-mlflow) demonstrate and expand upon concepts presented in this article.
