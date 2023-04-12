
# Train Keras models at scale with Azure Machine Learning

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK version you are using:"]
> * [v1](v1/how-to-train-keras.md)
> * [v2 (current version)](how-to-train-keras.md)

In this article, learn how to run your Keras training scripts using the Azure Machine Learning (AzureML) Python SDK v2.

The example code in this article uses AzureML to train, register, and deploy a Keras model built using the TensorFlow backend. The model, a deep neural network (DNN) built with the [Keras Python library](https://keras.io) running on top of [TensorFlow](https://www.tensorflow.org/overview), classifies handwritten digits from the popular [MNIST dataset](http://yann.lecun.com/exdb/mnist/).

Keras is a high-level neural network API capable of running top of other popular DNN frameworks to simplify development. With AzureML, you can rapidly scale out training jobs using elastic cloud compute resources. You can also track your training runs, version models, deploy models, and much more.

Whether you're developing a Keras model from the ground-up or you're bringing an existing model into the cloud, AzureML can help you build production-ready models.

> [!NOTE]
> If you are using the Keras API **tf.keras** built into TensorFlow and not the standalone Keras package, refer instead to [Train TensorFlow models](how-to-train-tensorflow.md).

## Prerequisites

To benefit from this article, you'll need to:

- Access an Azure subscription. If you don't have one already, [create a free account](https://azure.microsoft.com/free/).
- Run the code in this article using either an Azure Machine Learning compute instance or your own Jupyter notebook.
    - Azure Machine Learning compute instance—no downloads or installation necessary
        - Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to create a dedicated notebook server pre-loaded with the SDK and the sample repository.
        - In the samples deep learning folder on the notebook server, find a completed and expanded notebook by navigating to this directory: **v2  > sdk > python > jobs > single-step > tensorflow > train-hyperparameter-tune-deploy-with-keras**.
    - Your Jupyter notebook server
        - [Install the Azure Machine Learning SDK (v2)](https://aka.ms/sdk-v2-install).
- Download the training scripts [keras_mnist.py](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/tensorflow/train-hyperparameter-tune-deploy-with-keras/src/keras_mnist.py) and [utils.py](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/tensorflow/train-hyperparameter-tune-deploy-with-keras/src/utils.py).

You can also find a completed [Jupyter Notebook version](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/tensorflow/train-hyperparameter-tune-deploy-with-keras/train-hyperparameter-tune-deploy-with-keras.ipynb) of this guide on the GitHub samples page.

[!INCLUDE [gpu quota](../../includes/machine-learning-gpu-quota-prereq.md)]

## Set up the job

This section sets up the job for training by loading the required Python packages, connecting to a workspace, creating a compute resource to run a command job, and creating an environment to run the job.

### Connect to the workspace

First, you'll need to connect to your AzureML workspace. The [AzureML workspace](concept-workspace.md) is the top-level resource for the service. It provides you with a centralized place to work with all the artifacts you create when you use Azure Machine Learning.

We're using `DefaultAzureCredential` to get access to the workspace. This credential should be capable of handling most Azure SDK authentication scenarios.

If `DefaultAzureCredential` doesn't work for you, see [`azure-identity reference documentation`](/python/api/azure-identity/azure.identity) or [`Set up authentication`](how-to-setup-authentication.md?tabs=sdk) for more available credentials.
