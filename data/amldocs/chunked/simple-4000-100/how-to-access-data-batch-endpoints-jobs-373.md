| Data input type              | Credential in store             | Credentials used                                              | Access granted by |
|------------------------------|---------------------------------|---------------------------------------------------------------|-------------------|
| Data store                   | Yes                             | Data store's credentials in the workspace                     | Credentials       |
| Data store                   | No                              | Identity of the job                                           | Depends on type   |
| Data asset                   | Yes                             | Data store's credentials in the workspace                     | Credentials       |
| Data asset                   | No                              | Identity of the job                                           | Depends on store  |
| Azure Blob Storage           | Not apply                       | Identity of the job + Managed identity of the compute cluster | RBAC              |
| Azure Data Lake Storage Gen1 | Not apply                       | Identity of the job + Managed identity of the compute cluster | POSIX             |
| Azure Data Lake Storage Gen2 | Not apply                       | Identity of the job + Managed identity of the compute cluster | POSIX and RBAC    |

The managed identity of the compute cluster is used for mounting and configuring external data storage accounts. However, the identity of the job is still used to read the underlying data allowing you to achieve granular access control. That means that in order to successfully read data from external storage services, the managed identity of the compute cluster where the deployment is running must have at least [Storage Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) access to the storage account. Only storage account owners can [change your access level via the Azure portal](../storage/blobs/assign-azure-role-data-access.md).

> [!NOTE]
> To assign an identity to the compute used by a batch deployment, follow the instructions at [Set up authentication between Azure ML and other services](how-to-identity-based-service-authentication.md#compute-cluster). Configure the identity on the compute cluster associated with the deployment. Notice that all the jobs running on such compute are affected by this change. However, different deployments (even under the same deployment) can be configured to run under different clusters so you can administer the permissions accordingly depending on your requirements.

## Next steps

* [Troubleshooting batch endpoints](how-to-troubleshoot-batch-endpoints.md).
* [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md).
* [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md).
