
# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

You can create data inputs from training and validation MLTable from your local directory or cloud storage with the following code:

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=data-load)]

Training data is a required parameter and is passed in using the `training_data` parameter of the task specific `automl` type function. You can optionally specify another MLTable as a validation data with the `validation_data` parameter. If no validation data is specified, 20% of your training data will be used for validation by default, unless you pass `validation_data_size` argument with a different value.

Target column name is a required parameter and used as target for supervised ML task. It's passed in using the `target_column_name` parameter of the task specific `automl` function. For example,

```python
from azure.ai.ml import automl
image_object_detection_job = automl.image_object_detection(
    training_data=my_training_data_input,
    validation_data=my_validation_data_input,
    target_column_name="label"
)
```

## Compute to run experiment

Provide a [compute target](concept-azure-machine-learning-architecture.md#compute-targets) for automated ML to conduct model training. Automated ML models for computer vision tasks require GPU SKUs and support NC and ND families. We recommend the NCsv3-series (with v100 GPUs) for faster training. A compute target with a multi-GPU VM SKU leverages multiple GPUs to also speed up training. Additionally, when you set up a compute target with multiple nodes you can conduct faster model training through parallelism when tuning hyperparameters for your model.

> [!NOTE]
> If you are using a [compute instance](concept-compute-instance.md) as your compute target, please make sure that multiple AutoML jobs are not run at the same time. Also, please make sure that `max_concurrent_trials` is set to 1 in your [job limits](#job-limits).

The compute target is passed in using the `compute` parameter. For example:

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
compute: azureml:gpu-cluster
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml import automl

compute_name = "gpu-cluster"
image_object_detection_job = automl.image_object_detection(
    compute=compute_name,
)
```

## Configure experiments

For computer vision tasks, you can launch either [individual trials](#individual-trials), [manual sweeps](#manually-sweeping-model-hyperparameters) or [automatic sweeps](#automatically-sweeping-model-hyperparameters-automode). We recommend starting with an automatic sweep to get a first baseline model. Then, you can try out individual trials with certain models and hyperparameter configurations. Finally, with manual sweeps you can explore multiple hyperparameter values near the more promising models and hyperparameter configurations. This three step workflow (automatic sweep, individual trials, manual sweeps) avoids searching the entirety of the hyperparameter space, which grows exponentially in the number of hyperparameters.

Automatic sweeps can yield competitive results for many datasets. Additionally, they do not require advanced knowledge of model architectures, they take into account hyperparameter correlations and they work seamlessly across different hardware setups. All these reasons make them a strong option for the early stage of your experimentation process.

### Primary metric

An AutoML training job uses a primary metric for model optimization and hyperparameter tuning. The primary metric depends on the task type as shown below; other primary metric values are currently not supported. 

* [Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) for image classification
