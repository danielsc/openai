To help ensure that you securely connect to your storage service on Azure, Azure Machine Learning requires that you have permission to access the corresponding data storage.
 
> [!WARNING]
>  Cross tenant access to storage accounts is not supported. If cross tenant access is needed for your scenario, please reach out to the AzureML Data Support team alias at  amldatasupport@microsoft.com for assistance with a custom code solution.

Identity-based data access supports connections to **only** the following storage services.

* Azure Blob Storage
* Azure Data Lake Storage Gen1
* Azure Data Lake Storage Gen2

To access these storage services, you must have at least [Storage Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) access to the storage account. Only storage account owners can [change your access level via the Azure portal](../storage/blobs/assign-azure-role-data-access.md). 

### Access data for training jobs on compute using managed identity

Certain machine learning scenarios involve working with private data. In such cases, data scientists may not have direct access to data as Azure AD users. In this scenario, the managed identity of a compute can be used for data access authentication. In this scenario, the data can only be accessed from a compute instance or a machine learning compute cluster executing a training job. With this approach, the admin grants the compute instance or compute cluster managed identity Storage Blob Data Reader permissions on the storage. The individual data scientists don't need to be granted access.

To enable authentication with compute managed identity:

 * Create compute with managed identity enabled. See the [compute cluster](#compute-cluster) section, or for compute instance, the [Assign managed identity (preview)](how-to-create-manage-compute-instance.md) section.
 * Grant compute managed identity at least Storage Blob Data Reader role on the storage account.
 * Create any datastores with identity-based authentication enabled. See [Create datastores](how-to-datastore.md).

> [!NOTE]
> The name of the created system managed identity for compute instance or cluster will be in the format /workspace-name/computes/compute-name in your Azure Active Directory.

Once the identity-based authentication is enabled, the compute managed identity is used by default when accessing data within your training jobs. Optionally, you can authenticate with user identity using the steps described in next section.

For information on using configuring Azure RBAC for the storage, see [role-based access controls](../storage/blobs/assign-azure-role-data-access.md).

### Access data for training jobs on compute clusters using user identity

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

When training on [Azure Machine Learning compute clusters](how-to-create-attach-compute-cluster.md#what-is-a-compute-cluster), you can authenticate to storage with your user Azure Active Directory token. 

This authentication mode allows you to: 
* Set up fine-grained permissions, where different workspace users can have access to different storage accounts or folders within storage accounts.
* Let data scientists re-use existing permissions on storage systems.
* Audit storage access because the storage logs show which identities were used to access data.

> [!IMPORTANT] 
> This functionality has the following limitations
> * Feature is supported for experiments submitted via the [Azure Machine Learning CLI and Python SDK V2](concept-v2.md), but not via ML Studio.
> * User identity and compute managed identity cannot be used for authentication within same job.
> * For pipeline jobs, the user identity must be configured at job top level, not for individual pipeline steps.   

The following steps outline how to set up data access with user identity for training jobs on compute clusters from CLI. 

1. Grant the user identity access to storage resources. For example, grant StorageBlobReader access to the specific storage account you want to use or grant ACL-based permission to specific folders or files in Azure Data Lake Gen 2 storage.
