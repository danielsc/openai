    1. A configuration file containing your run configuration settings opens in the editor. If you're satisfied with the settings, select **Submit experiment**. Alternatively, you open the command palette (**View > Command Palette**) from the menu bar and enter the `Azure ML: Submit experiment` command into the text box.
1. Once your experiment is submitted, a Docker image containing your script and the configurations specified in your run configuration is created.

    When the Docker image build process begins, the contents of the `60_control_log.txt` file stream to the output console in VS Code.

    > [!NOTE]
    > The first time your Docker image is created can take several minutes.

1. Once your image is built, a prompt appears to start the debugger. Set your breakpoints in your script and select **Start debugger** when you're ready to start debugging. Doing so attaches the VS Code debugger to the container running your experiment. Alternatively, in the Azure Machine Learning extension, hover over the node for your current run and select the play icon to start the debugger.

    > [!IMPORTANT]
    > You cannot have multiple debug sessions for a single experiment. You can however debug two or more experiments using multiple VS Code instances.

At this point, you should be able to step-through and debug your code using VS Code.

If at any point you want to cancel your run, right-click your run node and select **Cancel run**.

Similar to remote experiment runs, you can expand your run node to inspect the logs and outputs.

> [!TIP]
> Docker images that use the same dependencies defined in your environment are reused between runs. However, if you run an experiment using a new or different environment, a new image is created. Since these images are saved to your local storage, it's recommended to remove old or unused Docker images. To remove images from your system, use the [Docker CLI](https://docs.docker.com/engine/reference/commandline/rmi/) or the [VS Code Docker extension](https://code.visualstudio.com/docs/containers/overview).

## Debug and troubleshoot machine learning pipelines

In some cases, you may need to interactively debug the Python code used in your ML pipeline. By using VS Code and debugpy, you can attach to the code as it runs in the training environment.

### Prerequisites

* An __Azure Machine Learning workspace__ that is configured to use an __Azure Virtual Network__.
* An __Azure Machine Learning pipeline__ that uses Python scripts as part of the pipeline steps. For example, a PythonScriptStep.
* An Azure Machine Learning Compute cluster, which is __in the virtual network__ and is __used by the pipeline for training__.
* A __development environment__ that is __in the virtual network__. The development environment might be one of the following:

  * An Azure Virtual Machine in the virtual network
  * A Compute instance of Notebook VM in the virtual network
  * A client machine that has private network connectivity to the virtual network, either by VPN or via ExpressRoute.

For more information on using an Azure Virtual Network with Azure Machine Learning, see [Virtual network isolation and privacy overview](how-to-network-security-overview.md).

> [!TIP]
> Although you can work with Azure Machine Learning resources that are not behind a virtual network, using a virtual network is recommended.

### How it works

Your ML pipeline steps run Python scripts. These scripts are modified to perform the following actions:

1. Log the IP address of the host that they're running on. You use the IP address to connect the debugger to the script.

2. Start the debugpy debug component, and wait for a debugger to connect.

3. From your development environment, you monitor the logs created by the training process to find the IP address where the script is running.

4. You tell VS Code the IP address to connect the debugger to by using a `launch.json` file.

5. You attach the debugger and interactively step through the script.
