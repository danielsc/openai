1. Azure Batch service receives the job from the workspace. It then submits the training job to the compute environment through the public load balancer for the compute resource. 

1. The compute resource receives the job and begins training. The compute resource uses information stored in key vault to access storage accounts to download training files and upload output.

:::image type="content" source="./media/how-to-network-security-overview/secure-training-job-submission.svg" alt-text="Diagram showing the secure training job submission workflow.":::
### Limitations

- Azure Compute Instance and Azure Compute Clusters must be in the same VNet, region, and subscription as the workspace and its associated resources. 

## Secure the inferencing environment

You can enable network isolation for managed online endpoints to secure the following network traffic:

* Inbound scoring requests.
* Outbound communication with the workspace, Azure Container Registry, and Azure Blob Storage.

For more information, see [Enable network isolation for managed online endpoints](how-to-secure-online-endpoint.md).

## Optional: Enable public access

You can secure the workspace behind a VNet using a private endpoint and still allow access over the public internet. The initial configuration is the same as [securing the workspace and associated resources](#secure-the-workspace-and-associated-resources). 

After securing the workspace with a private endpoint, use the following steps to enable clients to develop remotely using either the SDK or Azure Machine Learning studio:

1. [Enable public access](how-to-configure-private-link.md#enable-public-access) to the workspace.
1. [Configure the Azure Storage firewall](../storage/common/storage-network-security.md?toc=%2fazure%2fstorage%2fblobs%2ftoc.json#grant-access-from-an-internet-ip-range) to allow communication with the IP address of clients that connect over the public internet.

## Optional: enable studio functionality

If your storage is in a VNet, you must use extra configuration steps to enable full functionality in studio. By default, the following features are disabled:

* Preview data in the studio.
* Visualize data in the designer.
* Deploy a model in the designer.
* Submit an AutoML experiment.
* Start a labeling project.

To enable full studio functionality, see [Use Azure Machine Learning studio in a virtual network](how-to-enable-studio-virtual-network.md).

### Limitations

[ML-assisted data labeling](how-to-create-image-labeling-projects.md#use-ml-assisted-data-labeling) doesn't support a default storage account behind a virtual network. Instead, use a storage account other than the default for ML assisted data labeling. 

> [!TIP]
> As long as it is not the default storage account, the account used by data labeling can be secured behind the virtual network. 

## Configure firewall settings

Configure your firewall to control traffic between your Azure Machine Learning workspace resources and the public internet. While we recommend Azure Firewall, you can use other firewall products. 

For more information on firewall settings, see [Use workspace behind a Firewall](how-to-access-azureml-behind-firewall.md).

## Custom DNS

If you need to use a custom DNS solution for your virtual network, you must add host records for your workspace.

For more information on the required domain names and IP addresses, see [how to use a workspace with a custom DNS server](how-to-custom-dns.md).

## Microsoft Sentinel

Microsoft Sentinel is a security solution that can integrate with Azure Machine Learning. For example, using Jupyter notebooks provided through Azure Machine Learning. For more information, see [Use Jupyter notebooks to hunt for security threats](../sentinel/notebooks.md).

### Public access

Microsoft Sentinel can automatically create a workspace for you if you are OK with a public endpoint. In this configuration, the security operations center (SOC) analysts and system administrators connect to notebooks in your workspace through Sentinel.
