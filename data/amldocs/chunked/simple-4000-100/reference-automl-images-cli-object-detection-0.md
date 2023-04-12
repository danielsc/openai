
# CLI (v2) Automated ML image object detection job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLImageObjectDetectionJob.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

For information on all the keys in Yaml syntax, see [Yaml syntax](./reference-automl-images-cli-classification.md#yaml-syntax) of image classification task. Here we only describe the keys that have different values as compared to what's specified for image classification task.

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `task` | const | **Required.** The type of AutoML task. | `image_object_detection` | `image_object_detection` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`mean_average_precision` | `mean_average_precision` |
| `training_parameters` | object | Dictionary containing training parameters for the job. Provide an object that has keys as listed in following sections. <br> - [Model Specific Hyperparameters](./reference-automl-images-hyperparameters.md#model-specific-hyperparameters) for yolov5 (if you're using yolov5 for object detection) <br> - [Model agnostic hyperparameters](./reference-automl-images-hyperparameters.md#model-agnostic-hyperparameters) <br> - [Object detection and instance segmentation task specific hyperparameters](./reference-automl-images-hyperparameters.md#object-detection-and-instance-segmentation-task-specific-hyperparameters). <br> <br> For an example, see [Supported model architectures](./how-to-auto-train-image-models.md?tabs=cli#supported-model-architectures) section.| | |

## Remarks

The `az ml job` command can be used for managing Azure Machine Learning jobs.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs). Examples relevant to image object detection job are shown below.

## YAML: AutoML image object detection job

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLJob.schema.json
type: automl

# <experiment_name>
experiment_name: dpv2-cli-automl-image-object-detection-experiment
# </experiment_name>
description: An Image Object Detection job using fridge items dataset

# <compute_settings>
compute: azureml:gpu-cluster
# </compute_settings>

# <task_settings>
task: image_object_detection
log_verbosity: debug
primary_metric: mean_average_precision
# </task_settings>

# <mltable_settings>
target_column_name: label
training_data:
  # Update the path, if prepare_data.py is using data_path other than "./data"
  path: data/training-mltable-folder
  type: mltable
validation_data:
  # Update the path, if prepare_data.py is using data_path other than "./data"
  path: data/validation-mltable-folder
  type: mltable
# </mltable_settings>

# <limit_settings>
limits:
  timeout_minutes: 60
  max_trials: 10
  max_concurrent_trials: 2
# </limit_settings>

# <fixed_settings>
training_parameters:
  early_stopping: True
  evaluation_frequency: 1
# </fixed_settings>

# <sweep_settings>
sweep:
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_factor: 0.2
    delay_evaluation: 6
# </sweep_settings>

# <search_space_settings>
search_space:
  - model_name:
      type: choice
      values: [yolov5]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.01
    model_size:
      type: choice
      values: ['small', 'medium']
  - model_name:
      type: choice
      values: [fasterrcnn_resnet50_fpn]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.001
    optimizer:
      type: choice
      values: ['sgd', 'adam', 'adamw']
    min_size:
      type: choice
      values: [600, 800]
# </search_space_settings>

```
