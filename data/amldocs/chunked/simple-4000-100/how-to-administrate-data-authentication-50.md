| Access from UI | Yes | Workspace MSI |
| Access from UI | No | User's Identity |
| Access from Job | Yes/No | Compute MSI |
| Access from Notebook | Yes/No | User's identity |


Data access is complex and it's important to recognize that there are many pieces to it. For example, accessing data from Azure Machine Learning studio is different than using the SDK. When using the SDK on your local development environment, you're directly accessing data in the cloud. When using studio, you aren't always directly accessing the data store from your client. Studio relies on the workspace to access data on your behalf.

> [!TIP]
> If you need to access data from outside Azure Machine Learning, such as using Azure Storage Explorer, *user* identity is probably what is used. Consult the documentation for the tool or service you are using for specific information. For more information on how Azure Machine Learning works with data, see [Setup authentication between AzureML and other services](how-to-identity-based-service-authentication.md).

## Azure Storage Account

When using an Azure Storage Account from Azure Machine Learning studio, you must add the managed identity of the workspace to the following Azure RBAC roles for the storage account:

* [Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader)
* If the storage account uses a private endpoint to connect to the VNet, you must grant the managed identity the [Reader](../role-based-access-control/built-in-roles.md#reader) role for the storage account private endpoint.

For more information, see [Use Azure Machine Learning studio in an Azure Virtual Network](how-to-enable-studio-virtual-network.md).

See the following sections for information on limitations when using Azure Storage Account with your workspace in a VNet.

### Secure communication with Azure Storage Account 

To secure communication between Azure Machine Learning and Azure Storage Accounts, configure storage to [Grant access to trusted Azure services](../storage/common/storage-network-security.md#grant-access-to-trusted-azure-services).

### Azure Storage firewall

When an Azure Storage account is behind a virtual network, the storage firewall can normally be used to allow your client to directly connect over the internet. However, when using studio it isn't your client that connects to the storage account; it's the Azure Machine Learning service that makes the request. The IP address of the service isn't documented and changes frequently. __Enabling the storage firewall will not allow studio to access the storage account in a VNet configuration__.

### Azure Storage endpoint type

When the workspace uses a private endpoint and the storage account is also in the VNet, there are extra validation requirements when using studio:

* If the storage account uses a __service endpoint__, the workspace private endpoint and storage service endpoint must be in the same subnet of the VNet.
* If the storage account uses a __private endpoint__, the workspace private endpoint and storage service endpoint must be in the same VNet. In this case, they can be in different subnets.

## Azure Data Lake Storage Gen1

When using Azure Data Lake Storage Gen1 as a datastore, you can only use POSIX-style access control lists. You can assign the workspace's managed identity access to resources just like any other security principal. For more information, see [Access control in Azure Data Lake Storage Gen1](../data-lake-store/data-lake-store-access-control.md).

## Azure Data Lake Storage Gen2

When using Azure Data Lake Storage Gen2 as a datastore, you can use both Azure RBAC and POSIX-style access control lists (ACLs) to control data access inside of a virtual network.

__To use Azure RBAC__, follow the steps in the [Datastore: Azure Storage Account](how-to-enable-studio-virtual-network.md#datastore-azure-storage-account) section of the 'Use Azure Machine Learning studio in an Azure Virtual Network' article. Data Lake Storage Gen2 is based on Azure Storage, so the same steps apply when using Azure RBAC.
