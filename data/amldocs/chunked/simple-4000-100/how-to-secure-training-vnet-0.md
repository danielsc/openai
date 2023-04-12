
# Secure an Azure Machine Learning training environment with virtual networks

[!INCLUDE [SDK v2](../../includes/machine-learning-sdk-v2.md)]

> [!div class="op_single_selector" title1="Select the Azure Machine Learning SDK version you are using:"]
> * [SDK v1](./v1/how-to-secure-training-vnet.md)
> * [SDK v2 (current version)](how-to-secure-training-vnet.md)

Azure Machine Learning compute instance and compute cluster can be used to securely train models in a virtual network. When planning your environment, you can configure the compute instance/cluster with or without a public IP address. The general differences between the two are:

* **No public IP**: Reduces costs as it doesn't have the same networking resource requirements. Improves security by removing the requirement for inbound traffic from the internet. However, there are additional configuration changes required to enable outbound access to required resources (Azure Active Directory, Azure Resource Manager, etc.).
* **Public IP**: Works by default, but costs more due to additional Azure networking resources. Requires inbound communication from the Azure Machine Learning service over the public internet.

The following table contains the differences between these configurations:

| Configuration | With public IP | Without public IP |
| ----- | ----- | ----- |
| Inbound traffic | AzureMachineLearning | None |
| Outbound traffic | By default, can access the public internet with no restrictions.<br>You can restrict what it accesses using a Network Security Group or firewall. | By default, it cannot access the public internet since there is no public IP resource.<br>You need a Virtual Network NAT gateway or Firewall to route outbound traffic to required resources on the internet. |
| Azure networking resources | Public IP address, load balancer, network interface | None |

You can also use Azure Databricks or HDInsight to train models in a virtual network.

> [!TIP]
> This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:
>
> * [Virtual network overview](how-to-network-security-overview.md)
> * [Secure the workspace resources](how-to-secure-workspace-vnet.md)
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md)
> * [Enable studio functionality](how-to-enable-studio-virtual-network.md)
> * [Use custom DNS](how-to-custom-dns.md)
> * [Use a firewall](how-to-access-azureml-behind-firewall.md)
>
> For a tutorial on creating a secure workspace, see [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md) or [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md).

In this article you learn how to secure the following training compute resources in a virtual network:
> [!div class="checklist"]
> - Azure Machine Learning compute cluster
> - Azure Machine Learning compute instance
> - Azure Databricks
> - Virtual Machine
> - HDInsight cluster

## Prerequisites

+ Read the [Network security overview](how-to-network-security-overview.md) article to understand common virtual network scenarios and overall virtual network architecture.

+ An existing virtual network and subnet to use with your compute resources. This VNet must be in the same subscription as your Azure Machine Learning workspace.

    - We recommend putting the storage accounts used by your workspace and training jobs in the same Azure region that you plan to use for your compute instances and clusters. If they aren't in the same Azure region, you may incur data transfer costs and increased network latency.
    - Make sure that **WebSocket** communication is allowed to `*.instances.azureml.net` and `*.instances.azureml.ms` in your VNet. WebSockets are used by Jupyter on compute instances.

+ An existing subnet in the virtual network. This subnet is used when creating compute instances and clusters.

    - Make sure that the subnet isn't delegated to other Azure services.
    - Make sure that the subnet contains enough free IP addresses. Each compute instance requires one IP address. Each *node* within a compute cluster requires one IP address.
