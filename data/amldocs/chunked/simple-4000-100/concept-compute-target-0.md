
# What are compute targets in Azure Machine Learning?

A *compute target* is a designated compute resource or environment where you run your training script or host your service deployment. This location might be your local machine or a cloud-based compute resource. Using compute targets makes it easy for you to later change your compute environment without having to change your code.

In a typical model development lifecycle, you might:

1. Start by developing and experimenting on a small amount of data. At this stage, use your local environment, such as a local computer or cloud-based virtual machine (VM), as your compute target.
1. Scale up to larger data, or do [distributed training](how-to-train-distributed-gpu.md) by using one of these [training compute targets](#training-compute-targets).
1. After your model is ready, deploy it to a web hosting environment with one of these [deployment compute targets](#compute-targets-for-inference).

The compute resources you use for your compute targets are attached to a [workspace](concept-workspace.md). Compute resources other than the local machine are shared by users of the workspace.

## Training compute targets

Azure Machine Learning has varying support across different compute targets. A typical model development lifecycle starts with development or experimentation on a small amount of data. At this stage, use a local environment like your local computer or a cloud-based VM. As you scale up your training on larger datasets or perform [distributed training](how-to-train-distributed-gpu.md), use Azure Machine Learning compute to create a single- or multi-node cluster that autoscales each time you submit a job. You can also attach your own compute resource, although support for different scenarios might vary.

[!INCLUDE [aml-compute-target-train](../../includes/aml-compute-target-train.md)]


## Compute targets for inference

When performing inference, Azure Machine Learning creates a Docker container that hosts the model and associated resources needed to use it. This container is then used in a compute target.

[!INCLUDE [aml-deploy-target](../../includes/aml-compute-target-deploy.md)]

Learn [where and how to deploy your model to a compute target](how-to-deploy-online-endpoints.md).

## Azure Machine Learning compute (managed)

A managed compute resource is created and managed by Azure Machine Learning. This compute is optimized for machine learning workloads. Azure Machine Learning compute clusters and [compute instances](concept-compute-instance.md) are the only managed computes.

You can create Azure Machine Learning compute instances or compute clusters from:

* [Azure Machine Learning studio](how-to-create-attach-compute-studio.md).
* The Python SDK and the Azure CLI:
    * [Compute instance](how-to-create-manage-compute-instance.md).
    * [Compute cluster](how-to-create-attach-compute-cluster.md).
* An Azure Resource Manager template. For an example template, see [Create an Azure Machine Learning compute cluster](https://github.com/Azure/azure-quickstart-templates/tree/master/quickstarts/microsoft.machinelearningservices/machine-learning-compute-create-amlcompute).

When created, these compute resources are automatically part of your workspace, unlike other kinds of compute targets.


|Capability  |Compute cluster  |Compute instance  |
|---------|---------|---------|
|Single- or multi-node cluster     |    **&check;**       |    Single node cluster     |
|Autoscales each time you submit a job     |     **&check;**      |         |
|Automatic cluster management and job scheduling     |   **&check;**        |     **&check;**      |
|Support for both CPU and GPU resources     |  **&check;**         |    **&check;**       |


> [!NOTE]
> To avoid charges when the compute is idle:
> * For compute *cluster* make sure the minimum number of nodes is set to 0.
> * For a compute *instance*, [enable idle shutdown](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview).
