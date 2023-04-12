
# Authorization on batch endpoints

Batch endpoints support Azure Active Directory authentication, or `aad_token`. That means that in order to invoke a batch endpoint, the user must present a valid Azure Active Directory authentication token to the batch endpoint URI. Authorization is enforced at the endpoint level. The following article explains how to correctly interact with batch endpoints and the security requirements for it. 

## Prerequisites

* This example assumes that you have a model correctly deployed as a batch endpoint. Particularly, we are using the *heart condition classifier* created in the tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).

## How authorization works

To invoke a batch endpoint, the user must present a valid Azure Active Directory token representing a __security principal__. This principal can be a __user principal__ or a __service principal__. In any case, once an endpoint is invoked, a batch deployment job is created under the identity associated with the token. The identity needs the following permissions in order to successfully create a job:

> [!div class="checklist"]
> * Read batch endpoints/deployments.
> * Create jobs in batch inference endpoints/deployment.
> * Create experiments/runs.
> * Read and write from/to data stores.
> * Lists datastore secrets.

You can either use one of the [built-in security roles](../role-based-access-control/built-in-roles.md) or create a new one. In any case, the identity used to invoke the endpoints requires to be granted the permissions explicitly. See [Steps to assign an Azure role](../role-based-access-control/role-assignments-steps.md) for instructions to assign them.

> [!IMPORTANT]
> The identity used for invoking a batch endpoint may not be used to read the underlying data depending on how the data store is configured. Please see [Security considerations when reading data](how-to-access-data-batch-endpoints-jobs.md#security-considerations-when-reading-data) for more details.

## How to run jobs using different types of credentials

The following examples show different ways to start batch deployment jobs using different types of credentials:

> [!IMPORTANT] 
> When working on a private link-enabled workspaces, batch endpoints can't be invoked from the UI in Azure ML studio. Please use the Azure ML CLI v2 instead for job creation.

### Running jobs using user's credentials

In this case, we want to execute a batch endpoint using the identity of the user currently logged in. Follow these steps:

> [!NOTE]
> When working on Azure ML studio, batch endpoints/deployments are always executed using the identity of the current user logged in.

# [Azure CLI](#tab/cli)

1. Use the Azure CLI to log in using either interactive or device code authentication:

    ```azurecli
    az login
    ```

1. Once authenticated, use the following command to run a batch deployment job:

    ```azurecli
    az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci
    ```

# [Python](#tab/sdk)

1. Use the Azure ML SDK for Python to log in using either interactive or device authentication:

    ```python
    from azure.ai.ml import MLClient
    from azure.identity import InteractiveAzureCredentials

    subscription_id = "<subscription>"
    resource_group = "<resource-group>"
    workspace = "<workspace>"

    ml_client = MLClient(InteractiveAzureCredentials(), subscription_id, resource_group, workspace)
    ```

1. Once authenticated, use the following command to run a batch deployment job:

    ```python
    job = ml_client.batch_endpoints.invoke(
            endpoint_name, 
            input=Input(path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci")
        )
    ```

# [REST](#tab/rest)

When working with REST APIs, we recommend to using either a [service principal](#running-jobs-using-a-service-principal) or a [managed identity](#running-jobs-using-a-managed-identity) to interact with the API.
