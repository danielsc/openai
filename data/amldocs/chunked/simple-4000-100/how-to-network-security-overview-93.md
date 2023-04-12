1. Add the following services to the virtual network by using _either_ a __service endpoint__ or a __private endpoint__. Also allow trusted Microsoft services to access these services:

    | Service | Endpoint information | Allow trusted information |
    | ----- | ----- | ----- |
    | __Azure Key Vault__| [Service endpoint](../key-vault/general/overview-vnet-service-endpoints.md)</br>[Private endpoint](../key-vault/general/private-link-service.md) | [Allow trusted Microsoft services to bypass this firewall](how-to-secure-workspace-vnet.md#secure-azure-key-vault) |
    | __Azure Storage Account__ | [Service and private endpoint](how-to-secure-workspace-vnet.md?tabs=se#secure-azure-storage-accounts)</br>[Private endpoint](how-to-secure-workspace-vnet.md?tabs=pe#secure-azure-storage-accounts) | [Grant access from Azure resource instances](../storage/common/storage-network-security.md#grant-access-from-azure-resource-instances)</br>**or**</br>[Grant access to trusted Azure services](../storage/common/storage-network-security.md#grant-access-to-trusted-azure-services) |
    | __Azure Container Registry__ | [Private endpoint](../container-registry/container-registry-private-link.md) | [Allow trusted services](../container-registry/allow-access-trusted-services.md) |


:::image type="content" source="./media/how-to-network-security-overview/secure-workspace-resources.svg" alt-text="Diagram showing how the workspace and associated resources communicate inside a VNet.":::

For detailed instructions on how to complete these steps, see [Secure an Azure Machine Learning workspace](how-to-secure-workspace-vnet.md). 

### Limitations

Securing your workspace and associated resources within a virtual network have the following limitations:
- All resources must be behind the same VNet. However, subnets within the same VNet are allowed.

## Secure the training environment

In this section, you learn how to secure the training environment in Azure Machine Learning. You also learn how Azure Machine Learning completes a training job to understand how the network configurations work together.

To secure the training environment, use the following steps:

1. Create an Azure Machine Learning [compute instance and computer cluster in the virtual network](how-to-secure-training-vnet.md) to run the training job.
1. If your compute cluster or compute instance uses a public IP address, you must [Allow inbound communication](how-to-secure-training-vnet.md) so that management services can submit jobs to your compute resources. 

    > [!TIP]
    > Compute cluster and compute instance can be created with or without a public IP address. If created with a public IP address, you get a load balancer with a public IP to accept the inbound access from Azure batch service and Azure Machine Learning service. You need to configure User Defined Routing (UDR) if you use a firewall. If created without a public IP, you get a private link service to accept the inbound access from Azure batch service and Azure Machine Learning service without a public IP.

:::image type="content" source="./media/how-to-network-security-overview/secure-training-environment.svg" alt-text="Diagram showing how to secure managed compute clusters and instances.":::

For detailed instructions on how to complete these steps, see [Secure a training environment](how-to-secure-training-vnet.md). 

### Example training job submission 

In this section, you learn how Azure Machine Learning securely communicates between services to submit a training job. This shows you how all your configurations work together to secure communication.

1. The client uploads training scripts and training data to storage accounts that are secured with a service or private endpoint.

1. The client submits a training job to the Azure Machine Learning workspace through the private endpoint.

1. Azure Batch service receives the job from the workspace. It then submits the training job to the compute environment through the public load balancer for the compute resource. 
