

### Running jobs using a managed identity

You can use managed identities to invoke batch endpoint and deployments. Please notice that this manage identity doesn't belong to the batch endpoint, but it is the identity used to execute the endpoint and hence create a batch job. Both user assigned and system assigned identities can be use in this scenario.

# [Azure CLI](#tab/cli)

On resources configured for managed identities for Azure resources, you can sign in using the managed identity. Signing in with the resource's identity is done through the `--identity` flag. For more details see [Sign in with Azure CLI](/cli/azure/authenticate-azure-cli).

```azurecli
az login --identity
```

Once authenticated, use the following command to run a batch deployment job:

```azurecli
az ml batch-endpoint invoke --name $ENDPOINT_NAME --input https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci
```

# [Python](#tab/sdk)

On resources configured for managed identities for Azure resources, you can sign in using the managed identity. Use the resource ID along with the `ManagedIdentityCredential` object as demonstrated in the following example:

```python
from azure.ai.ml import MLClient
from azure.identity import ManagedIdentityCredential

subscription_id = "<subscription>"
resource_group = "<resource-group>"
workspace = "<workspace>"
resource_id = "<resource-id>"

ml_client = MLClient(ManagedIdentityCredential(resource_id), subscription_id, resource_group, workspace)
```

Once authenticated, use the following command to run a batch deployment job:

```python
job = ml_client.batch_endpoints.invoke(
        endpoint_name, 
        input=Input(path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci")
    )
```

# [REST](#tab/rest)

You can use the REST API of Azure Machine Learning to start a batch endpoints job using a managed identity. The steps vary depending on the underlying service being used. Some examples include (but are not limited to):

* [Managed identity for Azure Data Factory](../data-factory/data-factory-service-identity.md)
* [How to use managed identities for App Service and Azure Functions](../app-service/overview-managed-identity.md).
* [How to use managed identities for Azure resources on an Azure VM to acquire an access token](../active-directory/managed-identities-azure-resources/how-to-use-vm-token.md).

You can also use the Azure CLI to get an authentication token for the managed identity and the pass it to the batch endpoints URI.


## Next steps

* [Network isolation in batch endpoints](how-to-secure-batch-endpoint.md)
* [Invoking batch endpoints from Event Grid events in storage](how-to-use-event-grid-batch.md).
* [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md).
