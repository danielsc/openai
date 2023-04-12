- **Preparing**: A docker image is created according to the environment defined. The image is uploaded to the workspace's container registry and cached for later runs. Logs are also streamed to the job history and can be viewed to monitor progress. If a curated environment is specified, the cached image backing that curated environment will be used.

- **Scaling**: The cluster attempts to scale up if it requires more nodes to execute the run than are currently available.

- **Running**: All scripts in the script folder *src* are uploaded to the compute target, data stores are mounted or copied, and the script is executed. Outputs from *stdout* and the *./logs* folder are streamed to the job history and can be used to monitor the job.

## Tune model hyperparameters

You've trained the model with one set of parameters, let's now see if you can further improve the accuracy of your model. You can tune and optimize your model's hyperparameters using Azure Machine Learning's [`sweep`](/python/api/azure-ai-ml/azure.ai.ml.sweep) capabilities.

To tune the model's hyperparameters, define the parameter space in which to search during training. You'll do this by replacing some of the parameters passed to the training job with special inputs from the `azure.ml.sweep` package.

Since the training script uses a learning rate schedule to decay the learning rate every several epochs, you can tune the initial learning rate and the momentum parameters.

```python
from azure.ai.ml.sweep import Uniform

# we will reuse the command_job created before. we call it as a function so that we can apply inputs
job_for_sweep = job(
    learning_rate=Uniform(min_value=0.0005, max_value=0.005),
    momentum=Uniform(min_value=0.9, max_value=0.99),
)
```

Then, you'll configure sweep on the command job, using some sweep-specific parameters, such as the primary metric to watch and the sampling algorithm to use.

In the following code, we use random sampling to try different configuration sets of hyperparameters in an attempt to maximize our primary metric, `best_val_acc`.

We also define an early termination policy, the `BanditPolicy`, to terminate poorly performing runs early.
The `BanditPolicy` will terminate any run that doesn't fall within the slack factor of our primary evaluation metric. You will apply this policy every epoch (since we report our `best_val_acc` metric every epoch and `evaluation_interval`=1). Notice we will delay the first policy evaluation until after the first 10 epochs (`delay_evaluation`=10).

```python
from azure.ai.ml.sweep import BanditPolicy

sweep_job = job_for_sweep.sweep(
    compute="gpu-cluster",
    sampling_algorithm="random",
    primary_metric="best_val_acc",
    goal="Maximize",
    max_total_trials=8,
    max_concurrent_trials=4,
    early_termination_policy=BanditPolicy(
        slack_factor=0.15, evaluation_interval=1, delay_evaluation=10
    ),
)
```

Now, you can submit this job as before. This time, you'll be running a sweep job that sweeps over your train job.

```python
returned_sweep_job = ml_client.create_or_update(sweep_job)

# stream the output and wait until the job is finished
ml_client.jobs.stream(returned_sweep_job.name)

# refresh the latest status of the job after streaming
returned_sweep_job = ml_client.jobs.get(name=returned_sweep_job.name)
```

You can monitor the job by using the studio user interface link that is presented during the job run.

## Find the best model

Once all the runs complete, you can find the run that produced the model with the highest accuracy.

```python
from azure.ai.ml.entities import Model

if returned_sweep_job.status == "Completed":

    # First let us get the run which gave us the best result
    best_run = returned_sweep_job.properties["best_child_run_id"]

    # lets get the model from this run
    model = Model(
        # the script stores the model as "outputs"
        path="azureml://jobs/{}/outputs/artifacts/paths/outputs/".format(best_run),
        name="run-model-example",
        description="Model created from run.",
        type="custom_model",
    )

else:
    print(
        "Sweep job status: {}. Please wait until it completes".format(
            returned_sweep_job.status
        )
    )
```
