Batch Endpoint can only deploy registered models. In this case, we already have a local copy of the model in the repository, so we only need to publish the model to the registry in the workspace. You can skip this step if the model you are trying to deploy is already registered.
   
# [Azure CLI](#tab/cli)

```azurecli
MODEL_NAME='heart-classifier'
az ml model create --name $MODEL_NAME --type "mlflow_model" --path "heart-classifier-mlflow/model"
```

# [Python](#tab/sdk)

```python
model_name = 'heart-classifier'
model = ml_client.models.create_or_update(
     Model(name=model_name, path='heart-classifier-mlflow/model', type=AssetTypes.MLFLOW_MODEL)
)
```

> [!NOTE]
> The model used in this tutorial is an MLflow model. However, the steps apply for both MLflow models and custom models.

### Creating a scoring script

We need to create a scoring script that can read the input data provided by the batch deployment and return the scores of the model. We are also going to write directly to the output folder of the job. In summary, the proposed scoring script does as follows:

1. Reads the input data as CSV files.
2. Runs an MLflow model `predict` function over the input data.
3. Appends the predictions to a `pandas.DataFrame` along with the input data.
4. Writes the data in a file named as the input file, but in `parquet` format.

__batch_driver_parquet.py__

```python
import os
import mlflow
import pandas as pd
from pathlib import Path

def init():
    global model
    global output_path

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    # It is the path to the model folder
    # Please provide your model's folder name if there's one:
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")
    output_path = os.environ['AZUREML_BI_OUTPUT_PATH']
    model = mlflow.pyfunc.load_model(model_path)

def run(mini_batch):
    for file_path in mini_batch:        
        data = pd.read_csv(file_path)
        pred = model.predict(data)
        
        data['prediction'] = pred
        
        output_file_name = Path(file_path).stem
        output_file_path = os.path.join(output_path, output_file_name + '.parquet')
        data.to_parquet(output_file_path)
        
     return mini_batch
```

__Remarks:__
* Notice how the environment variable `AZUREML_BI_OUTPUT_PATH` is used to get access to the output path of the deployment job. 
* The `init()` function is populating a global variable called `output_path` that can be used later to know where to write.
* The `run` method returns a list of the processed files. It is required for the `run` function to return a `list` or a `pandas.DataFrame` object.

> [!WARNING]
> Take into account that all the batch executors will have write access to this path at the same time. This means that you need to account for concurrency. In this case, we are ensuring each executor writes its own file by using the input file name as the name of the output folder.

### Creating the deployment

Follow the next steps to create a deployment using the previous scoring script:

1. First, let's create an environment where the scoring script can be executed:

   # [Azure CLI](#tab/cli)
   
   No extra step is required for the Azure ML CLI. The environment definition will be included in the deployment file.
   
   # [Python](#tab/sdk)
   
   Let's get a reference to the environment:
   
   ```python
   environment = Environment(
       conda_file="./heart-classifier-mlflow/environment/conda.yaml",
       image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
   )
   ```

2. MLflow models don't require you to indicate an environment or a scoring script when creating the deployments as it is created for you. However, in this case we are going to indicate a scoring script and environment since we want to customize how inference is executed.

   > [!NOTE]
   > This example assumes you have an endpoint created with the name `heart-classifier-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).
