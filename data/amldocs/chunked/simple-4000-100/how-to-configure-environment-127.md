* [Deploy trained models](tutorial-train-deploy-image-classification-model-vscode.md).

## Azure Machine Learning compute instance

The Azure Machine Learning [compute instance](concept-compute-instance.md) is a secure, cloud-based Azure workstation that provides data scientists with a Jupyter Notebook server, JupyterLab, and a fully managed machine learning environment.

There's nothing to install or configure for a compute instance.  

Create one anytime from within your Azure Machine Learning workspace. Provide just a name and specify an Azure VM type. Try it now with this [Tutorial: Setup environment and workspace](quickstart-create-resources.md).

To learn more about compute instances, including how to install packages, see [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md).

> [!TIP]
> To prevent incurring charges for an unused compute instance, [enable idle shutdown](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview).

In addition to a Jupyter Notebook server and JupyterLab, you can use compute instances in the [integrated notebook feature inside of Azure Machine Learning studio](how-to-run-jupyter-notebooks.md).

You can also use the Azure Machine Learning Visual Studio Code extension to [connect to a remote compute instance using VS Code](how-to-set-up-vs-code-remote.md).

## Data Science Virtual Machine

The Data Science VM is a customized virtual machine (VM) image you can use as a development environment. It's designed for data science work that's pre-configured tools and software like:

  - Packages such as TensorFlow, PyTorch, Scikit-learn, XGBoost, and the Azure Machine Learning SDK
  - Popular data science tools such as Spark Standalone and Drill
  - Azure tools such as the Azure CLI, AzCopy, and Storage Explorer
  - Integrated development environments (IDEs) such as Visual Studio Code and PyCharm
  - Jupyter Notebook Server

For a more comprehensive list of the tools, see the [Data Science VM tools guide](data-science-virtual-machine/tools-included.md).

> [!IMPORTANT]
> If you plan to use the Data Science VM as a [compute target](concept-compute-target.md) for your training or inferencing jobs, only Ubuntu is supported.

To use the Data Science VM as a development environment:

1. Create a Data Science VM using one of the following methods:

    * Use the Azure portal to create an [Ubuntu](data-science-virtual-machine/dsvm-ubuntu-intro.md) or [Windows](data-science-virtual-machine/provision-vm.md) DSVM.
    * [Create a Data Science VM using ARM templates](data-science-virtual-machine/dsvm-tutorial-resource-manager.md).
    * Use the Azure CLI

        To create an Ubuntu Data Science VM, use the following command:

        ```azurecli-interactive
        # create a Ubuntu Data Science VM in your resource group
        # note you need to be at least a contributor to the resource group in order to execute this command successfully
        # If you need to create a new resource group use: "az group create --name YOUR-RESOURCE-GROUP-NAME --location YOUR-REGION (For example: westus2)"
        az vm create --resource-group YOUR-RESOURCE-GROUP-NAME --name YOUR-VM-NAME --image microsoft-dsvm:linux-data-science-vm-ubuntu:linuxdsvmubuntu:latest --admin-username YOUR-USERNAME --admin-password YOUR-PASSWORD --generate-ssh-keys --authentication-type password
        ```

        To create a Windows DSVM, use the following command:

        ```azurecli-interactive
        # create a Windows Server 2016 DSVM in your resource group
        # note you need to be at least a contributor to the resource group in order to execute this command successfully
        az vm create --resource-group YOUR-RESOURCE-GROUP-NAME --name YOUR-VM-NAME --image microsoft-dsvm:dsvm-windows:server-2016:latest --admin-username YOUR-USERNAME --admin-password YOUR-PASSWORD --authentication-type password
        ```

1. Create a conda environment for the Azure Machine Learning SDK:
