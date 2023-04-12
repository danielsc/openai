> While customizing the compute instance, make sure you do not delete the **azureml_py36** or **azureml_py38** conda environments.  Also do not delete **Python 3.6 - AzureML** or **Python 3.8 - AzureML** kernels. These are needed for Jupyter/JupyterLab functionality.

To add a new Jupyter kernel to the compute instance:

1. Use the terminal window to create a new environment.  For example, the code below creates `newenv`:

    ```shell
    conda create --name newenv
    ```

1. Activate the environment.  For example, after creating `newenv`:

    ```shell
    conda activate newenv
    ```

1. Install pip and ipykernel package to the new environment and create a kernel for that conda env

    ```shell
    conda install pip
    conda install ipykernel
    python -m ipykernel install --user --name newenv --display-name "Python (newenv)"
    ```

Any of the [available Jupyter Kernels](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels) can be installed.

### Remove added kernels

> [!WARNING]
> While customizing the compute instance, make sure you do not delete the **azureml_py36** or **azureml_py38** conda environments.  Also do not delete **Python 3.6 - AzureML** or **Python 3.8 - AzureML** kernels. These are needed for Jupyter/JupyterLab functionality.

To remove an added Jupyter kernel from the compute instance, you must remove the kernelspec, and (optionally) the conda environment. You can also choose to keep the conda environment. You must remove the kernelspec, or your kernel will still be selectable and cause unexpected behavior.

To remove the kernelspec:

1. Use the terminal window to list and find the kernelspec:

    ```shell
    jupyter kernelspec list
    ```

1. Remove the kernelspec, replacing UNWANTED_KERNEL with the kernel you'd like to remove:

    ```shell
    jupyter kernelspec uninstall UNWANTED_KERNEL
    ```

To also remove the conda environment:

1. Use the terminal window to list and find the conda environment:

    ```shell
    conda env list
    ```

1. Remove the conda environment, replacing ENV_NAME with the conda environment you'd like to remove:

    ```shell
    conda env remove -n ENV_NAME
    ```

Upon refresh, the kernel list in your notebooks view should reflect the changes you have made.

## Manage terminal sessions

Terminal sessions can stay active if terminal tabs are not properly closed. Too many active terminal sessions can impact the performance of your compute instance.

Select **Manage active sessions** in the terminal toolbar to see a list of all active terminal sessions and shut down the sessions you no longer need.

Learn more about how to manage sessions running on your compute at [Managing notebook and terminal sessions](how-to-manage-compute-sessions.md).

> [!WARNING]
> Make sure you close any sessions you no longer need to preserve your compute instance's resources and optimize your performance.
