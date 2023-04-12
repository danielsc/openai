    For example,  consider a Bandit policy applied at interval 10. Assume that the best performing job at interval 10 reported a primary metric is 0.8 with a goal to maximize the primary metric. If the policy specifies a `slack_factor` of 0.2, any training jobs whose best metric at interval 10 is less than 0.66 (0.8/(1+`slack_factor`)) will be terminated.
* `evaluation_interval`: (optional) the frequency for applying the policy
* `delay_evaluation`: (optional) delays the first policy evaluation for a specified number of intervals



```Python
from azure.ai.ml.sweep import BanditPolicy
sweep_job.early_termination = BanditPolicy(slack_factor = 0.1, delay_evaluation = 5, evaluation_interval = 1)
```

In this example, the early termination policy is applied at every interval when metrics are reported, starting at evaluation interval 5. Any jobs whose best metric is less than (1/(1+0.1) or 91% of the best performing jobs will be terminated.

### Median stopping policy

[Median stopping](/python/api/azure-ai-ml/azure.ai.ml.sweep.medianstoppingpolicy) is an early termination policy based on running averages of primary metrics reported by the jobs. This policy computes running averages across all training jobs and stops jobs whose primary metric value is worse than the median of the averages.

This policy takes the following configuration parameters:
* `evaluation_interval`: the frequency for applying the policy (optional parameter).
* `delay_evaluation`: delays the first policy evaluation for a specified number of intervals (optional parameter).


```Python
from azure.ai.ml.sweep import MedianStoppingPolicy
sweep_job.early_termination = MedianStoppingPolicy(delay_evaluation = 5, evaluation_interval = 1)
```

In this example, the early termination policy is applied at every interval starting at evaluation interval 5. A job is stopped at interval 5 if its best primary metric is worse than the median of the running averages over intervals 1:5 across all training jobs.

### Truncation selection policy

[Truncation selection](/python/api/azure-ai-ml/azure.ai.ml.sweep.truncationselectionpolicy) cancels a percentage of lowest performing jobs at each evaluation interval. jobs are compared using the primary metric. 

This policy takes the following configuration parameters:

* `truncation_percentage`: the percentage of lowest performing jobs to terminate at each evaluation interval. An integer value between 1 and 99.
* `evaluation_interval`: (optional) the frequency for applying the policy
* `delay_evaluation`: (optional) delays the first policy evaluation for a specified number of intervals
* `exclude_finished_jobs`: specifies whether to exclude finished jobs when applying the policy


```Python
from azure.ai.ml.sweep import TruncationSelectionPolicy
sweep_job.early_termination = TruncationSelectionPolicy(evaluation_interval=1, truncation_percentage=20, delay_evaluation=5, exclude_finished_jobs=true)
```

In this example, the early termination policy is applied at every interval starting at evaluation interval 5. A job terminates at interval 5 if its performance at interval 5 is in the lowest 20% of performance of all jobs at interval 5 and will exclude finished jobs when applying the policy.

### No termination policy (default)

If no policy is specified, the hyperparameter tuning service will let all training jobs execute to completion.

```Python
sweep_job.early_termination = None
```

### Picking an early termination policy

* For a conservative policy that provides savings without terminating promising jobs, consider a Median Stopping Policy with `evaluation_interval` 1 and `delay_evaluation` 5. These are conservative settings that can provide approximately 25%-35% savings with no loss on primary metric (based on our evaluation data).
* For more aggressive savings, use Bandit Policy with a smaller allowable slack or Truncation Selection Policy with a larger truncation percentage.

## Set limits for your sweep job

Control your resource budget by setting limits for your sweep job.
