
# Tutorial: Create production ML pipelines with Python SDK v2 in a Jupyter notebook

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!NOTE]
> For a tutorial that uses SDK v1 to build a pipeline, see [Tutorial: Build an Azure Machine Learning pipeline for image classification](v1/tutorial-pipeline-python-sdk.md)
> 

In this tutorial, you'll use Azure Machine Learning (Azure ML) to create a production ready machine learning (ML) project, using AzureML Python SDK v2.

You'll learn how to use the AzureML Python SDK v2 to:

> [!div class="checklist"]
> 
> * Connect to your Azure ML workspace
> * Create Azure ML data assets
> * Create reusable Azure ML components
> * Create, validate and run Azure ML pipelines
> * Deploy the newly-trained model as an endpoint
> * Call the Azure ML endpoint for inferencing

## Prerequisites

* Complete the [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to:
    * Create a workspace.
    * Create a cloud-based compute instance to use for your development environment.
    * Create a cloud-based compute cluster to use for training your model.
* Complete the [Quickstart: Run Jupyter notebooks in studio](quickstart-run-notebooks.md) to clone the **SDK v2/tutorials** folder.


## Open the notebook

1. Open the **tutorials** folder that was cloned into your **Files** section from the [Quickstart: Run Jupyter notebooks in studio](quickstart-run-notebooks.md).
    
1. Select the **e2e-ml-workflow.ipynb** file from your **tutorials/azureml-examples/tutorials/e2e-ds-experience/** folder. 

    :::image type="content" source="media/tutorial-pipeline-python-sdk/expand-folder.png" alt-text="Screenshot shows the open tutorials folder.":::

1. On the top bar, select the compute instance you created during the  [Quickstart: Get started with Azure Machine Learning](quickstart-create-resources.md) to use for running the notebook.

> [!Important]
> The rest of this article contains the same content as you see in the notebook.  
>
> Switch to the Jupyter Notebook now if you want to run the code while you read along.
> To run a single code cell in a notebook, click the code cell and hit **Shift+Enter**. Or, run the entire notebook by choosing **Run all** from the top toolbar

## Introduction

In this tutorial, you'll create an Azure ML pipeline to train a model for credit default prediction. The pipeline handles the data preparation, training and registering the trained model.  You'll then run the pipeline, deploy the model and use it.

The image below shows the pipeline as you'll see it in the AzureML portal once submitted. It's a rather simple pipeline we'll use to walk you through the AzureML SDK v2.

The two steps are first data preparation and second training. 

:::image type="content" source="media/tutorial-pipeline-python-sdk/pipeline-overview.jpg" alt-text="Diagram shows overview of the pipeline.":::

## Set up the pipeline resources

The Azure ML framework can be used from CLI, Python SDK, or studio interface. In this example, you'll use the AzureML Python SDK v2 to create a pipeline. 

Before creating the pipeline, you'll set up the resources the pipeline will use:

* The data asset for training
* The software environment to run the pipeline
* A compute resource to where the job will run

## Connect to the workspace

Before we dive in the code, you'll need to connect to your Azure ML workspace. The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. 

[!Notebook-python[] (~/azureml-examples-main/tutorials/e2e-ds-experience/e2e-ml-workflow.ipynb?name=import-mlclient)]

In the next cell, enter your Subscription ID, Resource Group name and Workspace name. To find your Subscription ID:
1. In the upper right Azure Machine Learning studio toolbar, select your workspace name.
1. You'll see the values you need for **<SUBSCRIPTION_ID>**, **<RESOURCE_GROUP>**, and **<AML_WORKSPACE_NAME>**.
