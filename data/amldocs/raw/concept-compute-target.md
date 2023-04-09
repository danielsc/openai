---
title: What are compute targets
titleSuffix: Azure Machine Learning
description: Learn how to designate a compute resource or environment to train or deploy your model with Azure Machine Learning.
services: machine-learning
ms.service: machine-learning
ms.subservice: core
ms.topic: conceptual
ms.author: vijetaj
author: vijetajo
ms.reviewer: sgilley
ms.date: 10/19/2022
ms.custom: ignite-fall-2021, event-tier1-build-2022, cliv2
#Customer intent: As a data scientist, I want to understand what a compute target is and why I need it.
---

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

### Supported VM series and sizes

> [!NOTE] 
> H-series virtual machine series will be retired on August 31, 2022. Create compute instance and compute clusters with alternate VM sizes. Existing compute instances and clusters with H-series virtual machines will not work after August 31, 2022.

When you select a node size for a managed compute resource in Azure Machine Learning, you can choose from among select VM sizes available in Azure. Azure offers a range of sizes for Linux and Windows for different workloads. To learn more, see [VM types and sizes](../virtual-machines/sizes.md).

There are a few exceptions and limitations to choosing a VM size:

* Some VM series aren't supported in Azure Machine Learning.
* There are some VM series, such as GPUs and other special SKUs, which may not initially appear in your list of available VMs.  But you can still use them, once you request a quota change. For more information about requesting quotas, see [Request quota increases](how-to-manage-quotas.md#request-quota-increases).
See the following table to learn more about supported series.

| **Supported VM series** | **Category** | **Supported by** |
|------------|------------|------------|------------|
| [DDSv4](../virtual-machines/ddv4-ddsv4-series.md#ddsv4-series) | General purpose | Compute clusters and instance |
| [Dv2](../virtual-machines/dv2-dsv2-series.md#dv2-series) | General purpose | Compute clusters and instance |
| [Dv3](../virtual-machines/dv3-dsv3-series.md#dv3-series) | General purpose | Compute clusters and instance |
| [DSv2](../virtual-machines/dv2-dsv2-series.md#dsv2-series) | General purpose | Compute clusters and instance |
| [DSv3](../virtual-machines/dv3-dsv3-series.md#dsv3-series) | General purpose | Compute clusters and instance |
| [EAv4](../virtual-machines/eav4-easv4-series.md) | Memory optimized | Compute clusters and instance |
| [Ev3](../virtual-machines/ev3-esv3-series.md) | Memory optimized | Compute clusters and instance |
| [ESv3](../virtual-machines/ev3-esv3-series.md) | Memory optimized | Compute clusters and instance |
| [FSv2](../virtual-machines/fsv2-series.md) | Compute optimized | Compute clusters and instance |
| [FX](../virtual-machines/fx-series.md) | Compute optimized | Compute clusters |
| [H](../virtual-machines/h-series.md) | High performance compute | Compute clusters and instance |
| [HB](../virtual-machines/hb-series.md) | High performance compute | Compute clusters and instance |
| [HBv2](../virtual-machines/hbv2-series.md) | High performance compute | Compute clusters and instance |
| [HBv3](../virtual-machines/hbv3-series.md) |  High performance compute | Compute clusters and instance |
| [HC](../virtual-machines/hc-series.md) |  High performance compute | Compute clusters and instance |
| [LSv2](../virtual-machines/lsv2-series.md) |  Storage optimized | Compute clusters and instance |
| [M](../virtual-machines/m-series.md) | Memory optimized | Compute clusters and instance |
| [NC](../virtual-machines/nc-series.md) |  GPU | Compute clusters and instance |
| [NC Promo](../virtual-machines/nc-series.md) | GPU | Compute clusters and instance |
| [NCv2](../virtual-machines/ncv2-series.md) | GPU | Compute clusters and instance |
| [NCv3](../virtual-machines/ncv3-series.md) | GPU | Compute clusters and instance |
| [ND](../virtual-machines/nd-series.md) | GPU | Compute clusters and instance |
| [NDv2](../virtual-machines/ndv2-series.md) | GPU | Compute clusters and instance |
| [NV](../virtual-machines/nv-series.md) | GPU | Compute clusters and instance |
| [NVv3](../virtual-machines/nvv3-series.md) | GPU | Compute clusters and instance |
| [NCasT4_v3](../virtual-machines/nct4-v3-series.md) | GPU | Compute clusters and instance |
| [NDasrA100_v4](../virtual-machines/nda100-v4-series.md) | GPU | Compute clusters and instance |


While Azure Machine Learning supports these VM series, they might not be available in all Azure regions. To check whether VM series are available, see [Products available by region](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines).

> [!NOTE]
> Azure Machine Learning doesn't support all VM sizes that Azure Compute supports. To list the available VM sizes, use one of the following methods:
> * [REST API](https://github.com/Azure/azure-rest-api-specs/blob/master/specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/stable/2020-08-01/examples/ListVMSizesResult.json)
> * The [Azure CLI extension 2.0 for machine learning](how-to-configure-cli.md) command, [az ml compute list-sizes](/cli/azure/ml/compute#az-ml-compute-list-sizes).

If using the GPU-enabled compute targets, it is important to ensure that the correct CUDA drivers are installed in the training environment. Use the following table to determine the correct CUDA version to use:

| **GPU Architecture**  | **Azure VM Series** | **Supported CUDA versions** |
|------------|------------|------------|
| Ampere | NDA100_v4 | 11.0+ |
| Turing | NCT4_v3 | 10.0+ |
| Volta | NCv3, NDv2 | 9.0+ |
| Pascal | NCv2, ND | 9.0+ |
| Maxwell | NV, NVv3 | 9.0+ |
| Kepler | NC, NC Promo| 9.0+ |

In addition to ensuring the CUDA version and hardware are compatible, also ensure that the CUDA version is compatible with the version of the machine learning framework you are using: 

- For PyTorch, you can check the compatibility by visiting [Pytorch's previous versions page](https://pytorch.org/get-started/previous-versions/). 
- For Tensorflow, you can check the compatibility by visiting [Tensorflow's build from source page](https://www.tensorflow.org/install/source#gpu).

### Compute isolation

Azure Machine Learning compute offers VM sizes that are isolated to a specific hardware type and dedicated to a single customer. Isolated VM sizes are best suited for workloads that require a high degree of isolation from other customers' workloads for reasons that include meeting compliance and regulatory requirements. Utilizing an isolated size guarantees that your VM will be the only one running on that specific server instance.

The current isolated VM offerings include:

* Standard_M128ms
* Standard_F72s_v2
* Standard_NC24s_v3
* Standard_NC24rs_v3*

*RDMA capable

To learn more about isolation, see [Isolation in the Azure public cloud](../security/fundamentals/isolation-choices.md).

## Unmanaged compute

An unmanaged compute target is *not* managed by Azure Machine Learning. You create this type of compute target outside Azure Machine Learning and then attach it to your workspace. Unmanaged compute resources can require additional steps for you to maintain or to improve performance for machine learning workloads. 

Azure Machine Learning supports the following unmanaged compute types:

* Remote virtual machines
* Azure HDInsight
* Azure Databricks
* Azure Data Lake Analytics
* [Azure Synapse Spark pool](v1/how-to-link-synapse-ml-workspaces.md) (preview)

    > [!TIP]
    > Currently this requires the Azure Machine Learning SDK v1.
* [Kubernetes](how-to-attach-kubernetes-anywhere.md)

For more information, see [Manage compute resources](how-to-create-attach-compute-studio.md).

## Next steps

Learn how to:
* [Deploy your model to a compute target](how-to-deploy-online-endpoints.md)
