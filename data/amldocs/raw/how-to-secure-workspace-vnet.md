---
title: Secure an Azure Machine Learning workspace with virtual networks
titleSuffix: Azure Machine Learning
description: Use an isolated Azure Virtual Network to secure your Azure Machine Learning workspace and associated resources.
services: machine-learning
ms.service: machine-learning
ms.subservice: enterprise-readiness
ms.reviewer: larryfr
ms.author: jhirono
author: jhirono
ms.date: 01/19/2023
ms.topic: how-to
ms.custom: contperf-fy20q4, tracking-python, contperf-fy21q1, security, cliv2, sdkv2, event-tier1-build-2022, engagement-fy23
---

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
    * If the storage account uses a __private endpoint__, the workspace private endpoint and storage private endpoint must be in the same VNet. In this case, they can be in different subnets.

### Azure Container Instances

When your Azure Machine Learning workspace is configured with a private endpoint, deploying to Azure Container Instances in a VNet is not supported. Instead, consider using a [Managed online endpoint with network isolation](how-to-secure-online-endpoint.md).

### Azure Container Registry

When ACR is behind a virtual network, Azure Machine Learning can’t use it to directly build Docker images. Instead, the compute cluster is used to build the images.

> [!IMPORTANT]
> The compute cluster used to build Docker images needs to be able to access the package repositories that are used to train and deploy your models. You may need to add network security rules that allow access to public repos, [use private Python packages](how-to-use-private-python-packages.md), or use [custom Docker images](v1/how-to-train-with-custom-image.md) that already include the packages.

> [!WARNING]
> If your Azure Container Registry uses a private endpoint or service endpoint to communicate with the virtual network, you cannot use a managed identity with an Azure Machine Learning compute cluster.

### Azure Monitor

