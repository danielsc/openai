    > Compute cluster and compute instance can be created with or without a public IP address. If created with a public IP address, you get a load balancer with a public IP to accept the inbound access from Azure batch service and Azure Machine Learning service. You need to configure User Defined Routing (UDR) if you use a firewall. If created without a public IP, you get a private link service to accept the inbound access from Azure batch service and Azure Machine Learning service without a public IP.

1. Extra NSG may be required depending on your case. For more information, see [How to secure your training environment](how-to-secure-training-vnet.md).

For more information, see the [Secure an Azure Machine Learning training environment with virtual networks](how-to-secure-training-vnet.md) article.

## Using two-networks architecture

There are cases where the input data is not in the same network as in the Azure Machine Learning resources. In those cases, your Azure Machine Learning workspace may need to interact with more than one VNet. You can achieve this configuration by adding an extra set of private endpoints to the VNet where the rest of the resources are located.

The following diagram shows the high level design:

:::image type="content" source="./media/how-to-secure-batch-endpoint/batch-vnet-two-networks.png" alt-text="Diagram that shows the high level architecture of an Azure Machine Learning workspace interacting with two networks.":::

### Considerations

Have the following considerations when using such architecture:

* Put the second set of private endpoints in a different resource group and hence in different private DNS zones. This prevents a name resolution conflict between the set of IPs used for the workspace and the ones used by the client VNets. Azure Private DNS provides a reliable, secure DNS service to manage and resolve domain names in a virtual network without the need to add a custom DNS solution. By using private DNS zones, you can use your own custom domain names rather than the Azure-provided names available today. Please note that the DNS resolution against a private DNS zone works only from virtual networks that are linked to it. For more details see [recommended zone names for Azure services](../private-link/private-endpoint-dns.md#azure-services-dns-zone-configuration).
* For your storage accounts, add 4 private endpoints in each VNet for blob, file, queue, and table as explained at [Secure Azure storage accounts](how-to-secure-workspace-vnet.md#secure-azure-storage-accounts).


## Recommended read

* [Secure Azure Machine Learning workspace resources using virtual networks (VNets)](how-to-network-security-overview.md)
