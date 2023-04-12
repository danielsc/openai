
When you start a new run with `mlflow.start_run`, it may be useful to indicate the parameter `run_name` which will then translate to the name of the run in Azure Machine Learning user interface and help you identify the run quicker:

```python
with mlflow.start_run(run_name="iris-classifier-random-forest") as run:
    mlflow.log_metric('mymetric', 1)
    mlflow.log_metric('anothermetric',1)
```

For more information on MLflow logging APIs, see the [MLflow reference](https://www.mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_artifact).

# [Training with jobs](#tab/jobs)

When running training jobs in Azure Machine Learning, you don't need to call `mlflow.start_run` as runs are automatically started. Hence, you can use mlflow tracking capabilities directly in your training scripts:

```python
import mlflow

mlflow.autolog()

mlflow.log_metric('mymetric', 1)
mlflow.log_metric('anothermetric',1)
```

> [!TIP]
> When submitting jobs using Azure ML CLI v2, you can set the experiment name using the property `experiment_name` in the YAML definition of the job. You don't have to configure it on your training script. See [YAML: display name, experiment name, description, and tags](reference-yaml-job-command.md#yaml-display-name-experiment-name-description-and-tags) for details.


## Logging parameters

MLflow supports the logging parameters used by your experiments. Parameters can be of any type, and can be logged using the following syntax:

```python
mlflow.log_param("num_epochs", 20)
```

MLflow also offers a convenient way to log multiple parameters by indicating all of them using a dictionary. Several frameworks can also pass parameters to models using dictionaries and hence this is a convenient way to log them in the experiment.

```python
params = {
    "num_epochs": 20,
    "dropout_rate": .6,
    "objective": "binary_crossentropy"
}

mlflow.log_params(params)
```

> [!NOTE] 
> Azure ML SDK v1 logging can't log parameters. We recommend the use of MLflow for tracking experiments as it offers a superior set of features.

## Logging metrics

Metrics, as opposite to parameters, are always numeric. The following table describes how to log specific numeric types:

|Logged Value|Example code| Notes|
|----|----|----|
|Log a numeric value (int or float) | `mlflow.log_metric("my_metric", 1)`| |
|Log a numeric value (int or float) over time | `mlflow.log_metric("my_metric", 1, step=1)`| Use parameter `step` to indicate the step at which you are logging the metric value. It can be any integer number. It defaults to zero. |
|Log a boolean value | `mlflow.log_metric("my_metric", 0)`| 0 = True, 1 = False|

> [!IMPORTANT]
> __Performance considerations:__ If you need to log multiple metrics (or multiple values for the same metric) avoid making calls to `mlflow.log_metric` in loops. Better performance can be achieved by logging batch of metrics. Use the method `mlflow.log_metrics` which accepts a dictionary with all the metrics you want to log at once or use `MLflowClient.log_batch` which accepts multiple type of elements for logging. See [Logging curves or list of values](#logging-curves-or-list-of-values) for an example.

### Logging curves or list of values

Curves (or list of numeric values) can be logged with MLflow by logging the same metric multiple times. The following example shows how to do it:

```python
list_to_log = [1, 2, 3, 2, 1, 2, 3, 2, 1]
from mlflow.entities import Metric
from mlflow.tracking import MlflowClient
import time

client = MlflowClient()
client.log_batch(mlflow.active_run().info.run_id, 
                 metrics=[Metric(key="sample_list", value=val, timestamp=int(time.time() * 1000), step=0) for val in list_to_log])
```

## Logging images

MLflow supports two ways of logging images:

|Logged Value|Example code| Notes|
|----|----|----|
|Log numpy metrics or PIL image objects|`mlflow.log_image(img, "figure.png")`| `img` should be an instance of `numpy.ndarray` or `PIL.Image.Image`. `figure.png` is the name of the artifact that will be generated inside of the run. It doesn't have to be an existing file.|
