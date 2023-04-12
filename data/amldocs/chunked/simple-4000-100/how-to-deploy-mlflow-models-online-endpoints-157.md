
# [Python (MLflow SDK)](#tab/mlflow)

```python
model_name = 'sklearn-diabetes'
model_local_path = "sklearn-diabetes/model"

registered_model = mlflow_client.create_model_version(
    name=model_name, source=f"file://{model_local_path}"
)
version = registered_model.version
```

# [Studio](#tab/studio)

To create a model in Azure Machine Learning, open the Models page in Azure Machine Learning. Select **Register model** and select where your model is located. Fill out the required fields, and then select __Register__.

:::image type="content" source="./media/how-to-manage-models/register-model-as-asset.png" alt-text="Screenshot of the UI to register a model." lightbox="./media/how-to-manage-models/register-model-as-asset.png":::


Alternatively, if your model was logged inside of a run, you can register it directly.

> [!TIP]
> To register the model, you will need to know the location where the model has been stored. If you are using `autolog` feature of MLflow, the path will depend on the type and framework of the model being used. We recommend to check the jobs output to identify which is the name of this folder. You can look for the folder that contains a file named `MLModel`. If you are logging your models manually using `log_model`, then the path is the argument you pass to such method. As an example, if you log the model using `mlflow.sklearn.log_model(my_model, "classifier")`, then the path where the model is stored is `classifier`.

# [Azure CLI](#tab/cli)

Use the Azure ML CLI v2 to create a model from a training job output. In the following example, a model named `$MODEL_NAME` is registered using the artifacts of a job with ID `$RUN_ID`. The path where the model is stored is `$MODEL_PATH`.

```bash
az ml model create --name $MODEL_NAME --path azureml://jobs/$RUN_ID/outputs/artifacts/$MODEL_PATH
```

> [!NOTE]
> The path `$MODEL_PATH` is the location where the model has been stored in the run.

# [Python (Azure ML SDK)](#tab/sdk)

```python
model_name = 'sklearn-diabetes'

ml_client.models.create_or_update(
    Model(
        path=f"azureml://jobs/{RUN_ID}/outputs/artifacts/{MODEL_PATH}"
        name=model_name,
        type=AssetTypes.MLFLOW_MODEL
    )
) 
```

> [!NOTE]
> The path `MODEL_PATH` is the location where the model has been stored in the run.

# [Python (MLflow SDK)](#tab/mlflow)

```python
model_name = 'sklearn-diabetes'

registered_model = mlflow_client.create_model_version(
    name=model_name, source=f"runs://{RUN_ID}/{MODEL_PATH}"
)
version = registered_model.version
```

> [!NOTE]
> The path `MODEL_PATH` is the location where the model has been stored in the run.

# [Studio](#tab/studio)

:::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-register-model-output.gif" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-register-model-output.gif" alt-text="Screenshot showing how to download Outputs and logs from Experimentation run":::


## Deploy an MLflow model to an online endpoint

1. First. we need to configure the endpoint where the model will be deployed. The following example configures the name and authentication mode of the endpoint:
    
    # [Azure CLI](#tab/cli)
    
    __endpoint.yaml__

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/managedOnlineEndpoint.schema.json
name: my-endpoint
auth_mode: key
```

    # [Python (Azure ML SDK)](#tab/sdk)

    ```python
    endpoint_name = "sklearn-diabetes-" + datetime.datetime.now().strftime("%m%d%H%M%f")

    endpoint = ManagedOnlineEndpoint(
        name=endpoint_name,
        description="An online endpoint to generate predictions for the diabetes dataset",
        auth_mode="key",
        tags={"foo": "bar"},
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
