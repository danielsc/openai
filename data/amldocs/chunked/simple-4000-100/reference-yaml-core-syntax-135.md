For a pipeline job YAML file, the `inputs` and `outputs` sections of each child job are evaluated within the parent context (the top-level pipeline job). The `command`, on the other hand, will resolve to the current context (the child job).

There are two ways to bind inputs and outputs in a pipeline job:

**Bind to the top-level inputs and outputs of the pipeline job**

You can bind the inputs or outputs of a child job (a pipeline step) to the inputs/outputs of the top-level parent pipeline job using the following syntax: `${{parent.inputs.<input_name>}}` or `${{parent.outputs.<output_name>}}`. This reference resolves to the `parent` context; hence the top-level inputs/outputs. 

In the example below, the input (`raw_data`) of the first `prep` step is bound to the top-level pipeline input via `${{parent.inputs.input_data}}`. The output (`model_dir`) of the final `train` step is bound to the top-level pipeline job output via `${{parent.outputs.trained_model}}`.

**Bind to the inputs and outputs of another child job (step)**

To bind the inputs/outputs of one step to the inputs/outputs of another step, use the following syntax: `${{parent.jobs.<step_name>.inputs.<input_name>}}` or `${{parent.jobs.<step_name>.outputs.<outputs_name>}}`. Again, this reference resolves to the parent context, so the expression must start with `parent.jobs.<step_name>`.

In the example below, the input (`training_data`) of the `train` step is bound to the output (`clean_data`) of the `prep` step via `${{parent.jobs.prep.outputs.clean_data}}`. The prepared data from the `prep` step will be used as the training data for the `train` step.

On the other hand, the context references within the `command` properties will resolve to the current context. For example, the `${{inputs.raw_data}}` reference in the `prep` step's `command` will resolve to the inputs of the current context, which is the `prep` child job. The lookup will be done on `prep.inputs`, so an input named `raw_data` must be defined there.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
inputs:
  input_data: 
    type: uri_folder
    path: https://azuremlexamples.blob.core.windows.net/datasets/cifar10/
outputs:
  trained_model:
jobs:
  prep:
    type: command
    inputs:
      raw_data: ${{parent.inputs.input_data}}
    outputs:
      clean_data:
    code: src/prep
    environment: azureml:AzureML-Minimal@latest
    command: >-
      python prep.py 
      --raw-data ${{inputs.raw_data}} 
      --prep-data ${{outputs.clean_data}}
    compute: azureml:cpu-cluster
  train:
    type: command
    inputs: 
      training_data: ${{parent.jobs.prep.outputs.clean_data}}
      num_epochs: 1000
    outputs:
      model_dir: ${{parent.outputs.trained_model}}
    code: src/train
    environment: azureml:AzureML-Minimal@latest
    command: >-
      python train.py 
      --epochs ${{inputs.num_epochs}}
      --training-data ${{inputs.training_data}} 
      --model-output ${{outputs.model_dir}}
    compute: azureml:gpu-cluster
```

### Parameterizing the `command` with the `inputs` and `outputs` contexts of a component

Similar to the `command` for a job, the `command` for a component can also be parameterized with references to the `inputs` and `outputs` contexts. In this case the reference is to the component's inputs and outputs. When the component is run in a job, Azure ML will resolve those references to the job runtime input and output values specified for the respective component inputs and outputs. Below is an example of using the context syntax for a command component YAML specification.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
name: train_data_component_cli
display_name: train_data
description: A example train component
tags:
  author: azureml-sdk-team
version: 7
type: command
inputs:
  training_data: 
    type: uri_folder
  max_epocs:
    type: integer
    optional: true
  learning_rate: 
    type: number
    default: 0.01
    optional: true
  learning_rate_schedule: 
    type: string
    default: time-based
    optional: true
outputs:
  model_output:
    type: uri_folder
code: ./train_src
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu:1
command: >-
  python train.py 
  --training_data ${{inputs.training_data}} 
  $[[--max_epocs ${{inputs.max_epocs}}]]
  $[[--learning_rate ${{inputs.learning_rate}}]]
  $[[--learning_rate_schedule ${{inputs.learning_rate_schedule}}]]
  --model_output ${{outputs.model_output}}

```
