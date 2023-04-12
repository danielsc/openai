| `outputs` | object | Dictionary of output configurations of the job. The key is a name for the output within the context of the job and the value is the output configuration. <br><br> Outputs can be referenced in the `command` using the `${{ outputs.<output_name> }}` expression. | |
| `outputs.<output_name>` | object | You can leave the object empty, in which case by default the output will be of type `uri_folder` and Azure ML will system-generate an output location for the output. File(s) to the output directory will be written via read-write mount. If you want to specify a different mode for the output, provide an object containing the [job output specification](#job-outputs). | |
| `identity` | object | The identity is used for data accessing. It can be [UserIdentityConfiguration](#useridentityconfiguration), [ManagedIdentityConfiguration](#managedidentityconfiguration) or None. If UserIdentityConfiguration, the identity of job submitter will be used to access input data and write result to output folder, otherwise, the managed identity of the compute target will be used. | |

### Sampling algorithms

#### RandomSamplingAlgorithm

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** The type of sampling algorithm. | `random` | |
| `seed` | integer | A random seed to use for initializing the random number generation. If omitted, the default seed value will be null. | | |
| `rule` | string | The type of random sampling to use. The default, `random`, will use simple uniform random sampling, while `sobol` will use the Sobol quasirandom sequence. | `random`, `sobol` | `random` |

#### GridSamplingAlgorithm

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of sampling algorithm. | `grid` |

#### BayesianSamplingAlgorithm

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of sampling algorithm. | `bayesian` |

### Early termination policies

#### BanditPolicy

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** The type of policy. | `bandit` | |
| `slack_factor` | number | The ratio used to calculate the allowed distance from the best performing trial. **One of `slack_factor` or `slack_amount` is required.** | | |
| `slack_amount` | number | The absolute distance allowed from the best performing trial. **One of `slack_factor` or `slack_amount` is required.** | | |
| `evaluation_interval` | integer | The frequency for applying the policy. | | `1` |
| `delay_evaluation` | integer | The number of intervals for which to delay the first policy evaluation. If specified, the policy applies on every multiple of `evaluation_interval` that is greater than or equal to `delay_evaluation`. | | `0` |

#### MedianStoppingPolicy

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** The type of policy. | `median_stopping` | |
| `evaluation_interval` | integer | The frequency for applying the policy. | | `1` |
| `delay_evaluation` | integer | The number of intervals for which to delay the first policy evaluation. If specified, the policy applies on every multiple of `evaluation_interval` that is greater than or equal to `delay_evaluation`. | | `0` |

#### TruncationSelectionPolicy

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** The type of policy. | `truncation_selection` | |
| `truncation_percentage` | integer | **Required.** The percentage of trial jobs to cancel at each evaluation interval. | | |
| `evaluation_interval` | integer | The frequency for applying the policy. | | `1` |
