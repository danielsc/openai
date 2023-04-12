
# CLI (v2) Automated ML image multi-Label classification job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLImageClassificationMultilabelJob.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

For information on all the keys in Yaml syntax, see [Yaml syntax](./reference-automl-images-cli-classification.md#yaml-syntax) of image classification task. Here we only describe the keys that have different values as compared to what's specified for image classification task.

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `task` | const | **Required.** The type of AutoML task. | `image_classification_multilabel` | `image_classification_multilabel` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`iou` | `iou` |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Examples relevant to image multi-label classification job are shown below.

## YAML: AutoML image multi-label classification job

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLJob.schema.json
type: automl

experiment_name: dpv2-cli-automl-image-classification-multilabel-experiment
description: A multi-label Image classification job using fridge items dataset

compute: azureml:gpu-cluster

task: image_classification_multilabel
log_verbosity: debug
primary_metric: iou

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
      values: [vitb16r224]
    learning_rate:
      type: uniform
      min_value: 0.005
      max_value: 0.05
    number_of_epochs:
      type: choice
      values: [15, 30]
    gradient_accumulation_step:
      type: choice
      values: [1, 2]

  - model_name:
      type: choice
      values: [seresnext]
    learning_rate:
      type: uniform
      min_value: 0.005
      max_value: 0.05
    validation_resize_size:
      type: choice
      values: [288, 320, 352]
    validation_crop_size:
      type: choice
      values: [224, 256]
    training_crop_size:
      type: choice
      values: [224, 256]
```

## YAML: AutoML image multi-label classification pipeline job

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

description: Pipeline using AutoML Image Multilabel Classification task

display_name: pipeline-with-image-classification-multilabel
experiment_name: pipeline-with-automl

settings:
  default_compute: azureml:gpu-cluster

inputs:
  image_multilabel_classification_training_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/training-mltable-folder
  image_multilabel_classification_validation_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/validation-mltable-folder

jobs:
  image_multilabel_classification_node:
    type: automl
    task: image_classification_multilabel
    log_verbosity: info
    primary_metric: iou
    limits:
      timeout_minutes: 180
      max_trials: 10
      max_concurrent_trials: 2
    target_column_name: label
    training_data: ${{parent.inputs.image_multilabel_classification_training_data}}
    validation_data: ${{parent.inputs.image_multilabel_classification_validation_data}}
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
          values: [vitb16r224]
        learning_rate:
          type: uniform
          min_value: 0.005
          max_value: 0.05
        number_of_epochs:
          type: choice
          values: [15, 30]
        gradient_accumulation_step:
          type: choice
          values: [1, 2]

      - model_name:
          type: choice
          values: [seresnext]
        learning_rate:
          type: uniform
          min_value: 0.005
          max_value: 0.05
        validation_resize_size:
          type: choice
          values: [288, 320, 352]
        validation_crop_size:
          type: choice
          values: [224, 256]
        training_crop_size:
          type: choice
          values: [224, 256]

    # currently need to specify outputs "mlflow_model" explicitly to reference it in following nodes
    outputs:
      best_model:
        type: mlflow_model
  register_model_node:
    type: command
    component: file:./components/component_register_model.yaml
    inputs:
      model_input_path: ${{parent.jobs.image_multilabel_classification_node.outputs.best_model}}
      model_base_name: fridge_items_multilabel_classification_model
      
```
