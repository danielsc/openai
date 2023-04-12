
# Train PyTorch models at scale with Azure Machine Learning

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK version you are using:"]
> * [v1](v1/how-to-train-pytorch.md)
> * [v2 (current version)](how-to-train-pytorch.md)

In this article, you'll learn to train, hyperparameter tune, and deploy a [PyTorch](https://pytorch.org/) model using the Azure Machine Learning (AzureML) Python SDK v2.

You'll use the example scripts in this article to classify chicken and turkey images to build a deep learning neural network (DNN) based on [PyTorch's transfer learning tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html). Transfer learning is a technique that applies knowledge gained from solving one problem to a different but related problem. Transfer learning shortens the training  process by requiring less data, time, and compute resources than training from scratch. To learn more about transfer learning, see the [deep learning vs machine learning](./concept-deep-learning-vs-machine-learning.md#what-is-transfer-learning) article.

Whether you're training a deep learning PyTorch model from the ground-up or you're bringing an existing model into the cloud, you can use AzureML to scale out open-source training jobs using elastic cloud compute resources. You can build, deploy, version, and monitor production-grade models with AzureML.

## Prerequisites

To benefit from this article, you'll need to:

- Access an Azure subscription. If you don't have one already, [create a free account](https://azure.microsoft.com/free/).
- Run the code in this article using either an Azure Machine Learning compute instance or your own Jupyter notebook.
    - Azure Machine Learning compute instance—no downloads or installation necessary
        - Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to create a dedicated notebook server pre-loaded with the SDK and the sample repository.
        - In the samples deep learning folder on the notebook server, find a completed and expanded notebook by navigating to this directory: **v2  > sdk > python > jobs > single-step > pytorch > train-hyperparameter-tune-deploy-with-pytorch**.
    - Your Jupyter notebook server
        - [Install the Azure Machine Learning SDK (v2)](https://aka.ms/sdk-v2-install).
        - Download the training script file [pytorch_train.py](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/pytorch/train-hyperparameter-tune-deploy-with-pytorch/src/pytorch_train.py).

You can also find a completed [Jupyter Notebook version](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/pytorch/train-hyperparameter-tune-deploy-with-pytorch/train-hyperparameter-tune-deploy-with-pytorch.ipynb) of this guide on the GitHub samples page.

[!INCLUDE [gpu quota](../../includes/machine-learning-gpu-quota-prereq.md)]

## Set up the job

This section sets up the job for training by loading the required Python packages, connecting to a workspace, creating a compute resource to run a command job, and creating an environment to run the job.

### Connect to the workspace

First, you'll need to connect to your AzureML workspace. The [AzureML workspace](concept-workspace.md) is the top-level resource for the service. It provides you with a centralized place to work with all the artifacts you create when you use Azure Machine Learning.

We're using `DefaultAzureCredential` to get access to the workspace. This credential should be capable of handling most Azure SDK authentication scenarios.

If `DefaultAzureCredential` doesn't work for you, see [`azure-identity reference documentation`](/python/api/azure-identity/azure.identity) or [`Set up authentication`](how-to-setup-authentication.md?tabs=sdk) for more available credentials.

```python
# Handle to the workspace
from azure.ai.ml import MLClient

# Authentication package
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```
