
### Create a green deployment under the endpoint

Let's imagine that there is a new version of the model created by the development team and it is ready to be in production. We can first try to fly this model and once we are confident, we can update the endpoint to route the traffic to it.

1. Register a new model version

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    MODEL_NAME='heart-classifier'
    az ml model create --name $MODEL_NAME --type "mlflow_model" --path "model"
    ```
    
    Let's get the version number of the new model:

    ```azurecli
    VERSION=$(az ml model show -n heart-classifier --label latest | jq -r ".version")
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    model_name = 'heart-classifier'
    model_local_path = "model"
    
    model = ml_client.models.create_or_update(
         Model(name=model_name, path=model_local_path, type=AssetTypes.MLFLOW_MODEL)
    )
    version = model.version
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)
    
    ```python
    model_name = 'heart-classifier'
    model_local_path = "model"
    
    registered_model = mlflow_client.create_model_version(
        name=model_name, source=f"file://{model_local_path}"
    )
    version = registered_model.version
    ```

1. Configure a new deployment

     # [Azure CLI](#tab/cli)
    
    __green-deployment.yml__

    ```yaml
    $schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
    name: xgboost-model
    endpoint_name: heart-classifier-edp
    model: azureml:heart-classifier@latest
    instance_type: Standard_DS2_v2
    instance_count: 1
    ```
    
    We will name the deployment as follows:

    ```azurecli
    GREEN_DEPLOYMENT_NAME="xgboost-model-$VERSION"
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)

    ```python
    green_deployment_name = f"xgboost-model-{version}"
    ```

    Configure the hardware requirements of your deployment:
    
    ```python
    green_deployment = ManagedOnlineDeployment(
        name=green_deployment_name,
        endpoint_name=endpoint_name,
        model=model,
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    green_deployment_name = f"xgboost-model-{version}"
    ```

    To configure the hardware requirements of your deployment, you need to create a JSON file with the desired configuration:

    ```python
    deploy_config = {
        "instance_type": "Standard_DS2_v2",
        "instance_count": 1,
    }
    ```
    
    > [!TIP]
    > We are using the same hardware confirmation indicated in the `deployment-config-file`. However, there is no requirements to have the same configuration. You can configure different hardware for different models depending on the requirements.
    
    Write the configuration to a file:

    ```python
    deployment_config_path = "deployment_config.json"
    with open(deployment_config_path, "w") as outfile:
        outfile.write(json.dumps(deploy_config))
    ```

1. Create the new deployment

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-deployment create -n $GREEN_DEPLOYMENT_NAME --endpoint-name $ENDPOINT_NAME -f green-deployment.yml
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_deployments.begin_create_or_update(green_deployment).result()
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    new_deployment = deployment_client.create_deployment(
        name=green_deployment_name,
        endpoint=endpoint_name,
        model_uri=f"models:/{model_name}/{version}",
        config={"deploy-config-file": deployment_config_path},
    ) 
    ```

1. Test the deployment without changing traffic

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint invoke --name $ENDPOINT_NAME --deployment-name $GREEN_DEPLOYMENT_NAME --request-file sample.json
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
