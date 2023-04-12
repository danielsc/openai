
The output should appear similar to the following JSON. The `provisioning_state` is `Succeeded`.

```json
{
  "auth_mode": "key",
  "location": "local",
  "name": "docs-endpoint",
  "properties": {},
  "provisioning_state": "Succeeded",
  "scoring_uri": "http://localhost:49158/score",
  "tags": {},
  "traffic": {}
}
```

# [Python](#tab/python)

```python
ml_client.online_endpoints.get(name=local_endpoint_name, local=True)
```

The method returns [`ManagedOnlineEndpoint` entity](/python/api/azure-ai-ml/azure.ai.ml.entities.managedonlineendpoint). The `provisioning_state` is `Succeeded`.

```python
ManagedOnlineEndpoint({'public_network_access': None, 'provisioning_state': 'Succeeded', 'scoring_uri': 'http://localhost:49158/score', 'swagger_uri': None, 'name': 'local-10061534497697', 'description': 'this is a sample local endpoint', 'tags': {}, 'properties': {}, 'id': None, 'Resource__source_path': None, 'base_path': '/path/to/your/working/directory', 'creation_context': None, 'serialize': <msrest.serialization.Serializer object at 0x7ffb781bccd0>, 'auth_mode': 'key', 'location': 'local', 'identity': None, 'traffic': {}, 'mirror_traffic': {}, 'kind': None})
```

# [ARM template](#tab/arm)

The template doesn't support local endpoints. See the Azure CLI or Python tabs for steps to test the endpoint locally.


The following table contains the possible values for `provisioning_state`:

| State         | Description                                    |
| ------------- | ---------------------------------------------- |
| __Creating__  | The resource is being created.                 |
| __Updating__  | The resource is being updated.                 |
| __Deleting__  | The resource is being deleted.                 |
| __Succeeded__ | The create/update operation was successful.    |
| __Failed__    | The create/update/delete operation has failed. |

### Invoke the local endpoint to score data by using your model

# [Azure CLI](#tab/azure-cli)

Invoke the endpoint to score the model by using the convenience command `invoke` and passing query parameters that are stored in a JSON file:

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

If you want to use a REST client (like curl), you must have the scoring URI. To get the scoring URI, run `az ml online-endpoint show --local -n $ENDPOINT_NAME`. In the returned data, find the `scoring_uri` attribute. Sample curl based commands are available later in this doc.
