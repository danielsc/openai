
# How to do hyperparameter tuning in pipeline (v2)

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

In this article, you'll learn how to do hyperparameter tuning in Azure Machine Learning pipeline.

## Prerequisite

1. Understand what is [hyperparameter tuning](how-to-tune-hyperparameters.md) and how to do hyperparameter tuning in Azure Machine Learning use SweepJob.
2. Understand what is a [Azure Machine Learning pipeline](concept-ml-pipelines.md)
3. Build a command component that takes hyperparameter as input.

## How to do hyperparameter tuning in Azure Machine Learning pipeline

This section explains how to do hyperparameter tuning in Azure Machine Learning pipeline using CLI v2 and Python SDK. Both approaches share the same prerequisite: you already have a command component created and the command component takes hyperparameters as inputs. If you don't have a command component yet. Follow below links to create a command component first.

- [AzureML CLI v2](how-to-create-component-pipelines-cli.md)
- [AzureML Python SDK v2](how-to-create-component-pipeline-python.md)

### CLI v2

The example used in this article can be found in [azureml-example repo](https://github.com/Azure/azureml-examples). Navigate to *[azureml-examples/cli/jobs/pipelines-with-components/pipeline_with_hyperparameter_sweep* to check the example.

Assume you already have a command component defined in `train.yaml`. A two-step pipeline job (train and predict) YAML file looks like below.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json
type: pipeline
display_name: pipeline_with_hyperparameter_sweep
description: Tune hyperparameters using TF component
settings:
    default_compute: azureml:cpu-cluster
jobs:
  sweep_step:
    type: sweep
    inputs:
      data: 
        type: uri_file
        path: wasbs://datasets@azuremlexamples.blob.core.windows.net/iris.csv
      degree: 3
      gamma: "scale"
      shrinking: False
      probability: False
      tol: 0.001
      cache_size: 1024
      verbose: False
      max_iter: -1
      decision_function_shape: "ovr"
      break_ties: False
      random_state: 42
    outputs:
      model_output:
      test_data:
    sampling_algorithm: random
    trial: ./train.yml
    search_space:
      c_value:
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
      max_total_trials: 5
      max_concurrent_trials: 3
      timeout: 7200

  predict_step:
    type: command
    inputs:
      model: ${{parent.jobs.sweep_step.outputs.model_output}}
      test_data: ${{parent.jobs.sweep_step.outputs.test_data}}
    outputs:
      predict_result:
    component: ./predict.yml

    
```

The `sweep_step` is the step for hyperparameter tuning. Its type needs to be `sweep`.  And `trial` refers to the command component defined in `train.yaml`. From the `search space` field we can see three hyparmeters (`c_value`, `kernel`, and `coef`) are added to the search space. After you submit this pipeline job, Azure Machine Learning will run the trial component multiple times to sweep over hyperparameters based on the search space and terminate policy you defined in `sweep_step`. Check [sweep job YAML schema](reference-yaml-job-sweep.md) for full schema of sweep job.

Below is the trial component definition (train.yml file). 

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
type: command

name: train_model
display_name: train_model
version: 1

inputs: 
  data:
    type: uri_folder
  c_value:
    type: number
    default: 1.0
  kernel:
    type: string
    default: rbf
  degree:
    type: integer
    default: 3
  gamma:
    type: string
    default: scale
  coef0: 
    type: number
    default: 0
  shrinking:
    type: boolean
    default: false
  probability:
    type: boolean
    default: false
  tol:
    type: number
    default: 1e-3
  cache_size:
    type: number
    default: 1024
  verbose:
    type: boolean
    default: false
  max_iter:
    type: integer
    default: -1
  decision_function_shape:
    type: string
    default: ovr
  break_ties:
    type: boolean
    default: false
  random_state:
    type: integer
    default: 42

outputs:
  model_output:
    type: mlflow_model
  test_data:
    type: uri_folder
  
code: ./train-src

environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest

command: >-
  python train.py 
  --data ${{inputs.data}}
  --C ${{inputs.c_value}}
  --kernel ${{inputs.kernel}}
  --degree ${{inputs.degree}}
  --gamma ${{inputs.gamma}}
  --coef0 ${{inputs.coef0}}
  --shrinking ${{inputs.shrinking}}
  --probability ${{inputs.probability}}
  --tol ${{inputs.tol}}
  --cache_size ${{inputs.cache_size}}
  --verbose ${{inputs.verbose}}
  --max_iter ${{inputs.max_iter}}
  --decision_function_shape ${{inputs.decision_function_shape}}
  --break_ties ${{inputs.break_ties}}
  --random_state ${{inputs.random_state}}
  --model_output ${{outputs.model_output}}
  --test_data ${{outputs.test_data}}
```
