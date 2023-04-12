

## <a name="specify-objective-to-optimize"></a> Specify the objective of the sweep

Define the objective of your sweep job by specifying the primary metric and goal you want hyperparameter tuning to optimize. Each training job is evaluated for the primary metric. The early termination policy uses the primary metric to identify low-performance jobs.

* `primary_metric`: The name of the primary metric needs to exactly match the name of the metric logged by the training script
* `goal`: It can be either `Maximize` or `Minimize` and determines whether the primary metric will be maximized or minimized when evaluating the jobs. 

```Python
from azure.ai.ml.sweep import Uniform, Choice

command_job_for_sweep = command_job(   
    learning_rate=Uniform(min_value=0.05, max_value=0.1),
    batch_size=Choice(values=[16, 32, 64, 128]),
)

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = "bayesian",
    primary_metric="accuracy",
    goal="Maximize",
)
```

This sample maximizes "accuracy".

### <a name="log-metrics-for-hyperparameter-tuning"></a>Log metrics for hyperparameter tuning

The training script for your model **must** log the primary metric during model training using the same corresponding metric name so that the SweepJob can access it for hyperparameter tuning.

Log the primary metric in your training script with the following sample snippet:

```Python
import mlflow
mlflow.log_metric("accuracy", float(val_accuracy))
```

The training script calculates the `val_accuracy` and logs it as the primary metric "accuracy". Each time the metric is logged, it's received by the hyperparameter tuning service. It's up to you to determine the frequency of reporting.

For more information on logging values for training jobs, see [Enable logging in Azure ML training jobs](how-to-log-view-metrics.md).

## <a name="early-termination"></a> Specify early termination policy

Automatically end poorly performing jobs with an early termination policy. Early termination improves computational efficiency.

You can configure the following parameters that control when a policy is applied:

* `evaluation_interval`: the frequency of applying the policy. Each time the training script logs the primary metric counts as one interval. An `evaluation_interval` of 1 will apply the policy every time the training script reports the primary metric. An `evaluation_interval` of 2 will apply the policy every other time. If not specified, `evaluation_interval` is set to 0 by default.
* `delay_evaluation`: delays the first policy evaluation for a specified number of intervals. This is an optional parameter that avoids premature termination of training jobs by allowing all configurations to run for a minimum number of intervals. If specified, the policy applies every multiple of evaluation_interval that is greater than or equal to delay_evaluation. If not specified, `delay_evaluation` is set to 0 by default.

Azure Machine Learning supports the following early termination policies:
* [Bandit policy](#bandit-policy)
* [Median stopping policy](#median-stopping-policy)
* [Truncation selection policy](#truncation-selection-policy)
* [No termination policy](#no-termination-policy-default)


### Bandit policy

[Bandit policy](/python/api/azure-ai-ml/azure.ai.ml.sweep.banditpolicy) is based on slack factor/slack amount and evaluation interval. Bandit policy ends a job when the primary metric isn't within the specified slack factor/slack amount of the most successful job.

Specify the following configuration parameters:

* `slack_factor` or `slack_amount`: the slack allowed with respect to the best performing training job. `slack_factor` specifies the allowable slack as a ratio. `slack_amount` specifies the allowable slack as an absolute amount, instead of a ratio.

    For example,  consider a Bandit policy applied at interval 10. Assume that the best performing job at interval 10 reported a primary metric is 0.8 with a goal to maximize the primary metric. If the policy specifies a `slack_factor` of 0.2, any training jobs whose best metric at interval 10 is less than 0.66 (0.8/(1+`slack_factor`)) will be terminated.
