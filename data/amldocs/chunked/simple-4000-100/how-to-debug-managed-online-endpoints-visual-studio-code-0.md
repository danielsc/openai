
# Debug online endpoints locally in Visual Studio Code

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Learn how to use the Visual Studio Code (VS Code) debugger to test and debug online endpoints locally before deploying them to Azure.

Azure Machine Learning local endpoints help you test and debug your scoring script, environment configuration, code configuration, and machine learning model locally.

## Online endpoint local debugging

Debugging endpoints locally before deploying them to the cloud can help you catch errors in your code and configuration earlier. You have different options for debugging endpoints locally with VS Code.

- [Azure Machine Learning inference HTTP server (Preview)](how-to-inference-server-http.md)
- Local endpoint

This guide focuses on local endpoints.

The following table provides an overview of scenarios to help you choose what works best for you.

| Scenario | Inference HTTP Server | Local endpoint |
|--|--|--|
| Update local Python environment, **without** Docker image rebuild | Yes | No |
| Update scoring script | Yes | Yes |
| Update deployment configurations (deployment, environment, code, model) | No | Yes |
| VS Code Debugger integration | Yes | Yes |

## Prerequisites

# [Azure CLI](#tab/cli)

This guide assumes you have the following items installed locally on your PC.

- [Docker](https://docs.docker.com/engine/install/)
- [VS Code](https://code.visualstudio.com/#alt-downloads)
- [Azure CLI](/cli/azure/install-azure-cli)
- [Azure CLI `ml` extension (v2)](how-to-configure-cli.md)

For more information, see the guide on [how to prepare your system to deploy online endpoints](how-to-deploy-online-endpoints.md#prepare-your-system).

The examples in this article are based on code samples contained in the [azureml-examples](https://github.com/azure/azureml-examples) repository. To run the commands locally without having to copy/paste YAML and other files, clone the repo and then change directories to the `cli` directory in the repo:

```azurecli
git clone https://github.com/Azure/azureml-examples --depth 1
cd azureml-examples
cd cli
```

If you haven't already set the defaults for the Azure CLI, save your default settings. To avoid passing in the values for your subscription, workspace, and resource group multiple times, use the following commands. Replace the following parameters with values for your specific configuration:

* Replace `<subscription>` with your Azure subscription ID.
* Replace `<workspace>` with your Azure Machine Learning workspace name.
* Replace `<resource-group>` with the Azure resource group that contains your workspace.
* Replace `<location>` with the Azure region that contains your workspace.

> [!TIP]
> You can see what your current defaults are by using the `az configure -l` command.

```azurecli
az account set --subscription <subscription>
az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
```

# [Python](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

This guide assumes you have the following items installed locally on your PC.

- [Docker](https://docs.docker.com/engine/install/)
- [VS Code](https://code.visualstudio.com/#alt-downloads)
- [Azure CLI](/cli/azure/install-azure-cli)
- [Azure CLI `ml` extension (v2)](how-to-configure-cli.md)
- [Azure ML Python SDK (v2)](https://aka.ms/sdk-v2-install)

For more information, see the guide on [how to prepare your system to deploy online endpoints](how-to-deploy-online-endpoints.md#prepare-your-system).

The examples in this article can be found in the [Debug online endpoints locally in Visual Studio Code](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/managed/debug-online-endpoints-locally-in-visual-studio-code.ipynb) notebook within the[azureml-examples](https://github.com/azure/azureml-examples) repository. To run the code locally, clone the repo and then change directories to the notebook's parent directory `sdk/endpoints/online/managed`. 
