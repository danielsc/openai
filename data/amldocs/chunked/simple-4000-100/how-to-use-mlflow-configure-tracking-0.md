

# Configure MLflow for Azure Machine Learning

Azure Machine Learning workspaces are MLflow-compatible, which means they can act as an MLflow server without any extra configuration. Each workspace has an MLflow tracking URI that can be used by MLflow to connect to the workspace. Azure Machine Learning workspaces **are already configured to work with MLflow** so no extra configuration is required.

However, if you are working outside of Azure Machine Learning (like your local machine, Azure Synapse Analytics, or Azure Databricks) you need to configure MLflow to point to the workspace. In this article, you'll learn how you can configure MLflow to connect to an Azure Machine Learning for tracking, registries, and deployment. 

> [!IMPORTANT]
> When running on Azure Compute (Azure ML Notebooks, Jupyter notebooks hosted on Azure ML Compute Instances, or jobs running on Azure ML compute clusters) you don't have to configure the tracking URI. **It's automatically configured for you**.

## Prerequisites

You will need the following prerequisites to follow this tutorial:

[!INCLUDE [mlflow-prereqs](../../includes/machine-learning-mlflow-prereqs.md)]


## Configure MLflow tracking URI

To connect MLflow to an Azure Machine Learning workspace you will need the tracking URI for the workspace. Each workspace has its own tracking URI and it has the protocol `azureml://`.

[!INCLUDE [cli v2](../../includes/machine-learning-mlflow-configure-tracking.md)]

## Configure authentication

Once the tracking is set, you'll also need to configure how the authentication needs to happen to the associated workspace. By default, the Azure Machine Learning plugin for MLflow will perform interactive authentication by opening the default browser to prompt for credentials.

The Azure Machine Learning plugin for MLflow supports several authentication mechanisms through the package `azure-identity`, which is installed as a dependency for the plugin `azureml-mlflow`. The following authentication methods are tried one by one until one of them succeeds:

1. __Environment__: it will read account information specified via environment variables and use it to authenticate.
1. __Managed Identity__: If the application is deployed to an Azure host with Managed Identity enabled, it will authenticate with it.  
1. __Azure CLI__: if a user has signed in via the Azure CLI `az login` command, it will authenticate as that user.
1. __Azure PowerShell__: if a user has signed in via Azure PowerShell's `Connect-AzAccount` command, it will authenticate as that user.
1. __Interactive browser__: it will interactively authenticate a user via the default browser.

[!INCLUDE [cli v2](../../includes/machine-learning-mlflow-configure-auth.md)]

If you'd rather use a certificate instead of a secret, you can configure the environment variables `AZURE_CLIENT_CERTIFICATE_PATH` to the path to a `PEM` or `PKCS12` certificate file (including private key) and 
`AZURE_CLIENT_CERTIFICATE_PASSWORD` with the password of the certificate file, if any.

### Troubleshooting authentication

MLflow will try to authenticate to Azure Machine Learning on the first operation interacting with the service, like `mlflow.set_experiment()` or `mlflow.start_run()`. If you find issues or unexpected authentication prompts during the process, you can increase the logging level to get more details about the error:

```python
import logging

logging.getLogger("azure").setLevel(logging.DEBUG)
```

## Set experiment name (optional)

All MLflow runs are logged to the active experiment. By default, runs are logged to an experiment named `Default` that is automatically created for you. You can configure the experiment where tracking is happening.

> [!TIP]
> When submitting jobs using Azure ML CLI v2, you can set the experiment name using the property `experiment_name` in the YAML definition of the job. You don't have to configure it on your training script. See [YAML: display name, experiment name, description, and tags](reference-yaml-job-command.md#yaml-display-name-experiment-name-description-and-tags) for details.
