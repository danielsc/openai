
### MLOps

Allows you to assign a role to a service principal and use that to automate your MLOps pipelines. For example, to submit runs against an already published pipeline:

`mlops_custom_role.json` :
```json
{
    "Name": "MLOps Custom",
    "IsCustom": true,
    "Description": "Can run pipelines against a published pipeline endpoint",
    "Actions": [
        "Microsoft.MachineLearningServices/workspaces/read",
        "Microsoft.MachineLearningServices/workspaces/endpoints/pipelines/read",
        "Microsoft.MachineLearningServices/workspaces/metadata/artifacts/read",
        "Microsoft.MachineLearningServices/workspaces/metadata/snapshots/read",
        "Microsoft.MachineLearningServices/workspaces/environments/read",    
        "Microsoft.MachineLearningServices/workspaces/metadata/secrets/read",
        "Microsoft.MachineLearningServices/workspaces/modules/read",
        "Microsoft.MachineLearningServices/workspaces/components/read",       
        "Microsoft.MachineLearningServices/workspaces/datasets/*/read",
        "Microsoft.MachineLearningServices/workspaces/datastores/read",
        "Microsoft.MachineLearningServices/workspaces/environments/write",
        "Microsoft.MachineLearningServices/workspaces/experiments/runs/read",       
        "Microsoft.MachineLearningServices/workspaces/experiments/runs/write",
        "Microsoft.MachineLearningServices/workspaces/experiments/runs/submit/action",
        "Microsoft.MachineLearningServices/workspaces/experiments/jobs/read",       
        "Microsoft.MachineLearningServices/workspaces/experiments/jobs/write",
        "Microsoft.MachineLearningServices/workspaces/metadata/artifacts/write",
        "Microsoft.MachineLearningServices/workspaces/metadata/snapshots/write",
        "Microsoft.MachineLearningServices/workspaces/metadata/codes/*/write",       
        "Microsoft.MachineLearningServices/workspaces/environments/build/action",
    ],
    "NotActions": [
        "Microsoft.MachineLearningServices/workspaces/computes/write",
        "Microsoft.MachineLearningServices/workspaces/write",
        "Microsoft.MachineLearningServices/workspaces/computes/delete",
        "Microsoft.MachineLearningServices/workspaces/delete",
        "Microsoft.MachineLearningServices/workspaces/computes/listKeys/action",
        "Microsoft.MachineLearningServices/workspaces/listKeys/action",
        "Microsoft.Authorization/*"
    ],
    "AssignableScopes": [
        "/subscriptions/<subscription_id>"
    ]
}
```

### Workspace Admin

Allows you to perform all operations within the scope of a workspace, **except**:

* Creating a new workspace
* Assigning subscription or workspace level quotas

The workspace admin also cannot create a new role. It can only assign existing built-in or custom roles within the scope of their workspace:

`workspace_admin_custom_role.json` :
```json
{
    "Name": "Workspace Admin Custom",
    "IsCustom": true,
    "Description": "Can perform all operations except quota management and upgrades",
    "Actions": [
        "Microsoft.MachineLearningServices/workspaces/*/read",
        "Microsoft.MachineLearningServices/workspaces/*/action",
        "Microsoft.MachineLearningServices/workspaces/*/write",
        "Microsoft.MachineLearningServices/workspaces/*/delete",
        "Microsoft.Authorization/roleAssignments/*"
    ],
    "NotActions": [
        "Microsoft.MachineLearningServices/workspaces/write"
    ],
    "AssignableScopes": [
        "/subscriptions/<subscription_id>"
    ]
}
```

### Data labeling

# [Data labeler](#tab/labeler)

Allows you to define a role scoped only to labeling data:

`labeler_custom_role.json` :
```json
{
    "Name": "Labeler Custom",
    "IsCustom": true,
    "Description": "Can label data for Labeling",
    "Actions": [
        "Microsoft.MachineLearningServices/workspaces/read",
        "Microsoft.MachineLearningServices/workspaces/labeling/projects/read",
        "Microsoft.MachineLearningServices/workspaces/labeling/projects/summary/read",
        "Microsoft.MachineLearningServices/workspaces/labeling/labels/read",
        "Microsoft.MachineLearningServices/workspaces/labeling/labels/write"   
    ],
    "NotActions": [        
    ],
    "AssignableScopes": [
        "/subscriptions/<subscription_id>"
    ]
}
```
