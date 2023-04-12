
# Hyperparameter tuning a model (v2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](v1/how-to-tune-hyperparameters-v1.md)
> * [v2 (current version)](how-to-tune-hyperparameters.md)

Automate efficient hyperparameter tuning using Azure Machine Learning SDK v2 and CLI v2 by way of the SweepJob type. 

1. Define the parameter search space for your trial
2. Specify the sampling algorithm for your sweep job
3. Specify the objective to optimize
4. Specify early termination policy for low-performing jobs
5. Define limits for the sweep job
6. Launch an experiment with the defined configuration
7. Visualize the training jobs
8. Select the best configuration for your model

## What is hyperparameter tuning?

**Hyperparameters** are adjustable parameters that let you control the model training process. For example, with neural networks, you decide the number of hidden layers and the number of nodes in each layer. Model performance depends heavily on hyperparameters.

 **Hyperparameter tuning**, also called **hyperparameter optimization**, is the process of finding the configuration of hyperparameters that results in the best performance. The process is typically computationally expensive and manual.

Azure Machine Learning lets you automate hyperparameter tuning and run experiments in parallel to efficiently optimize hyperparameters.


## Define the search space

Tune hyperparameters by exploring the range of values defined for each hyperparameter.

Hyperparameters can be discrete or continuous, and has a distribution of values described by a
[parameter expression](reference-yaml-job-sweep.md#parameter-expressions).

### Discrete hyperparameters

Discrete hyperparameters are specified as a `Choice` among discrete values. `Choice` can be:

* one or more comma-separated values
* a `range` object
* any arbitrary `list` object

```Python
from azure.ai.ml.sweep import Choice

command_job_for_sweep = command_job(
    batch_size=Choice(values=[16, 32, 64, 128]),
    number_of_hidden_layers=Choice(values=range(1,5)),
)
```

In this case, `batch_size` one of the values [16, 32, 64, 128] and `number_of_hidden_layers` takes one of the values [1, 2, 3, 4].

The following advanced discrete hyperparameters can also be specified using a distribution:

* `QUniform(min_value, max_value, q)` - Returns a value like round(Uniform(min_value, max_value) / q) * q
* `QLogUniform(min_value, max_value, q)` - Returns a value like round(exp(Uniform(min_value, max_value)) / q) * q
* `QNormal(mu, sigma, q)` - Returns a value like round(Normal(mu, sigma) / q) * q
* `QLogNormal(mu, sigma, q)` - Returns a value like round(exp(Normal(mu, sigma)) / q) * q

### Continuous hyperparameters 

The Continuous hyperparameters are specified as a distribution over a continuous range of values:

* `Uniform(min_value, max_value)` - Returns a value uniformly distributed between min_value and max_value
* `LogUniform(min_value, max_value)` - Returns a value drawn according to exp(Uniform(min_value, max_value)) so that the logarithm of the return value is uniformly distributed
* `Normal(mu, sigma)` - Returns a real value that's normally distributed with mean mu and standard deviation sigma
* `LogNormal(mu, sigma)` - Returns a value drawn according to exp(Normal(mu, sigma)) so that the logarithm of the return value is normally distributed

An example of a parameter space definition:

```Python
from azure.ai.ml.sweep import Normal, Uniform

command_job_for_sweep = command_job(   
    learning_rate=Normal(mu=10, sigma=3),
    keep_probability=Uniform(min_value=0.05, max_value=0.1),
)
```

This code defines a search space with two parameters - `learning_rate` and `keep_probability`. `learning_rate` has a normal distribution with mean value 10 and a standard deviation of 3. `keep_probability` has a uniform distribution with a minimum value of 0.05 and a maximum value of 0.1.
