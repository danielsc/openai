---
title: Deploy machine learning models to online endpoints
titleSuffix: Azure Machine Learning
description: Learn to deploy your machine learning model as an online endpoint in Azure.
services: machine-learning
ms.service: machine-learning
ms.subservice: mlops
author: dem108
ms.author: sehan
ms.reviewer: mopeakande
ms.date: 11/03/2022
ms.topic: how-to
ms.custom: how-to, devplatv2, ignite-fall-2021, cliv2, event-tier1-build-2022, sdkv2
---

# Deploy and score a machine learning model by using an online endpoint

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to use an online endpoint to deploy your model, so you don't have to create and manage the underlying infrastructure. You'll begin by deploying a model on your local machine to debug any errors, and then you'll deploy and test it in Azure.

You'll also learn how to view the logs and monitor the service-level agreement (SLA). You start with a model and end up with a scalable HTTPS/REST endpoint that you can use for online and real-time scoring. 

Online endpoints are endpoints that are used for online (real-time) inferencing. There are two types of online endpoints: **managed online endpoints** and **Kubernetes online endpoints**. For more information on endpoints, and differences between managed online endpoints and Kubernetes online endpoints, see [What are Azure Machine Learning endpoints?](concept-endpoints.md#managed-online-endpoints-vs-kubernetes-online-endpoints).

Managed online endpoints help to deploy your ML models in a turnkey manner. Managed online endpoints work with powerful CPU and GPU machines in Azure in a scalable, fully managed way. Managed online endpoints take care of serving, scaling, securing, and monitoring your models, freeing you from the overhead of setting up and managing the underlying infrastructure. 

The main example in this doc uses managed online endpoints for deployment. To use Kubernetes instead, see the notes in this document inline with the managed online endpoint discussion. 

> [!TIP]
> To create managed online endpoints in the Azure Machine Learning studio, see [Use managed online endpoints in the studio](how-to-use-managed-online-endpoint-studio.md).

## Prerequisites

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [basic prereqs cli](../../includes/machine-learning-cli-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.

> [!IMPORTANT]
> The examples in this document assume that you are using the Bash shell. For example, from a Linux system or [Windows Subsystem for Linux](/windows/wsl/about). 

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!INCLUDE [basic prereqs sdk](../../includes/machine-learning-sdk-v2-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* (Optional) To deploy locally, you must [install Docker Engine](https://docs.docker.com/engine/install/) on your local computer. We *highly recommend* this option, so it's easier to debug issues.

# [ARM template](#tab/arm)

> [!NOTE]
> While the Azure CLI and CLI extension for machine learning are used in these steps, they're not the main focus. they're used more as utilities, passing templates to Azure and checking the status of template deployments.

[!INCLUDE [basic prereqs cli](../../includes/machine-learning-cli-prereqs.md)]

* Azure role-based access controls (Azure RBAC) are used to grant access to operations in Azure Machine Learning. To perform the steps in this article, your user account must be assigned the __owner__ or __contributor__ role for the Azure Machine Learning workspace, or a custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

* If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, run this code:

   ```azurecli
   az account set --subscription <subscription ID>
   az configure --defaults workspace=<Azure Machine Learning workspace name> group=<resource group>
   ```

> [!IMPORTANT]
> The examples in this document assume that you are using the Bash shell. For example, from a Linux system or [Windows Subsystem for Linux](/windows/wsl/about). 

---

## Prepare your system

# [Azure CLI](#tab/azure-cli)

### Clone the sample repository

To follow along with this article, first clone the [samples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, run the following code to go to the samples directory:

```azurecli
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples
cd cli
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository, which reduces time to complete the operation.

### Set an endpoint name

To set your endpoint name, run the following command (replace `YOUR_ENDPOINT_NAME` with a unique name).

For Unix, run this command:

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="set_endpoint_name":::

> [!NOTE]
> Endpoint names must be unique within an Azure region. For example, in the Azure `westus2` region, there can be only one endpoint with the name `my-endpoint`. 

# [Python](#tab/python)

### Clone the sample repository

To run the training examples, first clone the [examples repository (azureml-examples)](https://github.com/azure/azureml-examples) and change into the `azureml-examples/sdk/python/endpoints/online/managed` directory:

```bash
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples/sdk/python/endpoints/online/managed
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository, which reduces time to complete the operation.

The information in this article is based on the [online-endpoints-simple-deployment.ipynb](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/online-endpoints-simple-deployment.ipynb) notebook. It contains the same content as this article, although the order of the codes is slightly different.

### Connect to Azure Machine Learning workspace

The [workspace](concept-workspace.md) is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. In this section, we'll connect to the workspace in which you'll perform deployment tasks.

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

    To connect to a workspace, we need identifier parameters - a subscription, resource group and workspace name. We'll use these details in the `MLClient` from `azure.ai.ml` to get a handle to the required Azure Machine Learning workspace. This example uses the [default Azure authentication](/python/api/azure-identity/azure.identity.defaultazurecredential).

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

# [ARM template](#tab/arm)

### Clone the sample repository

To follow along with this article, first clone the [samples repository (azureml-examples)](https://github.com/azure/azureml-examples). Then, run the following code to go to the samples directory:

```azurecli
git clone --depth 1 https://github.com/Azure/azureml-examples
cd azureml-examples
```

> [!TIP]
> Use `--depth 1` to clone only the latest commit to the repository, which reduces time to complete the operation.

### Set an endpoint name

To set your endpoint name, run the following command (replace `YOUR_ENDPOINT_NAME` with a unique name).

For Unix, run this command:

:::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" ID="set_endpoint_name":::

> [!NOTE]
> Endpoint names must be unique within an Azure region. For example, in the Azure `westus2` region, there can be only one endpoint with the name `my-endpoint`.

Also set the following environment variables, as they are used in the examples in this article. Replace the values with your Azure subscription ID, the Azure region where your workspace is located, the resource group that contains the workspace, and the workspace name:

```bash
export SUBSCRIPTION_ID="your Azure subscription ID"
export LOCATION="Azure region where your workspace is located"
export RESOURCE_GROUP="Azure resource group that contains your workspace"
export WORKSPACE="Azure Machine Learning workspace name"
```

A couple of the template examples require you to upload files to the Azure Blob store for your workspace. The following steps will query the workspace and store this information in environment variables used in the examples:

1. Get an access token:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="get_access_token":::

1. Set the REST API version:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="api_version":::

1. Get the storage information:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="get_storage_details":::

---

## Define the endpoint and deployment

# [Azure CLI](#tab/azure-cli)

The following snippet shows the *endpoints/online/managed/sample/endpoint.yml* file: 

:::code language="yaml" source="~/azureml-examples-main/cli/endpoints/online/managed/sample/endpoint.yml":::

> [!NOTE]
> For a full description of the YAML, see [Online endpoint YAML reference](reference-yaml-endpoint-online.md).

The reference for the endpoint YAML format is described in the following table. To learn how to specify these attributes, see the YAML example in [Prepare your system](#prepare-your-system) or the [online endpoint YAML reference](reference-yaml-endpoint-online.md). For information about limits related to managed endpoints, see [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).

| Key         | Description                                                                                                                                                                                                                                                 |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `$schema`   | (Optional) The YAML schema. To see all available options in the YAML file, you can view the schema in the preceding example in a browser.                                                                                                                   |
| `name`      | The name of the endpoint. It must be unique in the Azure region.<br>Naming rules are defined under [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).                                               |
| `auth_mode` | Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. `key` doesn't expire, but `aml_token` does expire. (Get the most recent token by using the `az ml online-endpoint get-credentials` command.) |

The example contains all the files needed to deploy a model on an online endpoint. To deploy a model, you must have:

- Model files (or the name and version of a model that's already registered in your workspace). In the example, we have a scikit-learn model that does regression.
- The code that's required to score the model. In this case, we have a *score.py* file.
- An environment in which your model runs. As you'll see, the environment might be a Docker image with Conda dependencies, or it might be a Dockerfile.
- Settings to specify the instance type and scaling capacity.

The following snippet shows the *endpoints/online/managed/sample/blue-deployment.yml* file, with all the required inputs: 

:::code language="yaml" source="~/azureml-examples-main/cli/endpoints/online/managed/sample/blue-deployment.yml":::

The table describes the attributes of a `deployment`:

| Key                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                              | The name of the deployment.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `model`                             | In this example, we specify the model properties inline: `path`. Model files are automatically uploaded and registered with an autogenerated name. For related best practices, see the tip in the next section.                                                                                                                                                                                                                                 |
| `code_configuration.code.path`      | The directory on the local development environment that contains all the Python source code for scoring the model. You can use nested directories and packages.                                                                                                                                                                                                                                                                                 |
| `code_configuration.scoring_script` | The Python file that's in the `code_configuration.code.path` scoring directory on the local development environment. This Python code must have an `init()` function and a `run()` function. The function `init()` will be called after the model is created or updated (you can use it to cache the model in memory, for example). The `run()` function is called at every invocation of the endpoint to do the actual scoring and prediction. |
| `environment`                       | Contains the details of the environment to host the model and code. In this example, we have inline definitions that include the`path`. We'll use `environment.docker.image` for the image. The `conda_file` dependencies will be installed on top of the image. For more information, see the tip in the next section.                                                                                                                         |
| `instance_type`                     | The VM SKU that will host your deployment instances. For more information, see [Managed online endpoints supported VM SKUs](reference-managed-online-endpoints-vm-sku-list.md).                                                                                                                                                                                                                                                                 |
| `instance_count`                    | The number of instances in the deployment. Base the value on the workload you expect. For high availability, we recommend that you set `instance_count` to at least `3`. We reserve an extra 20% for performing upgrades. For more information, see [managed online endpoint quotas](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).                                                                                  |

During deployment, the local files such as the Python source for the scoring model, are uploaded from the development environment.

For more information about the YAML schema, see the [online endpoint YAML reference](reference-yaml-endpoint-online.md).

> [!NOTE]
> To use Kubernetes instead of managed endpoints as a compute target:
> 1. Create and attach your Kubernetes cluster as a compute target to your Azure Machine Learning workspace by using [Azure Machine Learning studio](how-to-attach-kubernetes-to-workspace.md).
> 1. Use the [endpoint YAML](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-endpoint.yml) to target Kubernetes instead of the managed endpoint YAML. You'll need to edit the YAML to change the value of `target` to the name of your registered compute target. You can use this [deployment.yaml](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/kubernetes/kubernetes-blue-deployment.yml) that has additional properties applicable to Kubernetes deployment.
>
> All the commands that are used in this article (except the optional SLA monitoring and Azure Log Analytics integration) can be used either with managed endpoints or with Kubernetes endpoints.

# [Python](#tab/python)

In this article, we first define names of online endpoint and deployment for debug locally.

1. Define endpoint (with name for local endpoint):
      ```python
    # Creating a local endpoint
    import datetime

    local_endpoint_name = "local-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    # create an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=local_endpoint_name, description="this is a sample local endpoint"
    )
    ```

1. Define deployment (with name for local deployment)

    The example contains all the files needed to deploy a model on an online endpoint. To deploy a model, you must have:

    * Model files (or the name and version of a model that's already registered in your workspace). In the example, we have a scikit-learn model that does regression.
    * The code that's required to score the model. In this case, we have a score.py file.
    * An environment in which your model runs. As you'll see, the environment might be a Docker image with Conda dependencies, or it might be a Dockerfile.
    * Settings to specify the instance type and scaling capacity.

    **Key aspects of deployment**
    * `name` - Name of the deployment.
    * `endpoint_name` - Name of the endpoint to create the deployment under.
    * `model` - The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification.
    * `environment` - The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification.
    * `code_configuration` - the configuration for the source code and scoring script
        * `path`- Path to the source code directory for scoring the model
        * `scoring_script` - Relative path to the scoring file in the source code directory
    * `instance_type` - The VM size to use for the deployment. For the list of supported sizes, see [Managed online endpoints SKU list](reference-managed-online-endpoints-vm-sku-list.md).
    * `instance_count` - The number of instances to use for the deployment

    ```python
    model = Model(path="../model-1/model/sklearn_regression_model.pkl")
    env = Environment(
        conda_file="../model-1/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
    )

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=local_endpoint_name,
        model=model,
        environment=env,
        code_configuration=CodeConfiguration(
            code="../model-1/onlinescoring", scoring_script="score.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```

# [ARM template](#tab/arm)

The Azure Resource Manager templates [online-endpoint.json](https://github.com/Azure/azureml-examples/tree/main/arm-templates/online-endpoint.json) and [online-endpoint-deployment.json](https://github.com/Azure/azureml-examples/tree/main/arm-templates/online-endpoint-deployment.json) are used by the steps in this article.

---

### Register your model and environment separately

# [Azure CLI](#tab/azure-cli)

In this example, we specify the `path` (where to upload files from) inline. The CLI automatically uploads the files and registers the model and environment. As a best practice for production, you should register the model and environment and specify the registered name and version separately in the YAML. Use the form `model: azureml:my-model:1` or `environment: azureml:my-env:1`.

For registration, you can extract the YAML definitions of `model` and `environment` into separate YAML files and use the commands `az ml model create` and `az ml environment create`. To learn more about these commands, run `az ml model create -h` and `az ml environment create -h`.

# [Python](#tab/python)

In this example, we specify the `path` (where to upload files from) inline. The SDK automatically uploads the files and registers the model and environment. As a best practice for production, you should register the model and environment and specify the registered name and version separately in the codes. 

For more information on registering your model as an asset, see [Register your model as an asset in Machine Learning by using the SDK](how-to-manage-models.md#register-your-model-as-an-asset-in-machine-learning-by-using-the-sdk)

For more information on creating an environment, see 
[Manage Azure Machine Learning environments with the CLI & SDK (v2)](how-to-manage-environments-v2.md#create-an-environment)

# [ARM template](#tab/arm)

1. To register the model using a template, you must first upload the model file to an Azure Blob store. The following example uses the `az storage blob upload-batch` command to upload a file to the default storage for your workspace:

    :::code language="{language}" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="upload_model":::

1. After uploading the file, use the template to create a model registration. In the following example, the `modelUri` parameter contains the path to the model:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="create_model":::

1. Part of the environment is a conda file that specifies the model dependencies needed to host the model. The following example demonstrates how to read the contents of the conda file into environment variables:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="read_condafile":::

1. The following example demonstrates how to use the template to register the environment. The contents of the conda file from the previous step are passed to the template using the `condaFile` parameter:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="create_environment":::

---

### Use different CPU and GPU instance types

The preceding YAML uses a general-purpose type (`Standard_DS2_v2`) and a non-GPU Docker image (in the YAML, see the `image` attribute). For GPU compute, choose a GPU compute type SKU and a GPU Docker image.

For supported general-purpose and GPU instance types, see [Managed online endpoints supported VM SKUs](reference-managed-online-endpoints-vm-sku-list.md). For a list of Azure Machine Learning CPU and GPU base images, see [Azure Machine Learning base images](https://github.com/Azure/AzureML-Containers).

> [!NOTE]
> To use Kubernetes instead of managed endpoints as a compute target, see [Introduction to Kubernetes compute target](./how-to-attach-kubernetes-anywhere.md)

### Use more than one model

Currently, you can specify only one model per deployment in the YAML. If you've more than one model, when you register the model, copy all the models as files or subdirectories into a folder that you use for registration. In your scoring script, use the environment variable `AZUREML_MODEL_DIR` to get the path to the model root folder. The underlying directory structure is retained. For an example of deploying multiple models to one deployment, see [Deploy multiple models to one deployment](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/custom-container/minimal/multimodel).

## Understand the scoring script

> [!TIP]
> The format of the scoring script for online endpoints is the same format that's used in the preceding version of the CLI and in the Python SDK.

# [Azure CLI](#tab/azure-cli)
As noted earlier, the script specified in `code_configuration.scoring_script` must have an `init()` function and a `run()` function. 

# [Python](#tab/python)
As noted earlier, the script specified in `CodeConfiguration(scoring_script="score.py")` must have an `init()` function and a `run()` function. 

# [ARM template](#tab/arm)

As noted earlier, the script specified in `code_configuration.scoring_script` must have an `init()` function and a `run()` function. This example uses the [score.py file](https://github.com/Azure/azureml-examples/blob/main/cli/endpoints/online/model-1/onlinescoring/score.py). 

When using a template for deployment, you must first upload the scoring file(s) to an Azure Blob store, and then register it:

1. The following example uses the Azure CLI command `az storage blob upload-batch` to upload the scoring file(s):

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="upload_code":::

1. The following example demonstrates how to register the code using a template:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="create_code":::

---

This example uses the [score.py file](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/model-1/onlinescoring/score.py):
__score.py__
:::code language="python" source="~/azureml-examples-main/cli/endpoints/online/model-1/onlinescoring/score.py" :::

The `init()` function is called when the container is initialized or started. Initialization typically occurs shortly after the deployment is created or updated. Write logic here for global initialization operations like caching the model in memory (as we do in this example). The `run()` function is called for every invocation of the endpoint and should do the actual scoring and prediction. In the example, we extract the data from the JSON input, call the scikit-learn model's `predict()` method, and then return the result.

## Deploy and debug locally by using local endpoints

To save time debugging, we *highly recommend* that you test-run your endpoint locally. For more, see [Debug online endpoints locally in Visual Studio Code](how-to-debug-managed-online-endpoints-visual-studio-code.md).

> [!NOTE]
> * To deploy locally, [Docker Engine](https://docs.docker.com/engine/install/) must be installed.
> * Docker Engine must be running. Docker Engine typically starts when the computer starts. If it doesn't, you can [troubleshoot Docker Engine](https://docs.docker.com/config/daemon/#start-the-daemon-manually).

> [!IMPORTANT]
> The goal of a local endpoint deployment is to validate and debug your code and configuration before you deploy to Azure. Local deployment has the following limitations:
> - Local endpoints do *not* support traffic rules, authentication, or probe settings. 
> - Local endpoints support only one deployment per endpoint. 

> [!TIP]
> You can use [Azure Machine Learning inference HTTP server Python package](how-to-inference-server-http.md) to debug your scoring script locally **without Docker Engine**. Debugging with the inference server helps you to debug the scoring script before deploying to local endpoints so that you can debug without being affected by the deployment container configurations.

### Deploy the model locally

First create an endpoint. Optionally, for a local endpoint, you can skip this step and directly create the deployment (next step), which will, in turn, create the required metadata. Deploying models locally is useful for development and testing purposes.

# [Azure CLI](#tab/azure-cli)

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="create_endpoint":::

# [Python](#tab/python)

```python
ml_client.online_endpoints.begin_create_or_update(endpoint, local=True)
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.

---

Now, create a deployment named `blue` under the endpoint.

# [Azure CLI](#tab/azure-cli)

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="create_deployment":::

The `--local` flag directs the CLI to deploy the endpoint in the Docker environment.

# [Python](#tab/python)

```python
ml_client.online_deployments.begin_create_or_update(
    deployment=blue_deployment, local=True
)
```

The `local=True` flag directs the SDK to deploy the endpoint in the Docker environment.

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.

---

> [!TIP]
> Use Visual Studio Code to test and debug your endpoints locally. For more information, see [debug online endpoints locally in Visual Studio Code](how-to-debug-managed-online-endpoints-visual-studio-code.md).

### Verify the local deployment succeeded

Check the status to see whether the model was deployed without error:

# [Azure CLI](#tab/azure-cli)

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="get_status":::

The output should appear similar to the following JSON. The `provisioning_state` is `Succeeded`.

```json
{
  "auth_mode": "key",
  "location": "local",
  "name": "docs-endpoint",
  "properties": {},
  "provisioning_state": "Succeeded",
  "scoring_uri": "http://localhost:49158/score",
  "tags": {},
  "traffic": {}
}
```

# [Python](#tab/python)

```python
ml_client.online_endpoints.get(name=local_endpoint_name, local=True)
```

The method returns [`ManagedOnlineEndpoint` entity](/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint). The `provisioning_state` is `Succeeded`.

```python
ManagedOnlineEndpoint({'public_network_access': None, 'provisioning_state': 'Succeeded', 'scoring_uri': 'http://localhost:49158/score', 'swagger_uri': None, 'name': 'local-10061534497697', 'description': 'this is a sample local endpoint', 'tags': {}, 'properties': {}, 'id': None, 'Resource__source_path': None, 'base_path': '/path/to/your/working/directory', 'creation_context': None, 'serialize': <msrest.serialization.Serializer object at 0x7ffb781bccd0>, 'auth_mode': 'key', 'location': 'local', 'identity': None, 'traffic': {}, 'mirror_traffic': {}, 'kind': None})
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.

---

The following table contains the possible values for `provisioning_state`:

| State         | Description                                    |
| ------------- | ---------------------------------------------- |
| __Creating__  | The resource is being created.                 |
| __Updating__  | The resource is being updated.                 |
| __Deleting__  | The resource is being deleted.                 |
| __Succeeded__ | The create/update operation was successful.    |
| __Failed__    | The create/update/delete operation has failed. |

### Invoke the local endpoint to score data by using your model

# [Azure CLI](#tab/azure-cli)

Invoke the endpoint to score the model by using the convenience command `invoke` and passing query parameters that are stored in a JSON file:

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="test_endpoint":::

If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run `az ml online-endpoint show --local -n $ENDPOINT_NAME`. In the returned data, find the `scoring_uri` attribute. Sample curl based commands are available later in this doc.

# [Python](#tab/python)

Invoke the endpoint to score the model by using the convenience command invoke and passing query parameters that are stored in a JSON file

```python
ml_client.online_endpoints.invoke(
    endpoint_name=local_endpoint_name,
    request_file="../model-1/sample-request.json",
    local=True,
)
```

If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run the following code. In the returned data, find the `scoring_uri` attribute. Sample curl based commands are available later in this doc.

```python
endpoint = ml_client.online_endpoints.get(endpoint_name)
scoring_uri = endpoint.scoring_uri
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.

---

### Review the logs for output from the invoke operation

In the example *score.py* file, the `run()` method logs some output to the console. 

# [Azure CLI](#tab/azure-cli)

You can view this output by using the `get-logs` command:

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-local-endpoint.sh" ID="get_logs":::

# [Python](#tab/python)

You can view this output by using the `get_logs` method:

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=local_endpoint_name, local=True, lines=50
)
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.

---

##  Deploy your online endpoint to Azure

Next, deploy your online endpoint to Azure.

### Deploy to Azure

# [Azure CLI](#tab/azure-cli)

To create the endpoint in the cloud, run the following code:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="create_endpoint" :::

To create the deployment named `blue` under the endpoint, run the following code:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="create_deployment" :::

This deployment might take up to 15 minutes, depending on whether the underlying environment or image is being built for the first time. Subsequent deployments that use the same environment will finish processing more quickly.

> [!TIP]
> * If you prefer not to block your CLI console, you may add the flag `--no-wait` to the command. However, this will stop the interactive display of the deployment status.

> [!IMPORTANT]
> The `--all-traffic` flag in the above `az ml online-deployment create` allocates 100% of the traffic to the endpoint to the newly created deployment. Though this is helpful for development and testing purposes, for production, you might want to open traffic to the new deployment through an explicit command. For example,
> `az ml online-endpoint update -n $ENDPOINT_NAME --traffic "blue=100"` 

# [Python](#tab/python)

1. Configure online endpoint:

    > [!TIP]
    > * `endpoint_name`: The name of the endpoint. It must be unique in the Azure region. For more information on the naming rules, see [managed online endpoint limits](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints).
    > * `auth_mode` : Use `key` for key-based authentication. Use `aml_token` for Azure Machine Learning token-based authentication. A `key` doesn't expire, but `aml_token` does expire. For more information on authenticating, see [Authenticate to an online endpoint](how-to-authenticate-online-endpoint.md).
    > * Optionally, you can add description, tags to your endpoint.

    ```python
    # Creating a unique endpoint name with current datetime to avoid conflicts
    import datetime

    online_endpoint_name = "endpoint-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    # create an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="this is a sample online endpoint",
        auth_mode="key",
        tags={"foo": "bar"},
    )
    ```

1. Create the endpoint:

    Using the `MLClient` created earlier, we'll now create the Endpoint in the workspace. This command will start the endpoint creation and return a confirmation response while the endpoint creation continues.

    ```python
    ml_client.online_endpoints.begin_create_or_update(endpoint)
    ```

2. Configure online deployment:

    A deployment is a set of resources required for hosting the model that does the actual inferencing. We'll create a deployment for our endpoint using the `ManagedOnlineDeployment` class.

    ```python
    model = Model(path="../model-1/model/sklearn_regression_model.pkl")
    env = Environment(
        conda_file="../model-1/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
    )

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=online_endpoint_name,
        model=model,
        environment=env,
        code_configuration=CodeConfiguration(
            code="../model-1/onlinescoring", scoring_script="score.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```

3. Create the deployment:

    Using the `MLClient` created earlier, we'll now create the deployment in the workspace. This command will start the deployment creation and return a confirmation response while the deployment creation continues.

    ```python
    ml_client.online_deployments.begin_create_or_update(blue_deployment)
    ```

    > [!TIP]
    > * If you prefer not to block your Python console, you may add the flag `no_wait=True` to the parameters. However, this will stop the interactive display of the deployment status.

    ```python
    # blue deployment takes 100 traffic
    endpoint.traffic = {"blue": 100}
    ml_client.online_endpoints.begin_create_or_update(endpoint)
    ```

# [ARM template](#tab/arm)

1. The following example demonstrates using the template to create an online endpoint:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="create_endpoint":::

1. After the endpoint has been created, the following example demonstrates how to deploy the model to the endpoint:

    :::code language="azurecli" source="~/azureml-examples-main/deploy-arm-templates-az-cli.sh" id="create_deployment":::

---

> [!TIP]
> * Use [Troubleshooting online endpoints deployment](./how-to-troubleshoot-online-endpoints.md) to debug errors.

### Check the status of the endpoint

# [Azure CLI](#tab/azure-cli)

The `show` command contains information in `provisioning_status` for endpoint and deployment:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_status" :::

You can list all the endpoints in the workspace in a table format by using the `list` command:

```azurecli
az ml online-endpoint list --output table
```

# [Python](#tab/python)

Check the status to see whether the model was deployed without error:

```python
ml_client.online_endpoints.get(name=online_endpoint_name)
```

You can list all the endpoints in the workspace in a table format by using the `list` method:

```python
for endpoint in ml_client.online_endpoints.list():
    print(endpoint.name)
```

The method returns list (iterator) of `ManagedOnlineEndpoint` entities. You can get other information by specifying [parameters](/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint#parameters).

For example, output the list of endpoints like a table:

```python
print("Kind\tLocation\tName")
print("-------\t----------\t------------------------")
for endpoint in ml_client.online_endpoints.list():
    print(f"{endpoint.kind}\t{endpoint.location}\t{endpoint.name}")
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

The `show` command contains information in `provisioning_status` for endpoint and deployment:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_status" :::

You can list all the endpoints in the workspace in a table format by using the `list` command:

```azurecli
az ml online-endpoint list --output table
```

---

### Check the status of the online deployment

Check the logs to see whether the model was deployed without error:

# [Azure CLI](#tab/azure-cli)

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_logs" :::

By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `--container storage-initializer` flag.


# [Python](#tab/python)

You can view this output by using the `get_logs` method:

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=online_endpoint_name, lines=50
)
```

By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `container_type="storage-initializer"` option.

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=online_endpoint_name, lines=50, container_type="storage-initializer"
)
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_logs" :::

By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `--container storage-initializer` flag.

---

For more information on deployment logs, see [Get container logs](how-to-troubleshoot-online-endpoints.md#get-container-logs).

### Invoke the endpoint to score data by using your model

# [Azure CLI](#tab/azure-cli)

You can use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data: 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="test_endpoint" :::

The following example shows how to get the key used to authenticate to the endpoint:

> [!TIP]
> You can control which Azure Active Directory security principals can get the authentication key by assigning them to a custom role that allows `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/token/action` and `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/listkeys/action`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

:::code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="test_endpoint_using_curl_get_key":::

Next, use curl to score data.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="test_endpoint_using_curl" :::

Notice we use `show` and `get-credentials` commands to get the authentication credentials. Also notice that we're using the `--query` flag to filter attributes to only what we need. To learn more about `--query`, see [Query Azure CLI command output](/cli/azure/query-azure-cli).

To see the invocation logs, run `get-logs` again.

For information on authenticating using a token, see [Authenticate to online endpoints](how-to-authenticate-online-endpoint.md).


# [Python](#tab/python)

Using the `MLClient` created earlier, we'll get a handle to the endpoint. The endpoint can be invoked using the `invoke` command with the following parameters:

* `endpoint_name` - Name of the endpoint
* `request_file` - File with request data
* `deployment_name` - Name of the specific deployment to test in an endpoint

We'll send a sample request using a [json](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/model-1/sample-request.json) file.

```python
# test the blue deployment with some sample data
ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="blue",
    request_file="../model-1/sample-request.json",
)
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

You can use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data: 

```azurecli
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file cli/endpoints/online/model-1/sample-request.json
```

---

### (Optional) Update the deployment

# [Azure CLI](#tab/azure-cli)

If you want to update the code, model, or environment, update the YAML file, and then run the `az ml online-endpoint update` command. 

> [!NOTE]
> If you update instance count and along with other model settings (code, model, or environment) in a single `update` command: first the scaling operation will be performed, then the other updates will be applied. In production environment is a good practice to perform these operations separately.

To understand how `update` works:

1. Open the file *online/model-1/onlinescoring/score.py*.
1. Change the last line of the `init()` function: After `logging.info("Init complete")`, add `logging.info("Updated successfully")`. 
1. Save the file.
1. Run this command:

    ```azurecli
    az ml online-deployment update -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
    ```

    > [!Note]
    > Updating by using YAML is declarative. That is, changes in the YAML are reflected in the underlying Azure Resource Manager resources (endpoints and deployments). A declarative approach facilitates [GitOps](https://www.atlassian.com/git/tutorials/gitops): *All* changes to endpoints and deployments (even `instance_count`) go through the YAML.

    > [!TIP]
    > With the `update` command, you can use the [`--set` parameter in the Azure CLI](/cli/azure/use-cli-effectively#generic-update-parameters) to override attributes in your YAML *or* to set specific attributes without passing the YAML file. Using `--set` for single attributes is especially valuable in development and test scenarios. For example, to scale up the `instance_count` value for the first deployment, you could use the `--set instance_count=2` flag. However, because the YAML isn't updated, this technique doesn't facilitate [GitOps](https://www.atlassian.com/git/tutorials/gitops).

1. Because you modified the `init()` function (`init()` runs when the endpoint is created or updated), the message `Updated successfully` will be in the logs. Retrieve the logs by running:

    :::code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_logs" :::

The `update` command also works with local deployments. Use the same `az ml online-deployment update` command with the `--local` flag.

# [Python](#tab/python)

If you want to update the code, model, or environment, update the configuration, and then run the `MLClient`'s [`online_deployments.begin_create_or_update`](/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations#azure-ai-ml-operations-onlinedeploymentoperations-begin-create-or-update) module/method. 

> [!NOTE]
> If you update instance count and along with other model settings (code, model, or environment) in a single `begin_create_or_update` method: first the scaling operation will be performed, then the other updates will be applied. In production environment is a good practice to perform these operations separately.

To understand how `begin_create_or_update` works:

1. Open the file *online/model-1/onlinescoring/score.py*.
2. Change the last line of the `init()` function: After `logging.info("Init complete")`, add `logging.info("Updated successfully")`. 
3. Save the file.
4. Run the method:

    ```python
    ml_client.online_deployments.begin_create_or_update(blue_deployment)
    ```

5. Because you modified the `init()` function (`init()` runs when the endpoint is created or updated), the message `Updated successfully` will be in the logs. Retrieve the logs by running:

    ```python
    ml_client.online_deployments.get_logs(
        name="blue", endpoint_name=online_endpoint_name, lines=50
    )
    ```

The `begin_create_or_update` method also works with local deployments. Use the same method with the `local=True` flag.

# [ARM template](#tab/arm)

There currently is not an option to update the deployment using an ARM template.

---

> [!Note]
> The above is an example of inplace rolling update.
> * For managed online endpoint, the same deployment is updated with the new configuration, with 20% nodes at a time, i.e. if the deployment has 10 nodes, 2 nodes at a time will be updated. 
> * For Kubernetes online endpoint, the system will iterately create a new deployment instance with the new configuration and delete the old one.
> * For production usage, you might want to consider [blue-green deployment](how-to-safely-rollout-online-endpoints.md), which offers a safer alternative.

### (Optional) Configure autoscaling

Autoscale automatically runs the right amount of resources to handle the load on your application. Managed online endpoints support autoscaling through integration with the Azure monitor autoscale feature. To configure autoscaling, see [How to autoscale online endpoints](how-to-autoscale-endpoints.md).

### (Optional) Monitor SLA by using Azure Monitor

To view metrics and set alerts based on your SLA, complete the steps that are described in [Monitor online endpoints](how-to-monitor-online-endpoints.md).

### (Optional) Integrate with Log Analytics

The `get-logs` command for CLI or the `get_logs` method for SDK provides only the last few hundred lines of logs from an automatically selected instance. However, Log Analytics provides a way to durably store and analyze logs. For more information on using logging, see [Monitor online endpoints](how-to-monitor-online-endpoints.md#logs)

[!INCLUDE [Email Notification Include](../../includes/machine-learning-email-notifications.md)]

## Delete the endpoint and the deployment

If you aren't going use the deployment, you should delete it by running the following code (it deletes the endpoint and all the underlying deployments):

# [Azure CLI](#tab/azure-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="delete_endpoint" :::

# [Python](#tab/python)

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```

# [ARM template](#tab/arm)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="delete_endpoint" :::

---

## Next steps

Try safe rollout of your models as a next step:
- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)

To learn more, review these articles:

- [Deploy models with REST](how-to-deploy-with-rest.md)
- [Create and use online endpoints in the studio](how-to-use-managed-online-endpoint-studio.md)
- [How to autoscale managed online endpoints](how-to-autoscale-endpoints.md)
- [Use batch endpoints for batch scoring](batch-inference/how-to-use-batch-endpoint.md)
- [Access Azure resources from an online endpoint with a managed identity](how-to-access-resources-from-endpoints-managed-identities.md)
- [Troubleshoot online endpoints deployment](how-to-troubleshoot-online-endpoints.md)
- [Enable network isolation with managed online endpoints](how-to-secure-online-endpoint.md)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
