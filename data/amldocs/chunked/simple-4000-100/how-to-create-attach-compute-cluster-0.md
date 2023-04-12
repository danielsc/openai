
# Create an Azure Machine Learning compute cluster

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the Azure Machine Learning CLI or SDK version you are using:"]
> * [v1](v1/how-to-create-attach-compute-cluster.md)
> * [v2 (current version)](how-to-create-attach-compute-cluster.md)

Learn how to create and manage a [compute cluster](concept-compute-target.md#azure-machine-learning-compute-managed) in your Azure Machine Learning workspace.

You can use Azure Machine Learning compute cluster to distribute a training or batch inference process across a cluster of CPU or GPU compute nodes in the cloud. For more information on the VM sizes that include GPUs, see [GPU-optimized virtual machine sizes](../virtual-machines/sizes-gpu.md). 

In this article, learn how to:

* Create a compute cluster
* Lower your compute cluster cost with low priority VMs
* Set up a [managed identity](../active-directory/managed-identities-azure-resources/overview.md) for the cluster

## Prerequisites

* An Azure Machine Learning workspace. For more information, see [Create an Azure Machine Learning workspace](how-to-manage-workspace.md).

* The [Azure CLI extension for Machine Learning service (v2)](reference-azure-machine-learning-cli.md), [Azure Machine Learning Python SDK](/python/api/overview/azure/ai-ml-readme), or the [Azure Machine Learning Visual Studio Code extension](how-to-setup-vs-code.md).

* If using the Python SDK, [set up your development environment with a workspace](how-to-configure-environment.md).  Once your environment is set up, attach to the workspace in your Python script:

    [!INCLUDE [connect ws v2](../../includes/machine-learning-connect-ws-v2.md)]


## What is a compute cluster?

Azure Machine Learning compute cluster is a managed-compute infrastructure that allows you to easily create a single or multi-node compute. The compute cluster is a resource that can be shared with other users in your workspace. The compute scales up automatically when a job is submitted, and can be put in an Azure Virtual Network. Compute cluster supports **no public IP** deployment as well in virtual network. The compute executes in a containerized environment and packages your model dependencies in a [Docker container](https://www.docker.com/why-docker).

Compute clusters can run jobs securely in a [virtual network environment](how-to-secure-training-vnet.md), without requiring enterprises to open up SSH ports. The job executes in a containerized environment and packages your model dependencies in a Docker container. 

## Limitations

* Some of the scenarios listed in this document are marked as __preview__. Preview functionality is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

* Compute clusters can be created in a different region than your workspace. This functionality is in __preview__, and is only available for __compute clusters__, not compute instances. This preview isn't available if you're using a private endpoint-enabled workspace. 

    > [!WARNING]
    > When using a compute cluster in a different region than your workspace or datastores, you may see increased network latency and data transfer costs. The latency and costs can occur when creating the cluster, and when running jobs on it.

* We currently support only creation (and not updating) of clusters through [ARM templates](/azure/templates/microsoft.machinelearningservices/workspaces/computes). For updating compute, we recommend using the SDK, Azure CLI or UX for now.

* Azure Machine Learning Compute has default limits, such as the number of cores that can be allocated. For more information, see [Manage and request quotas for Azure resources](how-to-manage-quotas.md).
