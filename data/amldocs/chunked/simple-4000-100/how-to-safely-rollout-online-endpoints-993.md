
If you want to use a REST client to invoke the deployment directly without going through traffic rules, set the following HTTP header: `azureml-model-deployment: <deployment-name>`. The below code snippet uses `curl` to invoke the deployment directly. The code snippet should work in Unix/WSL environments:

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

# [Python](#tab/python)

Create a new deployment for your managed online endpoint and name the deployment `green`:

```python
# create green deployment
model2 = Model(path="../model-2/model/sklearn_regression_model.pkl")
env2 = Environment(
    conda_file="../model-2/environment/conda.yml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
)

green_deployment = ManagedOnlineDeployment(
    name="green",
    endpoint_name=online_endpoint_name,
    model=model2,
    environment=env2,
    code_configuration=CodeConfiguration(
        code="../model-2/onlinescoring", scoring_script="score.py"
    ),
    instance_type="Standard_DS3_v2",
    instance_count=1,
)
```

```python
# use MLClient to create green deployment
ml_client.online_deployments.begin_create_or_update(green_deployment).result()
```

> [!NOTE]
> If you're creating a deployment for a Kubernetes online endpoint, use the `KubernetesOnlineDeployment` class and specify a [Kubernetes instance type](how-to-manage-kubernetes-instance-types.md) in your Kubernetes cluster.

### Test the new deployment

Though `green` has 0% of traffic allocated, you can still invoke the endpoint and deployment with the [json](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/model-2/sample-request.json) file.
