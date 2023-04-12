Data profiling depends on the Azure Machine Learning managed service being able to access the default Azure Storage Account for your workspace. The managed service _doesn't exist in your VNet_, so can’t directly access the storage account in the VNet. Instead, the workspace uses a service principal to access storage.

> [!TIP]
> You can provide a service principal when creating the workspace. If you do not, one is created for you and will have the same name as your workspace.

To allow access to the storage account, configure the storage account to allow a __resource instance__ for your workspace or select the __Allow Azure services on the trusted services list to access this storage account__. This setting allows the managed service to access storage through the Azure data center network. 

Next, add the service principal for the workspace to the __Reader__ role to the private endpoint of the storage account. This role is used to verify the workspace and storage subnet information. If they're the same, access is allowed. Finally, the service principal also requires __Blob data contributor__ access to the storage account.

For more information, see the Azure Storage Account section of [How to secure a workspace in a virtual network](how-to-secure-workspace-vnet.md#secure-azure-storage-accounts).

:::image type="content" source="./media/concept-secure-network-traffic-flow/storage-traffic-studio.png" alt-text="Diagram of traffic between client, data profiling, and storage":::

## Scenario: Use compute instance and compute cluster

Azure Machine Learning compute instance and compute cluster are managed services hosted by Microsoft. They're built on top of the Azure Batch service. While they exist in a Microsoft managed environment, they're also injected into your VNet.

When you create a compute instance or compute cluster, the following resources are also created in your VNet:

* A Network Security Group with required outbound rules. These rules allow __inbound__ access from the Azure Machine Learning (TCP on port 44224) and Azure Batch service (TCP on ports 29876-29877).

    > [!IMPORTANT]
    > If you use a firewall to block internet access into the VNet, you must configure the firewall to allow this traffic. For example, with Azure Firewall you can create user-defined routes. For more information, see [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).

* A load balancer with a public IP.

Also allow __outbound__ access to the following service tags. For each tag, replace `region` with the Azure region of your compute instance/cluster:

* `Storage.region` - This outbound access is used to connect to the Azure Storage Account inside the Azure Batch service-managed VNet.
* `Keyvault.region` - This outbound access is used to connect to the Azure Key Vault account inside the Azure Batch service-managed VNet.

Data access from your compute instance or cluster goes through the private endpoint of the Storage Account for your VNet.

If you use Visual Studio Code on a compute instance, you must allow other outbound traffic. For more information, see [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).

:::image type="content" source="./media/concept-secure-network-traffic-flow/compute-instance-and-cluster.png" alt-text="Diagram of traffic flow when using compute instance or cluster":::

## Scenario: Use online endpoints

Securing an online endpoint with a private endpoint is a preview feature.

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

__Inbound__ communication with the scoring URL of the online endpoint can be secured using the `public_network_access` flag on the endpoint. Setting the flag to `disabled` restricts the online endpoint to receiving traffic only from the virtual network. For secure inbound communications, the Azure Machine Learning workspace's private endpoint is used.

__Outbound__ communication from a deployment can be secured on a per-deployment basis by using the `egress_public_network_access` flag. Outbound communication in this case is from the deployment to Azure Container Registry, storage blob, and workspace. Setting the flag to `true` will restrict communication with these resources to the virtual network.
