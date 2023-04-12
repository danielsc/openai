  * Add a new private endpoint to your workspace. This private endpoint should be in the same or peered VNet as your AKS cluster and have private DNS zone integration enabled.

If you have AKS cluster ready but don't have workspace created yet, you can use AKS cluster VNet when creating the workspace. Use the AKS cluster VNet information when following the [create secure workspace](./tutorial-create-secure-workspace.md) tutorial. Once the workspace has been created, add a new private endpoint to your workspace as the last step. For all the above steps, it's important to ensure that all private endpoints should exist in the same AKS cluster VNet and have private DNS zone integration enabled.

Special notes for configuring a secure AKS inferencing environment:
  * Use system-assigned managed identity when creating workspace, as storage account with private endpoint only allows access with system-assigned managed identity.
  * When attaching AKS cluster to an HBI workspace, assign a system-assigned managed identity with both `Storage Blob Data Contributor` and `Storage Account Contributor` roles.
  * If you're using default ACR created by workspace, ensure you have the __premium SKU__ for ACR. Also enable the `Firewall exception` to allow trusted Microsoft services to access ACR.
  * If your workspace is also behind a VNet, follow the instructions in [securely connect to your workspace](./how-to-secure-workspace-vnet.md#securely-connect-to-your-workspace) to access the workspace.
  * For storage account private endpoint, make sure to enable `Allow Azure services on the trusted services list to access this storage account`.

>[!Note]
>
> If your AKS that is behind a VNet has been stopped and **restarted**, you need to:
> 1. First, follow the steps in [Stop and start an Azure Kubernetes Service (AKS) cluster](../aks/start-stop-cluster.md) to delete and recreate a private endpoint linked to this cluster. 
> 1. Then, reattach the Kubernetes computes attached from this AKS in your workspace. 
>
> Otherwise, the creation, update, and deletion of endpoints/deployments to this AKS cluster will fail.

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Secure online endpoints (inference)](how-to-secure-online-endpoint.md)
* [Enable studio functionality](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Use a firewall](how-to-access-azureml-behind-firewall.md)
* [Tutorial: Create a secure workspace](tutorial-create-secure-workspace.md)
* [Tutorial: Create a secure workspace using a template](tutorial-create-secure-workspace-template.md)
* [API platform network isolation](how-to-configure-network-isolation-with-v2.md)