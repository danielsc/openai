    > We set the flag `--all-traffic` in the create command, which will assign all the traffic to the new deployment.
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_deployments.begin_create_or_update(blue_deployment).result()
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

1. Assign all the traffic to the deployment
    
    So far, the endpoint has one deployment, but none of its traffic is assigned to it. Let's assign it.

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI since we used the `--all-traffic` during creation.*
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    endpoint.traffic = { blue_deployment_name: 100 }
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    traffic_config = {"traffic": {blue_deployment_name: 100}}
    ```

    Write the configuration to a file:

    ```python
    traffic_config_path = "traffic_config.json"
    with open(traffic_config_path, "w") as outfile:
        outfile.write(json.dumps(traffic_config))
    ```

1. Update the endpoint configuration:

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI since we used the `--all-traffic` during creation.*
    
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

1. Create a sample input to test the deployment

    # [Azure CLI](#tab/cli)
    
    __sample.yml__

    ```yaml
    {
        "input_data": {
            "columns": [
                "age",
                "sex",
                "cp",
                "trestbps",
                "chol",
                "fbs",
                "restecg",
                "thalach",
                "exang",
                "oldpeak",
                "slope",
                "ca",
                "thal"
            ],
            "data": [
                [ 48, 0, 3, 130, 275, 0, 0, 139, 0, 0.2, 1, 0, "normal" ]
            ]
        }
    }
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    The following code samples 5 observations from the training dataset, removes the `target` column (as the model will predict it), and creates a request in the file `sample.json` that can be used with the model deployment.

    ```python
    samples = (
        pd.read_csv("data/heart.csv")
        .sample(n=5)
        .drop(columns=["target"])
        .reset_index(drop=True)
    )
    
    with open("sample.json", "w") as f:
        f.write(
            json.dumps(
                {"input_data": json.loads(samples.to_json(orient="split", index=False))}
            )
        )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    The following code samples 5 observations from the training dataset, removes the `target` column (as the model will predict it), and creates a request.

    ```python
    samples = (
        pd.read_csv("data/heart.csv")
        .sample(n=5)
        .drop(columns=["target"])
        .reset_index(drop=True)
    )    
    ```

1. Test the deployment

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    az ml online-endpoint invoke --name $ENDPOINT_NAME --request-file sample.json
    ```
    
    # [Python (Azure ML SDK)](#tab/sdk)
    
    ```python
    ml_client.online_endpoints.invoke(
        endpoint_name=endpoint_name,
        request_file="sample.json",
    )
    ```
    
    # [Python (MLflow SDK)](#tab/mlflow)

    ```python
    deployment_client.predict(
        endpoint=endpoint_name, 
        df=samples
    )
    ```
