    For more information, see the [Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) built-in role.

1. __Grant the workspace managed identity the 'Reader' role for storage private endpoints__. If your storage service uses a __private endpoint__, grant the workspace's managed identity __Reader__ access to the private endpoint. The workspace's managed identity in Azure AD has the same name as your Azure Machine Learning workspace.

    > [!TIP]
    > Your storage account may have multiple private endpoints. For example, one storage account may have separate private endpoint for blob, file, and dfs (Azure Data Lake Storage Gen2). Add the managed identity to all these endpoints.

    For more information, see the [Reader](../role-based-access-control/built-in-roles.md#reader) built-in role.

   <a id='enable-managed-identity'></a>
1. __Enable managed identity authentication for default storage accounts__. Each Azure Machine Learning workspace has two default storage accounts, a default blob storage account and a default file store account, which are defined when you create your workspace. You can also set new defaults in the __Datastore__ management page.

    ![Screenshot showing where default datastores can be found](./media/how-to-enable-studio-virtual-network/default-datastores.png)

    The following table describes why managed identity authentication is used for your workspace default storage accounts.

    |Storage account  | Notes  |
    |---------|---------|
    |Workspace default blob storage| Stores model assets from the designer. Enable managed identity authentication on this storage account to deploy models in the designer. If managed identity authentication is disabled, the user's identity is used to access data stored in the blob. <br> <br> You can visualize and run a designer pipeline if it uses a non-default datastore that has been configured to use managed identity. However, if you try to deploy a trained model without managed identity enabled on the default datastore, deployment will fail regardless of any other datastores in use.|
    |Workspace default file store| Stores AutoML experiment assets. Enable managed identity authentication on this storage account to submit AutoML experiments. |

1. __Configure datastores to use managed identity authentication__. After you add an Azure storage account to your virtual network with either a [service endpoint](how-to-secure-workspace-vnet.md?tabs=se#secure-azure-storage-accounts) or [private endpoint](how-to-secure-workspace-vnet.md?tabs=pe#secure-azure-storage-accounts), you must configure your datastore to use [managed identity](../active-directory/managed-identities-azure-resources/overview.md) authentication. Doing so lets the studio access data in your storage account.

    Azure Machine Learning uses [datastore](concept-data.md#datastore) to connect to storage accounts. When creating a new datastore, use the following steps to configure a datastore to use managed identity authentication:

    1. In the studio, select __Datastores__.

    1. To update an existing datastore, select the datastore and select __Update credentials__.

        To create a new datastore, select __+ New datastore__.

    1. In the datastore settings, select __Yes__ for  __Use workspace managed identity for data preview and profiling in Azure Machine Learning studio__.

        ![Screenshot showing how to enable managed workspace identity](./media/how-to-enable-studio-virtual-network/enable-managed-identity.png)

    1. In the __Networking__ settings for the __Azure Storage Account__, add the Microsoft.MachineLearningService/workspaces __Resource type__, and set the __Instance name__ to the workspace. 

    These steps add the workspace's managed identity as a __Reader__ to the new storage service using Azure RBAC. __Reader__ access allows the workspace to view the resource, but not make changes.

## Datastore: Azure Data Lake Storage Gen1

When using Azure Data Lake Storage Gen1 as a datastore, you can only use POSIX-style access control lists. You can assign the workspace's managed identity access to resources just like any other security principal. For more information, see [Access control in Azure Data Lake Storage Gen1](../data-lake-store/data-lake-store-access-control.md).
