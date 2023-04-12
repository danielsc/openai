
# [Studio](#tab/azure-studio)

1. Sign in to the [Azure Machine Learning studio](https://ml.azure.com), and then select your subscription and workspace.
1. Select the **Compute** page from the left navigation bar.
1. Select the **+ New** from the navigation bar of compute instance or compute cluster.
1. Configure the VM size and configuration you need, then select **Next**.
1. From the **Advanced Settings**, Select **Enable virtual network**, your virtual network and subnet, and finally select the **No Public IP** option under the VNet/subnet section.

    :::image type="content" source="./media/how-to-secure-training-vnet/no-public-ip.png" alt-text="A screenshot of how to configure no public IP for compute instance and compute cluster." lightbox="./media/how-to-secure-training-vnet/no-public-ip.png":::


## Compute instance/cluster with public IP

The following configurations are in addition to those listed in the [Prerequisites](#prerequisites) section, and are specific to **creating** compute instances/clusters that have a public IP:

+ If you put multiple compute instances/clusters in one virtual network, you may need to request a quota increase for one or more of your resources. The Machine Learning compute instance or cluster automatically allocates networking resources __in the resource group that contains the virtual network__. For each compute instance or cluster, the service allocates the following resources:

    * A network security group (NSG) is automatically created. This NSG allows inbound TCP traffic on port 44224 from the `AzureMachineLearning` service tag.

        > [!IMPORTANT]
        > Compute instance and compute cluster automatically create an NSG with the required rules.
        > 
        > If you have another NSG at the subnet level, the rules in the subnet level NSG mustn't conflict with the rules in the automatically created NSG.
        >
        > To learn how the NSGs filter your network traffic, see [How network security groups filter network traffic](../virtual-network/network-security-group-how-it-works.md).

    * One load balancer

    For compute clusters, these resources are deleted every time the cluster scales down to 0 nodes and created when scaling up.

    For a compute instance, these resources are kept until the instance is deleted. Stopping the instance doesn't remove the resources. 

    > [!IMPORTANT]
    > These resources are limited by the subscription's [resource quotas](../azure-resource-manager/management/azure-subscription-service-limits.md). If the virtual network resource group is locked then deletion of compute cluster/instance will fail. Load balancer cannot be deleted until the compute cluster/instance is deleted. Also please ensure there is no Azure Policy assignment which prohibits creation of network security groups.

+ In your VNet, allow **inbound** TCP traffic on port **44224** from the `AzureMachineLearning` service tag.
    > [!IMPORTANT]
    > The compute instance/cluster is dynamically assigned an IP address when it is created. Since the address is not known before creation, and inbound access is required as part of the creation process, you cannot statically assign it on your firewall. Instead, if you are using a firewall with the VNet you must create a user-defined route to allow this inbound traffic.
+ In your VNet, allow **outbound** traffic to the following service tags:

    | Service tag | Protocol | Port | Notes |
    | ----- |:-----:|:-----:| ----- |
    | `AzureMachineLearning` | TCP<br>UDP | 443/8787/18881<br>5831 | Communication with the Azure Machine Learning service.|
    | `BatchNodeManagement.<region>` | ANY | 443| Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. Communication with Azure Batch. Compute instance and compute cluster are implemented using the Azure Batch service.|
    | `Storage.<region>` | TCP | 443 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. This service tag is used to communicate with the Azure Storage account used by Azure Batch. |
