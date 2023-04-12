
To work with resources within a workspace, you'll switch from the general **management.azure.com** server to a REST API server specific to the location of the workspace. Note the value of the `discoveryUrl` key in the above JSON response. If you GET that URL, you'll receive a response something like:

```json
{
  "api": "https://centralus.api.azureml.ms",
  "catalog": "https://catalog.cortanaanalytics.com",
  "experimentation": "https://centralus.experiments.azureml.net",
  "gallery": "https://gallery.cortanaintelligence.com/project",
  "history": "https://centralus.experiments.azureml.net",
  "hyperdrive": "https://centralus.experiments.azureml.net",
  "labeling": "https://centralus.experiments.azureml.net",
  "modelmanagement": "https://centralus.modelmanagement.azureml.net",
  "pipelines": "https://centralus.aether.ms",
  "studiocoreservices": "https://centralus.studioservice.azureml.com"
}
```

The value of the `api` response is the URL of the server that you'll use for more requests. To list experiments, for instance, send the following command. Replace `REGIONAL-API-SERVER` with the value of the `api` response (for instance, `centralus.api.azureml.ms`). Also replace `YOUR-SUBSCRIPTION-ID`, `YOUR-RESOURCE-GROUP`, `YOUR-WORKSPACE-NAME`, and `YOUR-ACCESS-TOKEN` as usual:

```bash
curl https://<REGIONAL-API-SERVER>/history/v1.0/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.MachineLearningServices/workspaces/<YOUR-WORKSPACE-NAME>/experiments?api-version=2022-05-01 \
-H "Authorization:Bearer <YOUR-ACCESS-TOKEN>"
```

Similarly, to retrieve registered models in your workspace, send:

```bash
curl https://<REGIONAL-API-SERVER>/modelmanagement/v1.0/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.MachineLearningServices/workspaces/<YOUR-WORKSPACE-NAME>/models?api-version=2022-05-01 \
-H "Authorization:Bearer <YOUR-ACCESS-TOKEN>"
```

Notice that to list experiments the path begins with `history/v1.0` while to list models, the path begins with `modelmanagement/v1.0`. The REST API is divided into several operational groups, each with a distinct path. 

|Area|Path|
|-|-|
|Artifacts|/rest/api/azureml|
|Data stores|/azure/machine-learning/how-to-access-data|
|Hyperparameter tuning|hyperdrive/v1.0/|
|Models|modelmanagement/v1.0/|
|Run history|execution/v1.0/ and history/v1.0/|

You can explore the REST API using the general pattern of:

|URL component|Example|
|-|-|
| https://| |
| REGIONAL-API-SERVER/ | centralus.api.azureml.ms/ |
| operations-path/ | history/v1.0/ |
| subscriptions/YOUR-SUBSCRIPTION-ID/ | subscriptions/abcde123-abab-abab-1234-0123456789abc/ |
| resourceGroups/YOUR-RESOURCE-GROUP/ | resourceGroups/MyResourceGroup/ |
| providers/operation-provider/ | providers/Microsoft.MachineLearningServices/ |
| provider-resource-path/ | workspaces/MyWorkspace/experiments/FirstExperiment/runs/1/ |
| operations-endpoint/ | artifacts/metadata/ |


## Create and modify resources using PUT and POST requests

In addition to resource retrieval with the GET verb, the REST API supports the creation of all the resources necessary to train, deploy, and monitor ML solutions. 

Training and running ML models require compute resources. You can list the compute resources of a workspace with: 

```bash
curl https://management.azure.com/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.MachineLearningServices/workspaces/<YOUR-WORKSPACE-NAME>/computes?api-version=2022-05-01 \
-H "Authorization:Bearer <YOUR-ACCESS-TOKEN>"
```

To create or overwrite a named compute resource, you'll use a PUT request. In the following, in addition to the now-familiar replacements of `YOUR-SUBSCRIPTION-ID`, `YOUR-RESOURCE-GROUP`, `YOUR-WORKSPACE-NAME`, and `YOUR-ACCESS-TOKEN`, replace `YOUR-COMPUTE-NAME`, and values for `location`, `vmSize`, `vmPriority`, `scaleSettings`, `adminUserName`, and `adminUserPassword`. As specified in the reference at [Machine Learning Compute - Create Or Update SDK Reference](/rest/api/azureml/2022-10-01/workspaces/create-or-update), the following command creates a dedicated, single-node Standard_D1 (a basic CPU compute resource) that will scale down after 30 minutes:
