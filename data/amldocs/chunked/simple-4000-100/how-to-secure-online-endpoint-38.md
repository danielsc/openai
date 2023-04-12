> The end-to-end example in this article comes from the files in the __azureml-examples__ GitHub repository. To clone the samples repository and switch to the repository's `cli/` directory, use the following commands: 
>
> ```azurecli
> git clone https://github.com/Azure/azureml-examples
> cd azureml-examples/cli
> ```

## Limitations

* The `v1_legacy_mode` flag must be disabled (false) on your Azure Machine Learning workspace. If this flag is enabled, you won't be able to create a managed online endpoint. For more information, see [Network isolation with v2 API](how-to-configure-network-isolation-with-v2.md).

* If your Azure Machine Learning workspace has a private endpoint that was created before May 24, 2022, you must recreate the workspace's private endpoint before configuring your online endpoints to use a private endpoint. For more information on creating a private endpoint for your workspace, see [How to configure a private endpoint for Azure Machine Learning workspace](how-to-configure-private-link.md).

* Secure outbound communication creates three private endpoints per deployment. One to the Azure Blob storage, one to the Azure Container Registry, and one to your workspace.

* When you use network isolation with a deployment, Azure Log Analytics is partially supported. All metrics and the `AMLOnlineEndpointTrafficLog` table are supported via Azure Log Analytics. `AMLOnlineEndpointConsoleLog` and `AMLOnlineEndpointEventLog` tables are currently not supported. As a workaround, you can use the [az ml online-deployment get_logs](/cli/azure/ml/online-deployment#az-ml-online-deployment-get-logs) CLI command, the [OnlineDeploymentOperations.get_logs()](/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations#azure-ai-ml-operations-onlinedeploymentoperations-get-logs) Python SDK, or the Deployment log tab in the Azure Machine Learning studio instead. For more information, see [Monitoring online endpoints](how-to-monitor-online-endpoints.md).

* You can configure public access to a __managed online endpoint__ (_inbound_ and _outbound_). You can also configure [public access to an Azure Machine Learning workspace](how-to-configure-private-link.md#enable-public-access).

    Outbound communication from a managed online endpoint deployment is to the _workspace API_. When the endpoint is configured to use __public outbound__, then the workspace must be able to accept that public communication (allow public access).

> [!NOTE]
> Requests to create, update, or retrieve the authentication keys are sent to the Azure Resource Manager over the public network.
 
## Inbound (scoring)

To secure scoring requests to the online endpoint to your virtual network, set the `public_network_access` flag for the endpoint to `disabled`:

# [Azure CLI](#tab/cli)

```azurecli
az ml online-endpoint create -f endpoint.yml --set public_network_access=disabled
```

# [Python](#tab/python)

```python
from azure.ai.ml.entities import ManagedOnlineEndpoint

endpoint = ManagedOnlineEndpoint(name='my-online-endpoint',  
                         description='this is a sample online endpoint', 
                         tags={'foo': 'bar'}, 
                         auth_mode="key", 
                         public_network_access="disabled" 
                         # public_network_access="enabled" 
)
```

# [Studio](#tab/azure-studio)

1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. Select the **Workspaces** page from the left navigation bar.
1. Enter a workspace by clicking its name.
1. Select the **Endpoints** page from the left navigation bar.
1. Select **+ Create** to open the **Create deployment** setup wizard.
1. Disable the **Public network access** flag at the **Create endpoint** step.

    :::image type="content" source="media/how-to-secure-online-endpoint/endpoint-disable-public-network-access.png" alt-text="A screenshot of how to disable public network access for an endpoint." lightbox="media/how-to-secure-online-endpoint/endpoint-disable-public-network-access.png":::
