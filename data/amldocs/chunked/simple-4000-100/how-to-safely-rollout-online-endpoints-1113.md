Though `green` has 0% of traffic allocated, you can still invoke the endpoint and deployment with the [json](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/model-2/sample-request.json) file.

```python
ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="green",
    request_file="../model-2/sample-request.json",
)
```


## Test the deployment with mirrored traffic (preview)
[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

Once you've tested your `green` deployment, you can 'mirror' (or copy) a percentage of the live traffic to it. Mirroring traffic (also called shadowing) doesn't change the results returned to clients. Requests still flow 100% to the `blue` deployment. The mirrored percentage of the traffic is copied and submitted to the `green` deployment so you can gather metrics and logging without impacting your clients. Mirroring is useful when you want to validate a new deployment without impacting clients; for example, to check if latency is within acceptable bounds and that there are no HTTP errors. Testing the new deployment with traffic mirroring/shadowing is also known as [shadow testing](https://microsoft.github.io/code-with-engineering-playbook/automated-testing/shadow-testing/). The deployment receiving the mirrored traffic (in this case, the `green` deployment) can also be called the shadow deployment.

> [!WARNING]
> Mirroring traffic uses your [endpoint bandwidth quota](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints) (default 5 MBPS). Your endpoint bandwidth will be throttled if you exceed the allocated quota. For information on monitoring bandwidth throttling, see [Monitor managed online endpoints](how-to-monitor-online-endpoints.md#metrics-at-endpoint-scope).

> [!IMPORTANT]
> Mirrored traffic is supported for the CLI (v2) (version 2.4.0 or above) and Python SDK (v2) (version 1.0.0 or above). If you update the endpoint using an older version of CLI/SDK or Studio UI, the setting for mirrored traffic will be removed.

# [Azure CLI](#tab/azure-cli)

The following command mirrors 10% of the traffic to the `green` deployment:

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
