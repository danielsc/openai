
# Troubleshooting online endpoints deployment and scoring

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]


Learn how to resolve common issues in the deployment and scoring of Azure Machine Learning online endpoints.

This document is structured in the way you should approach troubleshooting:

1. Use [local deployment](#deploy-locally) to test and debug your models locally before deploying in the cloud.
1. Use [container logs](#get-container-logs) to help debug issues.
1. Understand [common deployment errors](#common-deployment-errors) that might arise and how to fix them.

The section [HTTP status codes](#http-status-codes) explains how invocation and prediction errors map to HTTP status codes when scoring endpoints with REST requests.

## Prerequisites

* An **Azure subscription**. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
* The [Azure CLI](/cli/azure/install-azure-cli).
* For Azure Machine Learning CLI v2, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).
* For Azure Machine Learning Python SDK v2, see [Install the Azure Machine Learning SDK v2 for Python](/python/api/overview/azure/ai-ml-readme).

## Deploy locally

Local deployment is deploying a model to a local Docker environment. Local deployment is useful for testing and debugging before deployment to the cloud.

> [!TIP]
> You can also use [Azure Machine Learning inference HTTP server Python package](how-to-inference-server-http.md) to debug your scoring script locally. Debugging with the inference server helps you to debug the scoring script before deploying to local endpoints so that you can debug without being affected by the deployment container configurations.


Local deployment supports creation, update, and deletion of a local endpoint. It also allows you to invoke and get logs from the endpoint. 

## [Azure CLI](#tab/cli)

To use local deployment, add `--local` to the appropriate CLI command:

```azurecli
az ml online-deployment create --endpoint-name <endpoint-name> -n <deployment-name> -f <spec_file.yaml> --local
```

## [Python SDK](#tab/python)

To use local deployment, add  `local=True` parameter in the command:

```python
ml_client.begin_create_or_update(online_deployment, local=True)
```

* `ml_client` is the instance for `MLCLient` class, and `online_deployment` is the instance for either `ManagedOnlineDeployment` class or `KubernetesOnlineDeployment` class.

## [Studio](#tab/studio)

The studio doesn't support local endpoints/deployments. See the Azure CLI or Python tabs for steps to perform deployment locally.


As a part of local deployment the following steps take place:

- Docker either builds a new container image or pulls an existing image from the local Docker cache. An existing image is used if there's one that matches the environment part of the specification file.
- Docker starts a new container with mounted local artifacts such as model and code files.

For more, see [Deploy locally in Deploy and score a machine learning model](how-to-deploy-managed-online-endpoint-sdk-v2.md#create-local-endpoint-and-deployment).

> [!TIP]
> Use Visual Studio Code to test and debug your endpoints locally. For more information, see [debug online endpoints locally in Visual Studio Code](how-to-debug-managed-online-endpoints-visual-studio-code.md).

## Conda installation
 
Generally, issues with MLflow deployment stem from issues with the installation of the user environment specified in the `conda.yaml` file. 

To debug conda installation problems, try the following:

1. Check the logs for conda installation. If the container crashed or taking too long to start up, it is likely that conda environment update has failed to resolve correctly.

1. Install the mlflow conda file locally with the command `conda env create -n userenv -f <CONDA_ENV_FILENAME>`. 

1. If there are errors locally, try resolving the conda environment and creating a functional one before redeploying. 

