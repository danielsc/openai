    - provide the compute cluster `gpu_compute_target = "gpu-cluster"` that you created for running this command;
    - provide the curated environment `curated_env_name` that you declared earlier;
    - configure the command line action itself—in this case, the command is `python tf_mnist.py`. You can access the inputs and outputs in the command via the `${{ ... }}` notation; and
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

- **Scaling**: The cluster attempts to scale up if it requires more nodes to execute the run than are currently available.

- **Running**: All scripts in the script folder *src* are uploaded to the compute target, data stores are mounted or copied, and the script is executed. Outputs from *stdout* and the *./logs* folder are streamed to the job history and can be used to monitor the job.

## Tune model hyperparameters

Now that you've seen how to do a TensorFlow training run using the SDK, let's see if you can further improve the accuracy of your model. You can tune and optimize your model's hyperparameters using Azure Machine Learning's [`sweep`](/python/api/azure-ai-ml/azure.ai.ml.sweep) capabilities.

To tune the model's hyperparameters, define the parameter space in which to search during training. You'll do this by replacing some of the parameters (`batch_size`, `first_layer_neurons`, `second_layer_neurons`, and `learning_rate`) passed to the training job with special inputs from the `azure.ml.sweep` package.

```python
from azure.ai.ml.sweep import Choice, LogUniform

# we will reuse the command_job created before. we call it as a function so that we can apply inputs
# we do not apply the 'iris_csv' input again -- we will just use what was already defined earlier
job_for_sweep = job(
    batch_size=Choice(values=[32, 64, 128]),
    first_layer_neurons=Choice(values=[16, 64, 128, 256, 512]),
    second_layer_neurons=Choice(values=[16, 64, 256, 512]),
    learning_rate=LogUniform(min_value=-6, max_value=-1),
)
```

Then, you'll configure sweep on the command job, using some sweep-specific parameters, such as the primary metric to watch and the sampling algorithm to use.

In the following code, we use random sampling to try different configuration sets of hyperparameters in an attempt to maximize our primary metric, `validation_acc`.

We also define an early termination policy—the `BanditPolicy`. This policy operates by checking the job every two iterations. If the primary metric, `validation_acc`, falls outside the top ten percent range, AzureML will terminate the job. This saves the model from continuing to explore hyperparameters that show no promise of helping to reach the target metric.
