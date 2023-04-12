

> [!TIP]
> * Use [Troubleshooting online endpoints deployment](./how-to-troubleshoot-online-endpoints.md) to debug errors.

### Check the status of the endpoint

# [Azure CLI](#tab/azure-cli)

The `show` command contains information in `provisioning_status` for endpoint and deployment:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_status" :::

You can list all the endpoints in the workspace in a table format by using the `list` command:

```azurecli
az ml online-endpoint list --output table
```

# [Python](#tab/python)

Check the status to see whether the model was deployed without error:

```python
ml_client.online_endpoints.get(name=online_endpoint_name)
```

You can list all the endpoints in the workspace in a table format by using the `list` method:

```python
for endpoint in ml_client.online_endpoints.list():
    print(endpoint.name)
```

The method returns list (iterator) of `ManagedOnlineEndpoint` entities. You can get other information by specifying [parameters](/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint#parameters).

For example, output the list of endpoints like a table:

```python
print("Kind\tLocation\tName")
print("-------\t----------\t------------------------")
for endpoint in ml_client.online_endpoints.list():
    print(f"{endpoint.kind}\t{endpoint.location}\t{endpoint.name}")
```

# [ARM template](#tab/arm)

> [!TIP]
> While templates are useful for deploying resources, they can't be used to list, show, or invoke resources.

The `show` command contains information in `provisioning_status` for endpoint and deployment:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="get_status" :::

You can list all the endpoints in the workspace in a table format by using the `list` command:

```azurecli
az ml online-endpoint list --output table
```


### Check the status of the online deployment

Check the logs to see whether the model was deployed without error:

# [Azure CLI](#tab/azure-cli)

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
