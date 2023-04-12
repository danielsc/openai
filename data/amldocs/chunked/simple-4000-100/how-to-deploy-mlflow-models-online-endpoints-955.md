1. Once your deployment completes, your deployment is ready to serve request. One of the easier ways to test the deployment is by using a sample request file along with the `invoke` method.

    **sample-request-sklearn.json**
    
```json
{"input_data": {
    "columns": [
      "age",
      "sex",
      "bmi",
      "bp",
      "s1",
      "s2",
      "s3",
      "s4",
      "s5",
      "s6"
    ],
    "data": [
      [ 1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0 ],
      [ 10.0,2.0,9.0,8.0,7.0,6.0,5.0,4.0,3.0,2.0]
    ],
    "index": [0,1]
  }}
```

    To submit a request to the endpoint, you can do as follows:
    
    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file endpoints/online/mlflow/sample-request-sklearn-custom.json
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_endpoints.invoke(
        endpoint_name=endpoint_name,
        deployment_name=deployment.name,
        request_file="sample-request-sklearn.json",
    )
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    *This operation is not supported in MLflow SDK*

    # [Studio](#tab/studio)
    
    MLflow models can use the __Test__ tab to create invocations to the created endpoints. To do that:
    
    1. Go to the __Endpoints__ tab and select the new endpoint created.
    1. Go to the __Test__ tab.
    1. Paste the content of the file `sample-request-sklearn.json`.
    1. Click on __Test__.
    1. The predictions will show up in the box on the right.
    
    
    The response will be similar to the following text:
    
    ```json
    {
      "predictions": [ 
        11633.100167144921,
        8522.117402884991
      ]
    }
    ```

    > [!WARNING]
    > __MLflow 2.0 advisory__: In MLflow 1.X, the key `predictions` will be missing.


## Clean up resources

Once you're done with the endpoint, you can delete the associated resources:

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
