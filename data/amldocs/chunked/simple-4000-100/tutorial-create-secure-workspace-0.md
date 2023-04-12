# How to create a secure workspace

In this article, learn how to create and connect to a secure Azure Machine Learning workspace. A secure workspace uses Azure Virtual Network to create a security boundary around resources used by Azure Machine Learning. 

In this tutorial, you accomplish the following tasks:

> [!div class="checklist"]
> * Create an Azure Virtual Network (VNet) to __secure communications between services in the virtual network__.
> * Create an Azure Storage Account (blob and file) behind the VNet. This service is used as __default storage for the workspace__.
> * Create an Azure Key Vault behind the VNet. This service is used to __store secrets used by the workspace__. For example, the security information needed to access the storage account.
> * Create an Azure Container Registry (ACR). This service is used as a repository for Docker images. __Docker images provide the compute environments needed when training a machine learning model or deploying a trained model as an endpoint__.
> * Create an Azure Machine Learning workspace.
> * Create a jump box. A jump box is an Azure Virtual Machine that is behind the VNet. Since the VNet restricts access from the public internet, __the jump box is used as a way to connect to resources behind the VNet__.
> * Configure Azure Machine Learning studio to work behind a VNet. The studio provides a __web interface for Azure Machine Learning__.
> * Create an Azure Machine Learning compute cluster. A compute cluster is used when __training machine learning models in the cloud__. In configurations where Azure Container Registry is behind the VNet, it is also used to build Docker images.
> * Connect to the jump box and use the Azure Machine Learning studio.

> [!TIP]
> If you're looking for a template (Microsoft Bicep or Hashicorp Terraform) that demonstrates how to create a secure workspace, see [Tutorial - Create a secure workspace using a template](tutorial-create-secure-workspace-template.md).

After completing this tutorial, you'll have the following architecture:

* An Azure Virtual Network, which contains three subnets:
    * __Training__: Contains the Azure Machine Learning workspace, dependency services, and resources used for training models.
    * __Scoring__: For the steps in this tutorial, it isn't used. However if you continue using this workspace for other tutorials, we recommend using this subnet when deploying models to [endpoints](concept-endpoints.md).
    * __AzureBastionSubnet__: Used by the Azure Bastion service to securely connect clients to Azure Virtual Machines.
* An Azure Machine Learning workspace that uses a private endpoint to communicate using the VNet.
* An Azure Storage Account that uses private endpoints to allow storage services such as blob and file to communicate using the VNet.
* An Azure Container Registry that uses a private endpoint communicate using the VNet.
* Azure Bastion, which allows you to use your browser to securely communicate with the jump box VM inside the VNet.
* An Azure Virtual Machine that you can remotely connect to and access resources secured inside the VNet.
* An Azure Machine Learning compute instance and compute cluster.

> [!TIP]
> The Azure Batch Service listed on the diagram is a back-end service required by the compute clusters and compute instances.

:::image type="content" source="./media/tutorial-create-secure-workspace/create-secure-vnet-end-state.svg" alt-text="Diagram of the final architecture created through this tutorial." lightbox="./media/tutorial-create-secure-workspace/create-secure-vnet-end-state.png":::

## Prerequisites

* Familiarity with Azure Virtual Networks and IP networking. If you aren't familiar, try the [Fundamentals of computer networking](/training/modules/network-fundamentals/) module.
* While most of the steps in this article use the Azure portal or the Azure Machine Learning studio, some steps use the Azure CLI extension for Machine Learning v2.

## Create a virtual network

To create a virtual network, use the following steps:
