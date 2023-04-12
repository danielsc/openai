To create or overwrite a named compute resource, you'll use a PUT request. In the following, in addition to the now-familiar replacements of `YOUR-SUBSCRIPTION-ID`, `YOUR-RESOURCE-GROUP`, `YOUR-WORKSPACE-NAME`, and `YOUR-ACCESS-TOKEN`, replace `YOUR-COMPUTE-NAME`, and values for `location`, `vmSize`, `vmPriority`, `scaleSettings`, `adminUserName`, and `adminUserPassword`. As specified in the reference at [Machine Learning Compute - Create Or Update SDK Reference](/rest/api/azureml/2022-10-01/workspaces/create-or-update), the following command creates a dedicated, single-node Standard_D1 (a basic CPU compute resource) that will scale down after 30 minutes:

```bash
curl -X PUT \
  'https://management.azure.com/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<YOUR-WORKSPACE-NAME>/computes/<YOUR-COMPUTE-NAME>?api-version=2022-05-01' \
  -H 'Authorization:Bearer <YOUR-ACCESS-TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "location": "eastus",
    "properties": {
        "computeType": "AmlCompute",
        "properties": {
            "vmSize": "Standard_D1",
            "vmPriority": "Dedicated",
            "scaleSettings": {
                "maxNodeCount": 1,
                "minNodeCount": 0,
                "nodeIdleTimeBeforeScaleDown": "PT30M"
            }
        }
    },
    "userAccountCredentials": {
        "adminUserName": "<ADMIN_USERNAME>",
        "adminUserPassword": "<ADMIN_PASSWORD>"
    }
}'
```

> [!Note]
> In Windows terminals you may have to escape the double-quote symbols when sending JSON data. That is, text such as `"location"` becomes `\"location\"`. 

A successful request will get a `201 Created` response, but note that this response simply means that the provisioning process has begun. You'll need to poll (or use the portal) to confirm its successful completion.

## Create a workspace using REST 

Every Azure ML workspace has a dependency on four other Azure resources: an Azure Container Registry resource, Azure Key Vault, Azure Application Insights, and an Azure Storage account. You can't create a workspace until these resources exist. Consult the REST API reference for the details of creating each such resource.

To create a workspace, PUT a call similar to the following to `management.azure.com`. While this call requires you to set a large number of variables, it's structurally identical to other calls that this article has discussed. 

```bash
curl -X PUT \
  'https://management.azure.com/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>\
/providers/Microsoft.MachineLearningServices/workspaces/<YOUR-NEW-WORKSPACE-NAME>?api-version=2022-05-01' \
  -H 'Authorization: Bearer <YOUR-ACCESS-TOKEN>' \
  -H 'Content-Type: application/json' \
  -d '{
    "location": "AZURE-LOCATION>",
    "identity" : {
        "type" : "systemAssigned"
    },
    "properties": {
        "friendlyName" : "<YOUR-WORKSPACE-FRIENDLY-NAME>",
        "description" : "<YOUR-WORKSPACE-DESCRIPTION>",
        "containerRegistry" : "/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.ContainerRegistry/registries/<YOUR-REGISTRY-NAME>",
        keyVault" : "/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>\
/providers/Microsoft.Keyvault/vaults/<YOUR-KEYVAULT-NAME>",
        "applicationInsights" : "subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.insights/components/<YOUR-APPLICATION-INSIGHTS-NAME>",
        "storageAccount" : "/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/\
providers/Microsoft.Storage/storageAccounts/<YOUR-STORAGE-ACCOUNT-NAME>"
    }
}'
```

You should receive a `202 Accepted` response and, in the returned headers, a `Location` URI. You can GET this URI for information on the deployment, including helpful debugging information if there's a problem with one of your dependent resources (for instance, if you forgot to enable admin access on your container registry). 
