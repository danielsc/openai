The [MLflow with Azure ML notebooks](https://github.com/Azure/azureml-examples/tree/main/sdk/python/using-mlflow) demonstrate and expand upon concepts presented in this article.

  * [Training and tracking a classifier with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/train-and-log/xgboost_classification_mlflow.ipynb): Demonstrates how to track experiments using MLflow, log models and combine multiple flavors into pipelines.
  * [Manage experiments and runs with MLflow](https://github.com/Azure/azureml-examples/blob/main/sdk/python/using-mlflow/runs-management/run_history.ipynb): Demonstrates how to query experiments, runs, metrics, parameters and artifacts from Azure ML using MLflow.


## Support matrix for querying runs and experiments

The MLflow SDK exposes several methods to retrieve runs, including options to control what is returned and how. Use the following table to learn about which of those methods are currently supported in MLflow when connected to Azure Machine Learning:

| Feature | Supported by MLflow | Supported by Azure ML |
| :- | :-: | :-: |
| Ordering runs by run fields (like `start_time`, `end_time`, etc) | **&check;** | **&check;** |
| Ordering runs by attributes | **&check;** | <sup>1</sup> |
| Ordering runs by metrics | **&check;** | <sup>1</sup> |
| Ordering runs by parameters | **&check;** | <sup>1</sup> |
| Ordering runs by tags | **&check;** | <sup>1</sup> |
| Filtering runs by run fields (like `start_time`, `end_time`, etc) |  | <sup>1</sup> |
| Filtering runs by attributes | **&check;** | <sup>1</sup> |
| Filtering runs by metrics | **&check;** | **&check;** |
| Filtering runs by metrics with special characters (escaped) | **&check;** |  |
| Filtering runs by parameters | **&check;** | **&check;** |
| Filtering runs by tags | **&check;** | **&check;** |
| Filtering runs with numeric comparators (metrics) including `=`, `!=`, `>`, `>=`, `<`, and `<=`  | **&check;** | **&check;** |
| Filtering runs with string comparators (params, tags, and attributes): `=` and `!=` | **&check;** | **&check;**<sup>2</sup> |
| Filtering runs with string comparators (params, tags, and attributes): `LIKE`/`ILIKE` | **&check;** |  |
| Filtering runs with comparators `AND` | **&check;** | **&check;** |
| Filtering runs with comparators `OR` |  |  |
| Renaming experiments | **&check;** |  |

> [!NOTE]
> - <sup>1</sup> Check the section [Getting runs inside an experiment](#getting-runs-inside-an-experiment) for instructions and examples on how to achieve the same functionality in Azure ML.
> - <sup>2</sup> `!=` for tags not supported.

## Next steps

* [Manage your models with MLflow](how-to-manage-models.md).
* [Deploy models with MLflow](how-to-deploy-mlflow-models.md).
