| `training_parameters` | object | Dictionary containing training parameters for the job. <br> See [supported hyperparameters](#supported-hyperparameters) for detail. <br> *Note*: Hyperparameters set in the `training_parameters` are fixed across all sweeping runs and thus don't need to be included in the search space. | | |
| `sweep` | object | Dictionary containing sweep parameters for the job. It has two keys - `sampling_algorithm` (**required**) and `early_termination`. For more information, see [model sweeping and hyperparameter tuning](./how-to-auto-train-nlp-models.md?tabs=cli#model-sweeping-and-hyperparameter-tuning-preview) sections. | | |
| `search_space` | object | Dictionary of the hyperparameter search space. The key is the name of the hyperparameter and the value is the parameter expression. All parameters that are fixable via `training_parameters` are supported here (to be instead swept over). See  [supported hyperparameters](#supported-hyperparameters) for more detail. <br> There are two types of hyperparameters: <br> - **Discrete Hyperparameters**: Discrete hyperparameters are specified as a [`choice`](./reference-yaml-job-sweep.md#choice) among discrete values. `choice` can be one or more comma-separated values, a `range` object, or any arbitrary `list` object. Advanced discrete hyperparameters can also be specified using a distribution - [`randint`](./reference-yaml-job-sweep.md#randint), [`qlognormal`, `qnormal`](./reference-yaml-job-sweep.md#qlognormal-qnormal), [`qloguniform`, `quniform`](./reference-yaml-job-sweep.md#qloguniform-quniform). For more information, see this [section](./how-to-tune-hyperparameters.md#discrete-hyperparameters). <br> - **Continuous hyperparameters**: Continuous hyperparameters are specified as a distribution over a continuous range of values. Currently supported distributions are - [`lognormal`, `normal`](./reference-yaml-job-sweep.md#lognormal-normal), [`loguniform`](./reference-yaml-job-sweep.md#loguniform), [`uniform`](./reference-yaml-job-sweep.md#uniform). For more information, see this [section](./how-to-tune-hyperparameters.md#continuous-hyperparameters). <br> <br> See [parameter expressions](./reference-yaml-job-sweep.md#parameter-expressions) for the set of possible expressions to use.  | | |
| `outputs` | object | Dictionary of output configurations of the job. The key is a name for the output within the context of the job and the value is the output configuration. | | |
| `outputs.best_model` | object | Dictionary of output configurations for best model. For more information, see [Best model output configuration](#best-model-output-configuration). | | |

Other syntax used in configurations:

### Limits

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `max_concurrent_trials` | integer | Represents the maximum number of trials (children jobs) that would be executed in parallel. | | `1` |
| `max_trials` | integer | Represents the maximum number of trials an AutoML nlp job can try to run a training algorithm with different combination of hyperparameters. | | `1` |
| `timeout_minutes ` | integer | Represents the maximum amount of time in minutes that the submitted AutoML NLP job can take to run . After this, the job will get terminated. The default timeout in AutoML NLP jobs is 7 days. | | `10080`|
| `trial_timeout_minutes ` | integer | Represents the maximum amount of time in minutes that each trial (child job) in the submitted AutoML job can take run. After this, the child job will get terminated.  | | |
|`max_nodes`| integer | The maximum number of nodes from the backing compute cluster to leverage for the job.| | `1` |

### Supported hyperparameters

The following table describes the hyperparameters that AutoML NLP supports. 

| Parameter name | Description | Syntax |
|-------|---------|---------| 
| gradient_accumulation_steps | The number of backward operations whose gradients are to be summed up before performing one step of gradient descent by calling the optimizer’s step function. <br><br> This is leveraged to use an effective batch size which is gradient_accumulation_steps times larger than the maximum size that fits the GPU. | Must be a positive integer.
