This code defines a search space with two parameters - `learning_rate` and `keep_probability`. `learning_rate` has a normal distribution with mean value 10 and a standard deviation of 3. `keep_probability` has a uniform distribution with a minimum value of 0.05 and a maximum value of 0.1.

For the CLI, you can use the [sweep job YAML schema](./reference-yaml-job-sweep.md), to define the search space in your YAML:
```YAML
    search_space:
        conv_size:
            type: choice
            values: [2, 5, 7]
        dropout_rate:
            type: uniform
            min_value: 0.1
            max_value: 0.2
```

## Sampling the hyperparameter space

Specify the parameter sampling method to use over the hyperparameter space. Azure Machine Learning supports the following methods:

* Random sampling
* Grid sampling
* Bayesian sampling

### Random sampling

Random sampling supports discrete and continuous hyperparameters. It supports early termination of low-performance jobs. Some users do an initial search with random sampling and then refine the search space to improve results.

In random sampling, hyperparameter values are randomly selected from the defined search space. After creating your command job, you can use the sweep parameter to define the sampling algorithm. 

```Python
from azure.ai.ml.sweep import Normal, Uniform, RandomParameterSampling

command_job_for_sweep = command_job(   
    learning_rate=Normal(mu=10, sigma=3),
    keep_probability=Uniform(min_value=0.05, max_value=0.1),
    batch_size=Choice(values=[16, 32, 64, 128]),
)

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = "random",
    ...
)
```
#### Sobol
Sobol is a type of random sampling supported by sweep job types. You can use sobol to reproduce your results using seed and cover the search space distribution more evenly. 

To use sobol, use the RandomParameterSampling class to add the seed and rule as shown in the example below. 

```Python
from azure.ai.ml.sweep import RandomParameterSampling

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = RandomParameterSampling(seed=123, rule="sobol"),
    ...
)
```

### Grid sampling

Grid sampling supports discrete hyperparameters. Use grid sampling if you can budget to exhaustively search over the search space. Supports early termination of low-performance jobs.

Grid sampling does a simple grid search over all possible values. Grid sampling can only be used with `choice` hyperparameters. For example, the following space has six samples:

```Python
from azure.ai.ml.sweep import Choice

command_job_for_sweep = command_job(
    batch_size=Choice(values=[16, 32]),
    number_of_hidden_layers=Choice(values=[1,2,3]),
)

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = "grid",
    ...
)
```

### Bayesian sampling

Bayesian sampling is based on the Bayesian optimization algorithm. It picks samples based on how previous samples did, so that new samples improve the primary metric.

Bayesian sampling is recommended if you have enough budget to explore the hyperparameter space. For best results, we recommend a maximum number of jobs greater than or equal to 20 times the number of hyperparameters being tuned. 

The number of concurrent jobs has an impact on the effectiveness of the tuning process. A smaller number of concurrent jobs may lead to better sampling convergence, since the smaller degree of parallelism increases the number of jobs that benefit from previously completed jobs.

Bayesian sampling only supports `choice`, `uniform`, and `quniform` distributions over the search space.

```Python
from azure.ai.ml.sweep import Uniform, Choice

command_job_for_sweep = command_job(   
    learning_rate=Uniform(min_value=0.05, max_value=0.1),
    batch_size=Choice(values=[16, 32, 64, 128]),
)

sweep_job = command_job_for_sweep.sweep(
    compute="cpu-cluster",
    sampling_algorithm = "bayesian",
    ...
)
```
