
# Create and manage an Azure Machine Learning compute instance

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK or CLI version you are using:"]
> * [v1](v1/how-to-create-manage-compute-instance.md)
> * [v2 (current version)](how-to-create-manage-compute-instance.md)

Learn how to create and manage a [compute instance](concept-compute-instance.md) in your Azure Machine Learning workspace. 

Use a compute instance as your fully configured and managed development environment in the cloud. For development and testing, you can also use the instance as a [training compute target](concept-compute-target.md#training-compute-targets).   A compute instance can run multiple jobs in parallel and has a job queue. As a development environment, a compute instance can't be shared with other users in your workspace.

In this article, you learn how to:

* [Create](#create) a compute instance
* [Manage](#manage) (start, stop, restart, delete) a compute instance
* [Create  a schedule](#schedule-automatic-start-and-stop) to automatically start and stop the compute instance
* [Enable idle shutdown](#enable-idle-shutdown-preview)

You can also [use a setup script (preview)](how-to-customize-compute-instance.md) to create the compute instance with your own custom environment.

Compute instances can run jobs securely in a [virtual network environment](how-to-secure-training-vnet.md), without requiring enterprises to open up SSH ports. The job executes in a containerized environment and packages your model dependencies in a Docker container.

> [!NOTE]
> This article shows CLI v2 in the sections below. If you are still using CLI v1, see [Create an Azure Machine Learning compute cluster CLI v1)](v1/how-to-create-manage-compute-instance.md).

## Prerequisites

* An Azure Machine Learning workspace. For more information, see [Create an Azure Machine Learning workspace](how-to-manage-workspace.md).

* The [Azure CLI extension for Machine Learning service (v2)](https://aka.ms/sdk-v2-install), [Azure Machine Learning Python SDK (v2)](https://aka.ms/sdk-v2-install), or the [Azure Machine Learning Visual Studio Code extension](how-to-setup-vs-code.md).

* If using the Python SDK, [set up your development environment with a workspace](how-to-configure-environment.md).  Once your environment is set up, attach to the workspace in your Python script:

  [!INCLUDE [connect ws v2](../../includes/machine-learning-connect-ws-v2.md)]


## Create

> [!IMPORTANT]
> Items marked (preview) below are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

**Time estimate**: Approximately 5 minutes.

Creating a compute instance is a one time process for your workspace. You can reuse the compute as a development workstation or as a compute target for training. You can have multiple compute instances attached to your workspace. 

The dedicated cores per region per VM family quota and total regional quota, which applies to compute instance creation, is unified and shared with Azure Machine Learning training compute cluster quota. Stopping the compute instance doesn't release quota to ensure you'll be able to restart the compute instance. It isn't possible to change the virtual machine size of compute instance once it's created.

The fastest way to create a compute instance is to follow the [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md). 

Or use the following examples to create a compute instance with more options:

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
