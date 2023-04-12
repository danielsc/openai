
# Tutorial: Azure Machine Learning in a day

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Learn how a data scientist uses Azure Machine Learning (Azure ML) to train a model, then use the model for prediction. This tutorial will help you become familiar with the core concepts of Azure ML and their most common usage.

You'll learn how to submit a *command job* to run your *training script* on a specified *compute resource*, configured with the *job environment* necessary to run the script.

The *training script* handles the data preparation, then trains and registers a model. Once you have the model, you'll deploy it as an *endpoint*, then call the endpoint for inferencing.

The steps you'll take are:

> [!div class="checklist"]
> * Connect to your Azure ML workspace
> * Create your compute resource and job environment
> * Create your training script
> * Create and run your command job to run the training script on the compute resource, configured with the appropriate job environment
> * View the output of your training script
> * Deploy the newly-trained model as an endpoint
> * Call the Azure ML endpoint for inferencing


## Prerequisites

* Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to:
    * Create a workspace.
    * Create a cloud-based compute instance to use for your development environment.

* Create a new notebook or copy our notebook.
    * Follow the [Quickstart: Run Juypter notebook in Azure Machine Learning studio](quickstart-run-notebooks.md) steps to create a new notebook.
    * Or use the steps in the quickstart to [clone the v2 tutorials folder](quickstart-run-notebooks.md#learn-from-sample-notebooks), then open the notebook from the **tutorials/azureml-in-a-day/azureml-in-a-day.ipynb** folder in your **File** section.

## Run your notebook

1. On the top bar, select the compute instance you created during the  [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md)  to use for running the notebook.

2. Make sure that the kernel, found on the top right, is `Python 3.10 - SDK v2`.  If not, use the dropdown to select this kernel.

:::image type="content" source="media/tutorial-azure-ml-in-a-day/set-kernel.png" alt-text="Screenshot: Set the kernel.":::


> [!Important]
> The rest of this tutorial contains cells of the tutorial notebook.  Copy/paste them into your new notebook, or switch to the notebook now if you cloned it.
>
> To run a single code cell in a notebook, click the code cell and hit **Shift+Enter**. Or, run the entire notebook by choosing **Run all** from the top toolbar.

## Connect to the workspace

Before you dive in the code, you'll need to connect to your Azure ML workspace. The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning.

We're using `DefaultAzureCredential` to get access to workspace. 
`DefaultAzureCredential` is used to handle most Azure SDK authentication scenarios. 

```python
# Handle to the workspace
from azure.ai.ml import MLClient

# Authentication package
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
```

In the next cell, enter your Subscription ID, Resource Group name and Workspace name. To find these values:

1. In the upper right Azure Machine Learning studio toolbar, select your workspace name.
1. Copy the value for workspace, resource group and subscription ID into the code.  
1. You'll need to copy one value, close the area and paste, then come back for the next one.

:::image type="content" source="media/tutorial-azure-ml-in-a-day/find-credentials.png" alt-text="Screenshot: find the credentials for your code in the upper right of the toolbar.":::

```python
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id="<SUBSCRIPTION_ID>",
    resource_group_name="<RESOURCE_GROUP>",
    workspace_name="<AML_WORKSPACE_NAME>",
)
```
