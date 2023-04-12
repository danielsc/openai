
# Access a compute instance terminal in your workspace

Access the terminal of a compute instance in your workspace to:

* Use files from Git and version files. These files are stored in your workspace file system, not restricted to a single compute instance.
* Install packages on the compute instance.
* Create extra kernels on the compute instance.

## Prerequisites

* An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/) before you begin.
* A Machine Learning workspace. See [Create workspace resources](quickstart-create-resources.md).

## Access a terminal

To access the terminal:

1. Open your workspace in [Azure Machine Learning studio](https://ml.azure.com).
1. On the left side, select **Notebooks**.
1. Select the **Open terminal** image.

    :::image type="content" source="media/how-to-use-terminal/open-terminal-window.png" alt-text="Open terminal window":::

1. When a compute instance is running, the terminal window for that compute instance appears.
1. When no compute instance is running, use the **Compute** section on the right to start or create a compute instance.
    :::image type="content" source="media/how-to-use-terminal/start-or-create-compute.png" alt-text="Start or create a compute instance":::

In addition to the steps above, you can also access the terminal from:

* RStudio or Posit Workbench (formerly RStudio Workbench) (See [Add custom applications such as RStudio or Posit Workbench)](how-to-create-manage-compute-instance.md?tabs=python#add-custom-applications-such-as-rstudio-or-posit-workbench-preview)): Select the **Terminal** tab on top left.
* Jupyter Lab:  Select the **Terminal** tile under the **Other** heading in the Launcher tab.
* Jupyter:  Select **New>Terminal** on top right in the Files tab.
* SSH to the machine, if you enabled SSH access when the compute instance was created.

## Copy and paste in the terminal

> * Windows: `Ctrl-Insert` to copy and use `Ctrl-Shift-v` or `Shift-Insert` to paste.
> * Mac OS: `Cmd-c` to copy and `Cmd-v` to paste.
> * FireFox/IE may not support clipboard permissions properly.

## <a name=git></a> Use files from Git and version files

Access all Git operations from the terminal. All Git files and folders will be stored in your workspace file system. This storage allows you to use these files from any compute instance in your workspace.

> [!NOTE]
> Add your files and folders anywhere under the **~/cloudfiles/code/Users** folder so they will be visible in all your Jupyter environments.

To integrate Git with your Azure Machine Learning workspace, see  [Git integration for Azure Machine Learning](concept-train-model-git-integration.md).

## Install packages

 Install packages from a terminal window. Install Python packages into the **Python 3.8 - AzureML** environment.  Install R packages into the **R** environment.

Or you can install packages directly in Jupyter Notebook, RStudio, or Posit Workbench (formerly RStudio Workbench):

* RStudio or Posit Workbench(see [Add custom applications such as RStudio or Posit Workbench](how-to-create-manage-compute-instance.md#add-custom-applications-such-as-rstudio-or-posit-workbench-preview)): Use the **Packages** tab on the bottom right, or the **Console** tab on the top left.  
* Python: Add install code and execute in a Jupyter Notebook cell.

> [!NOTE]
> For package management within a notebook, use **%pip** or **%conda** magic functions to automatically install packages into the **currently-running kernel**, rather than **!pip** or **!conda** which refers to all packages (including packages outside the currently-running kernel)

## Add new kernels

> [!WARNING]
> While customizing the compute instance, make sure you do not delete the **azureml_py36** or **azureml_py38** conda environments.  Also do not delete **Python 3.6 - AzureML** or **Python 3.8 - AzureML** kernels. These are needed for Jupyter/JupyterLab functionality.

To add a new Jupyter kernel to the compute instance:
