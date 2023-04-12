* The string will be logged as an _artifact_, not as a metric. In Azure Machine Learning studio, the value will be displayed in the __Outputs + logs__ tab.

### Log an image to a PNG or JPEG file

__SDK v1__

```python
azureml_run.log_image("sample_image", path="Azure.png")
```

__SDK v2 with MLflow__

```python
mlflow.log_artifact("Azure.png")
```

The image is logged as an artifact and will appear in the __Images__ tab in Azure Machine Learning Studio.

### Log a matplotlib.pyplot

__SDK v1__

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
azureml_run.log_image("sample_pyplot", plot=plt)
```

__SDK v2 with MLflow__

```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3])
fig, ax = plt.subplots()
ax.plot([0, 1], [2, 3])
mlflow.log_figure(fig, "sample_pyplot.png")
```

* The image is logged as an artifact and will appear in the __Images__ tab in Azure Machine Learning Studio.
* The `mlflow.log_figure` method is __experimental__.


### Log a list of metrics

__SDK v1__

```python
list_to_log = [1, 2, 3, 2, 1, 2, 3, 2, 1]
azureml_run.log_list('sample_list', list_to_log)
```

__SDK v2 with MLflow__

```python
list_to_log = [1, 2, 3, 2, 1, 2, 3, 2, 1]
from mlflow.entities import Metric
from mlflow.tracking import MlflowClient
import time

metrics = [Metric(key="sample_list", value=val, timestamp=int(time.time() * 1000), step=0) for val in list_to_log]
MlflowClient().log_batch(mlflow_run.info.run_id, metrics=metrics)
```
* Metrics appear in the __metrics__ tab in Azure Machine Learning studio.
* Text values are not supported.

### Log a row of metrics

__SDK v1__

```python
azureml_run.log_row("sample_table", col1=5, col2=10)
```

__SDK v2 with MLflow__

```python
metrics = {"sample_table.col1": 5, "sample_table.col2": 10}
mlflow.log_metrics(metrics)
```

* Metrics do not render as a table in Azure Machine Learning studio.
* Text values are not supported.
* Logged as an _artifact_, not as a metric.

### Log a table

__SDK v1__

```python
table = {
"col1" : [1, 2, 3],
"col2" : [4, 5, 6]
}
azureml_run.log_table("table", table)
```

__SDK v2 with MLflow__

```python
# Add a metric for each column prefixed by metric name. Similar to log_row
row1 = {"table.col1": 5, "table.col2": 10}
# To be done for each row in the table
mlflow.log_metrics(row1)

# Using mlflow.log_artifact
import json

with open("table.json", 'w') as f:
json.dump(table, f)
mlflow.log_artifact("table.json")
```

* Logs metrics for each column.
* Metrics do not render as a table in Azure Machine Learning studio.
* Text values are not supported.
* Logged as an _artifact_, not as a metric.

### Log an accuracy table

__SDK v1__

```python
ACCURACY_TABLE = '{"schema_type": "accuracy_table", "schema_version": "v1", "data": {"probability_tables": ' +\
        '[[[114311, 385689, 0, 0], [0, 0, 385689, 114311]], [[67998, 432002, 0, 0], [0, 0, ' + \
        '432002, 67998]]], "percentile_tables": [[[114311, 385689, 0, 0], [1, 0, 385689, ' + \
        '114310]], [[67998, 432002, 0, 0], [1, 0, 432002, 67997]]], "class_labels": ["0", "1"], ' + \
        '"probability_thresholds": [0.52], "percentile_thresholds": [0.09]}}'

azureml_run.log_accuracy_table('v1_accuracy_table', ACCURACY_TABLE)
```

__SDK v2 with MLflow__

```python
ACCURACY_TABLE = '{"schema_type": "accuracy_table", "schema_version": "v1", "data": {"probability_tables": ' +\
        '[[[114311, 385689, 0, 0], [0, 0, 385689, 114311]], [[67998, 432002, 0, 0], [0, 0, ' + \
        '432002, 67998]]], "percentile_tables": [[[114311, 385689, 0, 0], [1, 0, 385689, ' + \
        '114310]], [[67998, 432002, 0, 0], [1, 0, 432002, 67997]]], "class_labels": ["0", "1"], ' + \
        '"probability_thresholds": [0.52], "percentile_thresholds": [0.09]}}'

mlflow.log_dict(ACCURACY_TABLE, 'mlflow_accuracy_table.json')
```

* Metrics do not render as an accuracy table in Azure Machine Learning studio.
* Logged as an _artifact_, not as a metric.
* The `mlflow.log_dict` method is _experimental_.

### Log a confusion matrix
