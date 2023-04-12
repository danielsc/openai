* [Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) for image classification
* [Intersection over union](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.jaccard_score.html) for image classification multilabel
* [Mean average precision](how-to-understand-automated-ml.md#object-detection-and-instance-segmentation-metrics) for image object detection
* [Mean average precision](how-to-understand-automated-ml.md#object-detection-and-instance-segmentation-metrics) for image instance segmentation
    
### Job limits

You can control the resources spent on your AutoML Image training job by specifying the `timeout_minutes`, `max_trials` and the `max_concurrent_trials` for the job in limit settings as described in the below example.

Parameter | Detail
-----|----
`max_trials` |  Parameter for maximum number of trials to sweep. Must be an integer between 1 and 1000. When exploring just the default hyperparameters for a given model architecture, set this parameter to 1. The default value is 1.
`max_concurrent_trials`| Maximum number of trials that can run concurrently. If specified, must be an integer between 1 and 100.  The default value is 1. <br><br> **NOTE:** <li> The number of concurrent trials is gated on the resources available in the specified compute target. Ensure that the compute target has the available resources for the desired concurrency.  <li> `max_concurrent_trials` is capped at `max_trials` internally. For example, if user sets `max_concurrent_trials=4`, `max_trials=2`, values would be internally updated as `max_concurrent_trials=2`, `max_trials=2`.
`timeout_minutes`| The amount of time in minutes before the experiment terminates. If none specified, default experiment timeout_minutes is seven days (maximum 60 days)

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
limits:
  timeout_minutes: 60
  max_trials: 10
  max_concurrent_trials: 2
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=limit-settings)]


### Automatically sweeping model hyperparameters (AutoMode)

> [!IMPORTANT]
> This feature is currently in public preview. This preview version is provided without a service-level agreement. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

It is generally hard to predict the best model architecture and hyperparameters for a dataset. Also, in some cases the human time allocated to tuning hyperparameters may be limited. For computer vision tasks, you can specify a number of trials and the system will automatically determine the region of the hyperparameter space to sweep. You do not have to define a hyperparameter search space, a sampling method or an early termination policy.

#### Triggering AutoMode

You can run automatic sweeps by setting `max_trials` to a value greater than 1 in `limits` and by not specifying the search space, sampling method and termination policy. We call this functionality AutoMode; please see an example below.

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
image_object_detection_job.set_limits(max_trials=10, max_concurrent_trials=2)
```

A number of trials between 10 and 20 will likely work well on many datasets. The [time budget](#job-limits) for the AutoML job can still be set, but we recommend doing this only if each trial may take a long time.

> [!Warning]
