
# Work with models in Azure Machine Learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Azure Machine Learning allows you to work with different types of models. In this article, you learn about using Azure Machine Learning to work with different model types, such as custom, MLflow, and Triton. You also learn how to register a model from different locations, and how to use the Azure Machine Learning SDK, the user interface (UI), and the Azure Machine Learning CLI to manage your models.

> [!TIP]
> If you have model assets created that use the SDK/CLI v1, you can still use those with SDK/CLI v2. Full backward compatibility is provided. All models registered with the V1 SDK are assigned the type `custom`.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
* An Azure Machine Learning workspace.
* The Azure Machine Learning [SDK v2 for Python](https://aka.ms/sdk-v2-install).
* The Azure Machine Learning [CLI v2](how-to-configure-cli.md).

Additionally, you will need to:

# [Azure CLI](#tab/cli)

- Install the Azure CLI and the ml extension to the Azure CLI. For more information, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

# [Python SDK](#tab/python)

- Install the Azure Machine Learning SDK for Python
    
    ```bash
    pip install azure-ai-ml
    ```

## Supported paths

When you provide a model you want to register, you'll need to specify a `path` parameter that points to the data or job location. Below is a table that shows the different data locations supported in Azure Machine Learning and examples for the `path` parameter:


|Location  | Examples  |
|---------|---------|
|A path on your local computer     | `mlflow-model/model.pkl`         |
|A path on an AzureML Datastore   |   `azureml://datastores/<datastore-name>/paths/<path_on_datastore>`      |
|A path from an AzureML job   |   `azureml://jobs/<job-name>/outputs/<output-name>/paths/<path-to-model-relative-to-the-named-output-location>`      |
|A path from an MLflow job   |   `runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>`      |
|A path from a Model Asset in AzureML Workspace  | `azureml:<model-name>:<version>`|
|A path from a Model Asset in  AzureML Registry  | `azureml://registries/<registry-name>/models/<model-name>/versions/<version>`|

## Supported modes

When you run a job with model inputs/outputs, you can specify the *mode* - for example, whether you would like the model to be read-only mounted or downloaded to the compute target. The table below shows the possible modes for different type/mode/input/output combinations:

Type | Input/Output | `upload` | `download` | `ro_mount` | `rw_mount` | `direct` 
------ | ------ | :---: | :---: | :---: | :---: | :---: 
`custom` file  | Input  |   |  |   |  |    
`custom` folder    | Input |   | ✓ | ✓  | |✓  
`mlflow`    | Input |   | ✓ |  ✓ |   |   
`custom` file | Output  | ✓  |   |    | ✓  | ✓   
`custom` folder    | Output | ✓  |   |   | ✓ | ✓  
`mlflow`   | Output | ✓  |   |    | ✓  | ✓ 


### Follow along in Jupyter Notebooks

You can follow along this sample in a Jupyter Notebook. In the [azureml-examples](https://github.com/azure/azureml-examples) repository, open the notebook: [model.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/assets/model/model.ipynb).

## Create a model in the model registry

[Model registration](concept-model-management-and-deployment.md) allows you to store and version your models in the Azure cloud, in your workspace. The model registry helps you organize and keep track of your trained models.

The code snippets in this section cover how to:

* Register your model as an asset in Machine Learning by using the CLI.
* Register your model as an asset in Machine Learning by using the SDK.
* Register your model as an asset in Machine Learning by using the UI.
