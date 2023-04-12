
## Put the scoring file in its own directory

Create a directory called `src/` and place the scoring file you downloaded into it. This directory is uploaded to Azure and contains all the source code necessary to do inference. For an AutoML model, there's just the single scoring file. 

## Create the endpoint and deployment yaml file

To create an online endpoint from the command line, you'll need to create an *endpoint.yml* and a *deployment.yml* file. The following code, taken from the [Azure Machine Learning Examples repo](https://github.com/Azure/azureml-examples) shows the _endpoints/online/managed/sample/_, which captures all the required inputs:

__automl_endpoint.yml__

::: code language="yaml" source="~/azureml-examples-main/cli/endpoints/online/managed/sample/endpoint.yml" :::

__automl_deployment.yml__

::: code language="yaml" source="~/azureml-examples-main/cli/endpoints/online/managed/sample/blue-deployment.yml" :::

You'll need to modify this file to use the files you downloaded from the AutoML Models page.

1. Create a file `automl_endpoint.yml` and `automl_deployment.yml` and paste the contents of the above example.

1. Change the value of the `name` of the endpoint. The endpoint name needs to be unique within the Azure region. The name for an endpoint must start with an upper- or lowercase letter and only consist of '-'s and alphanumeric characters.

1. In the `automl_deployment` file, change the value of the keys at the following paths:

    | Path | Change to |
    | --- | --- |
    | `model:path` | The path to the `model.pkl` file you downloaded. |
    | `code_configuration:code:path` | The directory in which you placed the scoring file. | 
    | `code_configuration:scoring_script` | The name of the Python scoring file (`scoring_file_<VERSION>.py`). |
    | `environment:conda_file` | A file URL for the downloaded conda environment file (`conda_env_<VERSION>.yml`). |

    > [!NOTE]
    > For a full description of the YAML, see [Online endpoint YAML reference](reference-yaml-endpoint-online.md).

1. From the command line, run: 

    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

    ```azurecli
    az ml online-endpoint create -f automl_endpoint.yml
    az ml online-deployment create -f automl_deployment.yml
    ```
    
After you create a deployment, you can score it as described in [Invoke the endpoint to score data by using your model](how-to-deploy-online-endpoints.md#invoke-the-endpoint-to-score-data-by-using-your-model).


# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

## Configure the Python SDK

If you haven't installed Python SDK v2 yet, please install with this command:

```azurecli
pip install azure-ai-ml
```

For more information, see [Install the Azure Machine Learning SDK v2 for Python](/python/api/overview/azure/ai-ml-readme).

## Put the scoring file in its own directory

Create a directory called `src/` and place the scoring file you downloaded into it. This directory is uploaded to Azure and contains all the source code necessary to do inference. For an AutoML model, there's just the single scoring file. 

## Connect to Azure Machine Learning workspace

1. Import the required libraries:

    ```python
    # import required libraries
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import (
        ManagedOnlineEndpoint,
        ManagedOnlineDeployment,
        Model,
        Environment,
        CodeConfiguration,
    )
    from azure.identity import DefaultAzureCredential
    ```

1. Configure workspace details and get a handle to the workspace:

    ```python
    # enter details of your AzureML workspace
    subscription_id = "<SUBSCRIPTION_ID>"
    resource_group = "<RESOURCE_GROUP>"
    workspace = "<AZUREML_WORKSPACE_NAME>"
    ```

    ```python
    # get a handle to the workspace
    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
    ```

## Create the endpoint and deployment
