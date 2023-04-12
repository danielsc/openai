
# Data administration

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK or CLI extension you are using:"]
> * [v1](./v1/concept-network-data-access.md)
> * [v2 (current version)](how-to-administrate-data-authentication.md)

Learn how to manage data access and how to authenticate in Azure Machine Learning
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
[!INCLUDE [CLI v2](../../includes/machine-learning-CLI-v2.md)]

> [!IMPORTANT]
> The information in this article is intended for Azure administrators who are creating the infrastructure required for an Azure Machine Learning solution.

In general, data access from studio involves the following checks:

* Who is accessing?
    - There are multiple different types of authentication depending on the storage type. For example, account key, token, service principal, managed identity, and user identity.
    - If authentication is made using a user identity, then it's important to know *which* user is trying to access storage. For more information on authenticating a _user_, see [authentication for Azure Machine Learning](how-to-setup-authentication.md). For more information on service-level authentication, see [authentication between AzureML and other services](how-to-identity-based-service-authentication.md).
* Do they have permission?
    - Are the credentials correct? If so, does the service principal, managed identity, etc., have the necessary permissions on the storage? Permissions are granted using Azure role-based access controls (Azure RBAC).
    - [Reader](../role-based-access-control/built-in-roles.md#reader) of the storage account reads metadata of the storage.
    - [Storage Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) reads data within a blob container.
    - [Contributor](../role-based-access-control/built-in-roles.md#contributor) allows write access to a storage account.
    - More roles may be required depending on the type of storage.
* Where is access from?
    - User: Is the client IP address in the VNet/subnet range?
    - Workspace: Is the workspace public or does it have a private endpoint in a VNet/subnet?
    - Storage: Does the storage allow public access, or does it restrict access through a service endpoint or a private endpoint?
* What operation is being performed?
    - Create, read, update, and delete (CRUD) operations on a data store/dataset are handled by Azure Machine Learning.
    - Archive operation on data assets in the Studio requires the following RBAC operation: Microsoft.MachineLearningServices/workspaces/datasets/registered/delete
    - Data Access calls (such as preview or schema) go to the underlying storage and need extra permissions.
* Where is this operation being run; compute resources in your Azure subscription or resources hosted in a Microsoft subscription?
    - All calls to dataset and datastore services (except the "Generate Profile" option) use resources hosted in a __Microsoft subscription__ to run the operations.
    - Jobs, including the "Generate Profile" option for datasets, run on a compute resource in __your subscription__, and access the data from there. So the compute identity needs permission to the storage rather than the identity of the user submitting the job.

The following diagram shows the general flow of a data access call. In this example, a user is trying to make a data access call through a machine learning workspace, without using any compute resource.

:::image type="content" source="./media/concept-network-data-access/data-access-flow.svg" alt-text="Diagram of the logic flow when accessing data.":::

## Scenarios and identities

The following table lists what identities should be used for specific scenarios:

| Scenario | Use workspace</br>Managed Service Identity (MSI) | Identity to use |
|--|--|--|
| Access from UI | Yes | Workspace MSI |
| Access from UI | No | User's Identity |
| Access from Job | Yes/No | Compute MSI |
