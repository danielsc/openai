
# Move Azure Machine Learning workspaces between subscriptions (preview)

As the requirements of your machine learning application change, you may need to move your workspace to a different Azure subscription. For example, you may need to move the workspace in the following situations:

* Promote workspace from test subscription to production subscription.
* Change the design and architecture of your application.
* Move workspace to a subscription with more available quota.
* Move workspace to a subscription with different cost center.

Moving the workspace enables you to migrate the workspace and its contents as a single, automated step. The following table describes the workspace contents that are moved:

| Workspace contents | Moved with workspace |
| ----- |:-----:|
| Datastores | Yes |
| Datasets | No |
| Experiment jobs | Yes |
| Environments | Yes |
| Models and other assets stored in the workspace | Yes |
| Compute resources | No |
| Endpoints | No |

> [!IMPORTANT]	
> Workspace move is currently in public preview. This preview is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. 	
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## Prerequisites

- An Azure Machine Learning workspace in the source subscription. For more information, see [Create workspace resources](quickstart-create-resources.md).
- You must have permissions to manage resources in both source and target subscriptions. For example, Contributor or Owner role at the __subscription__ level. For more information on roles, see [Azure roles](../role-based-access-control/rbac-and-directory-admin-roles.md#azure-roles)
- The destination subscription must be registered for required resource providers. The following table contains a list of the resource providers required by Azure Machine Learning:

    | Resource provider | Why it's needed |
    | ----- | ----- |
    | __Microsoft.MachineLearningServices__ | Creating the Azure Machine Learning workspace. |
    | __Microsoft.Storage__ | Azure Storage Account is used as the default storage for the workspace. |
    | __Microsoft.ContainerRegistry__ | Azure Container Registry is used by the workspace to build Docker images. |
    | __Microsoft.KeyVault__ | Azure Key Vault is used by the workspace to store secrets. |
    | __Microsoft.Notebooks/NotebookProxies__ | Integrated notebooks on Azure Machine Learning compute instance. |
    | __Microsoft.ContainerService__ | If you plan on deploying trained models to Azure Kubernetes Services. |

    If you plan on using a customer-managed key with Azure Machine Learning, then the following service providers must be registered:

    | Resource provider | Why it's needed |
    | ----- | ----- |
    | __Microsoft.DocumentDB/databaseAccounts__ | Azure Cosmos DB instance that logs metadata for the workspace. |
    | __Microsoft.Search/searchServices__ | Azure Search provides indexing capabilities for the workspace. |

    For information on registering resource providers, see [Resolve errors for resource provider registration](/azure/azure-resource-manager/templates/error-register-resource-provider).

- The [Azure CLI](/cli/azure/install-azure-cli).

    > [!TIP]
    > The move operation does not use the Azure CLI extension for machine learning.

## Limitations

* Workspace move is not meant for replicating workspaces, or moving individual assets such as models or datasets from one workspace to another.
* Workspace move doesn't support migration across Azure regions or Azure Active Directory tenants.
* The workspace mustn't be in use during the move operation. Verify that all experiment jobs, data profiling jobs, and labeling projects have completed. Also verify that inference endpoints aren't being invoked.
* The workspace will become unavailable during the move.
