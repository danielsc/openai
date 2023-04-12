* Logged as an _artifact_, not as a metric.
* The `mlflow.log_dict` method is _experimental_.

### Log a confusion matrix

__SDK v1__

```python
CONF_MATRIX = '{"schema_type": "confusion_matrix", "schema_version": "v1", "data": {"class_labels": ' + \
    '["0", "1", "2", "3"], "matrix": [[3, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]}}'

azureml_run.log_confusion_matrix('v1_confusion_matrix', json.loads(CONF_MATRIX))
```

__SDK v2 with MLflow__

```python
CONF_MATRIX = '{"schema_type": "confusion_matrix", "schema_version": "v1", "data": {"class_labels": ' + \
    '["0", "1", "2", "3"], "matrix": [[3, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]]}}'

mlflow.log_dict(CONF_MATRIX, 'mlflow_confusion_matrix.json')
```

* Metrics do not render as a confusion matrix in Azure Machine Learning studio.
* Logged as an _artifact_, not as a metric.
* The `mlflow.log_dict` method is _experimental_.

### Log predictions

__SDK v1__

```python
PREDICTIONS = '{"schema_type": "predictions", "schema_version": "v1", "data": {"bin_averages": [0.25,' + \
    ' 0.75], "bin_errors": [0.013, 0.042], "bin_counts": [56, 34], "bin_edges": [0.0, 0.5, 1.0]}}'

azureml_run.log_predictions('test_predictions', json.loads(PREDICTIONS))
```

__SDK v2 with MLflow__

```python
PREDICTIONS = '{"schema_type": "predictions", "schema_version": "v1", "data": {"bin_averages": [0.25,' + \
    ' 0.75], "bin_errors": [0.013, 0.042], "bin_counts": [56, 34], "bin_edges": [0.0, 0.5, 1.0]}}'

mlflow.log_dict(PREDICTIONS, 'mlflow_predictions.json')
```

* Metrics do not render as a confusion matrix in Azure Machine Learning studio.
* Logged as an _artifact_, not as a metric.
* The `mlflow.log_dict` method is _experimental_.

### Log residuals

__SDK v1__

```python
RESIDUALS = '{"schema_type": "residuals", "schema_version": "v1", "data": {"bin_edges": [100, 200, 300], ' + \
'"bin_counts": [0.88, 20, 30, 50.99]}}'

azureml_run.log_residuals('test_residuals', json.loads(RESIDUALS))
```

__SDK v2 with MLflow__

```python
RESIDUALS = '{"schema_type": "residuals", "schema_version": "v1", "data": {"bin_edges": [100, 200, 300], ' + \
'"bin_counts": [0.88, 20, 30, 50.99]}}'

mlflow.log_dict(RESIDUALS, 'mlflow_residuals.json')
```

* Metrics do not render as a confusion matrix in Azure Machine Learning studio.
* Logged as an _artifact_, not as a metric.
* The `mlflow.log_dict` method is _experimental_.

## View run info and data

You can access run information using the MLflow run object's `data` and `info` properties. For more information, see [mlflow.entities.Run](https://mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.Run) reference.

The following example shows how to retrieve a finished run:

```python
from mlflow.tracking import MlflowClient

# Use MlFlow to retrieve the run that was just completed
client = MlflowClient()
finished_mlflow_run = MlflowClient().get_run(mlflow_run.info.run_id)
```

The following example shows how to view the `metrics`, `tags`, and `params`:

```python
metrics = finished_mlflow_run.data.metrics
tags = finished_mlflow_run.data.tags
params = finished_mlflow_run.data.params
```

> [!NOTE]
> The `metrics` will only have the most recently logged value for a given metric. For example, if you log in order a value of `1`, then `2`, `3`, and finally `4` to a metric named `sample_metric`, only `4` will be present in the `metrics` dictionary. To get all metrics logged for a specific named metric, use [MlFlowClient.get_metric_history](https://mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient.get_metric_history):
>
> ```python
> with mlflow.start_run() as multiple_metrics_run:
>     mlflow.log_metric("sample_metric", 1)
>     mlflow.log_metric("sample_metric", 2)
>     mlflow.log_metric("sample_metric", 3)
>     mlflow.log_metric("sample_metric", 4)
> 
> print(client.get_run(multiple_metrics_run.info.run_id).data.metrics)
> print(client.get_metric_history(multiple_metrics_run.info.run_id, "sample_metric"))
