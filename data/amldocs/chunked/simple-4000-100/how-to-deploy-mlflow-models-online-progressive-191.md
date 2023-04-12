    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    endpoint = ManagedOnlineEndpoint(
        name=endpoint_name,
        description="An endpoint to serve predictions of the UCI heart disease problem",
        auth_mode="key",
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    We can configure the properties of this endpoint using a configuration file. In this case, we are configuring the authentication mode of the endpoint to be "key".
    
    ```python
    endpoint_config = {
        "auth_mode": "key",
        "identity": {
            "type": "system_assigned"
        }
    }
    ```

    Let's write this configuration into a `JSON` file:

    ```python
    endpoint_config_path = "endpoint_config.json"
    with open(endpoint_config_path, "w") as outfile:
        outfile.write(json.dumps(endpoint_config))
    ```

1. Create the endpoint:

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint create -n $ENDPOINT_NAME -f endpoint.yml
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_endpoints.begin_create_or_update(endpoint).result()
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    endpoint = deployment_client.create_endpoint(
        name=endpoint_name,
        config={"endpoint-config-file": endpoint_config_path},
    )
    ```

1. Getting the authentication secret for the endpoint.

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    ENDPOINT_SECRET_KEY=$(az ml online-endpoint get-credentials -n $ENDPOINT_NAME | jq -r ".accessToken")
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    endpoint_secret_key = ml_client.online_endpoints.list_keys(
        name=endpoint_name
    ).access_token
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    This functionality is not available in the MLflow SDK. Go to [Azure ML studio](https://ml.azure.com), navigate to the endpoint and retrieve the secret key from there.

### Create a blue deployment

So far, the endpoint is empty. There are no deployments on it. Let's create the first one by deploying the same model we were working on before. We will call this deployment "default" and it will represent our "blue deployment".

1. Configure the deployment

    # [Azure CLI](#tab/cli)
    
    __blue-deployment.yml__

    ```yaml
    $schema: https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json
    name: default
    endpoint_name: heart-classifier-edp
    model: azureml:heart-classifier@latest
    instance_type: Standard_DS2_v2
    instance_count: 1
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)

    ```python
    blue_deployment_name = "default"
    ```

    Configure the hardware requirements of your deployment:
    
    ```python
    blue_deployment = ManagedOnlineDeployment(
        name=blue_deployment_name,
        endpoint_name=endpoint_name,
        model=model,
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    blue_deployment_name = "default"
    ```

    To configure the hardware requirements of your deployment, you need to create a JSON file with the desired configuration:

    ```python
    deploy_config = {
        "instance_type": "Standard_DS2_v2",
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

1. Create the deployment

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-deployment create --endpoint-name $ENDPOINT_NAME -f blue-deployment.yml --all-traffic
    ```
    
    > [!TIP]
    > We set the flag `--all-traffic` in the create command, which will assign all the traffic to the new deployment.
