
# Enterprise security and governance for Azure Machine Learning

In this article, you'll learn about security and governance features available for Azure Machine Learning. These features are useful for administrators, DevOps, and MLOps who want to create a secure configuration that is compliant with your companies policies. With Azure Machine Learning and the Azure platform, you can:

* Restrict access to resources and operations by user account or groups
* Restrict incoming and outgoing network communications
* Encrypt data in transit and at rest
* Scan for vulnerabilities
* Apply and audit configuration policies

## Restrict access to resources and operations

[Azure Active Directory (Azure AD)](../active-directory/fundamentals/active-directory-whatis.md) is the identity service provider for Azure Machine Learning. It allows you to create and manage the security objects (user, group, service principal, and managed identity) that are used to _authenticate_ to Azure resources. Multi-factor authentication is supported if Azure AD is configured to use it.

Here's the authentication process for Azure Machine Learning using multi-factor authentication in Azure AD:

1. The client signs in to Azure AD and gets an Azure Resource Manager token.
1. The client presents the token to Azure Resource Manager and to all Azure Machine Learning.
1. Azure Machine Learning provides a Machine Learning service token to the user compute target (for example, Azure Machine Learning compute cluster). This token is used by the user compute target to call back into the Machine Learning service after the job is complete. The scope is limited to the workspace.

[![Authentication in Azure Machine Learning](media/concept-enterprise-security/authentication.png)](media/concept-enterprise-security/authentication.png#lightbox)

Each workspace has an associated system-assigned [managed identity](../active-directory/managed-identities-azure-resources/overview.md) that has the same name as the workspace. This managed identity is used to securely access resources used by the workspace. It has the following Azure RBAC permissions on associated resources:

| Resource | Permissions |
| ----- | ----- |
| Workspace | Contributor |
| Storage account | Storage Blob Data Contributor |
| Key vault | Access to all keys, secrets, certificates |
| Azure Container Registry | Contributor |
| Resource group that contains the workspace | Contributor |

The system-assigned managed identity is used for internal service-to-service authentication between Azure Machine Learning and other Azure resources. The identity token is not accessible to users and cannot be used by them to gain access to these resources. Users can only access the resources through [Azure Machine Learning control and data plane APIs](how-to-assign-roles.md), if they have sufficient RBAC permissions.

We don't recommend that admins revoke the access of the managed identity to the resources mentioned in the preceding table. You can restore access by using the [resync keys operation](how-to-change-storage-access-key.md).

> [!NOTE]
> If your Azure Machine Learning workspaces has compute targets (compute cluster, compute instance, Azure Kubernetes Service, etc.) that were created __before May 14th, 2021__, you may also have an additional Azure Active Directory account. The account name starts with `Microsoft-AzureML-Support-App-` and has contributor-level access to your subscription for every workspace region.
> 
> If your workspace does not have an Azure Kubernetes Service (AKS) attached, you can safely delete this Azure AD account. 
> 
> If your workspace has attached AKS clusters, _and they were created before May 14th, 2021_, __do not delete this Azure AD account__. In this scenario, you must first delete and recreate the AKS cluster before you can delete the Azure AD account.

You can provision the workspace to use user-assigned managed identity, and grant the managed identity additional roles, for example to access your own Azure Container Registry for base Docker images. You can also configure managed identities for use with Azure Machine Learning compute cluster. This managed identity is independent of workspace managed identity. With a compute cluster, the managed identity is used to access resources such as secured datastores that the user running the training job may not have access to. For more information, see [Use managed identities for access control](how-to-identity-based-service-authentication.md).
