
# CLI (v2) batch deployment YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `name` | string | **Required.** Name of the deployment. | | |
| `description` | string | Description of the deployment. | | |
| `tags` | object | Dictionary of tags for the deployment. | | |
| `endpoint_name` | string | **Required.** Name of the endpoint to create the deployment under. | | |
| `model` | string or object | **Required.** The model to use for the deployment. This value can be either a reference to an existing versioned model in the workspace or an inline model specification. <br><br> To reference an existing model, use the `azureml:<model-name>:<model-version>` syntax. <br><br> To define a model inline, follow the [Model schema](reference-yaml-model.md#yaml-syntax). <br><br> As a best practice for production scenarios, you should create the model separately and reference it here. | | |
| `code_configuration` | object | Configuration for the scoring code logic. <br><br> This property is not required if your model is in MLflow format. | | |
| `code_configuration.code` | string | The local directory that contains all the Python source code to score the model. | | |
| `code_configuration.scoring_script` | string | The Python file in the above directory. This file must have an `init()` function and a `run()` function. Use the `init()` function for any costly or common preparation (for example, load the model in memory). `init()` will be called only once at beginning of process. Use `run(mini_batch)` to score each entry; the value of `mini_batch` is a list of file paths. The `run()` function should return a pandas DataFrame or an array. Each returned element indicates one successful run of input element in the `mini_batch`. For more information on how to author scoring script, see [Understanding the scoring script](batch-inference/how-to-batch-scoring-script.md#understanding-the-scoring-script).| | |
| `environment` | string or object | The environment to use for the deployment. This value can be either a reference to an existing versioned environment in the workspace or an inline environment specification. <br><br> This property is not required if your model is in MLflow format. <br><br> To reference an existing environment, use the `azureml:<environment-name>:<environment-version>` syntax. <br><br> To define an environment inline, follow the [Environment schema](reference-yaml-environment.md#yaml-syntax). <br><br> As a best practice for production scenarios, you should create the environment separately and reference it here. | | |
| `compute` | string | **Required.** Name of the compute target to execute the batch scoring jobs on. This value should be a reference to an existing compute in the workspace using the `azureml:<compute-name>` syntax. | | |
| `resources.instance_count` | integer | The number of nodes to use for each batch scoring job. | | `1` |
| `max_concurrency_per_instance` | integer | The maximum number of parallel `scoring_script` runs per instance. | | `1` |
| `error_threshold` | integer | The number of file failures that should be ignored. If the error count for the entire input goes above this value, the batch scoring job will be terminated. `error_threshold` is for the entire input and not for individual mini batches. If omitted, any number of file failures will be allowed without terminating the job.  | | `-1` |
| `logging_level` | string | The log verbosity level. | `warning`, `info`, `debug` | `info` |
