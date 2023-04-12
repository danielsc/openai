| `path` | string | Path can be a `file` path, `folder` path or `pattern` for paths. `pattern` specifies a search pattern to allow globbing(`*` and `**`) of files and folders containing data. Supported URI types are `azureml`, `https`, `wasbs`, `abfss`, and `adl`. For more information on how to use the `azureml://` URI format, see [Core yaml syntax](./reference-yaml-core-syntax.md). URI of the location of the artifact file. If this URI doesn't have a scheme (for example, http:, azureml: etc.), then it's considered a local reference and the file it points to is uploaded to the default workspace blob-storage as the entity is created.  | | |
| `mode` | string | Dataset delivery mechanism. | `direct` | `direct` |
| `type` | const |  In order to generate computer vision models, the user needs to bring labeled image data as input for model training in the form of an MLTable. | mltable | mltable|

### Best model output configuration

| Key | Type | Description | Allowed values |Default value |
| --- | ---- | ----------- | -------------- | ------------ |
| `type` | string | **Required.** Type of best model. AutoML allows only mlflow models. | `mlflow_model` | `mlflow_model` |
| `path` | string | **Required.** URI of the location where the model-artifact file(s) are stored. If this URI doesn't have a scheme (for example, http:, azureml: etc.), then it's considered a local reference and the file it points to is uploaded to the default workspace blob-storage as the entity is created. |  |  |
| `storage_uri` | string | The HTTP URL of the Model. Use this URL with `az storage copy -s THIS_URL -d DESTINATION_PATH --recursive` to download the data.  | | |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Examples relevant to image classification job are linked below.  

## YAML: AutoML image classification job

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLJob.schema.json

type: automl

experiment_name: dpv2-cli-automl-image-classification-experiment
description: A multi-class Image classification job using fridge items dataset

compute: azureml:gpu-cluster

task: image_classification
log_verbosity: debug
primary_metric: accuracy

target_column_name: label
training_data:
  # Update the path, if prepare_data.py is using data_path other than "./data"
  path: data/training-mltable-folder
  type: mltable
validation_data:
  # Update the path, if prepare_data.py is using data_path other than "./data"
  path: data/validation-mltable-folder
  type: mltable

limits:
  timeout_minutes: 60
  max_trials: 10
  max_concurrent_trials: 2

training_parameters:
  early_stopping: True
  evaluation_frequency: 1

sweep:
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_factor: 0.2
    delay_evaluation: 6

search_space:
  - model_name:
      type: choice
      values: [vitb16r224, vits16r224]
    learning_rate:
      type: uniform
      min_value: 0.001
      max_value: 0.01
    number_of_epochs:
      type: choice
      values: [15, 30]

  - model_name:
      type: choice
      values: [seresnext, resnet50]
    learning_rate:
      type: uniform
      min_value: 0.001
      max_value: 0.01
    layers_to_freeze:
      type: choice
      values: [0, 2]

```

## YAML: AutoML image classification pipeline job

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

description: Pipeline using AutoML Image Multiclass Classification task

display_name: pipeline-with-image-classification
experiment_name: pipeline-with-automl

settings:
  default_compute: azureml:gpu-cluster

inputs:
  image_multiclass_classification_training_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/training-mltable-folder
  image_multiclass_classification_validation_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/validation-mltable-folder

jobs:
  image_multiclass_classification_node:
    type: automl
    task: image_classification
    log_verbosity: info
    primary_metric: accuracy
    limits:
      timeout_minutes: 180
      max_trials: 10
      max_concurrent_trials: 2
    target_column_name: label
    training_data: ${{parent.inputs.image_multiclass_classification_training_data}}
    validation_data: ${{parent.inputs.image_multiclass_classification_validation_data}}
    sweep:
      sampling_algorithm: random
      early_termination:
        type: bandit
        evaluation_interval: 2
        slack_factor: 0.2
        delay_evaluation: 6
    search_space:
      - model_name:
          type: choice
          values: [vitb16r224, vits16r224]
        learning_rate:
          type: uniform
          min_value: 0.001
          max_value: 0.01
        number_of_epochs:
          type: choice
          values: [15, 30]

      - model_name:
          type: choice
          values: [seresnext, resnet50]
        learning_rate:
          type: uniform
          min_value: 0.001
          max_value: 0.01
        layers_to_freeze:
          type: choice
          values: [0, 2]
    training_parameters:
      early_stopping: True
      evaluation_frequency: 1
    # currently need to specify outputs "mlflow_model" explicitly to reference it in following nodes
    outputs:
      best_model:
        type: mlflow_model
  register_model_node:
    type: command
    component: file:./components/component_register_model.yaml
    inputs:
      model_input_path: ${{parent.jobs.image_multiclass_classification_node.outputs.best_model}}
      model_base_name: fridge_items_multiclass_classification_model
      
```
