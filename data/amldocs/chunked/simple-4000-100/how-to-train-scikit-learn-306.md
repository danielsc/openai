Now that you have all the assets required to run your job, it's time to build it using the AzureML Python SDK v2. For this, we'll be creating a `command`.

An AzureML `command` is a resource that specifies all the details needed to execute your training code in the cloud. These details include the inputs and outputs, type of hardware to use, software to install, and how to run your code. The `command` contains information to execute a single command.


#### Configure the command

You'll use the general purpose `command` to run the training script and perform your desired tasks. Create a `Command` object to specify the configuration details of your training job. 

- The inputs for this command include the number of epochs, learning rate, momentum, and output directory.
- For the parameter values:
    - provide the compute cluster `cpu_compute_target = "cpu-cluster"` that you created for running this command;
    - provide the custom environment `sklearn-env` that you created for running the AzureML job;
    - configure the command line action itself—in this case, the command is `python train_iris.py`. You can access the inputs and outputs in the command via the `${{ ... }}` notation; and
    - configure the metadata such as the display name and experiment name; where an experiment is a container for all the iterations one does on a certain project. Note that all the jobs submitted under the same experiment name would be listed next to each other in AzureML studio.

```python
from azure.ai.ml import command
from azure.ai.ml import Input

job = command(
    inputs=dict(kernel="linear", penalty=1.0),
    compute=cpu_compute_target,
    environment=f"{job_env.name}:{job_env.version}",
    code="./src/",
    command="python train_iris.py --kernel ${{inputs.kernel}} --penalty ${{inputs.penalty}}",
    experiment_name="sklearn-iris-flowers",
    display_name="sklearn-classify-iris-flower-images",
)
```

### Submit the job

It's now time to submit the job to run in AzureML. This time you'll use `create_or_update` on `ml_client.jobs`. 

```python
ml_client.jobs.create_or_update(job)
```

Once completed, the job will register a model in your workspace (as a result of training) and output a link for viewing the job in AzureML studio.

> [!WARNING]
> Azure Machine Learning runs training scripts by copying the entire source directory. If you have sensitive data that you don't want to upload, use a [.ignore file](concept-train-machine-learning-model.md#understand-what-happens-when-you-submit-a-training-job) or don't include it in the source directory.

### What happens during job execution
As the job is executed, it goes through the following stages:

- **Preparing**: A docker image is created according to the environment defined. The image is uploaded to the workspace's container registry and cached for later runs. Logs are also streamed to the run history and can be viewed to monitor progress. If a curated environment is specified, the cached image backing that curated environment will be used.

- **Scaling**: The cluster attempts to scale up if the cluster requires more nodes to execute the run than are currently available.

- **Running**: All scripts in the script folder *src* are uploaded to the compute target, data stores are mounted or copied, and the script is executed. Outputs from *stdout* and the *./logs* folder are streamed to the run history and can be used to monitor the run.

## Tune model hyperparameters

Now that you've seen how to do a simple Scikit-learn training run using the SDK, let's see if you can further improve the accuracy of your model. You can tune and optimize our model's hyperparameters using Azure Machine Learning's [`sweep`](/python/api/azure-ai-ml/azure.ai.ml.sweep) capabilities.

To tune the model's hyperparameters, define the parameter space in which to search during training. You'll do this by replacing some of the parameters (`kernel` and `penalty`) passed to the training job with special inputs from the `azure.ml.sweep` package.
