In your AutoML job, you can perform an automatic hyperparameter sweep in order to find the optimal model (we call this functionality AutoMode). You only specify the number of trials; the hyperparameter search space, sampling method and early termination policy are not needed. The system will automatically determine the region of the hyperparameter space to sweep based on the number of trials. A value between 10 and 20 will likely work well on many datasets.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
limits:
  max_trials: 10
  max_concurrent_trials: 2
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
# Trigger AutoMode
image_object_detection_job.set_limits(max_trials=10, max_concurrent_trials=2)
```

You can then submit the job to train an image model.

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


### Manual hyperparameter sweeping for image tasks

In your AutoML job, you can specify the model architectures by using `model_name` parameter and configure the settings to perform a hyperparameter sweep over a defined search space to find the optimal model.

In this example, we will train an object detection model with `yolov5` and `fasterrcnn_resnet50_fpn`, both of which are pretrained on COCO, a large-scale object detection, segmentation, and captioning dataset that contains over thousands of labeled images with over 80 label categories.

You can perform a hyperparameter sweep over a defined search space to find the optimal model.

#### Job limits

You can control the resources spent on your AutoML Image training job by specifying the `timeout_minutes`, `max_trials` and the `max_concurrent_trials` for the job in limit settings. Please refer to [detailed description on Job Limits parameters](./how-to-auto-train-image-models.md#job-limits).
# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
limits:
  timeout_minutes: 60
  max_trials: 10
  max_concurrent_trials: 2
```

# [Python SDK](#tab/python)

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=limit-settings)]


The following code defines the search space in preparation for the hyperparameter sweep for each defined architecture, `yolov5` and `fasterrcnn_resnet50_fpn`.  In the search space, specify the range of values for `learning_rate`, `optimizer`, `lr_scheduler`, etc., for AutoML to choose from as it attempts to generate a model with the optimal primary metric. If hyperparameter values are not specified, then default values are used for each architecture.

For the tuning settings, use random sampling to pick samples from this parameter space by using the `random` sampling_algorithm. The job limits configured above, tells automated ML to try a total of 10 trials with these different samples, running two trials at a time on our compute target, which was set up using four nodes. The more parameters the search space has, the more trials you need to find optimal models.

The Bandit early termination policy is also used. This policy terminates poor performing trials; that is, those trials that are not within 20% slack of the best performing trial, which significantly saves compute resources.
