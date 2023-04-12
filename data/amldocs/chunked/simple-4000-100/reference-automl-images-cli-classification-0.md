
# CLI (v2) Automated ML image classification job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLImageClassificationJob.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If the user uses the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of the file enables the user to invoke schema and resource completions. | | |
| `type` | const | **Required.** The type of job. | `automl` | `automl` |
| `task` | const | **Required.** The type of AutoML task. | `image_classification` | `image_classification` |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `compute` | string | Name of the compute target to execute the job on. This compute can be either a reference to an existing compute in the workspace (using the `azureml:<compute_name>` syntax) or `local` to designate local execution. For more information on compute for AutoML image jobs, see [Compute to run experiment](./how-to-auto-train-image-models.md?tabs=cli#compute-to-run-experiment) section.<br> <br>  *Note:* jobs in pipeline don't support `local` as `compute`. * | | `local` |
| `log_verbosity` | number | Different levels of log verbosity. |`not_set`, `debug`, `info`, `warning`, `error`, `critical` | `info` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`accuracy` | `accuracy` |
| `target_column_name` | string |  **Required.** The name of the column to target for predictions. It must always be specified. This parameter is applicable to `training_data` and `validation_data`. | |  |
| `training_data` | object |  **Required.** The data to be used within the job. It should contain both training feature columns and a target column. The parameter training_data must always be provided. For more information on keys and their descriptions, see [Training or validation data](#training-or-validation-data) section. For an example, see [Consume data](./how-to-auto-train-image-models.md?tabs=cli#consume-data) section. | |  |
| `validation_data` | object |  The validation data to be used within the job. It should contain both training features and label column (optionally a sample weights column). If `validation_data` is specified, then `training_data` and `target_column_name` parameters must be specified. For more information on keys and their descriptions, see [Training or validation data](#training-or-validation-data) section. For an example, see [Consume data](./how-to-auto-train-image-models.md?tabs=cli#consume-data) section| |  |
| `validation_data_size` | float |  What fraction of the data to hold out for validation when user validation data isn't specified. | A value in range (0.0, 1.0) |  |
| `limits` | object | Dictionary of limit configurations of the job. The key is name for the limit within the context of the job and the value is limit value. For more information, see [Configure your experiment settings](./how-to-auto-train-image-models.md?tabs=cli#job-limits) section. | | |
