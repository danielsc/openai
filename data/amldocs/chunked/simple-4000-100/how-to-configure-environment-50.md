    :::image type="content" source="media/how-to-configure-environment/configure.png" alt-text="Screenshot shows how to download your config file." lightbox="media/how-to-configure-environment/configure.png":::

* Azure Machine Learning Python SDK

    Create a script to connect to your Azure Machine Learning workspace. Make sure to replace `subscription_id`,`resource_group`, and `workspace_name` with your own.

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    ```python
        #import required libraries
        from azure.ai.ml import MLClient
        from azure.identity import DefaultAzureCredential

        #Enter details of your AzureML workspace
        subscription_id = '<SUBSCRIPTION_ID>'
        resource_group = '<RESOURCE_GROUP>'
        workspace = '<AZUREML_WORKSPACE_NAME>'
      
        #connect to the workspace
        ml_client = MLClient(DefaultAzureCredential(), subscription_id, resource_group, workspace)
    ```

## Local computer or remote VM environment

You can set up an environment on a local computer or remote virtual machine, such as an Azure Machine Learning compute instance or Data Science VM. 

To configure a local development environment or remote VM:

1. Create a Python virtual environment (virtualenv, conda).

    > [!NOTE]
    > Although not required, it's recommended you use [Anaconda](https://www.anaconda.com/download/) or [Miniconda](https://www.anaconda.com/download/) to manage Python virtual environments and install packages.

    > [!IMPORTANT]
    > If you're on Linux or macOS and use a shell other than bash (for example, zsh) you might receive errors when you run some commands. To work around this problem, use the `bash` command to start a new bash shell and run the commands there.

1. Activate your newly created Python virtual environment.
1. Install the [Azure Machine Learning Python SDK](/python/api/overview/azure/ai-ml-readme).
1. To configure your local environment to use your Azure Machine Learning workspace, [create a workspace configuration file](#local-and-dsvm-only-create-a-workspace-configuration-file) or use an existing one.

Now that you have your local environment set up, you're ready to start working with Azure Machine Learning. See the [Tutorial: Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md) to get started.

### Jupyter Notebooks

When running a local Jupyter Notebook server, it's recommended that you create an IPython kernel for your Python virtual environment. This helps ensure the expected kernel and package import behavior.

1. Enable environment-specific IPython kernels

    ```bash
    conda install notebook ipykernel
    ```

1. Create a kernel for your Python virtual environment. Make sure to replace `<myenv>` with the name of your Python virtual environment.

    ```bash
    ipython kernel install --user --name <myenv> --display-name "Python (myenv)"
    ```

1. Launch the Jupyter Notebook server

    > [!TIP]
    For example notebooks, see the [AzureML-Examples](https://github.com/Azure/azureml-examples) repository. SDK examples are located under [/sdk/python](https://github.com/Azure/azureml-examples/tree/main/sdk/python). For example, the [Configuration notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/configuration.ipynb) example.

### Visual Studio Code

To use Visual Studio Code for development:

1. Install [Visual Studio Code](https://code.visualstudio.com/Download).
1. Install the [Azure Machine Learning Visual Studio Code extension](how-to-setup-vs-code.md) (preview).

Once you have the Visual Studio Code extension installed, use it to:

* [Manage your Azure Machine Learning resources](how-to-manage-resources-vscode.md)
* [Connect to an Azure Machine Learning compute instance](how-to-set-up-vs-code-remote.md)
* [Run and debug experiments](how-to-debug-visual-studio-code.md)
* [Deploy trained models](tutorial-train-deploy-image-classification-model-vscode.md).

## Azure Machine Learning compute instance
