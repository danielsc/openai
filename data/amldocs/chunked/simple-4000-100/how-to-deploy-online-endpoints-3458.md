> You can control which Azure Active Directory security principals can get the authentication key by assigning them to a custom role that allows `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/token/action` and `Microsoft.MachineLearningServices/workspaces/onlineEndpoints/listkeys/action`. For more information, see [Manage access to an Azure Machine Learning workspace](how-to-assign-roles.md).

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

Next, use curl to score data.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="test_endpoint_using_curl" :::

Notice we use `show` and `get-credentials` commands to get the authentication credentials. Also notice that we're using the `--query` flag to filter attributes to only what we need. To learn more about `--query`, see [Query Azure CLI command output](/cli/azure/query-azure-cli).

To see the invocation logs, run `get-logs` again.

For information on authenticating using a token, see [Authenticate to online endpoints](how-to-authenticate-online-endpoint.md).


# [Python](#tab/python)

Using the `MLClient` created earlier, we'll get a handle to the endpoint. The endpoint can be invoked using the `invoke` command with the following parameters:

* `endpoint_name` - Name of the endpoint
* `request_file` - File with request data
* `deployment_name` - Name of the specific deployment to test in an endpoint

We'll send a sample request using a [json](https://github.com/Azure/azureml-examples/blob/main/sdk/python/endpoints/online/model-1/sample-request.json) file.

```python
# test the blue deployment with some sample data
ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="blue",
    request_file="../model-1/sample-request.json",
)
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

You can use either the `invoke` command or a REST client of your choice to invoke the endpoint and score some data: 
