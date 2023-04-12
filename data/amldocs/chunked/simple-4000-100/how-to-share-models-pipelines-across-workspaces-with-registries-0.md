
# Share models, components and environments across workspaces with registries (preview)

Azure Machine Learning registry (preview) enables you to collaborate across workspaces within your organization. Using registries, you can share models, components, and environments.
 
There are two scenarios where you'd want to use the same set of models, components and environments in multiple workspaces:

* __Cross-workspace MLOps__: You're training a model in a `dev` workspace and need to deploy it to `test` and `prod` workspaces. In this case you, want to have end-to-end lineage between endpoints to which the model is deployed in `test` or `prod` workspaces and the training job, metrics, code, data and environment that was used to train the model in the `dev` workspace.
* __Share and reuse models and pipelines across different teams__: Sharing and reuse improve collaboration and productivity. In this scenario, you may want to publish a trained model and the associated components and environments used to train it to a central catalog. From there, colleagues from other teams can search and reuse the assets you shared in their own experiments.

In this article, you'll learn how to:

* Create an environment and component in the registry.
* Use the component from registry to submit a model training job in a workspace.
* Register the trained model in the registry.
* Deploy the model from the registry to an online-endpoint in the workspace, then submit an inference request.
## Prerequisites

Before following the steps in this article, make sure you have the following prerequisites:

* An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

- An Azure Machine Learning registry (preview) to share models, components and environments. To create a registry, see [Learn how to create a registry](how-to-manage-registries.md).

- An Azure Machine Learning workspace. If you don't have one, use the steps in the [Quickstart: Create workspace resources](quickstart-create-resources.md) article to create one.

    > [!IMPORTANT]
    > The Azure region (location) where you create your workspace must be in the list of supported regions for Azure ML registry

- The Azure CLI and the `ml` extension __or__ the Azure Machine Learning Python SDK v2:

    # [Azure CLI](#tab/cli)

    To install the Azure CLI and extension, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).

    > [!IMPORTANT]
    > * The CLI examples in this article assume that you are using the Bash (or compatible) shell. For example, from a Linux system or [Windows Subsystem for Linux](/windows/wsl/about).
    > * The examples also assume that you have configured defaults for the Azure CLI so that you don't have to specify the parameters for your subscription, workspace, resource group, or location. To set default settings, use the following commands. Replace the following parameters with the values for your configuration:
    >
    >     * Replace `<subscription>` with your Azure subscription ID.
    >     * Replace `<workspace>` with your Azure Machine Learning workspace name.
    >     * Replace `<resource-group>` with the Azure resource group that contains your workspace.
    >     * Replace `<location>` with the Azure region that contains your workspace.
    >
    >     ```azurecli
    >     az account set --subscription <subscription>
    >     az configure --defaults workspace=<workspace> group=<resource-group> location=<location>
    >     ```
    >     You can see what your current defaults are by using the `az configure -l` command.

    # [Python SDK](#tab/python)

    To install the Python SDK v2, use the following command:

    ```bash
    pip install --pre azure-ai-ml
    ```


### Clone examples repository

The code examples in this article are based on the `nyc_taxi_data_regression` sample in the [examples repository](https://github.com/Azure/azureml-examples). To use these files on your development environment, use the following commands to clone the repository and change directories to the example:
