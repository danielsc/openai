
You can test mirror traffic by invoking the endpoint several times:

```azurecli
for i in {1..20} ; do
    az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
done
```

# [Python](#tab/python)

The following command mirrors 10% of the traffic to the `green` deployment:

```python
endpoint.mirror_traffic = {"green": 10}
ml_client.begin_create_or_update(endpoint).result()
```

You can test mirror traffic by invoking the endpoint several times:
```python
# You can test mirror traffic by invoking the endpoint several times
for i in range(20):
    ml_client.online_endpoints.invoke(
        endpoint_name=online_endpoint_name,
        request_file="../model-1/sample-request.json",
    )
```


Mirroring has the following limitations:
* You can only mirror traffic to one deployment.
* Mirror traffic isn't currently supported for Kubernetes online endpoints.
* The maximum mirrored traffic you can configure is 50%. This limit is to reduce the impact on your endpoint bandwidth quota.

Also note the following behavior:
* A deployment can only be set to live or mirror traffic, not both.
* You can send traffic directly to the mirror deployment by specifying the deployment set for mirror traffic.
* You can send traffic directly to a live deployment by specifying the deployment set for live traffic, but in this case the traffic won't be mirrored to the mirror deployment. Mirror traffic is routed from traffic sent to endpoint without specifying the deployment. 

> [!TIP]
> You can use `--deployment-name` option [for CLI v2](/cli/azure/ml/online-endpoint#az-ml-online-endpoint-invoke-optional-parameters), or `deployment_name` option [for SDK v2](/python/api/azure-ai-ml/azure.ai.ml.operations.onlineendpointoperations#azure-ai-ml-operations-onlineendpointoperations-invoke) to specify the deployment to be routed to.

:::image type="content" source="./media/how-to-safely-rollout-managed-endpoints/endpoint-concept-mirror.png" alt-text="Diagram showing 10% traffic mirrored to one deployment.":::

# [Azure CLI](#tab/azure-cli)
You can confirm that the specific percentage of the traffic was sent to the `green` deployment by seeing the logs from the deployment:

```azurecli
az ml online-deployment get-logs --name blue --endpoint $ENDPOINT_NAME
```

After testing, you can set the mirror traffic to zero to disable mirroring:

```azurecli
set -e

# <set_endpoint_name>
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

#  endpoint name
export ENDPOINT_NAME=endpt-sr-`echo $RANDOM`

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/managed/sample/endpoint.yml
# </create_endpoint>

# <create_blue>
az ml online-deployment create --name blue --endpoint-name $ENDPOINT_NAME -f endpoints/online/managed/sample/blue-deployment.yml --all-traffic
# </create_blue>

# <test_blue>
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/model-1/sample-request.json
# </test_blue>

# <scale_blue>
az ml online-deployment update --name blue --endpoint-name $ENDPOINT_NAME --set instance_count=2
# </scale_blue>

# <create_green>
az ml online-deployment create --name green --endpoint-name $ENDPOINT_NAME -f endpoints/online/managed/sample/green-deployment.yml
# </create_green>

# <get_traffic>
az ml online-endpoint show -n $ENDPOINT_NAME --query traffic
# </get_traffic>

# <test_green>
az ml online-endpoint invoke --name $ENDPOINT_NAME --deployment-name green --request-file endpoints/online/model-2/sample-request.json
# </test_green>

# supress printing secret
set +x

# <test_green_using_curl_get_key>
#get the key
ENDPOINT_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME -o tsv --query primaryKey)
# </test_green_using_curl_get_key>

set -x

# <test_green_using_curl>
# get the scoring uri
SCORING_URI=$(az ml online-endpoint show -n $ENDPOINT_NAME -o tsv --query scoring_uri)
# use curl to invoke the endpoint
curl --request POST "$SCORING_URI" --header "Authorization: Bearer $ENDPOINT_KEY" --header 'Content-Type: application/json' --header "azureml-model-deployment: green" --data @endpoints/online/model-2/sample-request.json
# </test_green_using_curl>

# <test_green_with_mirror_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --mirror-traffic "green=10"
# </test_green_with_mirror_traffic>

# <reset_mirror_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --mirror-traffic "green=0"
# </reset_mirror_traffic>

# <green_10pct_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --traffic "blue=90 green=10"
# </green_10pct_traffic>

# <green_100pct_traffic>
az ml online-endpoint update --name $ENDPOINT_NAME --traffic "blue=0 green=100"
# </green_100pct_traffic>

# <delete_blue>
az ml online-deployment delete --name blue --endpoint $ENDPOINT_NAME --yes --no-wait
# </delete_blue>

# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes --no-wait
# </delete_endpoint>

```
