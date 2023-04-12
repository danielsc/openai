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
        batch_size=50,
        first_layer_neurons=300,
        second_layer_neurons=100,
        learning_rate=0.001,
    ),
    compute=gpu_compute_target,
    environment=f"{job_env.name}:{job_env.version}",
    code="./src/",
    command="python keras_mnist.py --data-folder ${{inputs.data_folder}} --batch-size ${{inputs.batch_size}} --first-layer-neurons ${{inputs.first_layer_neurons}} --second-layer-neurons ${{inputs.second_layer_neurons}} --learning-rate ${{inputs.learning_rate}}",
    experiment_name="keras-dnn-image-classify",
    display_name="keras-classify-mnist-digit-images-with-dnn",
)
```

- The inputs for this command include the data location, batch size, number of neurons in the first and second layer, and learning rate. Notice that we've passed in the web path directly as an input.

- For the parameter values:
    - provide the compute cluster `gpu_compute_target = "gpu-cluster"` that you created for running this command;
    - provide the custom environment `keras-env` that you created for running the AzureML job;
    - configure the command line action itself—in this case, the command is `python keras_mnist.py`. You can access the inputs and outputs in the command via the `${{ ... }}` notation; and
    - configure metadata such as the display name and experiment name; where an experiment is a container for all the iterations one does on a certain project. All the jobs submitted under the same experiment name would be listed next to each other in AzureML studio.
 
- In this example, you'll use the `UserIdentity` to run the command. Using a user identity means that the command will use your identity to run the job and access the data from the blob.

### Submit the job

It's now time to submit the job to run in AzureML. This time, you'll use `create_or_update` on `ml_client.jobs`.

```python
ml_client.jobs.create_or_update(job)
```

Once completed, the job will register a model in your workspace (as a result of training) and output a link for viewing the job in AzureML studio.

> [!WARNING]
> Azure Machine Learning runs training scripts by copying the entire source directory. If you have sensitive data that you don't want to upload, use a [.ignore file](concept-train-machine-learning-model.md#understand-what-happens-when-you-submit-a-training-job) or don't include it in the source directory.

### What happens during job execution
As the job is executed, it goes through the following stages:

- **Preparing**: A docker image is created according to the environment defined. The image is uploaded to the workspace's container registry and cached for later runs. Logs are also streamed to the job history and can be viewed to monitor progress. If a curated environment is specified, the cached image backing that curated environment will be used.
