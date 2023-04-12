
# How Azure Machine Learning works: resources and assets

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

This article applies to the second version of the [Azure Machine Learning CLI & Python SDK (v2)](concept-v2.md). For version one (v1), see [How Azure Machine Learning works: Architecture and concepts (v1)](v1/concept-azure-machine-learning-architecture.md)

Azure Machine Learning includes several resources and assets to enable you to perform your machine learning tasks. These resources and assets are needed to run any job.

* **Resources**: setup or infrastructural resources needed to run a machine learning workflow. Resources include:
  * [Workspace](#workspace)
  * [Compute](#compute)
  * [Datastore](#datastore)
* **Assets**: created using Azure ML commands or as part of a training/scoring run. Assets are versioned and can be registered in the Azure ML workspace. They include:
  * [Model](#model)
  * [Environment](#environment)
  * [Data](#data)
  * [Component](#component)

This document provides a quick overview of these resources and assets.

## Workspace

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. The workspace keeps a history of all jobs, including logs, metrics, output, and a snapshot of your scripts. The workspace stores references to resources like datastores and compute. It also holds all assets like models, environments, components and data asset.

### Create a workspace

### [Azure CLI](#tab/cli)

To create a workspace using CLI v2, use the following command:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```bash
az ml workspace create --file my_workspace.yml
```

For more information, see [workspace YAML schema](reference-yaml-workspace.md).

### [Python SDK](#tab/sdk)

To create a workspace using Python SDK v2, you can use the following code:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
ws_basic = Workspace(
    name="my-workspace",
    location="eastus", # Azure region (location) of workspace
    display_name="Basic workspace-example",
    description="This example shows how to create a basic workspace"
)
ml_client.workspaces.begin_create(ws_basic) # use MLClient to connect to the subscription and resource group and create workspace
```

This [Jupyter notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/resources/workspace/workspace.ipynb) shows more ways to create an Azure ML workspace using SDK v2.


## Compute

A compute is a designated compute resource where you run your job or host your endpoint. Azure Machine learning supports the following types of compute:

* **Compute cluster** - a managed-compute infrastructure that allows you to easily create a cluster of CPU or GPU compute nodes in the cloud.
* **Compute instance** - a fully configured and managed development environment in the cloud. You can use the instance as a training or inference compute for development and testing. It's similar to a virtual machine on the cloud.
* **Inference cluster** - used to deploy trained machine learning models to Azure Kubernetes Service. You can create an Azure Kubernetes Service (AKS) cluster from your Azure ML workspace, or attach an existing AKS cluster.
* **Attached compute** - You can attach your own compute resources to your workspace and use them for training and inference.

### [Azure CLI](#tab/cli)

To create a compute using CLI v2, use the following command:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```bash
az ml compute --file my_compute.yml
```

For more information, see [compute YAML schema](reference-yaml-overview.md#compute).


### [Python SDK](#tab/sdk)

To create a compute using Python SDK v2, you can use the following code:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
cluster_basic = AmlCompute(
    name="basic-example",
    type="amlcompute",
    size="STANDARD_DS3_v2",
    location="westus",
    min_instances=0,
    max_instances=2,
    idle_time_before_scale_down=120,
)
ml_client.begin_create_or_update(cluster_basic)
```
