Controls whether a workspace is created using a system-assigned managed identity (default) or a user-assigned managed identity. The managed identity for the workspace is used to access associated resources such as Azure Storage, Azure Container Registry, Azure Key Vault, and Azure Application Insights. For more information, see [Use managed identities with Azure Machine Learning](how-to-identity-based-service-authentication.md).

To configure this policy, set the effect parameter to __audit__, __deny__, or __disabled__. If set to __audit__, you can create a workspace without specifying a user-assigned managed identity. A system-assigned identity is used and a warning event is created in the activity log.

If the policy is set to __deny__, then you cannot create a workspace unless you provide a user-assigned identity during the creation process. Attempting to create a workspace without providing a user-assigned identity results in an error. The error is also logged to the activity log. The policy identifier is returned as part of this error.

### Workspace should disable public network access

Controls whether a workspace should disable network access from the public internet.

To configure this policy, set thee effect parameter to __audit__, __deny__, or __disabled__. If set to __audit__, you can create a workspace with public access and a warning event is created in the activity log.

If the policy is set to __deny__, then you cannot create a workspace that allows network access from the public internet.

### Disable local authentication

Controls whether an Azure Machine Learning compute cluster or instance should disable local authentication (SSH).

To configure this policy, set the effect parameter to __audit__, __deny__, or __disabled__. If set to __audit__, you can create a compute with SSH enabled and a warning event is created in the activity log.

If the policy is set to __deny__, then you cannot create a compute unless SSH is disabled. Attempting to create a compute with SSH enabled results in an error. The error is also logged in the activity log. The policy identifier is returned as part of this error.

### Modify/disable local authentication

Modifies any Azure Machine Learning compute cluster or instance creation request to disable local authentication (SSH).

To configure this policy, set the effect parameter to __Modify__ or __Disabled__. If set __Modify__, any creation of a compute cluster or instance within the scope where the policy applies will automatically have local authentication disabled.

### Compute cluster and instance is behind virtual network

Controls auditing of compute cluster and instance resources behind a virtual network.

To configure this policy, set the effect parameter to __audit__ or __disabled__. If set to __audit__, you can create a compute that is not configured behind a virtual network and a warning event is created in the activity log.

## Next steps

* [Azure Policy documentation](../governance/policy/overview.md)
* [Built-in policies for Azure Machine Learning](policy-reference.md)
* [Working with security policies with Microsoft Defender for Cloud](../security-center/tutorial-security-policy.md)
* The [Cloud Adoption Framework scenario for data management and analytics](/azure/cloud-adoption-framework/scenarios/data-management/) outlines considerations in running data and analytics workloads in the cloud.
* [Cloud Adoption Framework data landing zones](https://github.com/Azure/data-landing-zone) provide a reference implementation for managing data and analytics workloads in Azure.
* [Learn how to use policy to integrate Azure Private Link with Azure Private DNS zones](/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale), to manage private link configuration for the workspace and dependent resources.
