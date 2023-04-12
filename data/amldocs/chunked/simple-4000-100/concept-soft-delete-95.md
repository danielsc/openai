Before disabling workspace soft delete on an Azure subscription, purge or recover soft-deleted workspaces. After you disable soft delete on a subscription, workspaces that remain in soft deleted state are automatically purged when the retention period elapses.

## Billing implications

In general, when a workspace is in soft-deleted state, there are only two operations possible: 'permanently delete' and 'recover'. All other operations will fail. Therefore, even though the workspace exists, no compute operations can be performed and hence no usage will occur. When a workspace is soft-deleted, any cost-incurring resources including compute clusters are hard deleted.

## General Data Protection Regulation (GDPR) implications

After soft-deletion, the service keeps necessary data and metadata during the recovery [retention period](#soft-delete-retention-period). From a GDPR and privacy perspective, a request to delete personal data should be interpreted as a request for *permanent* deletion of a workspace and not soft delete.

When the retention period expires, or in case you permanently delete a workspace, data and metadata will be actively deleted. You could choose to permanently delete a workspace at the time of deletion.

For more information, see the [Export or delete workspace data](how-to-export-delete-data.md) article.

## Next steps

+ [Create and manage a workspace](how-to-manage-workspace.md)
+ [Export or delete workspace data](how-to-export-delete-data.md)