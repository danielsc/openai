> Notice how the key `input_data` has been used in this example instead of `inputs` as used in MLflow serving. This is because Azure Machine Learning requires a different input format to be able to automatically generate the swagger contracts for the endpoints. See [Differences between models deployed in Azure Machine Learning and MLflow built-in server](how-to-deploy-mlflow-models.md#differences-between-models-deployed-in-azure-machine-learning-and-mlflow-built-in-server) for details about expected input format.

To submit a request to the endpoint, you can do as follows:

# [Azure CLI](#tab/cli)

```azurecli
set -e

# <set_endpoint_name>
export ENDPOINT_NAME="<YOUR_ENDPOINT_NAME>"
# </set_endpoint_name>

#  endpoint name
export ENDPOINT_NAME=endpt-ncd-`echo $RANDOM`
AML_MODEL_NAME=mir-sample-sklearn-ncd-model
echo $AML_MODEL_NAME

# <create_endpoint>
az ml online-endpoint create --name $ENDPOINT_NAME -f endpoints/online/ncd/create-endpoint.yaml
# </create_endpoint>

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

# cleanup of existing model
model_archive=$(az ml model archive -n $AML_MODEL_NAME --version 1 || true)

# <create_sklearn_deployment>
az ml online-deployment create --name sklearn-deployment --endpoint $ENDPOINT_NAME -f endpoints/online/ncd/sklearn-deployment.yaml --all-traffic
# </create_sklearn_deployment>

deploy_status=`az ml online-deployment show --name sklearn-deployment --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_sklearn_deployment>
az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/ncd/sample-request-sklearn.json
# </test_sklearn_deployment>

# <create_lightgbm_deployment>
az ml online-deployment create --name lightgbm-deployment --endpoint $ENDPOINT_NAME -f endpoints/online/ncd/lightgbm-deployment.yaml
# </create_lightgbm_deployment>

deploy_status=`az ml online-deployment show --name lightgbm-deployment --endpoint $ENDPOINT_NAME --query "provisioning_state" -o tsv`
echo $deploy_status
if [[ $deploy_status == "Succeeded" ]]
then
  echo "Deployment completed successfully"
else
  echo "Deployment failed"
  exit 1
fi

# <test_lightgbm_deployment>
az ml online-endpoint invoke --name $ENDPOINT_NAME --deployment lightgbm-deployment --request-file endpoints/online/ncd/sample-request-lightgbm.json
# </test_lightgbm_deployment>

# cleanup of model
model_archive=$(az ml model archive -n $AML_MODEL_NAME --version 1 || true)

# <delete_endpoint>
az ml online-endpoint delete --name $ENDPOINT_NAME --yes 
# </delete_endpoint>


```

# [Python (Azure ML SDK)](#tab/sdk)

```python
ml_client.online_endpoints.invoke(
    endpoint_name=endpoint_name,
    request_file="sample-request-sklearn.json",
)
```

# [Python (MLflow SDK)](#tab/mlflow)

```python
# Read the sample request we have in the json file to construct a pandas data frame
with open("sample-request-sklearn.json", "r") as f:
    sample_request = json.loads(f.read())
    samples = pd.DataFrame(**sample_request["input_data"])

deployment_client.predict(endpoint=endpoint_name, df=samples)
```

# [Studio](#tab/studio)

MLflow models can use the __Test__ tab to create invocations to the created endpoints. To do that:

1. Go to the __Endpoints__ tab and select the new endpoint created.
1. Go to the __Test__ tab.
1. Paste the content of the file `sample-request-sklearn.json`.
1. Click on __Test__.
1. The predictions will show up in the box on the right.


The response will be similar to the following text:

```json
[ 
  11633.100167144921,
  8522.117402884991
]
```

> [!IMPORTANT]
> For MLflow no-code-deployment, **[testing via local endpoints](how-to-deploy-online-endpoints.md#deploy-and-debug-locally-by-using-local-endpoints)** is currently not supported.
