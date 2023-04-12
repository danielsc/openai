
# Tutorial: Train an object detection model with AutoML and Python

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning you are using:"]
> * [v1](v1/tutorial-auto-train-image-models-v1.md)
> * [v2 (current version)](tutorial-auto-train-image-models.md)


In this tutorial, you learn how to train an object detection model using Azure Machine Learning automated ML with the Azure Machine Learning CLI extension v2 or the Azure Machine Learning Python SDK v2.
This object detection model identifies whether the image contains objects, such as a can, carton, milk bottle, or water bottle.

Automated ML accepts training data and configuration settings, and automatically iterates through combinations of different feature normalization/standardization methods, models, and hyperparameter settings to arrive at the best model.


You'll write code using the Python SDK in this tutorial and learn the following tasks:

> [!div class="checklist"]
> * Download and transform data
> * Train an automated machine learning object detection model
> * Specify hyperparameter values for your model
> * Perform a hyperparameter sweep
> * Deploy your model
> * Visualize detections

## Prerequisites

* If you don’t have an Azure subscription, create a free account before you begin. Try the [free or paid version](https://azure.microsoft.com/free/) of Azure Machine Learning today.

* Python 3.6 or 3.7 are supported for this feature

* Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md#create-the-workspace) if you don't already have an Azure Machine Learning workspace.

* Download and unzip the [**odFridgeObjects.zip*](https://cvbp-secondary.z19.web.core.windows.net/datasets/object_detection/odFridgeObjects.zip) data file. The dataset is annotated in Pascal VOC format, where each image corresponds to an xml file. Each xml file contains information on where its corresponding image file is located and also contains information about the bounding boxes and the object labels. In order to use this data, you first need to convert it to the required JSONL format as seen in the [Convert the downloaded data to JSONL](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb) section of the notebook. 

# [Azure CLI](#tab/cli)

 [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

This tutorial is also available in the [azureml-examples repository on GitHub](https://github.com/Azure/azureml-examples/tree/sdk-preview/cli/jobs/automl-standalone-jobs/cli-automl-image-object-detection-task-fridge-items). If you wish to run it in your own local environment, setup using the following instructions

* Install and [set up CLI (v2)](how-to-configure-cli.md#prerequisites) and make sure you install the `ml` extension.

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


This tutorial is also available in the [azureml-examples repository on GitHub](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items). If you wish to run it in your own local environment, setup using the following instructions

* Use the following commands to install Azure ML Python SDK v2:
   * Uninstall previous preview version:
   ```python
   pip uninstall azure-ai-ml
   ```
   * Install the Azure ML Python SDK v2:
   ```python
   pip install azure-ai-ml
   ```

    > [!NOTE]
    > Only Python 3.6 and 3.7 are compatible with automated ML support for computer vision tasks. 


## Compute target setup

You first need to set up a compute target to use for your automated ML model training. Automated ML models for image tasks require GPU SKUs.

This tutorial uses the NCsv3-series (with V100 GPUs) as this type of compute target leverages multiple GPUs to speed up training. Additionally, you can set up multiple nodes to take advantage of parallelism when tuning hyperparameters for your model.
