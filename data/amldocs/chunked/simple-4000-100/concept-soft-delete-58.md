Permanently deleting a workspace allows a workspace name to be reused immediately after deletion. This behavior may be useful in dev/test scenarios where you want to create and later delete a workspace. Permanently deleting a workspace may also be required for compliance if you manage highly sensitive data. See [General Data Protection Regulation (GDPR) implications](#general-data-protection-regulation-gdpr-implications) to learn more on how deletions are handled when soft delete is enabled.

:::image type="content" source="./media/concept-soft-delete/soft-delete-permanently-delete.png" alt-text="Screenshot of the delete workspace form in the portal.":::

## Manage soft-deleted workspaces

Soft-deleted workspaces can be managed under the Azure Machine Learning resource provider in the Azure portal. To list soft-deleted workspaces, use the following steps:

1. From the [Azure portal](https://portal.azure.com), select __More services__.  From the __AI + machine learning__ category, select __Azure Machine Learning__.
1. From the top of the page, select __Recently deleted__ to view workspaces that were soft-deleted and are still within the retention period.

    :::image type="content" source="./media/concept-soft-delete/soft-delete-manage-recently-deleted.png" alt-text="Screenshot highlighting the recently deleted link.":::

1. From the recently deleted workspaces view, you can recover or permanently delete a workspace.

    :::image type="content" source="./media/concept-soft-delete/soft-delete-manage-recently-deleted-panel.png" alt-text="Screenshot of the recently deleted workspaces view.":::

## Recover a soft-deleted workspace

When you select *Recover* on a soft-deleted workspace, it initiates an operation to restore the workspace state. The service attempts recreation or reattachment of a subset of resources, including Azure RBAC role assignments. Hard-deleted resources including compute clusters should be recreated by you.

Azure Machine Learning recovers Azure RBAC role assignments for the workspace identity, but doesn't recover role assignments you may have added for users or user groups. It may take up to 15 minutes for role assignments to propagate after workspace recovery.

Recovery of a workspace may not always be possible. Azure Machine Learning stores workspace metadata on [other Azure resources associated with the workspace](concept-workspace.md#associated-resources). In the event these dependent Azure resources were deleted, it may prevent the workspace from being recovered or correctly restored. Dependencies of the Azure Machine Learning workspace must be recovered first, before recovering a deleted workspace. Azure Container Registry isn't a hard requirement required for recovery.

Enable [data protection capabilities on Azure Storage](../storage/blobs/soft-delete-blob-overview.md) to improve chances of successful recovery.

## Permanently delete a soft-deleted workspace

When you select *Permanently delete* on a soft-deleted workspace, it triggers hard deletion of workspace data. Once deleted, workspace data can no longer be recovered. Permanent deletion of workspace data is also triggered when the soft delete retention period expires.

## Register soft-delete on an Azure subscription

During the time of preview, workspace soft delete is enabled on an opt-in basis per Azure subscription. When soft delete is enabled for a subscription, it's enabled for all Azure Machine Learning workspaces in that subscription.

To enable workspace soft delete on your Azure subscription, [register the preview feature](../azure-resource-manager/management/preview-features.md?tabs=azure-portal#register-preview-feature) in the Azure portal. Select `Workspace soft delete` under the `Microsoft.MachineLearningServices` resource provider. It may take 15 minutes for the UX to appear in the Azure portal after registering your subscription.

Before disabling workspace soft delete on an Azure subscription, purge or recover soft-deleted workspaces. After you disable soft delete on a subscription, workspaces that remain in soft deleted state are automatically purged when the retention period elapses.
