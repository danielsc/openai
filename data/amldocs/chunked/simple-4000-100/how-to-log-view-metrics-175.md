|Log numpy metrics or PIL image objects|`mlflow.log_image(img, "figure.png")`| `img` should be an instance of `numpy.ndarray` or `PIL.Image.Image`. `figure.png` is the name of the artifact that will be generated inside of the run. It doesn't have to be an existing file.|
|Log matlotlib plot or image file|` mlflow.log_figure(fig, "figure.png")`| `figure.png` is the name of the artifact that will be generated inside of the run. It doesn't have to be an existing file. |

## Logging other types of data

|Logged Value|Example code| Notes|
|----|----|----|
|Log text in a text file | `mlflow.log_text("text string", "notes.txt")`| Text is persisted inside of the run in a text file with name `notes.txt`. |
|Log dictionaries as `JSON` and `YAML` files | `mlflow.log_dict(dictionary, "file.yaml"` | `dictionary` is a dictionary object containing all the structure that you want to persist as `JSON` or `YAML` file. |
|Log a trivial file already existing | `mlflow.log_artifact("path/to/file.pkl")`| Files are always logged in the root of the run. If `artifact_path` is provided, then the file is logged in a folder as indicated in that parameter. |
|Log all the artifacts in an existing folder | `mlflow.log_artifacts("path/to/folder")`| Folder structure is copied to the run, but the root folder indicated is not included. |

## Logging models

MLflow introduces the concept of "models" as a way to package all the artifacts required for a given model to function. Models in MLflow are always a folder with an arbitrary number of files, depending on the framework used to generate the model. Logging models has the advantage of tracking all the elements of the model as a single entity that can be __registered__ and then __deployed__. On top of that, MLflow models enjoy the benefit of [no-code deployment](how-to-deploy-mlflow-models.md) and can be used with the [Responsible AI dashboard](how-to-responsible-ai-dashboard.md) in studio. Read the article [From artifacts to models in MLflow](concept-mlflow-models.md) for more information.

To save the model from a training run, use the `log_model()` API for the framework you're working with. For example, [mlflow.sklearn.log_model()](https://mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model). For more details about how to log MLflow models see [Logging MLflow models](how-to-log-mlflow-models.md) For migrating existing models to MLflow, see [Convert custom models to MLflow](how-to-convert-custom-model-to-mlflow.md).

## Automatic logging

With Azure Machine Learning and MLflow, users can log metrics, model parameters and model artifacts automatically when training a model. Each framework decides what to track automatically for you. A [variety of popular machine learning libraries](https://mlflow.org/docs/latest/tracking.html#automatic-logging) are supported. [Learn more about Automatic logging with MLflow](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog). 

To enable [automatic logging](https://mlflow.org/docs/latest/tracking.html#automatic-logging) insert the following code before your training code:

```Python
mlflow.autolog()
```

> [!TIP]
> You can control what gets automatically logged wit autolog. For instance, if you indicate `mlflow.autolog(log_models=False)`, MLflow will log everything but models for you. Such control is useful in cases where you want to log models manually but still enjoy automatic logging of metrics and parameters. Also notice that some frameworks may disable automatic logging of models if the trained model goes behond specific boundaries. Such behavior depends on the flavor used and we recommend you to view they documentation if this is your case.

## View jobs/runs information with MLflow

You can view the logged information using MLflow through the [MLflow.entities.Run](https://mlflow.org/docs/latest/python_api/mlflow.entities.html#mlflow.entities.Run) object:

```python
import mlflow

run = mlflow.get_run(run_id="<RUN_ID>")
```

You can view the metrics, parameters, and tags for the run in the data field of the run object.
