There are a few options you can define in the `set_limits()` function to end your experiment prior to job completion. 

|Criteria| description
|----|----
No&nbsp;criteria | If you don't define any exit parameters the experiment continues until no further progress is made on your primary metric.
`timeout`| Defines how long, in minutes, your experiment should continue to run. If not specified, the default job's total timeout is 6 days (8,640 minutes). To specify a timeout less than or equal to 1 hour (60 minutes), make sure your dataset's size isn't greater than 10,000,000 (rows times column) or an error results. <br><br> This timeout includes setup, featurization and training runs but doesn't include the ensembling and model explainability runs at the end of the process since those actions need to happen once all the trials (children jobs) are done. 
`trial_timeout_minutes` | Maximum time in minutes that each trial (child job) can run for before it terminates. If not specified, a value of 1 month or 43200 minutes is used
`enable_early_termination`|Whether to end the job if the score is not improving in the short term
`max_trials`| The maximum number of trials/runs each with a different combination of algorithm and hyperparameters to try during an AutoML job. If not specified, the default is 1000 trials. If using `enable_early_termination` the number of trials used can be smaller.
`max_concurrent_trials`| Represents the maximum number of trials (children jobs) that would be executed in parallel. It's a good practice to match this number with the number of nodes your cluster

## Run experiment
> [!NOTE]
> If you run an experiment with the same configuration settings and primary metric multiple times, you'll likely see variation in each experiments final metrics score and generated models. The algorithms automated ML employs have inherent randomness that can cause slight variation in the models output by the experiment and the recommended model's final metrics score, like accuracy. You'll likely also see results with the same model name, but different hyperparameters used. 

> [!WARNING]
> If you have set rules in firewall and/or Network Security Group over your workspace, verify that required permissions are given to inbound and outbound network traffic as defined in [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).

Submit the experiment to run and generate a model. With the `MLClient` created in the prerequisites, you can run the following command in the workspace.

```python

# Submit the AutoML job
returned_job = ml_client.jobs.create_or_update(
    classification_job
)  # submit the job to the backend

print(f"Created job: {returned_job}")

# Get a URL for the status of the job
returned_job.services["Studio"].endpoint

```

### Multiple child runs on clusters

Automated ML experiment child runs can be performed on a cluster that is already running another experiment. However, the timing depends on how many nodes the cluster has, and if those nodes are available to run a different experiment.

Each node in the cluster acts as an individual virtual machine (VM) that can accomplish a single training run; for automated ML this means a child run. If all the nodes are busy, the new experiment is queued. But if there are free nodes, the new experiment will run automated ML child runs in parallel in the available nodes/VMs.

To help manage child runs and when they can be performed, we recommend you create a dedicated cluster per experiment, and match the number of `max_concurrent_iterations` of your experiment to the number of nodes in the cluster. This way, you use all the nodes of the cluster at the same time with the number of concurrent child runs/iterations you want.

Configure `max_concurrent_iterations` in the .set_limits() setter function. If it is not configured, then by default only one concurrent child run/iteration is allowed per experiment.
In case of compute instance, `max_concurrent_trials` can be set to be the same as number of cores on the compute instance VM.
