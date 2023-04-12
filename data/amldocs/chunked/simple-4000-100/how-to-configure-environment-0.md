
# Set up a Python development environment for Azure Machine Learning

Learn how to configure a Python development environment for Azure Machine Learning.

The following table shows each development environment covered in this article, along with pros and cons.

| Environment | Pros | Cons |
| --- | --- | --- |
| [Local environment](#local-computer-or-remote-vm-environment) | Full control of your development environment and dependencies. Run with any build tool, environment, or IDE of your choice. | Takes longer to get started. Necessary SDK packages must be installed, and an environment must also be installed if you don't already have one. |
| [The Data Science Virtual Machine (DSVM)](#data-science-virtual-machine) | Similar to the cloud-based compute instance (Python is pre-installed), but with additional popular data science and machine learning tools pre-installed. Easy to scale and combine with other custom tools and workflows. | A slower getting started experience compared to the cloud-based compute instance. |
| [Azure Machine Learning compute instance](#azure-machine-learning-compute-instance) | Easiest way to get started. The SDK is already installed in your workspace VM, and notebook tutorials are pre-cloned and ready to run. | Lack of control over your development environment and dependencies. Additional cost incurred for Linux VM (VM can be stopped when not in use to avoid charges). See [pricing details](https://azure.microsoft.com/pricing/details/virtual-machines/linux/). |
| [Azure Databricks](how-to-configure-databricks-automl-environment.md) | Ideal for running large-scale intensive machine learning workflows on the scalable Apache Spark platform. | Overkill for experimental machine learning, or smaller-scale experiments and workflows. Additional cost incurred for Azure Databricks. See [pricing details](https://azure.microsoft.com/pricing/details/databricks/). |

This article also provides additional usage tips for the following tools:

* Jupyter Notebooks: If you're already using Jupyter Notebooks, the SDK has some extras that you should install.

* Visual Studio Code: If you use Visual Studio Code, the [Azure Machine Learning extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai) includes language support for Python, and features to make working with the Azure Machine Learning much more convenient and productive.

## Prerequisites

* Azure Machine Learning workspace. If you don't have one, you can create an Azure Machine Learning workspace through the [Azure portal](how-to-manage-workspace.md), [Azure CLI](how-to-manage-workspace-cli.md#create-a-workspace), and [Azure Resource Manager templates](how-to-create-workspace-template.md).

### Local and DSVM only: Create a workspace configuration file

The workspace configuration file is a JSON file that tells the SDK how to communicate with your Azure Machine Learning workspace. The file is named *config.json*, and it has the following format:

```json
{
    "subscription_id": "<subscription-id>",
    "resource_group": "<resource-group>",
    "workspace_name": "<workspace-name>"
}
```

This JSON file must be in the directory structure that contains your Python scripts or Jupyter Notebooks. It can be in the same directory, a subdirectory named.azureml*, or in a parent directory.

To use this file from your code, use the [`MLClient.from_config`](/python/api/azure-ai-ml/azure.ai.ml.mlclient#azure-ai-ml-mlclient-from-config) method. This code loads the information from the file and connects to your workspace.

Create a workspace configuration file in one of the following methods:

* Azure Machine Learning studio

    **Download the file**: 
    1. Sign in to [Azure Machine Learning studio](https://ml.azure.com)
    1. In the upper right Azure Machine Learning studio toolbar, select your workspace name.
    1. Select the **Download config file** link.

    :::image type="content" source="media/how-to-configure-environment/configure.png" alt-text="Screenshot shows how to download your config file." lightbox="media/how-to-configure-environment/configure.png":::
