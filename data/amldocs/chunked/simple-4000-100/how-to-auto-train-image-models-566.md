 Please note that these two flags are independent of each other and can also be used in combination using the following settings.

```python
from azure.ai.ml import automl

image_object_detection_job = automl.image_object_detection(...)

image_object_detection_job.set_training_parameters(
    ...,
    advanced_settings='{"apply_automl_train_augmentations": false, "apply_mosaic_for_yolo": false}'
)
```


In our experiments, we found that these augmentations help the model to generalize better. Therefore, when these augmentations are switched off, we recommend the users to combine them with other offline augmentations to get better results.


##  Incremental training (optional)

Once the training job is done, you have the option to further train the model by loading the trained model checkpoint. You can either use the same dataset or a different one for incremental training. 


### Pass the checkpoint via job ID

You can pass the job ID that you want to load the checkpoint from.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_parameters:
  checkpoint_run_id : "target_checkpoint_run_id"
```


# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

To find the job ID from the desired model, you can use the following code. 

```python
# find a job id to get a model checkpoint from
import mlflow

# Obtain the tracking URL from MLClient
MLFLOW_TRACKING_URI = ml_client.workspaces.get(
    name=ml_client.workspace_name
).mlflow_tracking_uri
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

from mlflow.tracking.client import MlflowClient

mlflow_client = MlflowClient()
mlflow_parent_run = mlflow_client.get_run(automl_job.name)

# Fetch the id of the best automl child trial.
target_checkpoint_run_id = mlflow_parent_run.data.tags["automl_best_child_run_id"]
```

To pass a checkpoint via the job ID, you need to use the `checkpoint_run_id` parameter in `set_training_parameters` function.

```python
image_object_detection_job = automl.image_object_detection(
    compute=compute_name,
    experiment_name=exp_name,
    training_data=my_training_data_input,
    validation_data=my_validation_data_input,
    target_column_name="label",
    primary_metric=ObjectDetectionPrimaryMetrics.MEAN_AVERAGE_PRECISION,
    tags={"my_custom_tag": "My custom value"},
)

image_object_detection_job.set_training_parameters(checkpoint_run_id=target_checkpoint_run_id)

automl_image_job_incremental = ml_client.jobs.create_or_update(
    image_object_detection_job
) 
```



## Submit the AutoML job



# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

To submit your AutoML job, you run the following CLI v2 command with the path to your .yml file, workspace name, resource group and subscription ID.

```azurecli
az ml job create --file ./hello-automl-job-basic.yml --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

When you've configured your AutoML Job to the desired settings, you can submit the job.

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=submit-run)]

## Outputs and evaluation metrics

The automated ML training jobs generates output model files, evaluation metrics, logs and deployment artifacts like the scoring file and the environment file which can be viewed from the outputs and logs and metrics tab of the child jobs.

> [!TIP]
> Check how to navigate to the job results from the  [View job results](how-to-understand-automated-ml.md#view-job-results) section.

For definitions and examples of the performance charts and metrics provided for each job, see [Evaluate automated machine learning experiment results](how-to-understand-automated-ml.md#metrics-for-image-models-preview).
