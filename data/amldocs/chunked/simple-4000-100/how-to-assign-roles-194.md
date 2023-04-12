You can make custom roles compatible with both V1 and V2 APIs by including both actions, or using wildcards that include both actions, for example Microsoft.MachineLearningServices/workspaces/datasets/*/read.

### Create a workspace using a customer-managed key

When using a customer-managed key (CMK), an Azure Key Vault is used to store the key. The user or service principal used to create the workspace must have owner or contributor access to the key vault.

Within the key vault, the user or service principal must have create, get, delete, and purge access to the key through a key vault access policy. For more information, see [Azure Key Vault security](../key-vault/general/security-features.md#controlling-access-to-key-vault-data).

### User-assigned managed identity with Azure ML compute cluster

To assign a user assigned identity to an Azure Machine Learning compute cluster, you need write permissions to create the compute and the [Managed Identity Operator Role](../role-based-access-control/built-in-roles.md#managed-identity-operator). For more information on Azure RBAC with Managed Identities, read [How to manage user assigned identity](../active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-portal.md)

### MLflow operations

To perform MLflow operations with your Azure Machine Learning workspace, use the following scopes your custom role:

| MLflow operation | Scope |
| --- | --- |
| (V1) List, read, create, update or delete experiments | `Microsoft.MachineLearningServices/workspaces/experiments/*` |
| (V2) List, read, create, update or delete jobs | `Microsoft.MachineLearningServices/workspaces/jobs/*` |
| Get registered model by name, fetch a list of all registered models in the registry, search for registered models, latest version models for each requests stage, get a registered model's version, search model versions, get URI where a model version's artifacts are stored, search for runs by experiment ids | `Microsoft.MachineLearningServices/workspaces/models/*/read` |
| Create a new registered model, update a registered model's name/description, rename existing registered model, create new version of the model, update a model version's description, transition a registered model to one of the stages | `Microsoft.MachineLearningServices/workspaces/models/*/write` |
| Delete a registered model along with all its version, delete specific versions of a registered model | `Microsoft.MachineLearningServices/workspaces/models/*/delete` |

<a id="customroles"></a>

## Example custom roles

### Data scientist

Allows a data scientist to perform all operations inside a workspace **except**:

* Creation of compute
* Deploying models to a production AKS cluster
* Deploying a pipeline endpoint in production

`data_scientist_custom_role.json` :
```json
{
    "Name": "Data Scientist Custom",
    "IsCustom": true,
    "Description": "Can run experiment but can't create or delete compute or deploy production endpoints.",
    "Actions": [
        "Microsoft.MachineLearningServices/workspaces/*/read",
        "Microsoft.MachineLearningServices/workspaces/*/action",
        "Microsoft.MachineLearningServices/workspaces/*/delete",
        "Microsoft.MachineLearningServices/workspaces/*/write"
    ],
    "NotActions": [
        "Microsoft.MachineLearningServices/workspaces/delete",
        "Microsoft.MachineLearningServices/workspaces/write",
        "Microsoft.MachineLearningServices/workspaces/computes/*/write",
        "Microsoft.MachineLearningServices/workspaces/computes/*/delete", 
        "Microsoft.Authorization/*",
        "Microsoft.MachineLearningServices/workspaces/computes/listKeys/action",
        "Microsoft.MachineLearningServices/workspaces/listKeys/action",
        "Microsoft.MachineLearningServices/workspaces/services/aks/write",
        "Microsoft.MachineLearningServices/workspaces/services/aks/delete",
        "Microsoft.MachineLearningServices/workspaces/endpoints/pipelines/write"
    ],
    "AssignableScopes": [
        "/subscriptions/<subscription_id>"
    ]
}
```
