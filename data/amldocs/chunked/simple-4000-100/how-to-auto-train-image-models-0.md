
# Set up AutoML to train computer vision models

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]
> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning you are using:"]
> * [v1](v1/how-to-auto-train-image-models-v1.md)
> * [v2 (current version)](how-to-auto-train-image-models.md)


In this article, you learn how to train computer vision models on image data with automated ML with the Azure Machine Learning CLI extension v2 or the Azure Machine Learning Python SDK v2.

Automated ML supports model training for computer vision tasks like image classification, object detection, and instance segmentation. Authoring AutoML models for computer vision tasks is currently supported via the Azure Machine Learning Python SDK. The resulting experimentation trials, models, and outputs are accessible from the Azure Machine Learning studio UI. [Learn more about automated ml for computer vision tasks on image data](concept-automated-ml.md).

## Prerequisites

# [Azure CLI](#tab/cli)
 [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]


* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).
* Install and [set up CLI (v2)](how-to-configure-cli.md#prerequisites) and make sure you install the `ml` extension.

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* The Azure Machine Learning Python SDK v2 installed.

    To install the SDK you can either,  
    * Create a compute instance, which automatically installs the SDK and is pre-configured for ML workflows. For more information, see [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md).

    * Use the following commands to install Azure ML Python SDK v2:
       * Uninstall previous preview version:
       ```python
       pip uninstall azure-ai-ml
       ```
       * Install the Azure ML Python SDK v2:
       ```python
       pip install azure-ai-ml
       ```
   

## Select your task type

Automated ML for images supports the following task types:

Task type | AutoML Job syntax
---|---
 image classification | CLI v2: `image_classification` <br> SDK v2: `image_classification()`
image classification multi-label | CLI v2: `image_classification_multilabel` <br> SDK v2: `image_classification_multilabel()`
image object detection | CLI v2: `image_object_detection` <br> SDK v2: `image_object_detection()`
image instance segmentation| CLI v2: `image_instance_segmentation` <br> SDK v2: `image_instance_segmentation()`

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

This task type is a required parameter and can be set using the `task` key.

For example:

```yaml
task: image_object_detection
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


Based on the task type, you can create AutoML image jobs using task specific `automl` functions.

For example:

```python
from azure.ai.ml import automl
image_object_detection_job = automl.image_object_detection()
```

## Training and validation data

In order to generate computer vision models, you need to bring labeled image data as input for model training in the form of an `MLTable`. You can create an `MLTable` from training data in JSONL format.

If your training data is in a different format (like, pascal VOC or COCO), you can apply the helper scripts included with the sample notebooks to convert the data to JSONL. Learn more about how to [prepare data for computer vision tasks with automated ML](how-to-prepare-datasets-for-automl-images.md). 

> [!Note]
> The training data needs to have at least 10 images in order to be able to submit an AutoML job. 

> [!Warning]
> Creation of `MLTable` from data in JSONL format is supported using the SDK and CLI only, for this capability. Creating the `MLTable` via UI is not supported at this time. 
