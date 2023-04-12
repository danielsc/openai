
# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=search-space-settings)]


#### Define the parameter search space

You can define the model architectures and hyperparameters to sweep in the parameter space. You can either specify a single model architecture or multiple ones. 

* See [Individual trials](#individual-trials) for the list of supported model architectures for each task type. 
* See [Hyperparameters for computer vision tasks](reference-automl-images-hyperparameters.md)  hyperparameters for each computer vision task type. 
* See [details on supported distributions for discrete and continuous hyperparameters](how-to-tune-hyperparameters.md#define-the-search-space).

#### Sampling methods for the sweep

When sweeping hyperparameters, you need to specify the sampling method to use for sweeping over the defined parameter space. Currently, the following sampling methods are supported with the `sampling_algorithm` parameter:

| Sampling type | AutoML Job syntax |
|-------|---------|
|[Random Sampling](how-to-tune-hyperparameters.md#random-sampling)| `random` |
|[Grid Sampling](how-to-tune-hyperparameters.md#grid-sampling)| `grid` |
|[Bayesian Sampling](how-to-tune-hyperparameters.md#bayesian-sampling)| `bayesian` |
    
> [!NOTE]
> Currently only random and grid sampling support conditional hyperparameter spaces.

#### Early termination policies

You can automatically end poorly performing trials with an early termination policy. Early termination improves computational efficiency, saving compute resources that would have been otherwise spent on less promising trials. Automated ML for images supports the following early termination policies using the `early_termination` parameter. If no termination policy is specified, all trials are run to completion.


| Early termination policy | AutoML Job syntax |
|-------|---------|
|[Bandit policy](how-to-tune-hyperparameters.md#bandit-policy)| CLI v2: `bandit` <br> SDK v2: `BanditPolicy()` |
|[Median stopping policy](how-to-tune-hyperparameters.md#median-stopping-policy)| CLI v2: `median_stopping` <br> SDK v2: `MedianStoppingPolicy()` |
|[Truncation selection policy](how-to-tune-hyperparameters.md#truncation-selection-policy)| CLI v2: `truncation_selection` <br> SDK v2: `TruncationSelectionPolicy()` |

Learn more about [how to configure the early termination policy for your hyperparameter sweep](how-to-tune-hyperparameters.md#early-termination).

> [!NOTE]
> For a complete sweep configuration sample, please refer to this [tutorial](tutorial-auto-train-image-models.md#manual-hyperparameter-sweeping-for-image-tasks).


You can configure all the sweep related parameters as shown in the example below.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
sweep:
  sampling_algorithm: random
  early_termination:
    type: bandit
    evaluation_interval: 2
    slack_factor: 0.2
    delay_evaluation: 6
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=sweep-settings)]


#### Fixed settings

You can pass fixed settings or parameters that don't change during the parameter space sweep as shown below.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_parameters:
  early_stopping: True
  evaluation_frequency: 1
```


# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
 
[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=pass-arguments)]
