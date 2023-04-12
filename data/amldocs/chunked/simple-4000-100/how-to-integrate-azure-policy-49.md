Landing zones are an architectural pattern to set up Azure environments that accounts for scale, governance, security, and productivity. A data landing zone is an administator-configured environment that an application team uses to host a data and analytics workload.

The purpose of the landing zone is to ensure when a team starts in the Azure environment, all infrastructure configuration work is done. For instance, security controls are set up in compliance with organizational standards and network connectivity is set up.

Using the landing zones pattern, machine learning teams can be enabled to self-service deploy and manage their own resources. By use of Azure policy, as an administrator you can audit and manage Azure resources for compliance and make sure workspaces are compliant to meet your requirements. 

Azure Machine Learning integrates with [data landing zones](https://github.com/Azure/data-landing-zone) in the [Cloud Adoption Framework data management and analytics scenario](/azure/cloud-adoption-framework/scenarios/data-management/). This reference implementation provides an optimized environment to migrate machine learning workloads onto and includes policies for Azure Machine Learning preconfigured.

## Configure built-in policies

### Workspace encryption with customer-managed key

Controls whether a workspace should be encrypted with a customer-managed key, or using a Microsoft-managed key to encrypt metrics and metadata. For more information on using customer-managed key, see the [Azure Cosmos DB](concept-data-encryption.md#azure-cosmos-db) section of the data encryption article.

To configure this policy, set the effect parameter to __audit__ or __deny__. If set to __audit__, you can create a workspace without a customer-managed key and a warning event is created in the activity log.

If the policy is set to __deny__, then you cannot create a workspace unless it specifies a customer-managed key. Attempting to create a workspace without a customer-managed key results in an error similar to `Resource 'clustername' was disallowed by policy` and creates an error in the activity log. The policy identifier is also returned as part of this error.

### Workspace should use private link

Controls whether a workspace should use Azure Private Link to communicate with Azure Virtual Network. For more information on using private link, see [Configure private link for a workspace](how-to-configure-private-link.md).

To configure this policy, set the effect parameter to __audit__ or __deny__. If set to __audit__, you can create a workspace without using private link and a warning event is created in the activity log.

If the policy is set to __deny__, then you cannot create a workspace unless it uses a private link. Attempting to create a workspace without a private link results in an error. The error is also logged in the activity log. The policy identifier is returned as part of this error.

### Workspace should use private endpoint

Configures a workspace to create a private endpoint within the specified subnet of an Azure Virtual Network.

To configure this policy, set the effect parameter to __DeployIfNotExists__. Set the __privateEndpointSubnetID__ to the Azure Resource Manager ID of the subnet.

### Workspace should use private DNS zones

Configures a workspace to use a private DNS zone, overriding the default DNS resolution for a private endpoint.

To configure this policy, set the effect parameter to __DeployIfNotExists__. Set the __privateDnsZoneId__ to the Azure Resource Manager ID of the private DNS zone to use. 

### Workspace should use user-assigned managed identity

Controls whether a workspace is created using a system-assigned managed identity (default) or a user-assigned managed identity. The managed identity for the workspace is used to access associated resources such as Azure Storage, Azure Container Registry, Azure Key Vault, and Azure Application Insights. For more information, see [Use managed identities with Azure Machine Learning](how-to-identity-based-service-authentication.md).
