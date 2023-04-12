If you don't want to use the default outbound rules and you do want to limit the outbound access of your virtual network, you must allow access to Azure Container Registry. For example, make sure that your Network Security Groups (NSG) contains a rule that allows access to the __AzureContainerRegistry.RegionName__ service tag where `{RegionName} is the name of an Azure region.

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the workspace resources](how-to-secure-workspace-vnet.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Enable studio functionality](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Use a firewall](how-to-access-azureml-behind-firewall.md)
