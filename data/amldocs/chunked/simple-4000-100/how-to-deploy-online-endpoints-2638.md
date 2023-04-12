If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run `az ml online-endpoint show --local -n $ENDPOINT_NAME`. In the returned data, find the `scoring_uri` attribute. Sample curl based commands are available later in this doc.

# [Python](#tab/python)

Invoke the endpoint to score the model by using the convenience command invoke and passing query parameters that are stored in a JSON file

```python
ml_client.online_endpoints.invoke(
    endpoint_name=local_endpoint_name,
    request_file="../model-1/sample-request.json",
    local=True,
)
```

If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run the following code. In the returned data, find the `scoring_uri` attribute. Sample curl based commands are available later in this doc.

```python
endpoint = ml_client.online_endpoints.get(endpoint_name)
scoring_uri = endpoint.scoring_uri
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.


### Review the logs for output from the invoke operation

In the example *score.py* file, the `run()` method logs some output to the console. 

# [Azure CLI](#tab/azure-cli)

You can view this output by using the `get-logs` command:

```azurecli
set -e

# <set_endpoint_name> 
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

export ENDPOINT_NAME=endpt-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --local -n $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_deployment>
az ml online-deployment create --local -n blue --endpoint $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml
# </create_deployment>

# <get_status>
az ml online-endpoint show -n $ENDPOINT_NAME --local
# </get_status>

# check if create was successful
endpoint_status=`az ml online-endpoint show --local --name $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $endpoint_status
if [[ $endpoint_status == "Succeeded" ]]
then
  echo "Endpoint created successfully"
else
  echo "Endpoint creation failed"
  exit 1
fi

deploy_status=`az ml online-deployment show --local --name blue --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_endpoint>
az ml online-endpoint invoke --local --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_endpoint>

# <test_endpoint_using_curl>
SCORING_URI=$(az ml online-endpoint show --local -n $ENDPOINT_NAME -o tsv --query scoring_uri)

curl --request POST "$SCORING_URI" --header 'Content-Type: application/json' --data @endpoints/online/model-1/sample-request.json
# </test_endpoint_using_curl>

# <get_logs>
az ml online-deployment get-logs --local -n blue --endpoint $ENDPOINT_NAME
# </get_logs>

# <delete_endpoint>
az ml online-endpoint delete --local --name $ENDPOINT_NAME --yes
# </delete_endpoint>
```

# [Python](#tab/python)

You can view this output by using the `get_logs` method:

```python
ml_client.online_deployments.get_logs(
    name="blue", endpoint_name=local_endpoint_name, local=True, lines=50
)
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.


##  Deploy your online endpoint to Azure

Next, deploy your online endpoint to Azure.

### Deploy to Azure

# [Azure CLI](#tab/azure-cli)

To create the endpoint in the cloud, run the following code:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="create_endpoint" :::

To create the deployment named `blue` under the endpoint, run the following code:

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="create_deployment" :::
