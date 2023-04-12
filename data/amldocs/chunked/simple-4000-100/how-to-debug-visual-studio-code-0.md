
# Interactive debugging with Visual Studio Code

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

Learn how to interactively debug Azure Machine Learning experiments, pipelines, and deployments using Visual Studio Code (VS Code) and [debugpy](https://github.com/microsoft/debugpy/).

## Run and debug experiments locally

Use the Azure Machine Learning extension to validate, run, and debug your machine learning experiments before submitting them to the cloud.

### Prerequisites

* Azure Machine Learning VS Code extension (preview). For more information, see [Set up Azure Machine Learning VS Code extension](how-to-setup-vs-code.md).

    > [!IMPORTANT]
    > The Azure Machine Learning VS Code extension uses the CLI (v2) by default. The instructions in this guide use 1.0 CLI. To switch to the 1.0 CLI, set the `azureML.CLI Compatibility Mode` setting in Visual Studio Code to `1.0`. For more information on modifying your settings in Visual Studio Code, see the [user and workspace settings documentation](https://code.visualstudio.com/docs/getstarted/settings).

* [Docker](https://www.docker.com/get-started)
  * Docker Desktop for Mac and Windows
  * Docker Engine for Linux.

    > [!NOTE]
    > On Windows, make sure to [configure Docker to use Linux containers](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers).

    > [!TIP]
    > For Windows, although not required, it's highly recommended to [use Docker with Windows Subsystem for Linux (WSL) 2](/windows/wsl/tutorials/wsl-containers#install-docker-desktop).

* [Python 3](https://www.python.org/downloads/)

### Debug experiment locally

> [!IMPORTANT]
> Before running your experiment locally make sure that:
>
> * Docker is running.
> * The `azureML.CLI Compatibility Mode` setting in Visual Studio Code is set to `1.0` as specified in the prerequisites

1. In VS Code, open the Azure Machine Learning extension view.
1. Expand the subscription node containing your workspace. If you don't already have one, you can [create an Azure Machine Learning workspace](how-to-manage-resources-vscode.md#create-a-workspace) using the extension.
1. Expand your workspace node.
1. Right-click the **Experiments** node and select **Create experiment**. When the prompt appears, provide a name for your experiment.
1. Expand the **Experiments** node, right-click the experiment you want to run and select **Run Experiment**.
1. From the list of options, select **Locally**.
1. **First time use on Windows only**. When prompted to allow File Share, select **Yes**. When you enable file share, it allows Docker to mount the directory containing your script to the container. Additionally, it also allows Docker to store the logs and outputs from your run in a temporary directory on your system.
1. Select **Yes** to debug your experiment. Otherwise, select **No**. Selecting no will run your experiment locally without attaching to the debugger.
1. Select **Create new Run Configuration** to create your run configuration. The run configuration defines the script you want to run, dependencies, and datasets used. Alternatively, if you already have one, select it from the dropdown.
    1. Choose your environment. You can choose from any of the [Azure Machine Learning curated](resource-curated-environments.md) or create your own.
    1. Provide the name of the script you want to run. The path is relative to the directory opened in VS Code.
    1. Choose whether you want to use an Azure Machine Learning dataset or not. You can create [Azure Machine Learning datasets](how-to-manage-resources-vscode.md#create-dataset) using the extension.
    1. Debugpy is required in order to attach the debugger to the container running your experiment. To add debugpy as a dependency,select **Add Debugpy**. Otherwise, select **Skip**. Not adding debugpy as a dependency runs your experiment without attaching to the debugger.
    1. A configuration file containing your run configuration settings opens in the editor. If you're satisfied with the settings, select **Submit experiment**. Alternatively, you open the command palette (**View > Command Palette**) from the menu bar and enter the `Azure ML: Submit experiment` command into the text box.
