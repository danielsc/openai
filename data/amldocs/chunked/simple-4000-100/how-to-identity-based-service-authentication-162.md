
# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.entities import ManagedIdentityConfiguration, IdentityConfiguration, AmlCompute
from azure.ai.ml.constants import ManagedServiceIdentityType

# Create an identity configuration from the user-assigned managed identity
managed_identity = ManagedIdentityConfiguration(resource_id="/subscriptions/<subscription_id>/resourcegroups/<resource_group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<identity>")
identity_config = IdentityConfiguration(type = ManagedServiceIdentityType.USER_ASSIGNED, user_assigned_identities=[managed_identity])

# specify aml compute name.
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    # Pass the identity configuration
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4, identity=identity_config
    )
    ml_client.compute.begin_create_or_update(compute)
```

# [Studio](#tab/azure-studio)

During cluster creation or when editing compute cluster details, in the **Advanced settings**, toggle **Assign a managed identity** and specify a system-assigned identity or user-assigned identity.


### Data storage

When you create a datastore that uses **identity-based data access**, your Azure account ([Azure Active Directory token](../active-directory/fundamentals/active-directory-whatis.md)) is used to confirm you have permission to access the storage service. In the **identity-based data access** scenario, no authentication credentials are saved. Only the storage account information is stored in the datastore.

In contrast, datastores that use **credential-based authentication** cache connection information, like your storage account key or SAS token, in the [key vault](https://azure.microsoft.com/services/key-vault/) that's associated with the workspace. This approach has the limitation that other workspace users with sufficient permissions can retrieve those credentials, which may be a security concern for some organization.

For more information on how data access is authenticated, see the [Data administration](how-to-administrate-data-authentication.md) article. For information on configuring identity based access to data, see [Create datastores](how-to-datastore.md).

There are two scenarios in which you can apply identity-based data access in Azure Machine Learning. These scenarios are a good fit for identity-based access when you're working with confidential data and need more granular data access management:

- Accessing storage services
- Training machine learning models

The identity-based access allows you to use [role-based access controls (RBAC)](../storage/blobs/assign-azure-role-data-access.md) to restrict which identities, such as users or compute resources, have access to the data. 

### Accessing storage services

You can connect to storage services via identity-based data access with[Azure Machine Learning datastores](how-to-datastore.md). 

When you use identity-based data access, Azure Machine Learning prompts you for your Azure Active Directory token for data access authentication instead of keeping your credentials in the datastore. That approach allows for data access management at the storage level and keeps credentials confidential. 

The same behavior applies when you work with data interactively via a Jupyter Notebook on your local computer or [compute instance](concept-compute-instance.md).

> [!NOTE]
> Credentials stored via credential-based authentication include subscription IDs, shared access signature (SAS) tokens, and storage access key and service principal information, like client IDs and tenant IDs.

To help ensure that you securely connect to your storage service on Azure, Azure Machine Learning requires that you have permission to access the corresponding data storage.
 
> [!WARNING]
