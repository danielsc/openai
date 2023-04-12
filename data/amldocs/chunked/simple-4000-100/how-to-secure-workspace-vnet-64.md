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
