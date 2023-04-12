
## Configure and submit your training job

In this section, we'll begin by introducing the data for training. We'll then cover how to run a training job, using a training script that we've provided. You'll learn to build the training job by configuring the command for running the training script. Then, you'll submit the training job to run in AzureML.

### Obtain the training data
You'll use data from the Modified National Institute of Standards and Technology (MNIST) database of handwritten digits. This data is sourced from Yan LeCun's website and stored in an Azure storage account.

```python
web_path = "wasbs://datasets@azuremlexamples.blob.core.windows.net/mnist/"
```

For more information about the MNIST dataset, visit [Yan LeCun's website](http://yann.lecun.com/exdb/mnist/).

### Prepare the training script

In this article, we've provided the training script *tf_mnist.py*. In practice, you should be able to take any custom training script as is and run it with AzureML without having to modify your code.

The provided training script does the following:
- handles the data preprocessing, splitting the data into test and train data;
- trains a model, using the data; and 
- returns the output model.

During the pipeline run, you'll use MLFlow to log the parameters and metrics. To learn how to enable MLFlow tracking, see [Track ML experiments and models with MLflow](how-to-use-mlflow-cli-runs.md).

In the training script `tf_mnist.py`, we create a simple deep neural network (DNN). This DNN has:

- An input layer with 28 * 28 = 784 neurons. Each neuron represents an image pixel.
- Two hidden layers. The first hidden layer has 300 neurons and the second hidden layer has 100 neurons.
- An output layer with 10 neurons. Each neuron represents a targeted label from 0 to 9.

:::image type="content" source="media/how-to-train-tensorflow/neural-network.png" alt-text="Diagram showing a deep neural network with 784 neurons at the input layer, two hidden layers, and 10 neurons at the output layer.":::

### Build the training job

Now that you have all the assets required to run your job, it's time to build it using the AzureML Python SDK v2. For this example, we'll be creating a `command`.

An AzureML `command` is a resource that specifies all the details needed to execute your training code in the cloud. These details include the inputs and outputs, type of hardware to use, software to install, and how to run your code. The `command` contains information to execute a single command.


#### Configure the command

You'll use the general purpose `command` to run the training script and perform your desired tasks. Create a `Command` object to specify the configuration details of your training job.

```python
from azure.ai.ml import command
from azure.ai.ml import UserIdentityConfiguration
from azure.ai.ml import Input

web_path = "wasbs://datasets@azuremlexamples.blob.core.windows.net/mnist/"

job = command(
    inputs=dict(
        data_folder=Input(type="uri_folder", path=web_path),
        batch_size=64,
        first_layer_neurons=256,
        second_layer_neurons=128,
        learning_rate=0.01,
    ),
    compute=gpu_compute_target,
    environment=curated_env_name,
    code="./src/",
    command="python tf_mnist.py --data-folder ${{inputs.data_folder}} --batch-size ${{inputs.batch_size}} --first-layer-neurons ${{inputs.first_layer_neurons}} --second-layer-neurons ${{inputs.second_layer_neurons}} --learning-rate ${{inputs.learning_rate}}",
    experiment_name="tf-dnn-image-classify",
    display_name="tensorflow-classify-mnist-digit-images-with-dnn",
)
```

- The inputs for this command include the data location, batch size, number of neurons in the first and second layer, and learning rate. Notice that we've passed in the web path directly as an input.

- For the parameter values:
    - provide the compute cluster `gpu_compute_target = "gpu-cluster"` that you created for running this command;
    - provide the curated environment `curated_env_name` that you declared earlier;
