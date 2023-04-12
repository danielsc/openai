
## YAML: AutoML text NER sweeping job

```yaml
$schema: https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLJob.schema.json

type: automl
experiment_name: dpv2-cli-text-ner
description: A text named entity recognition job using CoNLL 2003 data

compute: azureml:gpu-cluster

task: text_ner
primary_metric: accuracy
log_verbosity: debug

limits:
  timeout_minutes: 120
  max_nodes: 4
  max_trials: 2
  max_concurrent_trials: 2

training_data:
  path: "./training-mltable-folder"
  type: mltable
validation_data:
  type: mltable
  path: "./validation-mltable-folder"

# featurization:
#   dataset_language: "eng"

sweep:
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_amount: 0.05
    delay_evaluation: 6

search_space:
  - model_name:
      type: choice
      values: [bert_base_cased, roberta_base]
  - model_name:
      type: choice
      values: [distilroberta_base]
    weight_decay:
      type: uniform
      min_value: 0.01
      max_value: 0.1

```

## YAML: AutoML text NER pipeline job

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline

description: Pipeline using AutoML Text Ner task

display_name: pipeline-with-text-ner
experiment_name: pipeline-with-automl

settings:
  default_compute: azureml:gpu-cluster

inputs:
  text_ner_training_data:
    type: mltable
    path: ./training-mltable-folder
  text_ner_validation_data:
    type: mltable
    path: ./validation-mltable-folder

jobs:
  preprocessing_node:
    type: command
    component: file:./components/component_preprocessing.yaml
    inputs:
      train_data: ${{parent.inputs.text_ner_training_data}}
      validation_data: ${{parent.inputs.text_ner_validation_data}}
    outputs:
      preprocessed_train_data:
        type: mltable
      preprocessed_validation_data:
        type: mltable
  text_ner_node:
    type: automl
    task: text_ner
    log_verbosity: info
    primary_metric: accuracy
    limits:
      max_trials: 1
      timeout_minutes: 60
    target_column_name: label
    training_data: ${{parent.jobs.preprocessing_node.outputs.preprocessed_train_data}}
    validation_data: ${{parent.jobs.preprocessing_node.outputs.preprocessed_validation_data}}
    # currently need to specify outputs "mlflow_model" explicitly to reference it in following nodes
    outputs:
      best_model:
        type: mlflow_model
  register_model_node:
    type: command
    component: file:./components/component_register_model.yaml
    inputs:
      model_input_path: ${{parent.jobs.text_ner_node.outputs.best_model}}
      model_base_name: paper_categorization_model
      
```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
