
    Let's write this configuration into a `JSON` file:

    ```python
    endpoint_config_path = "endpoint_config.json"
    with open(endpoint_config_path, "w") as outfile:
        outfile.write(json.dumps(endpoint_config))
    ```

    # [Studio](#tab/studio)

    *You will perform this step in the deployment stage.*

1. Let's create the endpoint:
    
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
    ml_client.begin_create_or_update(endpoint)
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    endpoint = deployment_client.create_endpoint(
        name=endpoint_name,
        config={"endpoint-config-file": endpoint_config_path},
    )
    ```

    # [Studio](#tab/studio)

    *You will perform this step in the deployment stage.*

1. Now, it is time to configure the deployment. A deployment is a set of resources required for hosting the model that does the actual inferencing. 
    
    # [Azure CLI](#tab/cli)

    __sklearn-deployment.yaml__

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
name: sklearn-deployment
endpoint_name: my-endpoint
model:
  name: mir-sample-sklearn-mlflow-model
  version: 1
  path: sklearn-diabetes/model
  type: mlflow_model
instance_type: Standard_DS3_v2
instance_count: 1
```

    # [Python (Azure ML SDK)](#tab/sdk)

    ```python
    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name=endpoint_name,
        model=model,
        instance_type="Standard_F4s_v2",
        instance_count=1
    )
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    blue_deployment_name = "blue"
    ```
