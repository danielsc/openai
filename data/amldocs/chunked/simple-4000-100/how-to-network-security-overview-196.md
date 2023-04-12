Microsoft Sentinel can automatically create a workspace for you if you are OK with a public endpoint. In this configuration, the security operations center (SOC) analysts and system administrators connect to notebooks in your workspace through Sentinel.

For information on this process, see [Create an Azure ML workspace from Microsoft Sentinel](../sentinel/notebooks-hunt.md?tabs=public-endpoint#create-an-azure-ml-workspace-from-microsoft-sentinel)

:::image type="content" source="./media/how-to-network-security-overview/common-public-endpoint-deployment.svg" alt-text="Diagram showing Microsoft Sentinel public connection.":::

### Private endpoint

If you want to secure your workspace and associated resources in a VNet, you must create the Azure Machine Learning workspace first. You must also create a virtual machine 'jump box' in the same VNet as your workspace, and enable Azure Bastion connectivity to it. Similar to the public configuration, SOC analysts and administrators can connect using Microsoft Sentinel, but some operations must be performed using Azure Bastion to connect to the VM.

For more information on this configuration, see [Create an Azure ML workspace from Microsoft Sentinel](../sentinel/notebooks-hunt.md?tabs=private-endpoint#create-an-azure-ml-workspace-from-microsoft-sentinel)

:::image type="content" source="./media/how-to-network-security-overview/private-endpoint-deploy-bastion.svg" alt-text="Daigram showing Microsoft Sentinel connection through a VNet.":::

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Secure the workspace resources](how-to-secure-workspace-vnet.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Secure the inference environment](how-to-secure-inferencing-vnet.md)
* [Enable studio functionality](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Use a firewall](how-to-access-azureml-behind-firewall.md)
* [API platform network isolation](how-to-configure-network-isolation-with-v2.md)
