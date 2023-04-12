

# Manage access to an Azure Machine Learning workspace

In this article, you learn how to manage access (authorization) to an Azure Machine Learning workspace. [Azure role-based access control (Azure RBAC)](../role-based-access-control/overview.md) is used to manage access to Azure resources, such as the ability to create new resources or use existing ones. Users in your Azure Active Directory (Azure AD) are assigned specific roles, which grant access to resources. Azure provides both built-in roles and the ability to create custom roles.

> [!TIP]
> While this article focuses on Azure Machine Learning, individual services that Azure ML relies on provide their own RBAC settings. For example, using the information in this article, you can configure who can submit scoring requests to a model deployed as a web service on Azure Kubernetes Service. But Azure Kubernetes Service provides its own set of Azure roles. For service specific RBAC information that may be useful with Azure Machine Learning, see the following links:
>
> * [Control access to Azure Kubernetes cluster resources](../aks/azure-ad-rbac.md)
> * [Use Azure RBAC for Kubernetes authorization](../aks/manage-azure-rbac.md)
> * [Use Azure RBAC for access to blob data](../storage/blobs/assign-azure-role-data-access.md)

> [!WARNING]
> Applying some roles may limit UI functionality in Azure Machine Learning studio for other users. For example, if a user's role does not have the ability to create a compute instance, the option to create a compute instance will not be available in studio. This behavior is expected, and prevents the user from attempting operations that would return an access denied error.

## Default roles

Azure Machine Learning workspaces have a five built-in roles that are available by default. When adding users to a workspace, they can be assigned one of the built-in roles described below.

| Role | Access level |
| --- | --- |
| **AzureML Data Scientist** | Can perform all actions within an Azure Machine Learning workspace, except for creating or deleting compute resources and modifying the workspace itself. |
| **AzureML Compute Operator** | Can create, manage and access compute resources within a workspace.|
| **Reader** | Read-only actions in the workspace. Readers can list and view assets, including [datastore](how-to-access-data.md) credentials, in a workspace. Readers can't create or update these assets. |
| **Contributor** | View, create, edit, or delete (where applicable) assets in a workspace. For example, contributors can create an experiment, create or attach a compute cluster, submit a run, and deploy a web service. |
| **Owner** | Full access to the workspace, including the ability to view, create, edit, or delete (where applicable) assets in a workspace. Additionally, you can change role assignments. |

In addition, [Azure Machine Learning registries](how-to-manage-registries.md) have a **AzureML Registry User** role that can be assigned to a registry resource to grant data scientists user-level prermissions. For administrator-level permissions to create or delete registries, use **Contributor** or **Owner** role.

| Role | Access level |
| --- | --- |
| **AzureML Registry User** | Can get registries, and read, write and delete assets within them. Cannot create new registry resources or delete them. |

You can combine the roles to grant different levels of access. For example, you can grant a workspace user both **AzureML Data Scientist** and **Azure ML Compute Operator** roles to permit the user to perform experiments while creating computes in a self-service manner.

> [!IMPORTANT]
> Role access can be scoped to multiple levels in Azure. For example, someone with owner access to a workspace may not have owner access to the resource group that contains the workspace. For more information, see [How Azure RBAC works](../role-based-access-control/overview.md#how-azure-rbac-works).


## Manage workspace access

If you're an owner of a workspace, you can add and remove roles for the workspace. You can also assign roles to users. Use the following links to discover how to manage access:
