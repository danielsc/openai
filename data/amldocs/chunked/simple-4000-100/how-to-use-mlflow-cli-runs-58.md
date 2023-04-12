To configure the experiment you want to work on use MLflow command [`mlflow.set_experiment()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_experiment).
    
```Python
experiment_name = 'experiment_with_mlflow'
mlflow.set_experiment(experiment_name)
```

# [Using an environment variable](#tab/environ)

You can also set one of the MLflow environment variables [MLFLOW_EXPERIMENT_NAME or MLFLOW_EXPERIMENT_ID](https://mlflow.org/docs/latest/cli.html#cmdoption-mlflow-run-arg-uri) with the experiment name. 

```bash
export MLFLOW_EXPERIMENT_NAME="experiment_with_mlflow"
```


### Start training job

After you set the MLflow experiment name, you can start your training job with `start_run()`. Then use `log_metric()` to activate the MLflow logging API and begin logging your training job metrics.

```Python
import os
from random import random

with mlflow.start_run() as mlflow_run:
    mlflow.log_param("hello_param", "world")
    mlflow.log_metric("hello_metric", random())
    os.system(f"echo 'hello world' > helloworld.txt")
    mlflow.log_artifact("helloworld.txt")
```


For details about how to log metrics, parameters and artifacts in a run using MLflow view [How to log and view metrics](how-to-log-view-metrics.md).

## Track jobs running on Azure Machine Learning


[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Remote runs (jobs) let you train your models in a more robust and repetitive way. They can also leverage more powerful computes, such as Machine Learning Compute clusters. See [What are compute targets in Azure Machine Learning?](concept-compute-target.md) to learn about different compute options.

When submitting runs using jobs, Azure Machine Learning automatically configures MLflow to work with the workspace the job is running in. This means that there is no need to configure the MLflow tracking URI. On top of that, experiments are automatically named based on the details of the job.

> [!IMPORTANT]
> When submitting training jobs to Azure Machine Learning, you don't have to configure the MLflow tracking URI on your training logic as it is already configured for you.

### Creating a training routine

First, you should create a `src` subdirectory and create a file with your training code in a `hello_world.py` file in the `src` subdirectory. All your training code will go into the `src` subdirectory, including `train.py`.

The training code is taken from this [MLfLow example](https://github.com/Azure/azureml-examples/blob/main/cli/jobs/basics/src/hello-mlflow.py) in the Azure Machine Learning example repo. 

Copy this code into the file:

```python
# imports
import os
import mlflow

from random import random

# define functions
def main():
    mlflow.log_param("hello_param", "world")
    mlflow.log_metric("hello_metric", random())
    os.system(f"echo 'hello world' > helloworld.txt")
    mlflow.log_artifact("helloworld.txt")


# run functions
if __name__ == "__main__":
    # run main function
    main()

```


> [!NOTE]
> Note how this sample don't contains the instructions `mlflow.start_run` nor `mlflow.set_experiment`. This is automatically done by Azure Machine Learning.

### Submitting the job

Use the [Azure Machine Learning](how-to-train-model.md) to submit a remote run. When using the Azure Machine Learning CLI (v2), the MLflow tracking URI and experiment name are set automatically and directs the logging from MLflow to your workspace. Learn more about [logging Azure Machine Learning experiments with MLflow](how-to-use-mlflow-cli-runs.md) 


Create a YAML file with your job definition in a `job.yml` file. This file should be created outside the `src` directory. Copy this code into the file:

```azurecli
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
command: python hello-mlflow.py
code: src
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster

```

Open your terminal and use the following to submit the job.