> [!WARNING]
> Azure Monitor supports using Azure Private Link to connect to a VNet. However, you must use the open Private Link mode in Azure Monitor. For more information, see [Private Link access modes: Private only vs. Open](../azure-monitor/logs/private-link-security.md#private-link-access-modes-private-only-vs-open).

## Required public internet access

[!INCLUDE [machine-learning-required-public-internet-access](../../includes/machine-learning-public-internet-access.md)]

For information on using a firewall solution, see [Configure required input and output communication](how-to-access-azureml-behind-firewall.md).

## Secure the workspace with private endpoint

Azure Private Link lets you connect to your workspace using a private endpoint. The private endpoint is a set of private IP addresses within your virtual network. You can then limit access to your workspace to only occur over the private IP addresses. A private endpoint helps reduce the risk of data exfiltration.

For more information on configuring a private endpoint for your workspace, see [How to configure a private endpoint](how-to-configure-private-link.md).

> [!WARNING]
> Securing a workspace with private endpoints does not ensure end-to-end security by itself. You must follow the steps in the rest of this article, and the VNet series, to secure individual components of your solution. For example, if you use a private endpoint for the workspace, but your Azure Storage Account is not behind the VNet, traffic between the workspace and storage does not use the VNet for security.

## Secure Azure storage accounts

Azure Machine Learning supports storage accounts configured to use either a private endpoint or service endpoint. 

# [Private endpoint](#tab/pe)

1. In the Azure portal, select the Azure Storage Account.
1. Use the information in [Use private endpoints for Azure Storage](../storage/common/storage-private-endpoints.md#creating-a-private-endpoint) to add private endpoints for the following storage resources:

    * **Blob**
    * **File**
    * **Queue** - Only needed if you plan to use [Batch endpoints](concept-endpoints.md#what-are-batch-endpoints) or the [ParallelRunStep](./tutorial-pipeline-batch-scoring-classification.md) in an Azure Machine Learning pipeline.
    * **Table** - Only needed if you plan to use [Batch endpoints](concept-endpoints.md#what-are-batch-endpoints) or the [ParallelRunStep](./tutorial-pipeline-batch-scoring-classification.md) in an Azure Machine Learning pipeline.

    :::image type="content" source="./media/how-to-enable-studio-virtual-network/configure-storage-private-endpoint.png" alt-text="Screenshot showing private endpoint configuration page with blob and file options":::

    > [!TIP]
    > When configuring a storage account that is **not** the default storage, select the **Target subresource** type that corresponds to the storage account you want to add.

1. After creating the private endpoints for the storage resources, select the __Firewalls and virtual networks__ tab under __Networking__ for the storage account.
1. Select __Selected networks__, and then under __Resource instances__, select `Microsoft.MachineLearningServices/Workspace` as the __Resource type__. Select your workspace using __Instance name__. For more information, see [Trusted access based on system-assigned managed identity](../storage/common/storage-network-security.md#trusted-access-based-on-system-assigned-managed-identity).

    > [!TIP]
    > Alternatively, you can select __Allow Azure services on the trusted services list to access this storage account__ to more broadly allow access from trusted services. For more information, see [Configure Azure Storage firewalls and virtual networks](../storage/common/storage-network-security.md#trusted-microsoft-services).

    :::image type="content" source="./media/how-to-enable-virtual-network/storage-firewalls-and-virtual-networks-no-vnet.png" alt-text="The networking area on the Azure Storage page in the Azure portal when using private endpoint":::

1. Select __Save__ to save the configuration.

> [!TIP]
> When using a private endpoint, you can also disable public access. For more information, see [disallow public read access](../storage/blobs/anonymous-read-access-configure.md#allow-or-disallow-public-read-access-for-a-storage-account).

# [Service endpoint](#tab/se)

1. In the Azure portal, select the Azure Storage Account.

1. From the __Security + networking__ section on the left of the page, select __Networking__ and then select the __Firewalls and virtual networks__ tab.

1. Select __Selected networks__. Under __Virtual networks__, select the __Add existing virtual network__ link and select the virtual network that your workspace uses.

    > [!IMPORTANT]
    > The storage account must be in the same virtual network and subnet as the compute instances or clusters used for training or inference.

1. Under __Resource instances__, select `Microsoft.MachineLearningServices/Workspace` as the __Resource type__ and select your workspace using __Instance name__. For more information, see [Trusted access based on system-assigned managed identity](../storage/common/storage-network-security.md#trusted-access-based-on-system-assigned-managed-identity).

    > [!TIP]
    > Alternatively, you can select __Allow Azure services on the trusted services list to access this storage account__ to more broadly allow access from trusted services. For more information, see [Configure Azure Storage firewalls and virtual networks](../storage/common/storage-network-security.md#trusted-microsoft-services).

    :::image type="content" source="./media/how-to-enable-virtual-network/storage-firewalls-and-virtual-networks.png" alt-text="The networking area on the Azure Storage page in the Azure portal":::

1. Select __Save__ to save the configuration.

> [!TIP]
> When using a service endpoint, you can also disable public access. For more information, see [disallow public read access](../storage/blobs/anonymous-read-access-configure.md#allow-or-disallow-public-read-access-for-a-storage-account).

---

## Secure Azure Key Vault

Azure Machine Learning uses an associated Key Vault instance to store the following credentials:
* The associated storage account connection string
* Passwords to Azure Container Repository instances
* Connection strings to data stores

Azure key vault can be configured to use either a private endpoint or service endpoint. To use Azure Machine Learning experimentation capabilities with Azure Key Vault behind a virtual network, use the following steps:

> [!TIP]
> Regardless of whether you use a private endpoint or service endpoint, the key vault must be in the same network as the private endpoint of the workspace.

# [Private endpoint](#tab/pe)

For information on using a private endpoint with Azure Key Vault, see [Integrate Key Vault with Azure Private Link](../key-vault/general/private-link-service.md#establish-a-private-link-connection-to-key-vault-using-the-azure-portal).


# [Service endpoint](#tab/se)

1. Go to the Key Vault that's associated with the workspace.

1. On the __Key Vault__ page, in the left pane, select __Networking__.

1. On the __Firewalls and virtual networks__ tab, do the following actions:
    1. Under __Allow access from__, select __Allow public access from specific virtual networks and IP addresses__.
    1. Under __Virtual networks__, select __Add a virtual network__, __Add existing virtual networks__, and add the virtual network/subnet where your experimentation compute resides.
    1. Verify that __Allow trusted Microsoft services to bypass this firewall__ is checked, and then select __Apply__.

    :::image type="content" source="./media/how-to-enable-virtual-network/key-vault-firewalls-and-virtual-networks-page.png" alt-text="The Firewalls and virtual networks section in the Key Vault pane":::

For more information, see [Configure Azure Key Vault network settings](../key-vault/general/how-to-azure-key-vault-network-security.md).

---

## Enable Azure Container Registry (ACR)

> [!TIP]
> If you did not use an existing Azure Container Registry when creating the workspace, one may not exist. By default, the workspace will not create an ACR instance until it needs one. To force the creation of one, train or deploy a model using your workspace before using the steps in this section.

Azure Container Registry can be configured to use a private endpoint. Use the following steps to configure your workspace to use ACR when it is in the virtual network:

1. Find the name of the Azure Container Registry for your workspace, using one of the following methods:

    # [Azure CLI](#tab/cli)

    [!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

    If you've [installed the Machine Learning extension v2 for Azure CLI](how-to-configure-cli.md), you can use the `az ml workspace show` command to show the workspace information. The v1 extension does not return this information.

    ```azurecli-interactive
    az ml workspace show -n yourworkspacename -g resourcegroupname --query 'container_registry'
    ```

    This command returns a value similar to `"/subscriptions/{GUID}/resourceGroups/{resourcegroupname}/providers/Microsoft.ContainerRegistry/registries/{ACRname}"`. The last part of the string is the name of the Azure Container Registry for the workspace.

    # [Python SDK](#tab/python)

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    The following code snippet demonstrates how to get the container registry information using the [Azure Machine Learning SDK](/python/api/overview/azure/ai-ml-readme):

   ```python
    # import required libraries
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    subscription_id = "<your subscription ID>"
    resource_group = "<your resource group name>"
    workspace = "<your workspace name>"

    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
    
    # Get workspace info
    ws=ml_client.workspaces.get(name=workspace)
    print(ws.container_registry)
    ```

    This code returns a value similar to `"/subscriptions/{GUID}/resourceGroups/{resourcegroupname}/providers/Microsoft.ContainerRegistry/registries/{ACRname}"`. The last part of the string is the name of the Azure Container Registry for the workspace.

    # [Portal](#tab/portal)

    From the overview section of your workspace, the __Registry__ value links to the Azure Container Registry.

    :::image type="content" source="./media/how-to-enable-virtual-network/azure-machine-learning-container-registry.png" alt-text="Azure Container Registry for the workspace" border="true":::

    ---

1. Limit access to your virtual network using the steps in [Connect privately to an Azure Container Registry](../container-registry/container-registry-private-link.md). When adding the virtual network, select the virtual network and subnet for your Azure Machine Learning resources.

1. Configure the ACR for the workspace to [Allow access by trusted services](../container-registry/allow-access-trusted-services.md).

1. Create an Azure Machine Learning compute cluster. This cluster is used to build Docker images when ACR is behind a VNet. For more information, see [Create a compute cluster](how-to-create-attach-compute-cluster.md).

1. Use one of the following methods to configure the workspace to build Docker images using the compute cluster.

    > [!IMPORTANT]
    > The following limitations apply When using a compute cluster for image builds:
    > * Only a CPU SKU is supported.
    > * If you use a compute cluster configured for no public IP address, you must provide some way for the cluster to access the public internet. Internet access is required when accessing images stored on the Microsoft Container Registry, packages installed on Pypi, Conda, etc. You need to configure User Defined Routing (UDR) to reach to a public IP to access the internet. For example, you can use the public IP of your firewall, or you can use [Virtual Network NAT](../virtual-network/nat-gateway/nat-overview.md) with a public IP. For more information, see [How to securely train in a VNet](how-to-secure-training-vnet.md).

    # [Azure CLI](#tab/cli)

    You can use the `az ml workspace update` command to set a build compute. The command is the same for both the v1 and v2 Azure CLI extensions for machine learning. In the following command, replace `myworkspace` with your workspace name, `myresourcegroup` with the resource group that contains the workspace, and `mycomputecluster` with the compute cluster name:

    ```azurecli
    az ml workspace update --name myworkspace --resource-group myresourcegroup --image-build-compute mycomputecluster
    ```

    # [Python SDK](#tab/python)

    The following code snippet demonstrates how to update the workspace to set a build compute using the [Azure Machine Learning SDK](/python/api/overview/azure/ai-ml-readme). Replace `mycomputecluster` with the name of the cluster to use:

    [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

    ```python
    # import required libraries
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential

    subscription_id = "<your subscription ID>"
    resource_group = "<your resource group name>"
    workspace = "<your workspace name>"

    ml_client = MLClient(
        DefaultAzureCredential(), subscription_id, resource_group, workspace
    )
    
    # Get workspace info
    ws=ml_client.workspaces.get(name=workspace)
    # Update to use cpu-cluster for image builds
    ws.image_build_compute="cpu-cluster"
    ml_client.workspaces.begin_update(ws)
    # To switch back to using ACR to build (if ACR is not in the VNet):
    # ws.image_build_compute = ''
    # ml_client.workspaces.begin_update(ws)
    ```

    
    For more information, see the [begin_update](/python/api/azure-ai-ml/azure.ai.ml.operations.workspaceoperations#azure-ai-ml-operations-workspaceoperations-begin-update) method reference.

    # [Portal](#tab/portal)

    Currently there isn't a way to set the image build compute from the Azure portal.

    ---

> [!TIP]
> When ACR is behind a VNet, you can also [disable public access](../container-registry/container-registry-access-selected-networks.md#disable-public-network-access) to it.

## Securely connect to your workspace

[!INCLUDE [machine-learning-connect-secure-workspace](../../includes/machine-learning-connect-secure-workspace.md)]

## Workspace diagnostics

[!INCLUDE [machine-learning-workspace-diagnostics](../../includes/machine-learning-workspace-diagnostics.md)]

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Secure the inference environment](how-to-secure-inferencing-vnet.md)
* [Enable studio functionality](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Use a firewall](how-to-access-azureml-behind-firewall.md)
* [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md)
* [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md)
* [API platform network isolation](how-to-configure-network-isolation-with-v2.md)
