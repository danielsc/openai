
## Troubleshooting

Here are a few things to be aware of while you use Azure role-based access control (Azure RBAC):

- When you create a resource in Azure, such as a workspace, you're not directly the owner of the resource. Your role is inherited from the highest scope role that you're authorized against in that subscription. As an example if you're a Network Administrator, and have the permissions to create a Machine Learning workspace, you would be assigned the Network Administrator role against that workspace, and not the Owner role.

- To perform quota operations in a workspace, you need subscription level permissions. This means setting either subscription level quota or workspace level quota for your managed compute resources can only happen if you have write permissions at the subscription scope.

- When there are two role assignments to the same Azure Active Directory user with conflicting sections of Actions/NotActions, your operations listed in NotActions from one role might not take effect if they are also listed as Actions in another role. To learn more about how Azure parses role assignments, read [How Azure RBAC determines if a user has access to a resource](../role-based-access-control/overview.md#how-azure-rbac-determines-if-a-user-has-access-to-a-resource)

- To deploy your compute resources inside a VNet, you need to explicitly have permissions for the following actions:
    - `Microsoft.Network/virtualNetworks/*/read` on the VNet resources.
    - `Microsoft.Network/virtualNetworks/subnets/join/action` on the subnet resource.
    
    For more information on Azure RBAC with networking, see the [Networking built-in roles](../role-based-access-control/built-in-roles.md#networking).

- It can sometimes take up to 1 hour for your new role assignments to take effect over cached permissions across the stack.

## Next steps

- [Enterprise security overview](concept-enterprise-security.md)
- [Virtual network isolation and privacy overview](how-to-network-security-overview.md)
- [Tutorial: Train and deploy a model](tutorial-train-deploy-notebook.md)
- [Resource provider operations](../role-based-access-control/resource-provider-operations.md#microsoftmachinelearningservices)
