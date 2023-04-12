
# Train scikit-learn models at scale with Azure Machine Learning

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK version you are using:"]
> * [v1](v1/how-to-train-scikit-learn.md)
> * [v2 (current version)](how-to-train-scikit-learn.md)

In this article, learn how to run your scikit-learn training scripts with Azure Machine Learning Python SDK v2.

The example scripts in this article are used to classify iris flower images to build a machine learning model based on scikit-learn's [iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

Whether you're training a machine learning scikit-learn model from the ground-up or you're bringing an existing model into the cloud, you can use Azure Machine Learning to scale out open-source training jobs using elastic cloud compute resources. You can build, deploy, version, and monitor production-grade models with Azure Machine Learning.

## Prerequisites

You can run the code for this article in either an Azure Machine Learning compute instance, or your own Jupyter Notebook.

 - Azure Machine Learning compute instance
    - Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to create a compute instance. Every compute instance includes a dedicated notebook server pre-loaded with the SDK and the notebooks sample repository.
    - Select the notebook tab in the Azure Machine Learning studio. In the samples training folder, find a completed and expanded notebook by navigating to this directory: **v2  > sdk > jobs > single-step > scikit-learn > train-hyperparameter-tune-deploy-with-sklearn**.
    - You can use the pre-populated code in the sample training folder to complete this tutorial.

 - Your Jupyter notebook server.
    - [Install the Azure Machine Learning SDK (v2)](https://aka.ms/sdk-v2-install).


## Set up the job

This section sets up the job for training by loading the required Python packages, connecting to a workspace, creating a compute resource to run a command job, and creating an environment to run the job.

### Connect to the workspace

First, you'll need to connect to your AzureML workspace. The [AzureML workspace](concept-workspace.md) is the top-level resource for the service. It provides you with a centralized place to work with all the artifacts you create when you use Azure Machine Learning.

We're using `DefaultAzureCredential` to get access to the workspace. This credential should be capable of handling most Azure SDK authentication scenarios.

If `DefaultAzureCredential` does not work for you, see [`azure-identity reference documentation`](/python/api/azure-identity/azure.identity) or [`Set up authentication`](how-to-setup-authentication.md?tabs=sdk) for more available credentials.

```python
# Handle to the workspace
from azure.ai.ml import MLClient

# Authentication package
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

If you prefer to use a browser to sign in and authenticate, you should remove the comments in the following code and use it instead.

```python
# Handle to the workspace
# from azure.ai.ml import MLClient

# Authentication package
# from azure.identity import InteractiveBrowserCredential
# credential = InteractiveBrowserCredential()
```

Next, get a handle to the workspace by providing your Subscription ID, Resource Group name, and workspace name. To find these parameters:

1. Look in the upper-right corner of the Azure Machine Learning studio toolbar for your workspace name.
2. Select your workspace name to show your Resource Group and Subscription ID.
3. Copy the values for Resource Group and Subscription ID into the code.

```python
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id="<SUBSCRIPTION_ID>",
    resource_group_name="<RESOURCE_GROUP>",
    workspace_name="<AML_WORKSPACE_NAME>",
)
```

The result of running this script is a workspace handle that you'll use to manage other resources and jobs.
