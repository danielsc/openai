    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_endpoints.invoke(
        endpoint_name=endpoint_name,
        deployment_name=green_deployment_name
        request_file="sample.json",
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    deployment_client.predict(
        endpoint=endpoint_name, 
        deployment_name=green_deployment_name, 
        df=samples
    )
    ```


    > [!TIP]
    > Notice how now we are indicating the name of the deployment we want to invoke.

## Progressively update the traffic

One we are confident with the new deployment, we can update the traffic to route some of it to the new deployment. Traffic is configured at the endpoint level:

1. Configure the traffic:

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI*
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    endpoint.traffic = {blue_deployment_name: 90, green_deployment_name: 10}
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    traffic_config = {"traffic": {blue_deployment_name: 90, green_deployment_name: 10}}
    ```

    Write the configuration to a file:

    ```python
    traffic_config_path = "traffic_config.json"
    with open(traffic_config_path, "w") as outfile:
        outfile.write(json.dumps(traffic_config))
    ```

1. Update the endpoint

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint update --name $ENDPOINT_NAME --traffic "default=90 $GREEN_DEPLOYMENT_NAME=10"
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.begin_create_or_update(endpoint).result()
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    deployment_client.update_endpoint(
        endpoint=endpoint_name,
        config={"endpoint-config-file": traffic_config_path},
    )
    ```

1. If you decide to switch the entire traffic to the new deployment, update all the traffic:

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI*
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    endpoint.traffic = {blue_deployment_name: 0, green_deployment_name: 100}
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    traffic_config = {"traffic": {blue_deployment_name: 0, green_deployment_name: 100}}
    ```

    Write the configuration to a file:

    ```python
    traffic_config_path = "traffic_config.json"
    with open(traffic_config_path, "w") as outfile:
        outfile.write(json.dumps(traffic_config))
    ```

1. Update the endpoint

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint update --name $ENDPOINT_NAME --traffic "default=0 $GREEN_DEPLOYMENT_NAME=100"
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.begin_create_or_update(endpoint).result()
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    deployment_client.update_endpoint(
        endpoint=endpoint_name,
        config={"endpoint-config-file": traffic_config_path},
    )
    ```

1. Since the old deployment doesn't receive any traffic, you can safely delete it:

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-deployment delete --endpoint-name $ENDPOINT_NAME --name default
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_deployments.begin_delete(
        name=blue_deployment_name, 
        endpoint_name=endpoint_name
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    deployment_client.delete_deployment(
        blue_deployment_name, 
        endpoint=endpoint_name
    )
    ```


    > [!TIP]
    > Notice that at this point, the former "blue deployment" has been deleted and the new "green deployment" has taken the place of the "blue deployment".


## Clean-up resources

# [Azure CLI](#tab/cli)

```azurecli
az ml online-endpoint delete --name $ENDPOINT_NAME --yes
```
