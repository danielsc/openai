> Azure Machine Learning doesn't support deleting the entire model container. To achieve the same thing, you will need to delete all the model versions from a given model.

## Support matrix for managing models with MLflow

The MLflow client exposes several methods to retrieve and manage models. The following table shows which of those methods are currently supported in MLflow when connected to Azure ML. It also compares it with other models management capabilities in Azure ML.

| Feature | MLflow | Azure ML with MLflow | Azure ML CLIv2 | Azure ML Studio |
| :- | :-: | :-: | :-: | :-: |
| Registering models in MLflow format | **&check;** | **&check;** | **&check;** | **&check;** |
| Registering models not in MLflow format |  |  | **&check;** | **&check;** |
| Registering models from runs outputs/artifacts | **&check;** | **&check;**<sup>1</sup> | **&check;**<sup>2</sup> | **&check;** |
| Registering models from runs outputs/artifacts in a different tracking server/workspace | **&check;** |  | **&check;**<sup>5</sup> | **&check;**<sup>5</sup> |
| Listing registered models | **&check;** | **&check;** | **&check;** | **&check;** |
| Retrieving details of registered model's versions | **&check;** | **&check;** | **&check;** | **&check;** |
| Editing registered model's versions description | **&check;** | **&check;** | **&check;** | **&check;** |
| Editing registered model's versions tags | **&check;** | **&check;** | **&check;** | **&check;** |
| Renaming registered models | **&check;** | <sup>3</sup> | <sup>3</sup> | <sup>3</sup> |
| Deleting a registered model (container) | **&check;** | <sup>3</sup> | <sup>3</sup> | <sup>3</sup> |
| Deleting a registered model's version | **&check;** | **&check;** | **&check;** | **&check;** |
| Manage MLflow model stages | **&check;** | **&check;** |  |  |
| Search registered models by name | **&check;** | **&check;** | **&check;** | **&check;**<sup>4</sup> |
| Search registered models using string comparators `LIKE` and `ILIKE` | **&check;** |  |  | **&check;**<sup>4</sup> |
| Search registered models by tag |  |  |  | **&check;**<sup>4</sup> |

> [!NOTE]
> - <sup>1</sup> Use URIs with format `runs:/<ruin-id>/<path>`.
> - <sup>2</sup> Use URIs with format `azureml://jobs/<job-id>/outputs/artifacts/<path>`.
> - <sup>3</sup> Registered models are immutable objects in Azure ML.
> - <sup>4</sup> Use search box in Azure ML Studio. Partial match supported.
> - <sup>5</sup> Use [registries](how-to-manage-registries.md).

## Next steps

- [Logging MLflow models](how-to-log-mlflow-models.md)
- [Query & compare experiments and runs with MLflow](how-to-track-experiments-mlflow.md)
- [Guidelines for deploying MLflow models](how-to-deploy-mlflow-models.md)
