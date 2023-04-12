1. Add a new private endpoint for the Azure Storage Account, Azure Key Vault, and Azure Container Registry used by your workspace. These private endpoints should exist in the client VNet.
1. If you have other storage that is used by your workspace, add a new private endpoint for that storage. The private endpoint should exist in the client VNet and have private DNS zone integration enabled.
1. Add a new private endpoint to your workspace. This private endpoint should exist in the client VNet and have private DNS zone integration enabled.
1. Attach the AKS cluster to the Azure Machine Learning workspace. For more information, see [Create and attach an Azure Kubernetes Service cluster](how-to-create-attach-kubernetes.md#attach-an-existing-aks-cluster).

:::image type="content" source="./media/how-to-configure-private-link/multiple-private-endpoint-workspace-aks.png" alt-text="Diagram of isolated AKS VNet":::

## Next steps

* For more information on securing your Azure Machine Learning workspace, see the [Virtual network isolation and privacy overview](how-to-network-security-overview.md) article.

* If you plan on using a custom DNS solution in your virtual network, see [how to use a workspace with a custom DNS server](how-to-custom-dns.md).

* [API platform network isolation](how-to-configure-network-isolation-with-v2.md)
