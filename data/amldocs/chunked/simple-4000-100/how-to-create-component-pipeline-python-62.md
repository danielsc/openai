Fashion-MNIST is a dataset of fashion images divided into 10 classes. Each image is a 28x28 grayscale image and there are 60,000 training and 10,000 test images. As an image classification problem, Fashion-MNIST is harder than the classic MNIST handwritten digit database. It's distributed in the same compressed binary form as the original [handwritten digit database](http://yann.lecun.com/exdb/mnist/).

To define the input data of a job that references the Web-based data, run:

```python
from azure.ai.ml import Input

fashion_ds = Input(
    path="wasbs://demo@data4mldemo6150520719.blob.core.windows.net/mnist-fashion/"
)
```

By defining an `Input`, you create a reference to the data source location. The data remains in its existing location, so no extra storage cost is incurred.

## Create components for building pipeline

The image classification task can be split into three steps: prepare data, train model and score model.

[Azure Machine Learning component](concept-component.md) is a self-contained piece of code that does one step in a machine learning pipeline. In this article, you'll create three components for the image classification task:

- Prepare data for training and test
- Train a neural networking for image classification using training data
- Score the model using test data

For each component, you need to prepare the following staff:

1. Prepare the Python script containing the execution logic

1. Define the interface of the component,

1. Add other metadata of the component, including run-time environment, command to run the component, and etc.

The next section will show create components in two different ways: the first two components using Python function and the third component using yaml definition.

### Create the data-preparation component

The first component in this pipeline will convert the compressed data files of `fashion_ds` into two csv files, one for training and the other for scoring. You'll use Python function to define this component.

If you're following along with the example in the [AzureML Examples repo](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet), the source files are already available in `prep/` folder. This folder contains two files to construct the component: `prep_component.py`, which defines the component and `conda.yaml`, which defines the run-time environment of the component.

#### Define component using Python function

By using command_component() function as a decorator, you can easily define the component's interface, metadata and code to execute from a Python function. Each decorated Python function will be transformed into a single static specification (YAML) that the pipeline service can process.

```python
# Converts MNIST-formatted files at the passed-in input path to training data output path and test data output path
import os
from pathlib import Path
from mldesigner import command_component, Input, Output


@command_component(
    name="prep_data",
    version="1",
    display_name="Prep Data",
    description="Convert data to CSV file, and split to training and test data",
    environment=dict(
        conda_file=Path(__file__).parent / "conda.yaml",
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
    ),
)
def prepare_data_component(
    input_data: Input(type="uri_folder"),
    training_data: Output(type="uri_folder"),
    test_data: Output(type="uri_folder"),
):
    convert(
        os.path.join(input_data, "train-images-idx3-ubyte"),
        os.path.join(input_data, "train-labels-idx1-ubyte"),
        os.path.join(training_data, "mnist_train.csv"),
        60000,
    )
    convert(
        os.path.join(input_data, "t10k-images-idx3-ubyte"),
        os.path.join(input_data, "t10k-labels-idx1-ubyte"),
        os.path.join(test_data, "mnist_test.csv"),
        10000,
    )


def convert(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    l = open(labelf, "rb")
    o = open(outf, "w")

    f.read(16)
    l.read(8)
    images = []

    for i in range(n):
        image = [ord(l.read(1))]
        for j in range(28 * 28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        o.write(",".join(str(pix) for pix in image) + "\n")
    f.close()
    o.close()
    l.close()

```
