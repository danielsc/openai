
# Make predictions with ONNX on computer vision models from AutoML

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"] 
> * [v1](v1/how-to-inference-onnx-automl-image-models-v1.md) 
> * [v2 (current version)](how-to-inference-onnx-automl-image-models.md) 

In this article, you will learn how to use Open Neural Network Exchange (ONNX) to make predictions on computer vision models generated from automated machine learning (AutoML) in Azure Machine Learning. 

To use ONNX for predictions, you need to:
 
1. Download ONNX model files from an AutoML training run.
1. Understand the inputs and outputs of an ONNX model.
1. Preprocess your data so that it's in the required format for input images.
1. Perform inference with ONNX Runtime for Python.
1. Visualize predictions for object detection and instance segmentation tasks.

[ONNX](https://onnx.ai/about.html) is an open standard for machine learning and deep learning models. It enables model import and export (interoperability) across the popular AI frameworks. For more details, explore the [ONNX GitHub project](https://github.com/onnx/onnx).

[ONNX Runtime](https://onnxruntime.ai/index.html) is an open-source project that supports cross-platform inference. ONNX Runtime provides APIs across programming languages (including Python, C++, C#, C, Java, and JavaScript). You can use these APIs to perform inference on input images. After you have the model that has been exported to ONNX format, you can use these APIs on any programming language that your project needs. 

In this guide, you'll learn how to use [Python APIs for ONNX Runtime](https://onnxruntime.ai/docs/get-started/with-python.html) to make predictions on images for popular vision tasks. You can use these ONNX exported models across languages.

## Prerequisites

* Get an AutoML-trained computer vision model for any of the supported image tasks: classification, object detection, or instance segmentation. [Learn more about AutoML support for computer vision tasks](how-to-auto-train-image-models.md).

* Install the [onnxruntime](https://onnxruntime.ai/docs/get-started/with-python.html) package. The methods in this article have been tested with versions 1.3.0 to 1.8.0.


## Download ONNX model files

You can download ONNX model files from AutoML runs by using the Azure Machine Learning studio UI or the Azure Machine Learning Python SDK. We recommend downloading via the SDK with the experiment name and parent run ID.


### Azure Machine Learning studio

On Azure Machine Learning studio, go to your experiment by using the hyperlink to the experiment generated in the training notebook, or by selecting the experiment name on the **Experiments** tab under **Assets**. Then select the best child run. 

Within the best child run, go to **Outputs+logs** > **train_artifacts**. Use the **Download** button to manually download the following files:

- *labels.json*: File that contains all the classes or labels in the training dataset.
- *model.onnx*: Model in ONNX format. 

![Screenshot that shows selections for downloading O N N X model files.](./media/how-to-inference-onnx-automl-image-models/onnx-files-manual-download.png)

Save the downloaded model files in a directory. The example in this article uses the *./automl_models* directory. 

### Azure Machine Learning Python SDK

With the SDK, you can select the best child run (by primary metric) with the experiment name and parent run ID. Then, you can download the *labels.json* and *model.onnx* files.

The following code returns the best child run based on the relevant primary metric.
```python
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

credential = DefaultAzureCredential()
ml_client = None
try:
    ml_client = MLClient.from_config(credential)
except Exception as ex:
    print(ex)
    # Enter details of your AML workspace
    subscription_id = ''   
    resource_group = ''  
    workspace_name = ''
    ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)
```
