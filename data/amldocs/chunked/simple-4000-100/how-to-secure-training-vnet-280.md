    :::image type="content" source="./media/how-to-secure-training-vnet/with-public-ip.png" alt-text="A screenshot of how to configure a compute instance/cluster in a VNet with a public IP." lightbox="./media/how-to-secure-training-vnet/with-public-ip.png":::


## Azure Databricks

* The virtual network must be in the same subscription and region as the Azure Machine Learning workspace.
* If the Azure Storage Account(s) for the workspace are also secured in a virtual network, they must be in the same virtual network as the Azure Databricks cluster.
* In addition to the __databricks-private__ and __databricks-public__ subnets used by Azure Databricks, the __default__ subnet created for the virtual network is also required.
* Azure Databricks doesn't use a private endpoint to communicate with the virtual network.

For specific information on using Azure Databricks with a virtual network, see [Deploy Azure Databricks in your Azure Virtual Network](/azure/databricks/administration-guide/cloud-configurations/azure/vnet-inject).

## Virtual machine or HDInsight cluster

In this section, you learn how to use a virtual machine or Azure HDInsight cluster in a virtual network with your workspace.

### Create the VM or HDInsight cluster

> [!IMPORTANT]
> Azure Machine Learning supports only virtual machines that are running Ubuntu.

Create a VM or HDInsight cluster by using the Azure portal or the Azure CLI, and put the cluster in an Azure virtual network. For more information, see the following articles:
* [Create and manage Azure virtual networks for Linux VMs](../virtual-machines/linux/tutorial-virtual-network.md)

* [Extend HDInsight using an Azure virtual network](../hdinsight/hdinsight-plan-virtual-network-deployment.md)

### Configure network ports 

Allow Azure Machine Learning to communicate with the SSH port on the VM or cluster, configure a source entry for the network security group. The SSH port is usually port 22. To allow traffic from this source, do the following actions:

1. In the __Source__ drop-down list, select __Service Tag__.

1. In the __Source service tag__ drop-down list, select __AzureMachineLearning__.

    ![Inbound rules for doing experimentation on a VM or HDInsight cluster within a virtual network](./media/how-to-enable-virtual-network/experimentation-virtual-network-inbound.png)

1. In the __Source port ranges__ drop-down list, select __*__.

1. In the __Destination__ drop-down list, select __Any__.

1. In the __Destination port ranges__ drop-down list, select __22__.

1. Under __Protocol__, select __Any__.

1. Under __Action__, select __Allow__.

Keep the default outbound rules for the network security group. For more information, see the default security rules in [Security groups](../virtual-network/network-security-groups-overview.md#default-security-rules).

If you don't want to use the default outbound rules and you do want to limit the outbound access of your virtual network, see the [required public internet access](#required-public-internet-access-to-train-models) section.

### Attach the VM or HDInsight cluster

Attach the VM or HDInsight cluster to your Azure Machine Learning workspace. For more information, see [Manage compute resources for model training and deployment in studio](how-to-create-attach-compute-studio.md).

## Required public internet access to train models

> [!IMPORTANT]
> While previous sections of this article describe configurations required to **create** compute resources, the configuration information in this section is required to **use** these resources to train models.

[!INCLUDE [machine-learning-required-public-internet-access](../../includes/machine-learning-public-internet-access.md)]

For information on using a firewall solution, see [Use a firewall with Azure Machine Learning](how-to-access-azureml-behind-firewall.md).
## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
