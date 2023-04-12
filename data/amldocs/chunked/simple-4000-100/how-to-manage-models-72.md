* Register your model as an asset in Machine Learning by using the SDK.
* Register your model as an asset in Machine Learning by using the UI.

These snippets use `custom` and `mlflow`.

- `custom` is a type that refers to a model file or folder trained with a custom standard not currently supported by Azure ML.
- `mlflow` is a type that refers to a model trained with [mlflow](how-to-use-mlflow-cli-runs.md). MLflow trained models are in a folder that contains the *MLmodel* file, the *model* file, the *conda dependencies* file, and the *requirements.txt* file.

### Connect to your workspace

First, let's connect to Azure Machine Learning workspace where we are going to work on.

# [Azure CLI](#tab/cli)

```azurecli
az account set --subscription <subscription>
az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
```

# [Python SDK](#tab/python)

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace in which you'll perform deployment tasks.

1. Import the required libraries:

    ```python
    from azure.ai.ml import MLClient, Input
    from azure.ai.ml.entities import Model
    from azure.ai.ml.constants import AssetTypes
    from azure.identity import DefaultAzureCredential
    ```

2. Configure workspace details and get a handle to the workspace:

    ```python
    subscription_id = "<SUBSCRIPTION_ID>"
    resource_group = "<RESOURCE_GROUP>"
    workspace = "<AML_WORKSPACE_NAME>"
    
    ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
    ```


### Register your model as an asset in Machine Learning by using the CLI

Use the following tabs to select where your model is located.

# [Local model](#tab/use-local)

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/model.schema.json
name: local-file-example
path: mlflow-model/model.pkl
description: Model created from local file.

```

```bash
az ml model create -f <file-name>.yml
```

For a complete example, see the [model YAML](https://github.com/Azure/azureml-examples/tree/main/cli/assets/model).


# [Datastore](#tab/use-datastore)

You can create a model from a cloud path by using any one of the following supported URI formats.

```cli
az ml model create --name my-model --version 1 --path azureml://datastores/myblobstore/paths/models/cifar10/cifar.pt
```

The examples use the shorthand `azureml` scheme for pointing to a path on the `datastore` by using the syntax `azureml://datastores/<datastore-name>/paths/<path_on_datastore>`.

For a complete example, see the [CLI reference](/cli/azure/ml/model).

# [Job output](#tab/use-job-output)

You have two options here. You can use the MLflow run URI format, or you can use the `azureml job` URI format.

### MLflow

This option is optimized for MLflow users, who are likely already familiar with the MLflow run URI format. This option helps you create a model from artifacts in the default artifact location (where all MLflow-logged models and artifacts are located). This establishes a lineage between a registered model and the run the model came from.

Format:
`runs:/<run-id>/<path-to-model-relative-to-the-root-of-the-artifact-location>`

Example:
`runs:/<run-id>/model/`

```cli
az ml model create --name my-model --version 1 --path runs:/<run-id>/model/ --type mlflow_model
```

### azureml job

This option is an `azureml job` reference URI format, which helps you register a model from artifacts in any of the job's outputs. This format is aligned with the existing `azureml` datastore reference URI format, and also supports referencing artifacts from named outputs of the job (not just the default artifact location). You can establish a lineage between a registered model and the job it was trained from, if you didn't directly register your model within the training script by using MLflow.
