| `error_threshold` | integer | The number of file failures that should be ignored. If the error count for the entire input goes above this value, the batch scoring job will be terminated. `error_threshold` is for the entire input and not for individual mini batches. If omitted, any number of file failures will be allowed without terminating the job.  | | `-1` |
| `logging_level` | string | The log verbosity level. | `warning`, `info`, `debug` | `info` |
| `mini_batch_size` | integer | The number of files the `code_configuration.scoring_script` can process in one `run()` call. | | `10` |
| `retry_settings` | object | Retry settings for scoring each mini batch. | | |
| `retry_settings.max_retries` | integer | The maximum number of retries for a failed or timed-out mini batch. | | `3` |
| `retry_settings.timeout` | integer | The timeout in seconds for scoring a mini batch. | | `30` |
| `output_action` | string | Indicates how the output should be organized in the output file. | `append_row`, `summary_only` | `append_row` |
| `output_file_name` | string | Name of the batch scoring output file. | | `predictions.csv` |
| `environment_variables` | object | Dictionary of environment variable key-value pairs to set for each batch scoring job. | | |

## Remarks

The `az ml batch-deployment` commands can be used for managing Azure Machine Learning batch deployments.

## Examples

Examples are available in the [examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/cli/endpoints/batch). Several are shown below.

## YAML: basic (MLflow)

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
name: nyc-taxi-mlflow-dpl
endpoint_name: nyc-taxi-batch
model: 
  path: nyc-taxi/model
compute: azureml:batch-cluster
```

## YAML: custom model and scoring code

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json
name: mnist-torch-dpl
description: A deployment using Torch to solve the MNIST classification dataset.
endpoint_name: mnist-batch
model: 
  path: ./mnist/model/
code_configuration:
  code: ./mnist/code/
  scoring_script: batch_driver.py
environment:
  conda_file: ./mnist/environment/conda.yml
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest
compute: azureml:batch-cluster
resources:
  instance_count: 1
max_concurrency_per_instance: 2
mini_batch_size: 10
output_action: append_row
output_file_name: predictions.csv
retry_settings:
  max_retries: 3
  timeout: 30
error_threshold: -1
logging_level: info
```

## Next steps

- [Install and use the CLI (v2)](how-to-configure-cli.md)
