
# Set up authentication for Azure Machine Learning resources and workflows

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]
	
> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK you are using:"]
> * [v1](./v1/how-to-setup-authentication.md)
> * [v2 (current version)](how-to-setup-authentication.md)

Learn how to set up authentication to your Azure Machine Learning workspace from the Azure CLI or Azure Machine Learning SDK v2. Authentication to your Azure Machine Learning workspace is based on __Azure Active Directory__ (Azure AD) for most things. In general, there are four authentication workflows that you can use when connecting to the workspace:

* __Interactive__: You use your account in Azure Active Directory to either directly authenticate, or to get a token that is used for authentication. Interactive authentication is used during _experimentation and iterative development_. Interactive authentication enables you to control access to resources (such as a web service) on a per-user basis.

* __Service principal__: You create a service principal account in Azure Active Directory, and use it to authenticate or get a token. A service principal is used when you need an _automated process to authenticate_ to the service without requiring user interaction. For example, a continuous integration and deployment script that trains and tests a model every time the training code changes.

* __Azure CLI session__: You use an active Azure CLI session to authenticate. The Azure CLI extension for Machine Learning (the `ml` extension or CLI v2) is a command line tool for working with Azure Machine Learning. You can sign in to Azure via the Azure CLI on your local workstation, without storing credentials in Python code or prompting the user to authenticate. Similarly, you can reuse the same scripts as part of continuous integration and deployment pipelines, while authenticating the Azure CLI with a service principal identity.

* __Managed identity__: When using the Azure Machine Learning SDK v2 _on a compute instance_ or _on an Azure Virtual Machine_, you can use a managed identity for Azure. This workflow allows the VM to connect to the workspace using the managed identity, without storing credentials in Python code or prompting the user to authenticate. Azure Machine Learning compute clusters can also be configured to use a managed identity to access the workspace when _training models_.

Regardless of the authentication workflow used, Azure role-based access control (Azure RBAC) is used to scope the level of access (authorization) allowed to the resources. For example, an admin or automation process might have access to create a compute instance, but not use it, while a data scientist could use it, but not delete or create it. For more information, see [Manage access to Azure Machine Learning workspace](how-to-assign-roles.md).

## Prerequisites

* Create an [Azure Machine Learning workspace](how-to-manage-workspace.md).
* [Configure your development environment](how-to-configure-environment.md) or use a [Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md) and install the [Azure Machine Learning SDK v2](https://aka.ms/sdk-v2-install).

* Install the [Azure CLI](/cli/azure/install-azure-cli).

## Azure Active Directory

All the authentication workflows for your workspace rely on Azure Active Directory. If you want users to authenticate using individual accounts, they must have accounts in your Azure AD. If you want to use service principals, they must exist in your Azure AD. Managed identities are also a feature of Azure AD. 

For more on Azure AD, see [What is Azure Active Directory authentication](..//active-directory/authentication/overview-authentication.md).

Once you've created the Azure AD accounts, see [Manage access to Azure Machine Learning workspace](how-to-assign-roles.md) for information on granting them access to the workspace and other operations in Azure Machine Learning.
