| `mode` | string | Mode of how the data should be delivered to the compute target. <br><br> For read-only mount (`ro_mount`), the data will be consumed as a mount path. A folder will be mounted as a folder and a file will be mounted as a file. Azure ML will resolve the input to the mount path. <br><br> For `download` mode the data will be downloaded to the compute target. Azure ML will resolve the input to the downloaded path. <br><br> If you only want the URL of the storage location of the data artifact(s) rather than mounting or downloading the data itself, you can use the `direct` mode. This will pass in the URL of the storage location as the job input. In this case you're fully responsible for handling credentials to access the storage. | `ro_mount`, `download`, `direct` | `ro_mount` |

### Job outputs

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | The type of job output. For the default `uri_folder` type, the output will correspond to a folder. | `uri_file`, `uri_folder`, `mltable`, `mlflow_model`  | `uri_folder` |
| `mode` | string | Mode of how output file(s) will get delivered to the destination storage. For read-write mount mode (`rw_mount`) the output directory will be a mounted directory. For upload mode the file(s) written will get uploaded at the end of the job. | `rw_mount`, `upload` | `rw_mount` |

### Identity configurations

#### UserIdentityConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Identity type.  | `user_identity` |

#### ManagedIdentityConfiguration

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** Identity type.  | `managed` or `managed_identity` |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Several are shown below.

## YAML: hello sweep

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/sweepJob.schema.json
type: sweep
trial:
  command: >-
    python hello-sweep.py
    --A ${{inputs.A}}
    --B ${{search_space.B}}
    --C ${{search_space.C}}
  code: src
  environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
inputs:
  A: 0.5
compute: azureml:cpu-cluster
sampling_algorithm: random
search_space:
  B:
    type: choice
    values: ["hello", "world", "hello_world"]
  C:
    type: uniform
    min_value: 0.1
    max_value: 1.0
objective:
  goal: minimize
  primary_metric: random_metric
limits:
  max_total_trials: 4
  max_concurrent_trials: 2
  timeout: 3600
display_name: hello-sweep-example
experiment_name: hello-sweep-example
description: Hello sweep job example.

```

## YAML: basic Python model hyperparameter tuning

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/sweepJob.schema.json
type: sweep
trial:
  code: src
  command: >-
    python main.py 
    --iris-csv ${{inputs.iris_csv}}
    --C ${{search_space.C}}
    --kernel ${{search_space.kernel}}
    --coef0 ${{search_space.coef0}}
  environment: azureml:AzureML-sklearn-0.24-ubuntu18.04-py37-cpu@latest
inputs:
  iris_csv: 
    type: uri_file
    path: wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv
compute: azureml:cpu-cluster
sampling_algorithm: random
search_space:
  C:
    type: uniform
    min_value: 0.5
    max_value: 0.9
  kernel:
    type: choice
    values: ["rbf", "linear", "poly"]
  coef0:
    type: uniform
    min_value: 0.1
    max_value: 1
objective:
  goal: minimize
  primary_metric: training_f1_score
limits:
  max_total_trials: 20
  max_concurrent_trials: 10
  timeout: 7200
display_name: sklearn-iris-sweep-example
experiment_name: sklearn-iris-sweep-example
description: Sweep hyperparemeters for training a scikit-learn SVM on the Iris dataset.

```
