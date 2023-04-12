
# Query & compare experiments and runs with MLflow

Experiments and runs tracking information in Azure Machine Learning can be queried using MLflow. You don't need to install any specific SDK to manage what happens inside of a training job, creating a more seamless transition between local runs and the cloud by removing cloud-specific dependencies. 

> [!NOTE]
> The Azure Machine Learning Python SDK v2 does not provide native logging or tracking capabilities. This applies not just for logging but also for querying the metrics logged. Instead, we recommend to use MLflow to manage experiments and runs. This article explains how to use MLflow to manage experiments and runs in Azure ML.

MLflow allows you to:

* Create, delete and search for experiments in a workspace.
* Start, stop, cancel and query runs for experiments.
* Track and retrieve metrics, parameters, artifacts and models from runs.

In this article, you'll learn how to manage experiments and runs in your workspace using Azure ML and MLflow SDK in Python.

## Using MLflow SDK in Azure ML

Use MLflow to query and manage all the experiments in Azure Machine Learning. The MLflow SDK has capabilities to query everything that happens inside of a training job in Azure Machine Learning. See [Support matrix for querying runs and experiments in Azure Machine Learning](#support-matrix-for-querying-runs-and-experiments) for a detailed comparison between MLflow Open-Source and MLflow when connected to Azure Machine Learning.

### Prerequisites

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]

## Getting all the experiments

You can get all the active experiments in the workspace using MLFlow:

```python
experiments = mlflow.search_experiments()
for exp in experiments:
    print(exp.name)
```

> [!NOTE]
> __MLflow 2.0 advisory:__ In legacy versions of MLflow (<2.0) use method `list_experiments` instead.

If you want to retrieve archived experiments too, then include the option `ViewType.ALL` in the `view_type` argument. The following sample shows how:

```python
from mlflow.entities import ViewType

experiments = mlflow.search_experiments(view_type=ViewType.ALL)
for exp in experiments:
    print(exp.name)
```

## Getting a specific experiment

Details about a specific experiment can be retrieved using the `get_experiment_by_name` method:

```python
exp = mlflow.get_experiment_by_name(experiment_name)
print(exp)
```

## Getting runs inside an experiment

MLflow allows searching runs inside of any experiment, including multiple experiments at the same time. By default, MLflow returns the data in Pandas `Dataframe` format, which makes it handy when doing further processing our analysis of the runs. Returned data includes columns with:

- Basic information about the run.
- Parameters with column's name `params.<parameter-name>`.
- Metrics (last logged value of each) with column's name `metrics.<metric-name>`.

### Getting all the runs from an experiment

By experiment name:

```python
mlflow.search_runs(experiment_names=[ "my_experiment" ])
```  

By experiment ID:

```python
mlflow.search_runs(experiment_ids=[ "1234-5678-90AB-CDEFG" ])
```

> [!TIP]
> Notice that `experiment_ids` supports providing an array of experiments, so you can search runs across multiple experiments if required. This may be useful in case you want to compare runs of the same model when it is being logged in different experiments (by different people, different project iterations, etc). You can also use `search_all_experiments=True` if you want to search across all the experiments in the workspace.

Another important point to notice is that get returning runs, all metrics are parameters are also returned for them. However, for metrics containing multiple values (for instance, a loss curve, or a PR curve), only the last value of the metric is returned. If you want to retrieve all the values of a given metric, uses `mlflow.get_metric_history` method.

### Ordering runs

By default, experiments are ordered descending by `start_time`, which is the time the experiment was queue in Azure ML. However, you can change this default by using the parameter `order_by`.
