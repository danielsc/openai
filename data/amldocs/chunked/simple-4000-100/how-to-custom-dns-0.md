
# How to use your workspace with a custom DNS server

When using an Azure Machine Learning workspace with a private endpoint, there are [several ways to handle DNS name resolution](../private-link/private-endpoint-dns.md). By default, Azure automatically handles name resolution for your workspace and private endpoint. If you instead __use your own custom DNS server__, you must manually create DNS entries or use conditional forwarders for the workspace.

> [!IMPORTANT]
> This article covers how to find the fully qualified domain names (FQDN) and IP addresses for these entries if you would like to manually register DNS records in your DNS solution. Additionally this article provides architecture recommendations for how to configure your custom DNS solution to automatically resolve FQDNs to the correct IP addresses. This article does NOT provide information on configuring the DNS records for these items. Consult the documentation for your DNS software for information on how to add records.

> [!TIP]
> This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:
>
> * [Virtual network overview](how-to-network-security-overview.md)
> * [Secure the workspace resources](how-to-secure-workspace-vnet.md)
> * [Secure the training environment](how-to-secure-training-vnet.md)
> * [Secure the inference environment](how-to-secure-inferencing-vnet.md)
> * [Enable studio functionality](how-to-enable-studio-virtual-network.md)
> * [Use a firewall](how-to-access-azureml-behind-firewall.md)
## Prerequisites

- An Azure Virtual Network that uses [your own DNS server](../virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances.md#name-resolution-that-uses-your-own-dns-server).

- An Azure Machine Learning workspace with a private endpoint. For more information, see [Create an Azure Machine Learning workspace](how-to-manage-workspace.md).

- Familiarity with using [Network isolation during training & inference](./how-to-network-security-overview.md).

- Familiarity with [Azure Private Endpoint DNS zone configuration](../private-link/private-endpoint-dns.md)

- Familiarity with [Azure Private DNS](../dns/private-dns-privatednszone.md)

- Optionally, [Azure CLI](/cli/azure/install-azure-cli) or [Azure PowerShell](/powershell/azure/install-az-ps).

## Automated DNS server integration

### Introduction

There are two common architectures to use automated DNS server integration with Azure Machine Learning:

* A custom [DNS server hosted in an Azure Virtual Network](#dns-vnet).
* A custom [DNS server hosted on-premises](#dns-on-premises), connected to Azure Machine Learning through ExpressRoute.

While your architecture may differ from these examples, you can use them as a reference point. Both example architectures provide troubleshooting steps that can help you identify components that may be misconfigured.

Another option is to modify the `hosts` file on the client that is connecting to the Azure Virtual Network (VNet) that contains your workspace. For more information, see the [Host file](#hosts) section.
### Workspace DNS resolution path

Access to a given Azure Machine Learning workspace via Private Link is done by communicating with the following Fully Qualified Domains (called the workspace FQDNs) listed below:

**Azure Public regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.azureml.ms```
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.cert.api.azureml.ms```
- ```<compute instance name>.<region the workspace was created in>.instances.azureml.ms```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.azure.net```
- ```<managed online endpoint name>.<region>.inference.ml.azure.com``` - Used by managed online endpoints

**Azure China 21Vianet regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.ml.azure.cn```
