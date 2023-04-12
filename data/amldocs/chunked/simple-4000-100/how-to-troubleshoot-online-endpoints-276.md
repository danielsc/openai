If your container could not start, this means scoring could not happen. It might be that the container is requesting more resources than what `instance_type` can support. If so, consider updating the `instance_type` of the online deployment.

To get the exact reason for an error, run: 

#### [Azure CLI](#tab/cli)

```azurecli
az ml online-deployment get-logs -e <endpoint-name> -n <deployment-name> -l 100
```

#### [Python SDK](#tab/python)

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100
)
```

#### [Studio](#tab/studio)

Use the **Endpoints** in the studio:

1. In the left navigation bar, select **Endpoints**.
1. (Optional) Create a filter on compute type to show only managed compute types.
1. Select an endpoint name to view the endpoint's details page.
1. Select the **Deployment logs** tab in the endpoint's details page.
1. Use the dropdown to select the deployment whose log you want to see.


### ERROR: BadArgument

Below is a list of reasons you might run into this error when using either managed online endpoint or Kubernetes online endpoint:

* [Subscription does not exist](#subscription-does-not-exist)
* [Startup task failed due to authorization error](#authorization-error)
* [Startup task failed due to incorrect role assignments on resource](#authorization-error)
* [Unable to download user container image](#unable-to-download-user-container-image)
* [Unable to download user model](#unable-to-download-user-model)


Additionally, below is a list of reasons you might run into this error only when using Kubernetes online endpoint:

* [Resource request was greater than limits](#resource-requests-greater-than-limits)
* [azureml-fe for kubernetes online endpoint is not ready](#azureml-fe-not-ready)


#### Subscription does not exist

The Azure subscription that is entered must be existing. This error occurs when we cannot find the Azure subscription that was referenced. This is likely due to a typo in the subscription ID. Please double-check that the subscription ID was correctly typed and that it is currently active.

For more information about Azure subscriptions, refer to the [prerequisites section](#prerequisites).

#### Authorization error

After you've provisioned the compute resource (while creating a deployment), Azure tries to pull the user container image from the workspace Azure Container Registry (ACR) and mount the user model and code artifacts into the user container from the workspace storage account.

To do these, Azure uses [managed identities](../active-directory/managed-identities-azure-resources/overview.md) to access the storage account and the container registry.

- If you created the associated endpoint with System Assigned Identity, Azure role-based access control (RBAC) permission is automatically granted, and no further permissions are needed.

- If you created the associated endpoint with User Assigned Identity, the user's managed identity must have Storage blob data reader permission on the storage account for the workspace, and AcrPull permission on the Azure Container Registry (ACR) for the workspace. Make sure your User Assigned Identity has the right permission.

For more information, please see [Container Registry Authorication Error](#container-registry-authorization-error).

#### Unable to download user container image

It's possible that the user container couldn't be found. Check [container logs](#get-container-logs) to get more details.

Make sure container image is available in workspace ACR.

For example, if image is `testacr.azurecr.io/azureml/azureml_92a029f831ce58d2ed011c3c42d35acb:latest` check the repository with
`az acr repository show-tags -n testacr --repository azureml/azureml_92a029f831ce58d2ed011c3c42d35acb --orderby time_desc --output table`.

#### Unable to download user model

It is possible that the user's model can't be found. Check [container logs](#get-container-logs) to get more details.

Make sure the model is registered to the same workspace as the deployment. To show details for a model in a workspace: 
