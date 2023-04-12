
# Use Azure Machine Learning studio in an Azure virtual network

In this article, you learn how to use Azure Machine Learning studio in a virtual network. The studio includes features like AutoML, the designer, and data labeling. 

Some of the studio's features are disabled by default in a virtual network. To re-enable these features, you must enable managed identity for storage accounts you intend to use in the studio. 

The following operations are disabled by default in a virtual network:

* Preview data in the studio.
* Visualize data in the designer.
* Deploy a model in the designer.
* Submit an AutoML experiment.
* Start a labeling project.

The studio supports reading data from the following datastore types in a virtual network:

* Azure Storage Account (blob & file)
* Azure Data Lake Storage Gen1
* Azure Data Lake Storage Gen2
* Azure SQL Database

In this article, you learn how to:

> [!div class="checklist"]
> - Give the studio access to data stored inside of a virtual network.
> - Access the studio from a resource inside of a virtual network.
> - Understand how the studio impacts storage security.

> [!TIP]
> This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:
>
> * [Virtual network overview](how-to-network-security-overview.md)
> * [Secure the workspace resources](how-to-secure-workspace-vnet.md)
> * [Secure the training environment](how-to-secure-training-vnet.md)
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md)
> * [Use custom DNS](how-to-custom-dns.md)
> * [Use a firewall](how-to-access-azureml-behind-firewall.md)
>
> For a tutorial on creating a secure workspace, see [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md) or [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md).

## Prerequisites

+ Read the [Network security overview](how-to-network-security-overview.md) to understand common virtual network scenarios and architecture.

+ A pre-existing virtual network and subnet to use.

+ An existing [Azure Machine Learning workspace with a private endpoint](how-to-secure-workspace-vnet.md#secure-the-workspace-with-private-endpoint).

+ An existing [Azure storage account added your virtual network](how-to-secure-workspace-vnet.md#secure-azure-storage-accounts).

## Limitations

### Azure Storage Account

* When the storage account is in the VNet, there are extra validation requirements when using studio:

    * If the storage account uses a __service endpoint__, the workspace private endpoint and storage service endpoint must be in the same subnet of the VNet.
    * If the storage account uses a __private endpoint__, the workspace private endpoint and storage private endpoint must be in the same VNet. In this case, they can be in different subnets.

### Designer sample pipeline

There's a known issue where user cannot run sample pipeline in Designer homepage. This is the sample dataset used in the sample pipeline is Azure Global dataset, and it cannot satisfy all virtual network environment.

To resolve this issue, you can use a public workspace to run sample pipeline to get to know how to use the designer and then replace the sample dataset with your own dataset in the workspace within virtual network.

## Datastore: Azure Storage Account

Use the following steps to enable access to data stored in Azure Blob and File storage:

> [!TIP]
> The first step is not required for the default storage account for the workspace. All other steps are required for *any* storage account behind the VNet and used by the workspace, including the default storage account.

1. **If the storage account is the *default* storage for your workspace, skip this step**. If it is not the default, __Grant the workspace managed identity the 'Storage Blob Data Reader' role__ for the Azure storage account so that it can read data from blob storage.

    For more information, see the [Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) built-in role.
