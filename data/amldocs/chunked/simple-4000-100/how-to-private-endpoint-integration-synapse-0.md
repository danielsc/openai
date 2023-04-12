
# How to securely integrate Azure Machine Learning and Azure Synapse

In this article, learn how to securely integrate with Azure Machine Learning from Azure Synapse. This integration enables you to use Azure Machine Learning from notebooks in your Azure Synapse workspace. Communication between the two workspaces is secured using an Azure Virtual Network.

> [!TIP]
> You can also perform integration in the opposite direction, using Azure Synapse spark pool from Azure Machine Learning. For more information, see [Link Azure Synapse and Azure Machine Learning](v1/how-to-link-synapse-ml-workspaces.md).

## Prerequisites

* An Azure subscription.
* An Azure Machine Learning workspace with a private endpoint connection to a virtual network. The following workspace dependency services must also have a private endpoint connection to the virtual network:

    * Azure Storage Account

        > [!TIP]
        > For the storage account there are three separate private endpoints; one each for blob, file, and dfs.

    * Azure Key Vault
    * Azure Container Registry

    A quick and easy way to build this configuration is to use a [Microsoft Bicep or HashiCorp Terraform template](tutorial-create-secure-workspace-template.md).

* An Azure Synapse workspace in a __managed__ virtual network, using a __managed__ private endpoint. For more information, see [Azure Synapse Analytics Managed Virtual Network](../synapse-analytics/security/synapse-workspace-managed-vnet.md).

    > [!WARNING]
    > The Azure Machine Learning integration is not currently supported in Synapse Workspaces with data exfiltration protection. When configuring your Azure Synapse workspace, do __not__ enable data exfiltration protection. For more information, see [Azure Synapse Analytics Managed Virtual Network](../synapse-analytics/security/synapse-workspace-managed-vnet.md).

    > [!NOTE]
    > The steps in this article make the following assumptions:
    > * The Azure Synapse workspace is in a different resource group than the Azure Machine Learning workspace.
    > * The Azure Synapse workspace uses a __managed virtual network__. The managed virtual network secures the connectivity between Azure Synapse and Azure Machine Learning. It does __not__ restrict access to the Azure Synapse workspace. You will access the workspace over the public internet.

## Understanding the network communication

In this configuration, Azure Synapse uses a __managed__ private endpoint and virtual network. The managed virtual network and private endpoint secures the internal communications from Azure Synapse to Azure Machine Learning by restricting network traffic to the virtual network. It does __not__ restrict communication between your client and the Azure Synapse workspace.

Azure Machine Learning doesn't provide managed private endpoints or virtual networks, and instead uses a __user-managed__ private endpoint and virtual network. In this configuration, both internal and client/service communication is restricted to the virtual network. For example, if you wanted to directly access the Azure Machine Learning studio from outside the virtual network, you would use one of the following options:

* Create an Azure Virtual Machine inside the virtual network and use Azure Bastion to connect to it. Then connect to Azure Machine Learning from the VM.
* Create a VPN gateway or use ExpressRoute to connect clients to the virtual network.

Since the Azure Synapse workspace is publicly accessible, you can connect to it without having to create things like a VPN gateway. The Synapse workspace securely connects to Azure Machine Learning over the virtual network. Azure Machine Learning and its resources are secured within the virtual network.

When adding data sources, you can also secure those behind the virtual network. For example, securely connecting to an Azure Storage Account or Data Lake Store Gen 2 through the virtual network.

For more information, see the following articles:

* [Azure Synapse Analytics Managed Virtual Network](../synapse-analytics/security/synapse-workspace-managed-vnet.md)
