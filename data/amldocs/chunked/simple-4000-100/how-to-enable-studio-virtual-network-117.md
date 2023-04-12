When using Azure Data Lake Storage Gen1 as a datastore, you can only use POSIX-style access control lists. You can assign the workspace's managed identity access to resources just like any other security principal. For more information, see [Access control in Azure Data Lake Storage Gen1](../data-lake-store/data-lake-store-access-control.md).

## Datastore: Azure Data Lake Storage Gen2

When using Azure Data Lake Storage Gen2 as a datastore, you can use both Azure RBAC and POSIX-style access control lists (ACLs) to control data access inside of a virtual network.

__To use Azure RBAC__, follow the steps in the [Datastore: Azure Storage Account](#datastore-azure-storage-account) section of this article. Data Lake Storage Gen2 is based on Azure Storage, so the same steps apply when using Azure RBAC.

__To use ACLs__, the workspace's managed identity can be assigned access just like any other security principal. For more information, see [Access control lists on files and directories](../storage/blobs/data-lake-storage-access-control.md#access-control-lists-on-files-and-directories).

## Datastore: Azure SQL Database

To access data stored in an Azure SQL Database with a managed identity, you must create a SQL contained user that maps to the managed identity. For more information on creating a user from an external provider, see [Create contained users mapped to Azure AD identities](/azure/azure-sql/database/authentication-aad-configure#create-contained-users-mapped-to-azure-ad-identities).

After you create a SQL contained user, grant permissions to it by using the [GRANT T-SQL command](/sql/t-sql/statements/grant-object-permissions-transact-sql).

## Intermediate component output

When using the Azure Machine Learning designer intermediate component output, you can specify the output location for any component in the designer. Use this to store intermediate datasets in separate location for security, logging, or auditing purposes. To specify output, use the following steps:

1. Select the component whose output you'd like to specify.
1. In the component settings pane that appears to the right, select __Output settings__.
1. Specify the datastore you want to use for each component output.

Make sure that you have access to the intermediate storage accounts in your virtual network. Otherwise, the pipeline will fail.

[Enable managed identity authentication](#enable-managed-identity) for intermediate storage accounts to visualize output data.
## Access the studio from a resource inside the VNet

If you are accessing the studio from a resource inside of a virtual network (for example, a compute instance or virtual machine), you must allow outbound traffic from the virtual network to the studio. 

For example, if you are using network security groups (NSG) to restrict outbound traffic, add a rule to a __service tag__ destination of __AzureFrontDoor.Frontend__.

## Firewall settings

Some storage services, such as Azure Storage Account, have firewall settings that apply to the public endpoint for that specific service instance. Usually this setting allows you to allow/disallow access from specific IP addresses from the public internet. __This is not supported__ when using Azure Machine Learning studio. It is supported when using the Azure Machine Learning SDK or CLI.

> [!TIP]
> Azure Machine Learning studio is supported when using the Azure Firewall service. For more information, see [Use your workspace behind a firewall](how-to-access-azureml-behind-firewall.md).
## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the workspace resources](how-to-secure-workspace-vnet.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Secure the inference environment](how-to-secure-inferencing-vnet.md)
* [Use custom DNS](how-to-custom-dns.md)
* [Use a firewall](how-to-access-azureml-behind-firewall.md)
