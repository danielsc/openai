- **Preparing**: A docker image is created according to the environment defined. The image is uploaded to the workspace's container registry and cached for later runs. Logs are also streamed to the job history and can be viewed to monitor progress. If a curated environment is specified, the cached image backing that curated environment will be used.

- **Scaling**: The cluster attempts to scale up if it requires more nodes to execute the run than are currently available.

- **Running**: All scripts in the script folder *src* are uploaded to the compute target, data stores are mounted or copied, and the script is executed. Outputs from *stdout* and the *./logs* folder are streamed to the job history and can be used to monitor the job.

## Tune model hyperparameters

You've trained the model with one set of parameters, let's now see if you can further improve the accuracy of your model. You can tune and optimize your model's hyperparameters using Azure Machine Learning's [`sweep`](/python/api/azure-ai-ml/azure.ai.ml.sweep) capabilities.

To tune the model's hyperparameters, define the parameter space in which to search during training. You'll do this by replacing some of the parameters (`batch_size`, `first_layer_neurons`, `second_layer_neurons`, and `learning_rate`) passed to the training job with special inputs from the `azure.ml.sweep` package.

```python
from azure.ai.ml.sweep import Choice, LogUniform

# we will reuse the command_job created before. we call it as a function so that we can apply inputs
# we do not apply the 'iris_csv' input again -- we will just use what was already defined earlier
job_for_sweep = job(
    batch_size=Choice(values=[25, 50, 100]),
    first_layer_neurons=Choice(values=[10, 50, 200, 300, 500]),
    second_layer_neurons=Choice(values=[10, 50, 200, 500]),
    learning_rate=LogUniform(min_value=-6, max_value=-1),
)
```

Then, you'll configure sweep on the command job, using some sweep-specific parameters, such as the primary metric to watch and the sampling algorithm to use.

In the following code, we use random sampling to try different configuration sets of hyperparameters in an attempt to maximize our primary metric, `validation_acc`.

We also define an early termination policy—the `BanditPolicy`. This policy operates by checking the job every two iterations. If the primary metric, `validation_acc`, falls outside the top ten percent range, AzureML will terminate the job. This saves the model from continuing to explore hyperparameters that show no promise of helping to reach the target metric.

```python
from azure.ai.ml.sweep import BanditPolicy

sweep_job = job_for_sweep.sweep(
    compute=gpu_compute_target,
    sampling_algorithm="random",
    primary_metric="Accuracy",
    goal="Maximize",
    max_total_trials=20,
    max_concurrent_trials=4,
    early_termination_policy=BanditPolicy(slack_factor=0.1, evaluation_interval=2),
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

## Find and register the best model

Once all the runs complete, you can find the run that produced the model with the highest accuracy.

```python
from azure.ai.ml.entities import Model

if returned_sweep_job.status == "Completed":

    # First let us get the run which gave us the best result
    best_run = returned_sweep_job.properties["best_child_run_id"]

    # lets get the model from this run
    model = Model(
        # the script stores the model as "keras_dnn_mnist_model"
        path="azureml://jobs/{}/outputs/artifacts/paths/keras_dnn_mnist_model/".format(
            best_run
        ),
        name="run-model-example",
        description="Model created from run.",
        type="mlflow_model",
    )

else:
    print(
        "Sweep job status: {}. Please wait until it completes".format(
            returned_sweep_job.status
        )
    )
```
