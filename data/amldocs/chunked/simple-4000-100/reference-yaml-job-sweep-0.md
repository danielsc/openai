
# CLI (v2) sweep job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/sweepJob.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `type` | const | **Required.** The type of job. | `sweep` | `sweep` |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `sampling_algorithm` | object | **Required.** The hyperparameter sampling algorithm to use over the `search_space`. One of [RandomSamplingAlgorithm](#randomsamplingalgorithm), [GridSamplingAlgorithm](#gridsamplingalgorithm),or [BayesianSamplingAlgorithm](#bayesiansamplingalgorithm). | | |
| `search_space` | object | **Required.** Dictionary of the hyperparameter search space. The key is the name of the hyperparameter and the value is the parameter expression. <br><br> Hyperparameters can be referenced in the `trial.command` using the `${{ search_space.<hyperparameter> }}` expression. | | |
| `search_space.<hyperparameter>` | object | See [Parameter expressions](#parameter-expressions) for the set of possible expressions to use. | | |
| `objective.primary_metric` | string | **Required.** The name of the primary metric reported by each trial job. The metric must be logged in the user's training script using `mlflow.log_metric()` with the same corresponding metric name. | | |
| `objective.goal` | string | **Required.** The optimization goal of the `objective.primary_metric`. | `maximize`, `minimize` | |
| `early_termination` | object | The early termination policy to use. A trial job is canceled when the criteria of the specified policy are met. If omitted, no early termination policy will be applied. One of [BanditPolicy](#banditpolicy), [MedianStoppingPolicy](#medianstoppingpolicy),or [TruncationSelectionPolicy](#truncationselectionpolicy). | | |
| `limits` | object | Limits for the sweep job. See [Attributes of the `limits` key](#attributes-of-the-limits-key). | | |
| `compute` | string | **Required.** Name of the compute target to execute the job on, using the `azureml:<compute_name>` syntax. | | |
| `trial` | object | **Required.** The job template for each trial. Each trial job will be provided with a different combination of hyperparameter values that the system samples from the `search_space`. See [Attributes of the `trial` key](#attributes-of-the-trial-key). | | |
| `inputs` | object | Dictionary of inputs to the job. The key is a name for the input within the context of the job and the value is the input value. <br><br> Inputs can be referenced in the `command` using the `${{ inputs.<input_name> }}` expression. | | |
| `inputs.<input_name>` | number, integer, boolean, string or object | One of a literal value (of type number, integer, boolean, or string) or an object containing a [job input data specification](#job-inputs). | | |
| `outputs` | object | Dictionary of output configurations of the job. The key is a name for the output within the context of the job and the value is the output configuration. <br><br> Outputs can be referenced in the `command` using the `${{ outputs.<output_name> }}` expression. | |
