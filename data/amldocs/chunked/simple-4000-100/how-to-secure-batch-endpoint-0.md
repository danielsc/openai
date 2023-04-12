
# Network isolation in batch endpoints

When deploying a machine learning model to a batch endpoint, you can secure their communication using private networks. This article explains the requirements to use batch endpoint in an environment secured by private networks.

## Prerequisites

* A secure Azure Machine Learning workspace. For more details about how to achieve it read [Create a secure workspace](tutorial-create-secure-workspace.md).
* For Azure Container Registry in private networks, please note that there are [some prerequisites about their configuration](how-to-secure-workspace-vnet.md#prerequisites).

    > [!WARNING]
    > Azure Container Registries with Quarantine feature enabled are not supported by the moment.

* Ensure blob, file, queue, and table private endpoints are configured for the storage accounts as explained at [Secure Azure storage accounts](how-to-secure-workspace-vnet.md#secure-azure-storage-accounts). Batch deployments require all the 4 to properly work.

## Securing batch endpoints

All the batch endpoints created inside of secure workspace are deployed as private batch endpoints by default. No further configuration is required.

> [!IMPORTANT]
> When working on a private link-enabled workspaces, batch endpoints can be created and managed using Azure Machine Learning studio. However, they can't be invoked from the UI in studio. Please use the Azure ML CLI v2 instead for job creation. For more details about how to use it see [Invoke the batch endpoint to start a batch scoring job](how-to-use-batch-endpoint.md#invoke-the-batch-endpoint-to-start-a-batch-job).

The following diagram shows how the networking looks like for batch endpoints when deployed in a private workspace:

:::image type="content" source="./media/how-to-secure-batch-endpoint/batch-vnet-peering.png" alt-text="Diagram that shows the high level architecture of a secure Azure Machine Learning workspace deployment.":::

In order to enable the jump host VM (or self-hosted agent VMs if using [Azure Bastion](../bastion/bastion-overview.md)) access to the resources in Azure Machine Learning VNET, the previous architecture uses virtual network peering to seamlessly connect these two virtual networks. Thus the two virtual networks appear as one for connectivity purposes. The traffic between VMs and Azure Machine Learning resources in peered virtual networks uses the Microsoft backbone infrastructure. Like traffic between them in the same network, traffic is routed through Microsoft's private network only.

## Securing batch deployment jobs

Azure Machine Learning batch deployments run on compute clusters. To secure batch deployment jobs, those compute clusters have to be deployed in a virtual network too.

1. Create an Azure Machine Learning [computer cluster in the virtual network](how-to-secure-training-vnet.md).
2. Ensure all related services have private endpoints configured in the network. Private endpoints are used for not only Azure Machine Learning workspace, but also its associated resources such as Azure Storage, Azure Key Vault, or Azure Container Registry. Azure Container Registry is a required service. While securing the Azure Machine Learning workspace with virtual networks, please note that there are [some prerequisites about Azure Container Registry](how-to-secure-workspace-vnet.md#prerequisites).
4. If your compute instance uses a public IP address, you must [Allow inbound communication](how-to-secure-training-vnet.md#compute-instancecluster-with-public-ip) so that management services can submit jobs to your compute resources.
    
    > [!TIP]
    > Compute cluster and compute instance can be created with or without a public IP address. If created with a public IP address, you get a load balancer with a public IP to accept the inbound access from Azure batch service and Azure Machine Learning service. You need to configure User Defined Routing (UDR) if you use a firewall. If created without a public IP, you get a private link service to accept the inbound access from Azure batch service and Azure Machine Learning service without a public IP.
