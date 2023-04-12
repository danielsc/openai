> print(client.get_run(multiple_metrics_run.info.run_id).data.metrics)
> print(client.get_metric_history(multiple_metrics_run.info.run_id, "sample_metric"))
> ```
> 
> For more information, see the [MlFlowClient](https://mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient) reference.

The `info` field provides general information about the run, such as start time, run ID, experiment ID, etc.:

```python
run_start_time = finished_mlflow_run.info.start_time
run_experiment_id = finished_mlflow_run.info.experiment_id
run_id = finished_mlflow_run.info.run_id
```

## View run artifacts

To view the artifacts of a run, use [MlFlowClient.list_artifacts](https://mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient.list_artifacts):

```python
client.list_artifacts(finished_mlflow_run.info.run_id)
```

To download an artifact, use [MlFlowClient.download_artifacts](https://www.mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient.download_artifacts):

```python
client.download_artifacts(finished_mlflow_run.info.run_id, "Azure.png")
```
## Next steps

* [Track ML experiments and models with MLflow](how-to-use-mlflow-cli-runs.md)
* [Log and view metrics](how-to-log-view-metrics.md)
