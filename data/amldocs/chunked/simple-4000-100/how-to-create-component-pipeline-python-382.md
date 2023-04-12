

The code in score.py takes three command-line arguments: `input_data`, `input_model` and `output_result`. The program score the input model using input data and then output the scoring result.

#### Define component via Yaml

In this section, you'll learn to create a component specification in the valid YAML component specification format. This file specifies the following information:

- Metadata: name, display_name, version, type, and so on.
- Interface: inputs and outputs
- Command, code, & environment: The command, code, and environment used to run the component

```python
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
type: command

name: score_image_classification_keras
display_name: Score Image Classification Keras
inputs:
  input_data: 
    type: uri_folder
  input_model:
    type: uri_folder
outputs:
  output_result:
    type: uri_folder
code: ./
command: python score.py --input_data ${{inputs.input_data}} --input_model ${{inputs.input_model}} --output_result ${{outputs.output_result}}
environment:
  conda_file: ./conda.yaml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04


```

* `name` is the unique identifier of the component. Its display name is `Score Image Classification Keras`. 
* This component has two inputs and one output. 
* The source code path of it's defined in the `code` section and when the component is run in cloud, all files from that path will be uploaded as the snapshot of this component. 
* The `command` section specifies the command to execute while running this component. 
* The `environment` section contains a docker image and a conda yaml file. The source file is in the [sample repository](https://github.com/Azure/azureml-examples/blob/v2samplesreorg/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet/score/conda.yaml).

Now, you've got all source files for score-model component.

## Load components to build pipeline

For prep-data component and train-model component defined by Python function, you can import the components just like normal Python functions. 

In the following code, you import `prepare_data_component()` and `keras_train_component()` function from the `prep_component.py` file under `prep` folder and `train_component` file under `train` folder respectively.

```python
%load_ext autoreload
%autoreload 2

# load component function from component python file
from prep.prep_component import prepare_data_component
from train.train_component import keras_train_component

# print hint of components
help(prepare_data_component)
help(keras_train_component)
```

For score component defined by yaml, you can use `load_component()` function to load.

```python
# load component function from yaml
keras_score_component = load_component(source="./score/score.yaml")
```

## Build your pipeline

Now that you've created and loaded all components and input data to build the pipeline. You can compose them into a pipeline:

```python
# define a pipeline containing 3 nodes: Prepare data node, train node, and score node
@pipeline(
    default_compute=cpu_compute_target,
)
def image_classification_keras_minist_convnet(pipeline_input_data):
    """E2E image classification pipeline with keras using python sdk."""
    prepare_data_node = prepare_data_component(input_data=pipeline_input_data)

    train_node = keras_train_component(
        input_data=prepare_data_node.outputs.training_data
    )
    train_node.compute = gpu_compute_target

    score_node = keras_score_component(
        input_data=prepare_data_node.outputs.test_data,
        input_model=train_node.outputs.output_model,
    )


# create a pipeline
pipeline_job = image_classification_keras_minist_convnet(pipeline_input_data=fashion_ds)
```

The pipeline has a default compute `cpu_compute_target`, which means if you don't specify compute for a specific node, that node will run on the default compute.

The pipeline has a pipeline level input `pipeline_input_data`. You can assign value to pipeline input when you submit a pipeline job.
