
You can view the metrics, parameters, and tags for the run in the data field of the run object.

```python
metrics = run.data.metrics
params = run.data.params
tags = run.data.tags
```

>[!NOTE]
> The metrics dictionary returned by `mlflow.get_run` or `mlflow.seach_runs` only returns the most recently logged value for a given metric name. For example, if you log a metric called `iteration` multiple times with values, `1`, then `2`, then `3`, then `4`, only `4` is returned when calling `run.data.metrics['iteration']`.
> 
> To get all metrics logged for a particular metric name, you can use `MlFlowClient.get_metric_history()` as explained in the example [Getting params and metrics from a run](how-to-track-experiments-mlflow.md#getting-params-and-metrics-from-a-run).

<a name="view-the-experiment-in-the-web-portal"></a>

> [!TIP]
> MLflow can retrieve metrics and parameters from multiple runs at the same time, allowing for quick comparisons across multiple trials. Learn about this in [Query & compare experiments and runs with MLflow](how-to-track-experiments-mlflow.md).

Any artifact logged by a run can be queried by MLflow. Artifacts can't be accessed using the run object itself and the MLflow client should be used instead:

```python
client = mlflow.tracking.MlflowClient()
client.list_artifacts("<RUN_ID>")
```

The method above will list all the artifacts logged in the run, but they will remain stored in the artifacts store (Azure ML storage). To download any of them, use the method `download_artifact`:

```python
file_path = client.download_artifacts("<RUN_ID>", path="feature_importance_weight.png")
```

For more information please refer to [Getting metrics, parameters, artifacts and models](how-to-track-experiments-mlflow.md#getting-metrics-parameters-artifacts-and-models).

## View jobs/runs information in the studio

You can browse completed job records, including logged metrics, in the [Azure Machine Learning studio](https://ml.azure.com).

Navigate to the **Jobs** tab. To view all your jobs in your Workspace across Experiments, select the **All jobs** tab. You can drill down on jobs for specific Experiments by applying the Experiment filter in the top menu bar. Click on the job of interest to enter the details view, and then select the **Metrics** tab.

Select the logged metrics to render charts on the right side. You can customize the charts by applying smoothing, changing the color, or plotting multiple metrics on a single graph. You can also resize and rearrange the layout as you wish. Once you have created your desired view, you can save it for future use and share it with your teammates using a direct link.

:::image type="content" source="media/how-to-log-view-metrics/metrics.png" alt-text="Screenshot of the metrics view.":::

### View and download diagnostic logs

Log files are an essential resource for debugging the Azure ML workloads. After submitting a training job, drill down to a specific run to view its logs and outputs:  

1. Navigate to the **Jobs** tab.
1. Select the runID for a specific run.
1. Select **Outputs and logs** at the top of the page.
2. Select **Download all** to download all your logs into a zip folder.
3. You can also download individual log files by choosing the log file and selecting **Download**

:::image type="content" source="media/how-to-log-view-metrics/download-logs.png" alt-text="Screenshot of Output and logs section of a run.":::

#### user_logs folder

This folder contains information about the user generated logs. This folder is open by default, and the **std_log.txt** log is selected. The **std_log.txt** is where your code's logs (for example, print statements) show up. This file contains `stdout` log and `stderr` logs from your control script and training script, one per process.  In most cases, you'll monitor the logs here.

#### system_logs folder

This folder contains the logs generated by Azure Machine Learning and it will be closed by default. The logs generated by the system are grouped into different folders, based on the stage of the job in the runtime.