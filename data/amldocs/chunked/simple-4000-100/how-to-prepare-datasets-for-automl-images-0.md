
# Prepare data for computer vision tasks with automated machine learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning you are using:"]
> * [v1](v1/how-to-prepare-datasets-for-automl-images-v1.md)
> * [v2 (current version)](how-to-prepare-datasets-for-automl-images.md)

> [!IMPORTANT]
> Support for training computer vision models with automated ML in Azure Machine Learning is an experimental public preview feature. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

In this article, you learn how to prepare image data for training computer vision models with [automated machine learning in Azure Machine Learning](concept-automated-ml.md). 

To generate models for computer vision tasks with automated machine learning, you need to bring labeled image data as input for model training in the form of an `MLTable`. 

You can create an `MLTable` from labeled training data in JSONL format. 
If your labeled training data is in a different format (like, pascal VOC or COCO), you can use a [conversion script](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/coco2jsonl.py) to first convert it to JSONL, and then create an `MLTable`. Alternatively, you can use  Azure Machine Learning's [data labeling tool](how-to-create-image-labeling-projects.md) to manually label images, and export the labeled data to use for training your AutoML model.

## Prerequisites

* Familiarize yourself with the accepted [schemas for JSONL files for AutoML computer vision experiments](reference-automl-images-schema.md).

## Get labeled data 
In order to train computer vision models using AutoML, you need to first get labeled training data. The images need to be uploaded to the cloud and label annotations need to be in JSONL format. You can either use the Azure ML Data Labeling tool to label your data or you could start with pre-labeled image data.

### Using Azure ML Data Labeling tool to label your training data
If you don't have pre-labeled data, you can use Azure Machine Learning's [data labeling tool](how-to-create-image-labeling-projects.md) to manually label images. This tool automatically generates the data required for training in the accepted format.

It helps to create, manage, and monitor data labeling tasks for 

+ Image classification (multi-class and multi-label)
+ Object detection (bounding box)
+ Instance segmentation (polygon)

If you already have a data labeling project and you want to use that data, you can [export your labeled data as an Azure ML Dataset](how-to-create-image-labeling-projects.md#export-the-labels) and then access the dataset under 'Datasets' tab in Azure ML Studio. This exported dataset can then be passed as an input using `azureml:<tabulardataset_name>:<version>` format. Here is an example on how to pass existing dataset as input for training computer vision models.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_data:
  path: azureml:odFridgeObjectsTrainingDataset:1
  type: mltable
  mode: direct
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.constants import AssetTypes, InputOutputModes
from azure.ai.ml import Input

# Training MLTable with v1 TabularDataset
my_training_data_input = Input(
    type=AssetTypes.MLTABLE, path="azureml:odFridgeObjectsTrainingDataset:1",
    mode=InputOutputModes.DIRECT
)
```

# [Studio](#tab/Studio)

Please refer to Cli/Sdk tabs for reference.


### Using pre-labeled training data from local machine
If you have previously labeled data that you would like to use to train your model, you will first need to upload the images to the default Azure Blob Storage of your Azure ML Workspace and register it as a [data asset](how-to-create-data-assets.md). 
