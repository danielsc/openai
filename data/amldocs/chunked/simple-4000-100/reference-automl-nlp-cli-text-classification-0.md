
# CLI (v2) Automated ML text classification job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

Every Azure Machine Learning entity has a schematized YAML representation. You can create a new entity from a YAML configuration file with a `.yml` or `.yaml` extension.

This article provides a reference for some syntax concepts you will encounter while configuring these YAML files for NLP text classification jobs.

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLNLPTextClassificationJob.schema.json



## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | Represents the location/url to load the YAML schema. If the user uses the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of the file enables the user to invoke schema and resource completions. | | |
| `type` | const | **Required.** The type of job. | `automl` | `automl` |
| `task` | const | **Required.** The type of AutoML task. <br> Task description of text classification: <br> There are multiple possible classes and each sample can be classified as exactly one class. The task is to predict the correct class for each sample. For example, classifying a movie script as "Comedy" or "Romantic". | `text_classification` |  |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `compute` | string | Name of the compute target to execute the job on. To reference an existing compute in the workspace, we use syntax: `azureml:<compute_name>` | | |
| `log_verbosity` | number | Different levels of log verbosity. |`not_set`, `debug`, `info`, `warning`, `error`, `critical` | `info` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`accuracy`,<br> `auc_weighted`,  <br> `precision_score_weighted` | `accuracy` |
| `target_column_name` | string |  **Required.** The name of the column to target for predictions. It must always be specified. This parameter is applicable to `training_data` and `validation_data`. | |  |
| `training_data` | object |  **Required.** The data to be used within the job. For multi-class classification, the dataset can contain several text columns and exactly one label column. | |  |
| `validation_data` | object | **Required.** The validation data to be used within the job. It should be consistent with the training data in terms of the set of columns, data type for each column, order of columns from left to right and at least two unique labels. <br> *Note*: the column names within each dataset should be unique.| | |
| `limits` | object | Dictionary of limit configurations of the job. Parameters in this section: `max_concurrent_trials`, `max_nodes`, `max_trials`, `timeout_minutes`, `trial_timeout_minutes`. See [limits](#limits) for detail.| | |
| `training_parameters` | object | Dictionary containing training parameters for the job. <br> See [supported hyperparameters](#supported-hyperparameters) for detail. <br> *Note*: Hyperparameters set in the `training_parameters` are fixed across all sweeping runs and thus don't need to be included in the search space. | | |
