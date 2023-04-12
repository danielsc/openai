

# What is an Azure Machine Learning workspace?

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning.  The workspace keeps a history of all training runs, including logs, metrics, output, and a snapshot of your scripts. You use this information to determine which training run produces the best model.  

Once you have a model you like, you register it with the workspace. You then use the registered model and scoring scripts to deploy to an [online endpoint](concept-endpoints.md) as a REST-based HTTP endpoint.

## Taxonomy 

+ A workspace can contain [Azure Machine Learning compute instances](concept-compute-instance.md), cloud resources configured with the Python environment necessary to run Azure Machine Learning.

+ [User roles](how-to-assign-roles.md) enable you to share your workspace with other users, teams, or projects.
+ [Compute targets](concept-compute-target.md) are used to run your experiments.
+ When you create the workspace, [associated resources](#associated-resources) are also created for you.
+ Jobs are training runs you use to build your models.  You can organize your jobs into Experiments.
+ [Pipelines](concept-ml-pipelines.md) are reusable workflows for training and retraining your model.
+ [Data assets](concept-data.md) aid in management of the data you use for model training and pipeline creation.
+ Once you have a model you want to deploy, you create a registered model.
+ Use the registered model and a scoring script to create an [online endpoint](concept-endpoints.md).

## Tools for workspace interaction

You can interact with your workspace in the following ways:

+ On the web:
    + [Azure Machine Learning studio ](https://ml.azure.com) 
    + [Azure Machine Learning designer](concept-designer.md) 
+ In any Python environment with the [Azure Machine Learning SDK for Python](https://aka.ms/sdk-v2-install).
+ On the command line using the Azure Machine Learning [CLI extension](how-to-configure-cli.md)
+ [Azure Machine Learning VS Code Extension](how-to-manage-resources-vscode.md#workspaces)

## Machine learning with a workspace

Machine learning tasks read and/or write artifacts to your workspace.

+ Run an experiment to train a model - writes job run results to the workspace.
+ Use automated ML to train a model - writes training results to the workspace.
+ Register a model in the workspace.
+ Deploy a model - uses the registered model to create a deployment.
+ Create and run reusable workflows.
+ View machine learning artifacts such as jobs, pipelines, models, deployments.
+ Track and monitor models.

## Workspace management

You can also perform the following workspace management tasks:

| Workspace management task           | Portal      | Studio      | Python SDK  | Azure CLI   | VS Code     |
|-------------------------------------|-------------|-------------|-------------|-------------|-------------|
| Create a workspace                  | **&check;** | **&check;** | **&check;** | **&check;** | **&check;** |
| Manage workspace access             | **&check;** |             |             | **&check;** |             |
| Create and manage compute resources | **&check;** | **&check;** | **&check;** | **&check;** | **&check;** |
| Create a compute instance           |             | **&check;** | **&check;** | **&check;** | **&check;** |

> [!WARNING]
> Moving your Azure Machine Learning workspace to a different subscription, or moving the owning subscription to a new tenant, is not supported. Doing so may cause errors.

## Create a workspace

There are multiple ways to create a workspace:  

* Use [Azure Machine Learning studio](quickstart-create-resources.md) to quickly create a workspace with default settings.
* Use the [Azure portal](how-to-manage-workspace.md?tabs=azure-portal#create-a-workspace) for a point-and-click interface with more options. 
* Use the [Azure Machine Learning SDK for Python](how-to-manage-workspace.md?tabs=python#create-a-workspace) to create a workspace on the fly from Python scripts or Jupyter notebooks.
