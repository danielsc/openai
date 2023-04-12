
This [Jupyter notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/resources/compute/compute.ipynb) shows more ways to create compute using SDK v2.


## Datastore

Azure Machine Learning datastores securely keep the connection information to your data storage on Azure, so you don't have to code it in your scripts. You can register and create a datastore to easily connect to your storage account, and access the data in your underlying storage service. The CLI v2 and SDK v2 support the following types of cloud-based storage services:

* Azure Blob Container
* Azure File Share
* Azure Data Lake
* Azure Data Lake Gen2

### [Azure CLI](#tab/cli)

To create a datastore using CLI v2, use the following command:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```bash
az ml datastore create --file my_datastore.yml
```
For more information, see [datastore YAML schema](reference-yaml-overview.md#datastore).


### [Python SDK](#tab/sdk)

To create a datastore using Python SDK v2, you can use the following code:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
blob_datastore1 = AzureBlobDatastore(
    name="blob-example",
    description="Datastore pointing to a blob container.",
    account_name="mytestblobstore",
    container_name="data-container",
    credentials={
        "account_key": "XXXxxxXXXxXXXXxxXXXXXxXXXXXxXxxXxXXXxXXXxXXxxxXXxxXXXxXxXXXxxXxxXXXXxxxxxXXxxxxxxXXXxXXX"
    },
)
ml_client.create_or_update(blob_datastore1)
```

This [Jupyter notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/resources/datastores/datastore.ipynb) shows more ways to create datastores using SDK v2.


## Model

Azure machine learning models consist of the binary file(s) that represent a machine learning model and any corresponding metadata. Models can be created from a local or remote file or directory. For remote locations `https`, `wasbs` and `azureml` locations are supported. The created model will be tracked in the workspace under the specified name and version. Azure ML supports three types of storage format for models:

* `custom_model`
* `mlflow_model`
* `triton_model`

### Creating a model

### [Azure CLI](#tab/cli)

To create a model using CLI v2, use the following command:

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```bash
az ml model create --file my_model.yml
```

For more information, see [model YAML schema](reference-yaml-model.md).


### [Python SDK](#tab/sdk)

To create a model using Python SDK v2, you can use the following code:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
my_model = Model(
    path="model.pkl", # the path to where my model file is located
    type="custom_model", # can be custom_model, mlflow_model or triton_model
    name="my-model",
    description="Model created from local file.",
)

ml_client.models.create_or_update(my_model) # use the MLClient to connect to workspace and create/register the model
```


## Environment

Azure Machine Learning environments are an encapsulation of the environment where your machine learning task happens. They specify the software packages, environment variables, and software settings around your training and scoring scripts. The environments are managed and versioned entities within your Machine Learning workspace. Environments enable reproducible, auditable, and portable machine learning workflows across a variety of computes.

### Types of environment

Azure ML supports two types of environments: curated and custom.

Curated environments are provided by Azure Machine Learning and are available in your workspace by default. Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks. These pre-created environments also allow for faster deployment time. For a full list, see the [curated environments article](resource-curated-environments.md).

In custom environments, you're responsible for setting up your environment and installing packages or any other dependencies that your training or scoring script needs on the compute. Azure ML allows you to create your own environment using
