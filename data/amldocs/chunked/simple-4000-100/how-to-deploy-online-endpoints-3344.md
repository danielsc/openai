
By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `--container storage-initializer` flag.


# [Python](#tab/python)

You can view this output by using the `get_logs` method:

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=online_endpoint_name, lines=50
)
```

By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `container_type="storage-initializer"` option.

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=online_endpoint_name, lines=50, container_type="storage-initializer"
)
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

```azurecli
set -e

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-moe-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --name blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml --all-traffic
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_endpoint>
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_endpoint>

# supress printing secret
set +x

# <test_endpoint_using_curl_get_key>
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
# </test_endpoint_using_curl_get_key>

set -x

# <test_endpoint_using_curl>
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
# </test_endpoint_using_curl>

# <get_logs>
az ml online-deployment get-logs --name blue --endpoint $ENDPOINT_NAME
# </get_logs>

# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>
```

By default, logs are pulled from inference-server. To see the logs from storage-initializer (it mounts assets like model and code to the container), add the `--container storage-initializer` flag.


For more information on deployment logs, see [Get container logs](how-to-troubleshoot-online-endpoints.md#get-container-logs).

### Invoke the endpoint to score data by using your model

# [Azure CLI](#tab/azure-cli)

You can use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data: 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="test_endpoint" :::

The following example shows how to get the key used to authenticate to the endpoint:

> [!TIP]
> You can control which Azure Active Directory security principals can get the authentication key by assigning them to a custom role that allows `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/token/action` and `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/listkeys/action`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).
