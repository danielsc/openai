1. Submit the local run and ensure you set the parameter `backend = "azureml"`, which adds support of automatic tracking, model's capture, log files, snapshots, and printed errors in your workspace. In this example we assume the MLflow project you are trying to run is in the same folder you currently are, `uri="."`.

    # [MLflow CLI](#tab/cli)
 
    ```bash
    mlflow run . --backend azureml --backend-config backend_config.json -P alpha=0.3
    ```
  
    # [Python](#tab/sdk)
  
    ```python
    local_env_run = mlflow.projects.run(
        uri=".", 
        parameters={"alpha":0.3},
        backend = "azureml",
        backend_config = backend_config, 
    )
    ```
    
  
    > [!NOTE]
    > Since Azure Machine Learning jobs always run in the context of environments, the parameter `env_manager` is ignored.
  
    View your runs and metrics in the [Azure Machine Learning studio](https://ml.azure.com).


## Clean up resources

If you don't plan to use the logged metrics and artifacts in your workspace, the ability to delete them individually is currently unavailable. Instead, delete the resource group that contains the storage account and workspace, so you don't incur any charges:

1. In the Azure portal, select **Resource groups** on the far left.

    :::image type="content" source="media/how-to-use-mlflow-azure-databricks/delete-resources.png" alt-text="Image showing how to delete an Azure resource group.":::    

1. From the list, select the resource group you created.

1. Select **Delete resource group**.

1. Enter the resource group name. Then select **Delete**.

## Example notebooks

The [MLflow with Azure ML notebooks](https://github.com/Azure/MachineLearningNotebooks/tree/master/how-to-use-azureml/track-and-monitor-experiments/using-mlflow) demonstrate and expand upon concepts presented in this article.

  * [Train an MLflow project on a local compute](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/track-and-monitor-experiments/using-mlflow/train-projects-local/train-projects-local.ipynb)
  * [Train an MLflow project on remote compute](https://github.com/Azure/MachineLearningNotebooks/blob/master/how-to-use-azureml/track-and-monitor-experiments/using-mlflow/train-projects-remote/train-projects-remote.ipynb).

> [!NOTE]
> A community-driven repository of examples using mlflow can be found at https://github.com/Azure/azureml-examples.

## Next steps

* [Track Azure Databricks runs with MLflow](how-to-use-mlflow-azure-databricks.md).
* [Query & compare experiments and runs with MLflow](how-to-track-experiments-mlflow.md).
* [Manage models registries in Azure Machine Learning with MLflow](how-to-manage-models-mlflow.md).
* [Guidelines for deploying MLflow models](how-to-deploy-mlflow-models.md).

