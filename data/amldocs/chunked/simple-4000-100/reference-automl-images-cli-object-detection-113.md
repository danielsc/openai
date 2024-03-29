
## YAML: AutoML image object detection pipeline job

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

description: Pipeline using AutoML Image Object Detection task

display_name: pipeline-with-image-object-detection
experiment_name: pipeline-with-automl

settings:
  default_compute: azureml:gpu-cluster

inputs:
  image_object_detection_training_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/training-mltable-folder
  image_object_detection_validation_data:
    type: mltable
    # Update the path, if prepare_data.py is using data_path other than "./data"
    path: data/validation-mltable-folder

jobs:
  image_object_detection_node:
    type: automl
    task: image_object_detection
    log_verbosity: info
    primary_metric: mean_average_precision
    limits:
      timeout_minutes: 180
      max_trials: 10
      max_concurrent_trials: 2
    target_column_name: label
    training_data: ${{parent.inputs.image_object_detection_training_data}}
    validation_data: ${{parent.inputs.image_object_detection_validation_data}}
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
          values: [yolov5]
        learning_rate:
          type: uniform
          min_value: 0.0001
          max_value: 0.001
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
    # currently need to specify outputs "mlflow_model" explicitly to reference it in following nodes
    outputs:
      best_model:
        type: mlflow_model
  register_model_node:
    type: command
    component: file:./components/component_register_model.yaml
    inputs:
      model_input_path: ${{parent.jobs.image_object_detection_node.outputs.best_model}}
      model_base_name: fridge_items_object_detection_model
      
```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
