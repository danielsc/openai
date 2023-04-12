
You can define a search space with customized settings:

```python 
text_ner_job.extend_search_space( 
    [ 
        SearchSpace( 
            model_name=Choice([NlpModels.BERT_BASE_CASED, NlpModels.ROBERTA_BASE]) 
        ), 
        SearchSpace( 
            model_name=Choice([NlpModels.DISTILROBERTA_BASE]), 
            learning_rate_scheduler=Choice([NlpLearningRateScheduler.LINEAR,  
                                            NlpLearningRateScheduler.COSINE]), 
            learning_rate=Uniform(5e-6, 5e-5) 
        ) 
    ] 
) 
 ```

You can configure the sweep procedure via sampling algorithm early termination: 
```python
text_ner_job.set_sweep( 
    sampling_algorithm="Random", 
    early_termination=BanditPolicy( 
        evaluation_interval=2, slack_factor=0.05, delay_evaluation=6 
    ) 
) 
```


### Sampling methods for the sweep 

When sweeping hyperparameters, you need to specify the sampling method to use for sweeping over the defined parameter space. Currently, the following sampling methods are supported with the `sampling_algorithm` parameter:

| Sampling type | AutoML Job syntax |
|-------|---------|
|[Random Sampling](how-to-tune-hyperparameters.md#random-sampling)| `random` |
|[Grid Sampling](how-to-tune-hyperparameters.md#grid-sampling)| `grid` |
|[Bayesian Sampling](how-to-tune-hyperparameters.md#bayesian-sampling)| `bayesian` |

### Experiment budget 

You can optionally specify the experiment budget for your AutoML NLP training job using the `timeout_minutes` parameter in the `limits` - the amount of time in minutes before the experiment terminates. If none specified, the default experiment timeout is seven days (maximum 60 days).  

AutoML NLP also supports `trial_timeout_minutes`, the maximum amount of time in minutes an individual trial can run before being terminated, and `max_nodes`, the maximum number of nodes from the backing compute cluster to leverage for the job. These parameters also belong to the `limits` section.  



[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
limits: 
  timeout_minutes: 60 
  trial_timeout_minutes: 20 
  max_nodes: 2 
```


### Early termination policies  

You can automatically end poorly performing runs with an early termination policy. Early termination improves computational efficiency, saving compute resources that would have been otherwise spent on less promising configurations. AutoML NLP supports early termination policies using the `early_termination` parameter. If no termination policy is specified, all configurations are run to completion. 

Learn more about [how to configure the early termination policy for your hyperparameter sweep.](how-to-tune-hyperparameters.md#early-termination) 

### Resources for the sweep

You can control the resources spent on your hyperparameter sweep by specifying the `max_trials` and the `max_concurrent_trials` for the sweep.

Parameter | Detail
-----|----
`max_trials` |  Parameter for maximum number of configurations to sweep. Must be an integer between 1 and 1000. When exploring just the default hyperparameters for a given model algorithm, set this parameter to 1. The default value is 1.
`max_concurrent_trials`| Maximum number of runs that can run concurrently. If specified, must be an integer between 1 and 100.  The default value is 1. <br><br> **NOTE:** <li> The number of concurrent runs is gated on the resources available in the specified compute target. Ensure that the compute target has the available resources for the desired concurrency.  <li> `max_concurrent_trials` is capped at `max_trials` internally. For example, if user sets `max_concurrent_trials=4`, `max_trials=2`, values would be internally updated as `max_concurrent_trials=2`, `max_trials=2`.

You can configure all the sweep related parameters as shown in the example below.


[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
sweep:
  limits:
    max_trials: 10
    max_concurrent_trials: 2
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_factor: 0.2
    delay_evaluation: 6
```
