Azure Machine Learning supports deploying models to both online and batch endpoints. Online Endpoints compare to [MLflow built-in server](https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools) and they provide a scalable, synchronous, and lightweight way to run models for inference. Batch Endpoints, on the other hand, provide a way to run asynchronous inference over long running inferencing processes that can scale to big amounts of data. This capability is not present by the moment in MLflow server although similar capability can be achieved [using Spark jobs](how-to-deploy-mlflow-model-spark-jobs.md). 

The rest of this section mostly applies to online endpoints but you can learn more of batch endpoint and MLflow models at [Use MLflow models in batch deployments](how-to-mlflow-batch.md).

### Input formats

| Input type | MLflow built-in server | Azure ML Online Endpoints |
| :- | :-: | :-: |
| JSON-serialized pandas DataFrames in the split orientation | **&check;** | **&check;** |
| JSON-serialized pandas DataFrames in the records orientation | Deprecated |  |
| CSV-serialized pandas DataFrames | **&check;** | Use batch<sup>1</sup> |
| Tensor input format as JSON-serialized lists (tensors) and dictionary of lists (named tensors) | **&check;** | **&check;** |
| Tensor input formatted as in TF Serving’s API | **&check;** |  |

> [!NOTE]
> - <sup>1</sup> We suggest you to explore batch inference for processing files. See [Deploy MLflow models to Batch Endpoints](how-to-mlflow-batch.md).

### Input structure

Regardless of the input type used, Azure Machine Learning requires inputs to be provided in a JSON payload, within a dictionary key `input_data`. The following section shows different payload examples and the differences between MLflow built-in server and Azure Machine Learning inferencing server.

> [!WARNING]
> Note that such key is not required when serving models using the command `mlflow models serve` and hence payloads can't be used interchangeably.

> [!IMPORTANT]
> **MLflow 2.0 advisory**: Notice that the payload's structure has changed in MLflow 2.0.

#### Payload example for a JSON-serialized pandas DataFrames in the split orientation

# [Azure Machine Learning](#tab/azureml)

```json
{
    "input_data": {
        "columns": [
            "age", "sex", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ],
        "index": [1],
        "data": [
            [1, 1, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
        ]
    }
}
```

# [MLflow built-in server](#tab/builtin)

```json
{
    "dataframe_split": {
        "columns": [
            "age", "sex", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ],
        "index": [1],
        "data": [
            [1, 1, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
        ]
    }
}
```

The previous payload corresponds to MLflow server 2.0+.



#### Payload example for a tensor input

# [Azure Machine Learning](#tab/azureml)

```json
{
    "input_data": [
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2],
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2],
          [1, 1, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
    ]
}
```

# [MLflow built-in server](#tab/builtin)

```json
{
    "inputs": [
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2],
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
          [1, 1, 0, 233, 1, 2, 150, 0, 2.3, 3, 0, 2],
          [1, 1, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
    ]
}
```


#### Payload example for a named-tensor input

# [Azure Machine Learning](#tab/azureml)

```json
{
    "input_data": {
        "tokens": [
          [0, 655, 85, 5, 23, 84, 23, 52, 856, 5, 23, 1]
        ],
        "mask": [
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ]
    }
}
```

# [MLflow built-in server](#tab/builtin)

```json
{
    "inputs": {
        "tokens": [
          [0, 655, 85, 5, 23, 84, 23, 52, 856, 5, 23, 1]
        ],
        "mask": [
          [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        ]
    }
}
```
