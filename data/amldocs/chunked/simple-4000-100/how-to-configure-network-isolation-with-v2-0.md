
# Network Isolation Change with Our New API Platform on Azure Resource Manager

In this article, you'll learn about network isolation changes with our new v2 API platform on Azure Resource Manager (ARM) and its effect on network isolation.


## Prerequisites

* The [Azure Machine Learning Python SDK v1](/python/api/overview/azure/ml/install) or [Azure CLI extension for machine learning v1](reference-azure-machine-learning-cli.md).

    > [!IMPORTANT]
    > The v1 extension (`azure-cli-ml`) version must be 1.41.0 or greater. Use the `az version` command to view version information.
 
## What is the new API platform on Azure Resource Manager (ARM)

There are two types of operations used by the v1 and v2 APIs, __Azure Resource Manager (ARM)__ and __Azure Machine Learning workspace__.

With the v1 API, most operations used the workspace. For v2, we've moved most operations to use public ARM.

| API version | Public ARM | Inside workspace virtual network |
| ----- | ----- | ----- |
| v1 | Workspace and compute create, update, and delete (CRUD) operations. | Other operations such as experiments. |
| v2 | Most operations such as workspace, compute, datastore, dataset, job, environment, code, component, endpoints. | Remaining operations. |


The v2 API provides a consistent API in one place. You can more easily use Azure role-based access control and Azure Policy for resources with the v2 API because it's based on Azure Resource Manager.

The Azure Machine Learning CLI v2 uses our new v2 API platform. New features such as [managed online endpoints](concept-endpoints.md) are only available using the v2 API platform.

## What are the network isolation changes with V2

As mentioned in the previous section, there are two types of operations; with ARM and with the workspace. With the __legacy v1 API__, most operations used the workspace. With the v1 API, adding a private endpoint to the workspace provided network isolation for everything except CRUD operations on the workspace or compute resources.

With the __new v2 API__, most operations use ARM. So enabling a private endpoint on your workspace doesn't provide the same level of network isolation. Operations that use ARM communicate  over public networks, and include any metadata (such as your resource IDs) or parameters used by the operation. For example, the [create or update job](/rest/api/azureml/2022-10-01/jobs/create-or-update) api sends metadata, and [parameters](./reference-yaml-job-command.md).

> [!IMPORTANT]
> For most people, using the public ARM communications is OK:
> * Public ARM communications is the standard for management operations with Azure services. For example, creating an Azure Storage Account or Azure Virtual Network uses ARM.
> * The Azure Machine Learning operations do not expose data in your storage account (or other storage in the VNet) on public networks. For example, a training job that runs on a compute cluster in the VNet, and uses data from a storage account in the VNet, would securely access the data directly using the VNet.
> * All communication with public ARM is encrypted using TLS 1.2.

If you need time to evaluate the new v2 API before adopting it in your enterprise solutions, or have a company policy that prohibits sending communication over public networks, you can enable the *v1_legacy_mode* parameter. When enabled, this parameter disables the v2 API for your workspace.

> [!WARNING]
> Enabling v1_legacy_mode may prevent you from using features provided by the v2 API. For example, some features of Azure Machine Learning studio may be unavailable.

## Scenarios and Required Actions

> [!WARNING]
> The *v1_legacy_mode* parameter is available now, but the v2 API blocking functionality will be enforced starting the week of May 15th, 2022.

* If you don't plan on using a private endpoint with your workspace, you don't need to enable parameter.

* If you're OK with operations communicating with public ARM, you don't need to enable the parameter.

* You only need to enable the parameter if you're using a private endpoint with the workspace _and_ don't want to allow operations with ARM over public networks.
