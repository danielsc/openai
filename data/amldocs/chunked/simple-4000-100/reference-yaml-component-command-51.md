| `process_count_per_instance` | integer | The number of processes per node to launch for the job. | |  `1` |

#### TensorFlowConfiguration

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** Distribution type.  | `tensorflow` |
| `worker_count` | integer | The number of workers to launch for the job. | | Defaults to `resources.instance_count`. |
| `parameter_server_count` | integer | The number of parameter servers to launch for the job. | | `0` |

### Component input

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | **Required.** The type of component input. [Learn more about data access](concept-data.md) | `number`, `integer`, `boolean`, `string`, `uri_file`, `uri_folder`, `mltable`, `mlflow_model`| |
| `description` | string | Description of the input. | | |
| `default` | number, integer, boolean, or string | The default value for the input. | | |
| `optional` | boolean | Whether the input is required. If set to `true`, you need use the command includes optional inputs with `$[[]]`| | `false` |
| `min` | integer or number | The minimum accepted value for the input. This field can only be specified if `type` field is `number` or `integer`. | |
| `max` | integer or number | The maximum accepted value for the input. This field can only be specified if `type` field is `number` or `integer`. | |
| `enum` | array | The list of allowed values for the input. Only applicable if `type` field is `string`.| |

### Component output

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | string | **Required.** The type of component output. | `uri_file`, `uri_folder`, `mltable`, `mlflow_model` | |
| `description` | string | Description of the output. | | |

## Remarks

The `az ml component` commands can be used for managing Azure Machine Learning components.

## Examples

Command component examples are available in the examples GitHub repository. Select examples for are shown below.

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/jobs/pipelines-with-components). Several are shown below.

## YAML: Hello world command component

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
type: command

name: hello_python_world
display_name: Hello_Python_World
version: 1

code: ./src

environment: 
  image: python

command: >-
  python hello.py

```

## YAML: Component with different input types

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

### Define optional inputs in command line
When the input is set as `optional = true`, you need use `$[[]]` to embrace the command line with inputs. For example `$[[--input1 ${{inputs.input1}}]`. The command line at runtime may have different inputs.
- If  you are using only specify the required `training_data` and `model_output` parameters, the command line will look like:

```azurecli
python train.py --training_data some_input_path --learning_rate 0.01 --learning_rate_schedule time-based --model_output some_output_path
```
