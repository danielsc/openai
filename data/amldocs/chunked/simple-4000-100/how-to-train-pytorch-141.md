
## Configure and submit your training job

In this section, we'll begin by introducing the data for training. We'll then cover how to run a training job, using a training script that we've provided. You'll learn to build the training job by configuring the command for running the training script. Then, you'll submit the training job to run in AzureML.

### Obtain the training data
You'll use data that is stored on a public blob as a [zip file](https://azuremlexamples.blob.core.windows.net/datasets/fowl_data.zip). This dataset consists of about 120 training images each for two classes (turkeys and chickens), with 100 validation images for each class. The images are a subset of the [Open Images v5 Dataset](https://storage.googleapis.com/openimages/web/index.html). We'll download and extract the dataset as part of our training script `pytorch_train.py`.

### Prepare the training script

In this article, we've provided the training script *pytorch_train.py*. In practice, you should be able to take any custom training script as is and run it with AzureML without having to modify your code.

The provided training script downloads the data, trains a model, and registers the model.

### Build the training job

Now that you have all the assets required to run your job, it's time to build it using the AzureML Python SDK v2. For this example, we'll be creating a `command`.

An AzureML `command` is a resource that specifies all the details needed to execute your training code in the cloud. These details include the inputs and outputs, type of hardware to use, software to install, and how to run your code. The `command` contains information to execute a single command.


#### Configure the command

You'll use the general purpose `command` to run the training script and perform your desired tasks. Create a `Command` object to specify the configuration details of your training job.

```python
from azure.ai.ml import command
from azure.ai.ml import Input

job = command(
    inputs=dict(
        num_epochs=30, learning_rate=0.001, momentum=0.9, output_dir="./outputs"
    ),
    compute=gpu_compute_taget,
    environment=curated_env_name,
    code="./src/",  # location of source code
    command="python pytorch_train.py --num_epochs ${{inputs.num_epochs}} --output_dir ${{inputs.output_dir}}",
    experiment_name="pytorch-birds",
    display_name="pytorch-birds-image",
)
```

- The inputs for this command include the number of epochs, learning rate, momentum, and output directory.
- For the parameter values:
    - provide the compute cluster `gpu_compute_target = "gpu-cluster"` that you created for running this command;
    - provide the curated environment `AzureML-pytorch-1.9-ubuntu18.04-py37-cuda11-gpu` that you initialized earlier;
    - configure the command line action itself—in this case, the command is `python pytorch_train.py`. You can access the inputs and outputs in the command via the `${{ ... }}` notation; and
    - configure metadata such as the display name and experiment name; where an experiment is a container for all the iterations one does on a certain project. All the jobs submitted under the same experiment name would be listed next to each other in AzureML studio.

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
