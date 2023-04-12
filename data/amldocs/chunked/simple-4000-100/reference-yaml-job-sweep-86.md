| `truncation_percentage` | integer | **Required.** The percentage of trial jobs to cancel at each evaluation interval. | | |
| `evaluation_interval` | integer | The frequency for applying the policy. | | `1` |
| `delay_evaluation` | integer | The number of intervals for which to delay the first policy evaluation. If specified, the policy applies on every multiple of `evaluation_interval` that is greater than or equal to `delay_evaluation`. | | `0` |

### Parameter expressions

#### choice

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `choice` |
| `values` | array | **Required.** The list of discrete values to choose from. | |

#### randint

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `randint` |
| `upper` | integer | **Required.** The exclusive upper bound for the range of integers. | |

#### qlognormal, qnormal

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `qlognormal`, `qnormal` |
| `mu` | number | **Required.** The mean of the normal distribution. | |
| `sigma` | number | **Required.** The standard deviation of the normal distribution. | |
| `q` | integer | **Required.** The smoothing factor. | |

#### qloguniform, quniform

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `qloguniform`, `quniform` |
| `min_value` | number | **Required.** The minimum value in the range (inclusive). | |
| `max_value` | number | **Required.** The maximum value in the range (inclusive). | |
| `q` | integer | **Required.** The smoothing factor. | |

#### lognormal, normal

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `lognormal`, `normal` |
| `mu` | number | **Required.** The mean of the normal distribution. | |
| `sigma` | number | **Required.** The standard deviation of the normal distribution. | |

#### loguniform

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `loguniform` |
| `min_value` | number | **Required.** The minimum value in the range will be `exp(min_value)` (inclusive). | |
| `max_value` | number | **Required.** The maximum value in the range will be `exp(max_value)` (inclusive). | |

#### uniform

| Key | Type | Description | Allowed values |
| --- | ---- | ----------- | -------------- |
| `type` | const | **Required.** The type of expression. | `uniform` |
| `min_value` | number | **Required.** The minimum value in the range (inclusive). | |
| `max_value` | number | **Required.** The maximum value in the range (inclusive). | |

### Attributes of the `limits` key

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `max_total_trials` | integer | The maximum number of trial jobs. | `1000` |
| `max_concurrent_trials` | integer | The maximum number of trial jobs that can run concurrently. | Defaults to `max_total_trials`. |
| `timeout` | integer | The maximum time in seconds the entire sweep job is allowed to run. Once this limit is reached, the system will cancel the sweep job, including all its trials. | `5184000` |
| `trial_timeout` | integer | The maximum time in seconds each trial job is allowed to run. Once this limit is reached, the system will cancel the trial. | |

### Attributes of the `trial` key

| Key | Type | Description | Default value |
| --- | ---- | ----------- | ------------- |
| `command` | string | **Required.** The command to execute. | |
| `code` | string | Local path to the source code directory to be uploaded and used for the job. | |
| `environment` | string or object | **Required.** The environment to use for the job. This can be either a reference to an existing versioned environment in the workspace or an inline environment specification. <br> <br> To reference an existing environment, use the `azureml:<environment-name>:<environment-version>` syntax. <br><br> To define an environment inline, follow the [Environment schema](reference-yaml-environment.md#yaml-syntax). Exclude the `name` and `version` properties as they aren't supported for inline environments. | |
