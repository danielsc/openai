        :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/create-from-endpoints.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/create-from-endpoints.png" alt-text="Screenshot showing create option on the Endpoints UI page.":::

    1. Provide a name and authentication type for the endpoint, and then select __Next__.
    1. When selecting a model, select the MLflow model registered previously. Select __Next__ to continue.
    1. When you select a model registered in MLflow format, in the Environment step of the wizard, you don't need a scoring script or an environment.

        :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/ncd-wizard.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/ncd-wizard.png" alt-text="Screenshot showing no code and environment needed for MLflow models":::

    1. Complete the wizard to deploy the model to the endpoint.

        :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/review-screen-ncd.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/review-screen-ncd.png" alt-text="Screenshot showing NCD review screen":::

1. Assign all the traffic to the deployment: So far, the endpoint has one deployment, but none of its traffic is assigned to it. Let's assign it.

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI since we used the `--all-traffic` during creation. If you need to change traffic, you can use the command `az ml online-endpoint update --traffic` as explained at [Progressively update traffic](how-to-deploy-mlflow-models-online-progressive.md#progressively-update-the-traffic).*
    
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

    # [Studio](#tab/studio)

    *This step in not required in studio since we assigned the traffic during creation.*

1. Update the endpoint configuration:

    # [Azure CLI](#tab/cli)
    
    *This step in not required in the Azure CLI since we used the `--all-traffic` during creation. If you need to change traffic, you can use the command `az ml online-endpoint update --traffic` as explained at [Progressively update traffic](how-to-deploy-mlflow-models-online-progressive.md#progressively-update-the-traffic).*
    
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

    # [Studio](#tab/studio)

    *This step in not required in studio since we assigned the traffic during creation.*

### Invoke the endpoint

Once your deployment completes, your deployment is ready to serve request. One of the easier ways to test the deployment is by using the built-in invocation capability in the deployment client you are using.

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

> [!NOTE]
> Notice how the key `input_data` has been used in this example instead of `inputs` as used in MLflow serving. This is because Azure Machine Learning requires a different input format to be able to automatically generate the swagger contracts for the endpoints. See [Differences between models deployed in Azure Machine Learning and MLflow built-in server](how-to-deploy-mlflow-models.md#differences-between-models-deployed-in-azure-machine-learning-and-mlflow-built-in-server) for details about expected input format.
