You can provision the workspace to use user-assigned managed identity, and grant the managed identity additional roles, for example to access your own Azure Container Registry for base Docker images. You can also configure managed identities for use with Azure Machine Learning compute cluster. This managed identity is independent of workspace managed identity. With a compute cluster, the managed identity is used to access resources such as secured datastores that the user running the training job may not have access to. For more information, see [Use managed identities for access control](how-to-identity-based-service-authentication.md).

> [!TIP]
> There are some exceptions to the use of Azure AD and Azure RBAC within Azure Machine Learning:
> * You can optionally enable __SSH__ access to compute resources such as Azure Machine Learning compute instance and compute cluster. SSH access is based on public/private key pairs, not Azure AD. SSH access is not governed by Azure RBAC.
> * You can authenticate to models deployed as online endpoints using __key__ or __token__-based authentication. Keys are static strings, while tokens are retrieved using an Azure AD security object. For more information, see [How to authenticate online endpoints](how-to-authenticate-online-endpoint.md).

For more information, see the following articles:
* [Authentication for Azure Machine Learning workspace](how-to-setup-authentication.md)
* [Manage access to Azure Machine Learning](how-to-assign-roles.md)
* [Connect to storage services](how-to-access-data.md)
* [Use Azure Key Vault for secrets when training](how-to-use-secrets-in-runs.md)
* [Use Azure AD managed identity with Azure Machine Learning](how-to-identity-based-service-authentication.md)

## Network security and isolation

To restrict network access to Azure Machine Learning resources, you can use [Azure Virtual Network (VNet)](../virtual-network/virtual-networks-overview.md). VNets allow you to create network environments that are partially, or fully, isolated from the public internet. This reduces the attack surface for your solution, as well as the chances of data exfiltration.

You might use a virtual private network (VPN) gateway to connect individual clients, or your own network, to the VNet

The Azure Machine Learning workspace can use [Azure Private Link](../private-link/private-link-overview.md) to create a private endpoint behind the VNet. This provides a set of private IP addresses that can be used to access the workspace from within the VNet. Some of the services that Azure Machine Learning relies on can also use Azure Private Link, but some rely on network security groups or user-defined routing.

For more information, see the following documents:

* [Virtual network isolation and privacy overview](how-to-network-security-overview.md)
* [Secure workspace resources](how-to-secure-workspace-vnet.md)
* [Secure training environment](how-to-secure-training-vnet.md)
* [Secure inference environment](./how-to-secure-inferencing-vnet.md)
* [Use studio in a secured virtual network](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Configure firewall](how-to-access-azureml-behind-firewall.md)

<a id="encryption-at-rest"></a><a id="azure-blob-storage"></a>

## Data encryption

Azure Machine Learning uses a variety of compute resources and data stores on the Azure platform. To learn more about how each of these supports data encryption at rest and in transit, see [Data encryption with Azure Machine Learning](concept-data-encryption.md).

## Data exfiltration prevention (preview)

Azure Machine Learning has several inbound and outbound network dependencies. Some of these dependencies can expose a data exfiltration risk by malicious agents within your organization. These risks are associated with the outbound requirements to Azure Storage, Azure Front Door, and Azure Monitor. For recommendations on mitigating this risk, see the [Azure Machine Learning data exfiltration prevention](how-to-prevent-data-loss-exfiltration.md) article.
