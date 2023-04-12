If you're an owner of a workspace, you can add and remove roles for the workspace. You can also assign roles to users. Use the following links to discover how to manage access:
- [Azure portal UI](../role-based-access-control/role-assignments-portal.md)
- [PowerShell](../role-based-access-control/role-assignments-powershell.md)
- [Azure CLI](../role-based-access-control/role-assignments-cli.md)
- [REST API](../role-based-access-control/role-assignments-rest.md)
- [Azure Resource Manager templates](../role-based-access-control/role-assignments-template.md)

## Use Azure AD security groups to manage workspace access

You can use Azure AD security groups to manage access to workspaces. This approach has following benefits:
 * Team or project leaders can manage user access to workspace as security group owners, without needing Owner role on the workspace resource directly.
 * You can organize, manage and revoke users' permissions on workspace and other resources as a group, without having to manage permissions on user-by-user basis.
 * Using Azure AD groups helps you to avoid reaching the [subscription limit](../role-based-access-control/troubleshooting.md#limits) on role assignments. 

To use Azure AD security groups:
 1. [Create a security group](../active-directory/fundamentals/active-directory-groups-view-azure-portal.md).
 2. [Add a group owner](../active-directory/fundamentals/how-to-manage-groups.md#add-or-remove-members-and-owners). This user has permissions to add or remove group members. Note that the group owner isn't required to be group member, or have direct RBAC role on the workspace.
 3. Assign the group an RBAC role on the workspace, such as AzureML Data Scientist, Reader or Contributor. 
 4. [Add group members](../active-directory/fundamentals/how-to-manage-groups.md#add-or-remove-members-and-owners). The members consequently gain access to the workspace.

## Create custom role

If the built-in roles are insufficient, you can create custom roles. Custom roles might have read, write, delete, and compute resource permissions in that workspace. You can make the role available at a specific workspace level, a specific resource group level, or a specific subscription level.

> [!NOTE]
> You must be an owner of the resource at that level to create custom roles within that resource.

To create a custom role, first construct a role definition JSON file that specifies the permission and scope for the role. The following example defines a custom role named "Data Scientist Custom" scoped at a specific workspace level:

`data_scientist_custom_role.json` :
```json
{
    "Name": "Data Scientist Custom",
    "IsCustom": true,
    "Description": "Can run experiment but can't create or delete compute.",
    "Actions": ["*"],
    "NotActions": [
        "Microsoft.MachineLearningServices/workspaces/*/delete",
        "Microsoft.MachineLearningServices/workspaces/write",
        "Microsoft.MachineLearningServices/workspaces/computes/*/write",
        "Microsoft.MachineLearningServices/workspaces/computes/*/delete", 
        "Microsoft.Authorization/*/write"
    ],
    "AssignableScopes": [
        "/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.MachineLearningServices/workspaces/<workspace_name>"
    ]
}
```

> [!TIP]
> You can change the `AssignableScopes` field to set the scope of this custom role at the subscription level, the resource group level, or a specific workspace level.
> The above custom role is just an example, see some suggested [custom roles for the Azure Machine Learning service](#customroles).

This custom role can do everything in the workspace except for the following actions:

- It can't delete the workspace.
- It can't create or update the workspace.
- It can't create or update compute resources.
- It can't delete compute resources.
- It can't add, delete, or alter role assignments.

To deploy this custom role, use the following Azure CLI command:

```azurecli-interactive 
az role definition create --role-definition data_scientist_role.json
```
