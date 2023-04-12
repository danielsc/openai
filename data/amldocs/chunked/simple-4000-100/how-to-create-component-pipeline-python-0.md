
# Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

In this article, you learn how to build an [Azure Machine Learning pipeline](concept-ml-pipelines.md) using Python SDK v2 to complete an image classification task containing three steps: prepare data, train an image classification model, and score the model. Machine learning pipelines optimize your workflow with speed, portability, and reuse, so you can focus on machine learning instead of infrastructure and automation.  

The example trains a small [Keras](https://keras.io/) convolutional neural network to classify images in the [Fashion MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset. The pipeline looks like following.

:::image type="content" source="./media/how-to-create-component-pipeline-python/pipeline-graph.png" alt-text="Screenshot showing pipeline graph of the image classification Keras example." lightbox ="./media/how-to-create-component-pipeline-python/pipeline-graph.png":::


In this article, you complete the following tasks:

> [!div class="checklist"]
> * Prepare input data for the pipeline job
> * Create three components to prepare the data, train and score
> * Compose a Pipeline from the components
> * Get access to workspace with compute
> * Submit the pipeline job
> * Review the output of the components and the trained neural network
> * (Optional) Register the component for further reuse and sharing within workspace

If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/) today.

## Prerequisites

* Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) if you don't already have an Azure Machine Learning workspace.
* A Python environment in which you've installed Azure Machine Learning Python SDK v2 - [install instructions](https://github.com/Azure/azureml-examples/tree/sdk-preview/sdk#getting-started) - check the getting started section. This environment is for defining and controlling your Azure Machine Learning resources and is separate from the environment used at runtime for training.
* Clone examples repository

    To run the training examples, first clone the examples repository and change into the `sdk` directory:

    ```bash
    git clone --depth 1 https://github.com/Azure/azureml-examples --branch sdk-preview
    cd azureml-examples/sdk
    ```

## Start an interactive Python session

This article uses the Python SDK for Azure ML to create and control an Azure Machine Learning pipeline. The article assumes that you'll be running the code snippets interactively in either a Python REPL environment or a Jupyter notebook.

This article is based on the [image_classification_keras_minist_convnet.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet/image_classification_keras_minist_convnet.ipynb) notebook found in the `sdk/jobs/pipelines/2e_image_classification_keras_minist_convnet` directory of the [AzureML Examples](https://github.com/azure/azureml-examples) repository.

## Import required libraries

Import all the Azure Machine Learning required libraries that you'll need for this article:

```python
# import required libraries
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential

from azure.ai.ml import MLClient
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import load_component
```

## Prepare input data for your pipeline job

You need to prepare the input data for this image classification pipeline.

Fashion-MNIST is a dataset of fashion images divided into 10 classes. Each image is a 28x28 grayscale image and there are 60,000 training and 10,000 test images. As an image classification problem, Fashion-MNIST is harder than the classic MNIST handwritten digit database. It's distributed in the same compressed binary form as the original [handwritten digit database](http://yann.lecun.com/exdb/mnist/).
