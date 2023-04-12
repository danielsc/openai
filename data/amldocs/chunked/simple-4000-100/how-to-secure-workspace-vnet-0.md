
# Secure an Azure Machine Learning workspace with virtual networks

[!INCLUDE [sdk/cli v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK/CLI extension you are using:"]
> * [v1](v1/how-to-secure-workspace-vnet.md)
> * [v2 (current version)](how-to-secure-workspace-vnet.md)

In this article, you learn how to secure an Azure Machine Learning workspace and its associated resources in a virtual network.

> [!TIP]
> This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:
>
> * [Virtual network overview](how-to-network-security-overview.md)
> * [Secure the training environment](how-to-secure-training-vnet.md)
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md)
> * [Enable studio functionality](how-to-enable-studio-virtual-network.md)
> * [Use custom DNS](how-to-custom-dns.md)
> * [Use a firewall](how-to-access-azureml-behind-firewall.md)
> * [API platform network isolation](how-to-configure-network-isolation-with-v2.md)
>
> For a tutorial on creating a secure workspace, see [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md) or [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md).

In this article you learn how to enable the following workspaces resources in a virtual network:
> [!div class="checklist"]
> - Azure Machine Learning workspace
> - Azure Storage accounts
> - Azure Key Vault
> - Azure Container Registry

## Prerequisites

+ Read the [Network security overview](how-to-network-security-overview.md) article to understand common virtual network scenarios and overall virtual network architecture.

+ Read the [Azure Machine Learning best practices for enterprise security](/azure/cloud-adoption-framework/ready/azure-best-practices/ai-machine-learning-enterprise-security) article to learn about best practices.

+ An existing virtual network and subnet to use with your compute resources.

    > [!IMPORTANT]
    > We do not recommend using the 172.17.0.0/16 IP address range for your VNet. This is the default subnet range used by the Docker bridge network. Other ranges may also conflict depending on what you want to connect to the virtual network. For example, if you plan to connect your on premises network to the VNet, and your on-premises network also uses the 172.16.0.0/16 range. Ultimately, it is up to __you__ to plan your network infrastructure.

+ To deploy resources into a virtual network or subnet, your user account must have permissions to the following actions in Azure role-based access control (Azure RBAC):

    - "Microsoft.Network/virtualNetworks/join/action" on the virtual network resource.
    - "Microsoft.Network/virtualNetworks/subnets/join/action" on the subnet resource.

    For more information on Azure RBAC with networking, see the [Networking built-in roles](../role-based-access-control/built-in-roles.md#networking)

### Azure Container Registry

* Your Azure Container Registry must be Premium version. For more information on upgrading, see [Changing SKUs](../container-registry/container-registry-skus.md#changing-tiers).

* If your Azure Container Registry uses a __private endpoint__, it must be in the same _virtual network_ as the storage account and compute targets used for training or inference. If it uses a __service endpoint__, it must be in the same _virtual network_ and _subnet_ as the storage account and compute targets.

* Your Azure Machine Learning workspace must contain an [Azure Machine Learning compute cluster](how-to-create-attach-compute-cluster.md).

## Limitations

### Azure storage account

* If you plan to use Azure Machine Learning studio and the storage account is also in the VNet, there are extra validation requirements:

    * If the storage account uses a __service endpoint__, the workspace private endpoint and storage service endpoint must be in the same subnet of the VNet.
