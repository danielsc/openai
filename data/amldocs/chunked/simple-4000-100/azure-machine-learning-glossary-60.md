Curated environments are provided by Azure Machine Learning and are available in your workspace by default. Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks. These pre-created environments also allow for faster deployment time. For a full list, see the [curated environments article](resource-curated-environments.md).

In custom environments, you're responsible for setting up your environment. Make sure to install the packages and any other dependencies that your training or scoring script needs on the compute. Azure ML allows you to create your own environment using

* A docker image
* A base docker image with a conda YAML to customize further
* A docker build context

## Model

Azure machine learning models consist of the binary file(s) that represent a machine learning model and any corresponding metadata. Models can be created from a local or remote file or directory. For remote locations `https`, `wasbs` and `azureml` locations are supported. The created model will be tracked in the workspace under the specified name and version. Azure ML supports three types of storage format for models:

* `custom_model`
* `mlflow_model`
* `triton_model`

## Workspace

The workspace is the top-level resource for Azure Machine Learning, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning. The workspace keeps a history of all jobs, including logs, metrics, output, and a snapshot of your scripts. The workspace stores references to resources like datastores and compute. It also holds all assets like models, environments, components and data asset.

## Next steps

[What is Azure Machine Learning?](overview-what-is-azure-machine-learning.md)
