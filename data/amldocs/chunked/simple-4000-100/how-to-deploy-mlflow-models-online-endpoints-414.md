
    To configure the hardware requirements of your deployment, you need to create a JSON file with the desired configuration:

    ```python
    deploy_config = {
        "instance_type": "Standard_F4s_v2",
        "instance_count": 1,
    }
    ```
    
    > [!NOTE]
    > The full specification of this configuration can be found at [Managed online deployment schema (v2)](reference-yaml-deployment-managed-online.md).
    
    Write the configuration to a file:

    ```python
    deployment_config_path = "deployment_config.json"
    with open(deployment_config_path, "w") as outfile:
        outfile.write(json.dumps(deploy_config))
    ```

    # [Studio](#tab/studio)

    *You will perform this step in the deployment stage.*

    
    > [!NOTE]
    > `scoring_script` and `environment` auto generation are only supported for `pyfunc` model's flavor. To use a different flavor, see [Customizing MLflow model deployments](#customizing-mlflow-model-deployments).

1. Let's create the deployment:
    
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
    ml_client.online_deployments.begin_create_or_update(blue_deployment)
    ```

    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    blue_deployment = deployment_client.create_deployment(
        name=blue_deployment_name,
        endpoint=endpoint_name,
        model_uri=f"models:/{model_name}/{version}",
        config={"deploy-config-file": deployment_config_path},
    )    
    ```

    # [Studio](#tab/studio)

    1. From the __Endpoints__ page, Select **+Create**.

        :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/create-from-endpoints.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/create-from-endpoints.png" alt-text="Screenshot showing create option on the Endpoints UI page.":::
