> For MLflow no-code-deployment, **[testing via local endpoints](how-to-deploy-online-endpoints.md#deploy-and-debug-locally-by-using-local-endpoints)** is currently not supported.


## Customizing MLflow model deployments

MLflow models can be deployed to online endpoints without indicating a scoring script in the deployment definition. However, you can opt in to indicate it to customize how inference is executed.

You will typically select this workflow when:

> [!div class="checklist"]
> - You need to customize the way the model is run, for instance, use an specific flavor to load it with `mlflow.<flavor>.load_model()`.
> - You need to do pre/pos processing in your scoring routine when it is not done by the model itself.
> - The output of the model can't be nicely represented in tabular data. For instance, it is a tensor representing an image.
> - Your endpoint is under a private link-enabled workspace.

> [!IMPORTANT]
> If you choose to indicate an scoring script for an MLflow model deployment, you will also have to specify the environment where the deployment will run.

> [!WARNING]
> Customizing the scoring script for MLflow deployments is only available from the Azure CLI or SDK for Python. If you are creating a deployment using [Azure ML studio](https://ml.azure.com), please switch to the CLI or the SDK.

### Steps

Use the following steps to deploy an MLflow model with a custom scoring script.

1. Identify the folder where your MLflow model is placed.

    a. Go to [Azure Machine Learning portal](https://ml.azure.com).

    b. Go to the section __Models__.

    c. Select the model you are trying to deploy and click on the tab __Artifacts__.

    d. Take note of the folder that is displayed. This folder was indicated when the model was registered.

    :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-model-folder-name.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-model-folder-name.png" alt-text="Screenshot showing the folder where the model artifacts are placed.":::

1. Create a scoring script. Notice how the folder name `model` you identified before has been included in the `init()` function.

    __score.py__

    ```python
    import logging
    import mlflow
    import os
    from io import StringIO
    from mlflow.pyfunc.scoring_server import infer_and_parse_json_input, predictions_to_json

    def init():
        global model
        global input_schema
        # The path 'model' corresponds to the path where the MLflow artifacts where stored when
        # registering the model using MLflow format.
        model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model')
        model = mlflow.pyfunc.load_model(model_path)
        input_schema = model.metadata.get_input_schema()
    
    def run(raw_data):
        json_data = json.loads(raw_data)
        if "input_data" not in json_data.keys():
            raise Exception("Request must contain a top level key named 'input_data'")
        
        serving_input = json.dumps(json_data["input_data"])
        data = infer_and_parse_json_input(raw_data, input_schema)
        result = model.predict(data)
        
        result = StringIO()
        predictions_to_json(raw_predictions, result)
        return result.getvalue()
    ```

    > [!TIP]
    > The previous scoring script is provided as an example about how to perform inference of an MLflow model. You can adapt this example to your needs or change any of its parts to reflect your scenario.

    > [!WARNING]
    > __MLflow 2.0 advisory__: The provided scoring script will work with both MLflow 1.X and MLflow 2.X. However, be advised that the expected input/output formats on those versions may vary. Check the environment definition used to ensure you are using the expected MLflow version. Notice that MLflow 2.0 is only supported in Python 3.8+.

1. Let's create an environment where the scoring script can be executed. Since our model is MLflow, the conda requirements are also specified in the model package (for more details about MLflow models and the files included on it see The MLmodel format). We are going then to build the environment using the conda dependencies from the file. However, we need also to include the package `azureml-inference-server-http` which is required for Online Deployments in Azure Machine Learning.
