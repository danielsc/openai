
# Configure a private endpoint for an Azure Machine Learning workspace

[!INCLUDE [CLI v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the Azure Machine Learning version you are using:"]
> * [CLI or SDK v1](v1/how-to-configure-private-link.md)
> * [CLI v2 (current)](how-to-configure-private-link.md)

In this document, you learn how to configure a private endpoint for your Azure Machine Learning workspace. For information on creating a virtual network for Azure Machine Learning, see [Virtual network isolation and privacy overview](how-to-network-security-overview.md).

Azure Private Link enables you to connect to your workspace using a private endpoint. The private endpoint is a set of private IP addresses within your virtual network. You can then limit access to your workspace to only occur over the private IP addresses. A private endpoint helps reduce the risk of data exfiltration. To learn more about private endpoints, see the [Azure Private Link](../private-link/private-link-overview.md) article.

> [!WARNING]
> Securing a workspace with private endpoints does not ensure end-to-end security by itself. You must secure all of the individual components of your solution. For example, if you use a private endpoint for the workspace, but your Azure Storage Account is not behind the VNet, traffic between the workspace and storage does not use the VNet for security.
>
> For more information on securing resources used by Azure Machine Learning, see the following articles:
>
> * [Virtual network isolation and privacy overview](how-to-network-security-overview.md).
> * [Secure workspace resources](how-to-secure-workspace-vnet.md).
> * [Secure training environments](how-to-secure-training-vnet.md).
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md).
> * [Use Azure Machine Learning studio in a VNet](how-to-enable-studio-virtual-network.md).
> * [API platform network isolation](how-to-configure-network-isolation-with-v2.md).

## Prerequisites

* You must have an existing virtual network to create the private endpoint in. 

    > [!IMPORTANT]
    > We do not recommend using the 172.17.0.0/16 IP address range for your VNet. This is the default subnet range used by the Docker bridge network. Other ranges may also conflict depending on what you want to connect to the virtual network. For example, if you plan to connect your on premises network to the VNet, and your on-premises network also uses the 172.16.0.0/16 range. Ultimately, it is up to __you__ to plan your network infrastructure.

* [Disable network policies for private endpoints](../private-link/disable-private-endpoint-network-policy.md) before adding the private endpoint.

## Limitations

* If you enable public access for a workspace secured with private endpoint and use Azure Machine Learning studio over the public internet, some features such as the designer may fail to access your data. This problem happens when the data is stored on a service that is secured behind the VNet. For example, an Azure Storage Account.
* You may encounter problems trying to access the private endpoint for your workspace if you're using Mozilla Firefox. This problem may be related to DNS over HTTPS in Mozilla Firefox. We recommend using Microsoft Edge or Google Chrome.
* Using a private endpoint doesn't affect Azure control plane (management operations) such as deleting the workspace or managing compute resources. For example, creating, updating, or deleting a compute target. These operations are performed over the public Internet as normal. Data plane operations, such as using Azure Machine Learning studio, APIs (including published pipelines), or the SDK use the private endpoint.
* When creating a compute instance or compute cluster in a workspace with a private endpoint, the compute instance and compute cluster must be in the same Azure region as the workspace.
* When attaching an Azure Kubernetes Service cluster to a workspace with a private endpoint, the cluster must be in the same region as the workspace.
