To run an AzureML job, you'll need an environment. An AzureML [environment](concept-environments.md) encapsulates the dependencies (such as software runtime and libraries) needed to run your machine learning training script on your compute resource. This environment is similar to a Python environment on your local machine.

AzureML allows you to either use a curated (or ready-made) environment or create a custom environment using a Docker image or a Conda configuration. In this article, you'll create a custom Conda environment for your jobs, using a Conda YAML file.

#### Create a custom environment

To create your custom environment, you'll define your Conda dependencies in a YAML file. First, create a directory for storing the file. In this example, we've named the directory `dependencies`.

```python
import os

dependencies_dir = "./dependencies"
os.makedirs(dependencies_dir, exist_ok=True)
```
Then, create the file in the dependencies directory. In this example, we've named the file `conda.yml`.

```python
%%writefile {dependencies_dir}/conda.yml
name: keras-env
channels:
  - conda-forge
dependencies:
  - python=3.8
  - pip=21.2.4
  - pip:
    - protobuf~=3.20
    - numpy==1.21.2
    - tensorflow-gpu==2.2.0
    - keras<=2.3.1
    - matplotlib
    - mlflow== 1.26.1
    - azureml-mlflow==1.42.0
```

The specification contains some usual packages (such as numpy and pip) that you'll use in your job.

Next, use the YAML file to create and register this custom environment in your workspace. The environment will be packaged into a Docker container at runtime.

```python
from azure.ai.ml.entities import Environment

custom_env_name = "keras-env"

job_env = Environment(
    name=custom_env_name,
    description="Custom environment for keras image classification",
    conda_file=os.path.join(dependencies_dir, "conda.yml"),
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
)
job_env = ml_client.environments.create_or_update(job_env)

print(
    f"Environment with name {job_env.name} is registered to workspace, the environment version is {job_env.version}"
)
```

For more information on creating and using environments, see [Create and use software environments in Azure Machine Learning](how-to-use-environments.md).

## Configure and submit your training job

In this section, we'll begin by introducing the data for training. We'll then cover how to run a training job, using a training script that we've provided. You'll learn to build the training job by configuring the command for running the training script. Then, you'll submit the training job to run in AzureML.

### Obtain the training data
You'll use data from the Modified National Institute of Standards and Technology (MNIST) database of handwritten digits. This data is sourced from Yan LeCun's website and stored in an Azure storage account.

```python
web_path = "wasbs://datasets@azuremlexamples.blob.core.windows.net/mnist/"
```

For more information about the MNIST dataset, visit [Yan LeCun's website](http://yann.lecun.com/exdb/mnist/).

### Prepare the training script

In this article, we've provided the training script *keras_mnist.py*. In practice, you should be able to take any custom training script as is and run it with AzureML without having to modify your code.

The provided training script does the following:
 - handles the data preprocessing, splitting the data into test and train data;
 - trains a model, using the data; and
 - returns the output model.

During the pipeline run, you'll use MLFlow to log the parameters and metrics. To learn how to enable MLFlow tracking, see [Track ML experiments and models with MLflow](how-to-use-mlflow-cli-runs.md).

In the training script `keras_mnist.py`, we create a simple deep neural network (DNN). This DNN has:

- An input layer with 28 * 28 = 784 neurons. Each neuron represents an image pixel.
- Two hidden layers. The first hidden layer has 300 neurons and the second hidden layer has 100 neurons.
- An output layer with 10 neurons. Each neuron represents a targeted label from 0 to 9.
