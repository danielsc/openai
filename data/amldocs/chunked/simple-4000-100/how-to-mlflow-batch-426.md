> Signatures in MLflow models are optional but they are highly encouraged as they provide a convenient way to early detect data compatibility issues. For more information about how to log models with signatures read [Logging models with a custom signature, environment or samples](how-to-log-mlflow-models.md#logging-models-with-a-custom-signature-environment-or-samples).

You can inspect the model signature of your model by opening the `MLmodel` file associated with your MLflow model. For more details about how signatures work in MLflow see [Signatures in MLflow](concept-mlflow-models.md#signatures).

### Flavor support

Batch deployments only support deploying MLflow models with a `pyfunc` flavor. If you need to deploy a different flavor, see [Using MLflow models with a scoring script](#customizing-mlflow-models-deployments-with-a-scoring-script).

## Customizing MLflow models deployments with a scoring script

MLflow models can be deployed to batch endpoints without indicating a scoring script in the deployment definition. However, you can opt in to indicate this file (usually referred as the *batch driver*) to customize how inference is executed. 

You will typically select this workflow when: 
> [!div class="checklist"]
> * You need to process a file type not supported by batch deployments MLflow deployments.
> * You need to customize the way the model is run, for instance, use an specific flavor to load it with `mlflow.<flavor>.load()`.
> * You need to do pre/pos processing in your scoring routine when it is not done by the model itself.
> * The output of the model can't be nicely represented in tabular data. For instance, it is a tensor representing an image.
> * You model can't process each file at once because of memory constrains and it needs to read it in chunks.

> [!IMPORTANT]
> If you choose to indicate an scoring script for an MLflow model deployment, you will also have to specify the environment where the deployment will run.

> [!WARNING]
> Customizing the scoring script for MLflow deployments is only available from the Azure CLI or SDK for Python. If you are creating a deployment using [Azure ML studio UI](https://ml.azure.com), please switch to the CLI or the SDK.


### Steps

Use the following steps to deploy an MLflow model with a custom scoring script.

1. Identify the folder where your MLflow model is placed.

    a. Go to [Azure Machine Learning portal](https://ml.azure.com).

    b. Go to the section __Models__.

    c. Select the model you are trying to deploy and click on the tab __Artifacts__.

    d. Take note of the folder that is displayed. This folder was indicated when the model was registered.

    :::image type="content" source="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-model-folder-name.png" lightbox="media/how-to-deploy-mlflow-models-online-endpoints/mlflow-model-folder-name.png" alt-text="Screenshot showing the folder where the model artifacts are placed.":::

1. Create a scoring script. Notice how the folder name `model` you identified before has been included in the `init()` function.

   __batch_driver.py__

   ```python
   import os
   import mlflow
   import pandas as pd

   def init():
       global model

       # AZUREML_MODEL_DIR is an environment variable created during deployment
       # It is the path to the model folder
       model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")
       model = mlflow.pyfunc.load_model(model_path)

   def run(mini_batch):
       results = pd.DataFrame(columns=['file', 'predictions'])

       for file_path in mini_batch:        
           data = pd.read_csv(file_path)
           pred = model.predict(data)

           df = pd.DataFrame(pred, columns=['predictions'])
           df['file'] = os.path.basename(file_path)
           results = pd.concat([results, df])

       return results
   ```

1. Let's create an environment where the scoring script can be executed. Since our model is MLflow, the conda requirements are also specified in the model package (for more details about MLflow models and the files included on it see [The MLmodel format](concept-mlflow-models.md#the-mlmodel-format)). We are going then to build the environment using the conda dependencies from the file. However, __we need also to include__ the package `azureml-core` which is required for Batch Deployments.
