
The code above define a component with display name `Prep Data` using `@command_component` decorator:

* `name` is the unique identifier of the component.
* `version` is the current version of the component. A component can have multiple versions.
* `display_name` is a friendly display name of the component in UI, which isn't unique.
* `description` usually describes what task this component can complete.
* `environment` specifies the run-time environment for this component. The environment of this component specifies a docker image and refers to the `conda.yaml` file.

    The `conda.yaml` file contains all packages used for the component like following:


* The `prepare_data_component` function defines one input for `input_data` and two outputs for `training_data` and `test_data`. 
`input_data` is input data path. `training_data` and `test_data` are output data paths for training data and test data. 
* This component converts the data from `input_data` into a training data csv to `training_data` and a test data csv to `test_data`.

Following is what a component looks like in the studio UI.

- A component is a block in a pipeline graph.
- The `input_data`, `training_data` and `test_data` are ports of the component, which connects to other components for data streaming.

:::image type="content" source="./media/how-to-create-component-pipeline-python/prep-data-component.png" alt-text="Screenshot of the Prep Data component in the UI and code." lightbox ="./media/how-to-create-component-pipeline-python/prep-data-component.png":::

Now, you've prepared all source files for the `Prep Data` component.


### Create the train-model component

In this section, you'll create a component for training the image classification model in the Python function like the `Prep Data` component.

The difference is that since the training logic is more complicated, you can put the original training code in a separate Python file.

The source files of this component are under `train/` folder in the [AzureML Examples repo](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet). This folder contains three files to construct the component:

- `train.py`: contains the actual logic to train model.
- `train_component.py`: defines the interface of the component and imports the function in `train.py`.
-  `conda.yaml`: defines the run-time environment of the component.

#### Get a script containing execution logic

The `train.py` file contains a normal Python function, which performs the training model logic to train a Keras neural network for image classification. You can find the code [here](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet/train/train.py).

#### Define component using Python function

After defining the training function successfully, you can use @command_component in Azure Machine Learning SDK v2 to wrap your function as a component, which can be used in AzureML pipelines.

```python
import os
from pathlib import Path
from mldesigner import command_component, Input, Output


@command_component(
    name="train_image_classification_keras",
    version="1",
    display_name="Train Image Classification Keras",
    description="train image classification with keras",
    environment=dict(
        conda_file=Path(__file__).parent / "conda.yaml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
    ),
)
def keras_train_component(
    input_data: Input(type="uri_folder"),
    output_model: Output(type="uri_folder"),
    epochs=10,
):
    # avoid dependency issue, execution logic is in train() func in train.py file
    from train import train

    train(input_data, output_model, epochs)

```

The code above define a component with display name `Train Image Classification Keras` using `@command_component`:

* The `keras_train_component` function defines one input `input_data` where training data comes from, one input `epochs` specifying epochs during training, and one output `output_model` where outputs the model file. The default value of `epochs` is 10. The execution logic of this component is from `train()` function in `train.py` above.
