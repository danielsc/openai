By default, experiments are ordered descending by `start_time`, which is the time the experiment was queue in Azure ML. However, you can change this default by using the parameter `order_by`.

```python
mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ], order_by=["start_time DESC"])
```
  
Use the argument `max_results` from `search_runs` to limit the number of runs returned. For instance, the following example returns the last run of the experiment:

```python
mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ], max_results=1, order_by=["start_time DESC"])
```

> [!WARNING]
> Using `order_by` with expressions containing `metrics.*` in the parameter `order_by` is not supported by the moment. Please use `order_values` method from Pandas as shown in the next example.

You can also order by metrics to know which run generated the best results:

```python
mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ]).sort_values("metrics.accuracy", ascending=False)
```
  
### Filtering runs

You can also look for a run with a specific combination in the hyperparameters using the parameter `filter_string`. Use `params` to access run's parameters and `metrics` to access metrics logged in the run. MLflow supports expressions joined by the AND keyword (the syntax does not support OR):

```python
mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ], 
                   filter_string="params.num_boost_round='100'")
```

### Filter runs by status

You can also filter experiment by status. It becomes useful to find runs that are running, completed, canceled or failed. In MLflow, `status` is an `attribute`, so we can access this value using the expression `attributes.status`. The following table shows the possible values:

| Azure ML Job status | MLFlow's `attributes.status` | Meaning |
| :-: | :-: | :- |
| Not started | `SCHEDULED` | The job/run was just registered in Azure ML but it has processed it yet. |
| Queue | `SCHEDULED` | The job/run is scheduled for running, but it hasn't started yet. |
| Preparing | `SCHEDULED` | The job/run has not started yet, but a compute has been allocated for the execution and it is on building state. |
| Running | `RUNNING` | The job/run is currently under active execution. |
| Completed | `FINISHED` | The job/run has completed without errors. |
| Failed | `FAILED` | The job/run has completed with errors. |
| Canceled | `KILLED` | The job/run has been canceled or killed by the user/system. |

> [!WARNING]
> Expressions containing `attributes.status` in the parameter `filter_string` are not support at the moment. Please use Pandas filtering expressions as shown in the next example.

The following example shows all the completed runs:

```python
runs = mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ])
runs[runs.status == "FINISHED"]
```
  
## Getting metrics, parameters, artifacts and models

The method `search_runs` returns a Pandas `Dataframe` containing a limited amount of information by default. You can get Python objects if needed, which may be useful to get details about them. Use the `output_format` parameter to control how output is returned:

```python
runs = mlflow.search_runs(
    experiment_ids=[ "1234-5678-90AB-CDEFG" ],
    filter_string="params.num_boost_round='100'",
    output_format="list",
)
```

Details can then be accessed from the `info` member. The following sample shows how to get the `run_id`:

```python
last_run = runs[-1]
print("Last run ID:", last_run.info.run_id)
```
  
### Getting params and metrics from a run

When runs are returned using `output_format="list"`, you can easily access parameters using the key `data`:

```python
last_run.data.params
```

In the same way, you can query metrics:

```python
last_run.data.metrics
```

For metrics that contain multiple values (for instance, a loss curve, or a PR curve), only the last logged value of the metric is returned. If you want to retrieve all the values of a given metric, uses `mlflow.get_metric_history` method. This method requires you to use the `MlflowClient`:
