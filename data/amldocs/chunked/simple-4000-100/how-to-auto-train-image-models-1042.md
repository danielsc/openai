By default, each model trains on a single VM. If training a model is taking too much time, using VMs that contain multiple GPUs may help. The time to train a model on large datasets should decrease in roughly linear proportion to the number of GPUs used. (For instance, a model should train roughly twice as fast on a VM with two GPUs as on a VM with one GPU.) If the time to train a model is still high on a VM with multiple GPUs, you can increase the number of VMs used to train each model. Similar to multi-GPU training, the time to train a model on large datasets should also decrease in roughly linear proportion to the number of VMs used. When training a model across multiple VMs, be sure to use a compute SKU that supports [InfiniBand](how-to-train-distributed-gpu.md#accelerating-distributed-gpu-training-with-infiniband) for best results. You can configure the number of VMs used to train a single model by setting the `node_count_per_trial` property of the AutoML job.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
properties:
  node_count_per_trial: "2"
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Multi-node training is supported for all tasks. The `node_count_per_trial` property can be specified using the task-specific `automl` functions. For instance, for object detection:

```python
from azure.ai.ml import automl

image_object_detection_job = automl.image_object_detection(
    ...,
    properties={"node_count_per_trial": 2}
)
```

### Streaming image files from storage

By default, all image files are downloaded to disk prior to model training. If the size of the image files is greater than available disk space, the job will fail. Instead of downloading all images to disk, you can select to stream image files from Azure storage as they're needed during training. Image files are streamed from Azure storage directly to system memory, bypassing disk. At the same time, as many files as possible from storage are cached on disk to minimize the number of requests to storage.

> [!NOTE]
> If streaming is enabled, ensure the Azure storage account is located in the same region as compute to minimize cost and latency.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_parameters:
  advanced_settings: >
    {"stream_image_files": true}
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml import automl

image_object_detection_job = automl.image_object_detection(...)

image_object_detection_job.set_training_parameters(
    ...,
    advanced_settings='{"stream_image_files": true}'
)
```


## Example notebooks
Review detailed code examples and use cases in the [GitHub notebook repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs). Please check the folders with 'automl-image-' prefix for samples specific to building computer vision models.


## Code examples

# [Azure CLI](#tab/cli)

Review detailed code examples and use cases in the [azureml-examples repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/automl-standalone-jobs). 


# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Review detailed code examples and use cases in the [GitHub notebook repository for automated machine learning samples](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs). 

## Next steps

* [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md).
* [Troubleshoot automated ML experiments](how-to-troubleshoot-auto-ml.md).
