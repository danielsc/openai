In custom environments, you're responsible for setting up your environment and installing packages or any other dependencies that your training or scoring script needs on the compute. Azure ML allows you to create your own environment using

* A docker image
* A base docker image with a conda YAML to customize further
* A docker build context

### Create an Azure ML custom environment

### [Azure CLI](#tab/cli)

To create an environment using CLI v2, use the following command:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```bash
az ml environment create --file my_environment.yml
```
For more information, see [environment YAML schema](reference-yaml-environment.md).



### [Python SDK](#tab/sdk)

To create an environment using Python SDK v2, you can use the following code:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
my_env = Environment(
    image="pytorch/pytorch:latest", # base image to use
    name="docker-image-example", # name of the model
    description="Environment created from a Docker image.",
)

ml_client.environments.create_or_update(my_env) # use the MLClient to connect to workspace and create/register the environment
```

This [Jupyter notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/assets/environment/environment.ipynb) shows more ways to create custom environments using SDK v2.


## Data

Azure Machine Learning allows you to work with different types of data:

* URIs (a location in local/cloud storage)
  * `uri_folder`
  * `uri_file`
* Tables (a tabular data abstraction)
  * `mltable`
* Primitives
  * `string`
  * `boolean`
  * `number`

For most scenarios, you'll use URIs (`uri_folder` and `uri_file`) - a location in storage that can be easily mapped to the filesystem of a compute node in a job by either mounting or downloading the storage to the node.

`mltable` is an abstraction for tabular data that is to be used for AutoML Jobs, Parallel Jobs, and some advanced scenarios. If you're just starting to use Azure Machine Learning and aren't using AutoML, we strongly encourage you to begin with URIs.

## Component

An Azure Machine Learning [component](concept-component.md) is a self-contained piece of code that does one step in a machine learning pipeline. Components are the building blocks of advanced machine learning pipelines. Components can do tasks such as data processing, model training, model scoring, and so on. A component is analogous to a function - it has a name, parameters, expects input, and returns output. 

## Next steps

* [How to upgrade from v1 to v2](how-to-migrate-from-v1.md)
* [Train models with the v2 CLI and SDK](how-to-train-model.md)
