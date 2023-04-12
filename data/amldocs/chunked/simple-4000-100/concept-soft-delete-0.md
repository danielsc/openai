
# Recover workspace data after accidental deletion with soft delete (Preview)

The soft-delete feature for Azure Machine Learning workspace provides a data protection capability that enables you to attempt recovery of workspace data after accidental deletion. Soft delete introduces a two-step approach in deleting a workspace. When a workspace is deleted, it's first soft deleted. While in soft-deleted state, you can choose to recover or permanently delete a workspace and its data during a data retention period.

> [!IMPORTANT]	
> Workspace soft delete is currently in public preview. This preview is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. 	
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).
> To enroll your Azure Subscription, see [Register soft-delete on an Azure subscription](#register-soft-delete-on-an-azure-subscription).

## How workspace soft delete works

When a workspace is soft-deleted, data and metadata stored service-side get soft-deleted, but some configurations get hard-deleted. Below table provides an overview of which configurations and objects get soft-deleted, and which are hard-deleted.

> [!IMPORTANT] 
> Soft delete is not supported for workspaces encrypted with customer-managed keys (CMK), and these workspaces are always hard deleted.

Data / configuration | Soft-deleted | Hard-deleted
---|---|---
Run History | ✓ | 
Models | ✓ | 
Data | ✓ | 
Environments | ✓ | 
Components | ✓ |
Notebooks | ✓ | 
Pipelines | ✓ |
Designer pipelines | ✓ | 
AutoML jobs | ✓ |
Data labeling projects | ✓ | 
Datastores | ✓ | 
Queued or running jobs | | ✓
Role assignments | | ✓*
Internal cache | | ✓ 
Compute instance |  | ✓ 
Compute clusters |  | ✓ 
Inference endpoints | | ✓ 
Linked Databricks workspaces | | ✓*

\* *Microsoft attempts recreation or reattachment when a workspace is recovered. Recovery isn't guaranteed, and a best effort attempt.*

After soft-deletion, the service keeps necessary data and metadata during the recovery [retention period](#soft-delete-retention-period). When the retention period expires, or in case you permanently delete a workspace, data and metadata will be actively deleted.

## Soft-delete retention period

A default retention period of 14 days holds for deleted workspaces. The retention period indicates how long workspace data remains available after it's deleted. The clock starts on the retention period as soon as a workspace is soft-deleted.

During the retention period, soft-deleted workspaces can be recovered or permanently deleted. Any other operations on the workspace, like submitting a training job,  will fail. You can't reuse the name of a workspace that has been soft-deleted until the retention period has passed. Once the retention period elapses, a soft deleted workspace automatically gets permanently deleted.

> [!TIP]
> During preview of workspace soft-delete, the retention period is fixed to 14 days and can’t be modified. 

## Deleting a workspace

The default deletion behavior when deleting a workspace is soft delete. This behavior excludes workspaces that are [encrypted with a customer-managed key](concept-customer-managed-keys.md), which aren't supported for soft delete.

Optionally, you may permanently delete a workspace going to soft delete state first by checking __Delete the workspace permanently__ in the Azure portal. Permanently deleting workspaces can only be done one workspace at time, and not using a batch operation.

Permanently deleting a workspace allows a workspace name to be reused immediately after deletion. This behavior may be useful in dev/test scenarios where you want to create and later delete a workspace. Permanently deleting a workspace may also be required for compliance if you manage highly sensitive data. See [General Data Protection Regulation (GDPR) implications](#general-data-protection-regulation-gdpr-implications) to learn more on how deletions are handled when soft delete is enabled.
