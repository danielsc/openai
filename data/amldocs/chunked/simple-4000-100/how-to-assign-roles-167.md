| Submitting any type of run (V2) | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/*/read", "/workspaces/environments/write", "/workspaces/jobs/*", "/workspaces/metadata/artifacts/write", "/workspaces/metadata/codes/*/write", "/workspaces/environments/build/action", "/workspaces/environments/readSecrets/action"` |
| Publishing pipelines and endpoints (V1) | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/endpoints/pipelines/*", "/workspaces/pipelinedrafts/*", "/workspaces/modules/*"` |
| Publishing pipelines and endpoints (V2) | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/endpoints/pipelines/*", "/workspaces/pipelinedrafts/*", "/workspaces/components/*"` |
| Attach an AKS resource <sub>2</sub> | Not required | Owner or contributor on the resource group that contains AKS | 
| Deploying a registered model on an AKS/ACI resource | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/services/aks/write", "/workspaces/services/aci/write"` |
| Scoring against a deployed AKS endpoint | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/services/aks/score/action", "/workspaces/services/aks/listkeys/action"` (when you are not using Azure Active Directory auth) OR `"/workspaces/read"` (when you are using token auth) |
| Accessing storage using interactive notebooks | Not required | Not required | Owner, contributor, or custom role allowing: `"/workspaces/computes/read", "/workspaces/notebooks/samples/read", "/workspaces/notebooks/storage/*", "/workspaces/listStorageAccountKeys/action", "/workspaces/listNotebookAccessToken/read"`|
| Create new custom role | Owner, contributor, or custom role allowing `Microsoft.Authorization/roleDefinitions/write` | Not required | Owner, contributor, or custom role allowing: `/workspaces/computes/write` |
| Create/manage online endpoints and deployments | Not required | Not required | Owner, contributor, or custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/*` |
| Retrieve authentication credentials for online endpoints | Not required | Not required | Owner, contributor, or custom role allowing `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/token/action` and `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/listkeys/action`.

1: If you receive a failure when trying to create a workspace for the first time, make sure that your role allows `Microsoft.MachineLearningServices/register/action`. This action allows you to register the Azure Machine Learning resource provider with your Azure subscription.

2: When attaching an AKS cluster, you also need to have the [Azure Kubernetes Service Cluster Admin Role](../role-based-access-control/built-in-roles.md#azure-kubernetes-service-cluster-admin-role) on the cluster.

### Differences between actions for V1 and V2 APIs

There are certain differences between actions for V1 APIs and V2 APIs.

| Asset | Action path for V1 API | Action path for V2 API
| ----- | ----- | ----- |
| Dataset | Microsoft.MachineLearningServices/workspaces/datasets | Microsoft.MachineLearningServices/workspaces/datasets/versions |
| Experiment runs and jobs | Microsoft.MachineLearningServices/workspaces/experiments | Microsoft.MachineLearningServices/workspaces/jobs |
| Models | Microsoft.MachineLearningServices/workspaces/models | Microsoft.MachineLearningServices/workspaces/models/versions |
| Snapshots and code | Microsoft.MachineLearningServices/workspaces/snapshots | Microsoft.MachineLearningServices/workspaces/codes/versions |
| Modules and components | Microsoft.MachineLearningServices/workspaces/modules | Microsoft.MachineLearningServices/workspaces/components |

You can make custom roles compatible with both V1 and V2 APIs by including both actions, or using wildcards that include both actions, for example Microsoft.MachineLearningServices/workspaces/datasets/*/read.
