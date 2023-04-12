## Set limits for your sweep job

Control your resource budget by setting limits for your sweep job.

* `max_total_trials`: Maximum number of trial jobs. Must be an integer between 1 and 1000.
* `max_concurrent_trials`: (optional) Maximum number of trial jobs that can run concurrently. If not specified, max_total_trials number of jobs launch in parallel. If specified, must be an integer between 1 and 1000.
* `timeout`: Maximum time in seconds the entire sweep job is allowed to run. Once this limit is reached the system will cancel the sweep job, including all its trials.
* `trial_timeout`: Maximum time in seconds each trial job is allowed to run. Once this limit is reached the system will cancel the trial. 

>[!NOTE] 
>If both max_total_trials and timeout are specified, the hyperparameter tuning experiment terminates when the first of these two thresholds is reached.

>[!NOTE] 
>The number of concurrent trial jobs is gated on the resources available in the specified compute target. Ensure that the compute target has the available resources for the desired concurrency.

```Python
sweep_job.set_limits(max_total_trials=20, max_concurrent_trials=4, timeout=1200)
```

This code configures the hyperparameter tuning experiment to use a maximum of 20 total trial jobs, running four trial jobs at a time with a timeout of 1200 seconds for the entire sweep job.

## Configure hyperparameter tuning experiment

To configure your hyperparameter tuning experiment, provide the following:
* The defined hyperparameter search space
* Your sampling algorithm
* Your early termination policy
* Your objective
* Resource limits
* CommandJob or CommandComponent
* SweepJob

SweepJob can run a hyperparameter sweep on the Command or Command Component. 

> [!NOTE]
>The compute target used in `sweep_job` must have enough resources to satisfy your concurrency level. For more information on compute targets, see [Compute targets](concept-compute-target.md).

Configure your hyperparameter tuning experiment:

```Python
from azure.ai.ml import MLClient
from azure.ai.ml import command, Input
from azure.ai.ml.sweep import Choice, Uniform, MedianStoppingPolicy
from azure.identity import DefaultAzureCredential

# Create your base command job
command_job = command(
    code="./src",
    command="python main.py --iris-csv ${{inputs.iris_csv}} --learning-rate ${{inputs.learning_rate}} --boosting ${{inputs.boosting}}",
    environment="AzureML-lightgbm-3.2-ubuntu18.04-py37-cpu@latest",
    inputs={
        "iris_csv": Input(
            type="uri_file",
            path="https://azuremlexamples.blob.core.windows.net/datasets/iris.csv",
        ),
        "learning_rate": 0.9,
        "boosting": "gbdt",
    },
    compute="cpu-cluster",
)

# Override your inputs with parameter expressions
command_job_for_sweep = command_job(
    learning_rate=Uniform(min_value=0.01, max_value=0.9),
    boosting=Choice(values=["gbdt", "dart"]),
)

# Call sweep() on your command job to sweep over your parameter expressions
sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm="random",
    primary_metric="test-multi_logloss",
    goal="Minimize",
)

# Specify your experiment details
sweep_job.display_name = "lightgbm-iris-sweep-example"
sweep_job.experiment_name = "lightgbm-iris-sweep-example"
sweep_job.description = "Run a hyperparameter sweep job for LightGBM on Iris dataset."

# Define the limits for this sweep
sweep_job.set_limits(max_total_trials=20, max_concurrent_trials=10, timeout=7200)

# Set early stopping on this one
sweep_job.early_termination = MedianStoppingPolicy(
    delay_evaluation=5, evaluation_interval=2
)
```

The `command_job` is called as a function so we can apply the parameter expressions to the sweep inputs. The `sweep` function is then configured with `trial`, `sampling-algorithm`, `objective`, `limits`, and `compute`. The above code snippet is taken from the sample notebook [Run hyperparameter sweep on a Command or CommandComponent](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/single-step/lightgbm/iris/lightgbm-iris-sweep.ipynb). In this sample, the `learning_rate` and `boosting` parameters will be tuned. Early stopping of jobs will be determined by a `MedianStoppingPolicy`, which stops a job whose primary metric value is worse than the median of the averages across all training jobs.(see [MedianStoppingPolicy class reference](/python/api/azure-ai-ml/azure.ai.ml.sweep.medianstoppingpolicy)).
