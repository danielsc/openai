
# CLI (v2) Automated ML text NER job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

Every Azure Machine Learning entity has a schematized YAML representation. You can create a new entity from a YAML configuration file with a `.yml` or `.yaml` extension.

This article provides a reference for some syntax concepts you will encounter while configuring these YAML files for NLP text NER jobs.

The source JSON schema can be found at https://azuremlsdk2.blob.core.windows.net/preview/0.0.1/autoMLNLPTextNERJob.schema.json

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | Represents the location/url to load the YAML schema. If the user uses the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of the file enables the user to invoke schema and resource completions. | | |
| `type` | const | **Required.** The type of job. | `automl` | `automl` |
| `task` | const | **Required.** The type of AutoML task. <br> Task description for NER: <br> There are multiple possible tags for tokens in sequences. The task is to predict the tags for all the tokens for each sequence. For example, extracting domain-specific entities from unstructured text, such as contracts or financial documents. | `text_ner` |  |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `compute` | string | Name of the compute target to execute the job on. To reference an existing compute in the workspace, we use syntax: `azureml:<compute_name>` | | |
| `log_verbosity` | number | Different levels of log verbosity. |`not_set`, `debug`, `info`, `warning`, `error`, `critical` | `info` |
| `primary_metric` | string |  The metric that AutoML will optimize for model selection. |`accuracy`| `accuracy` |
| `training_data` | object |  **Required.** The data to be used within the job. Unlike multi-class or multi-label, which takes .csv format datasets, named entity recognition requires CoNLL format. The file must contain exactly two columns and in each row, the token and the label is separated by a single space. See [NER](./how-to-auto-train-nlp-models.md?tabs=cli#named-entity-recognition-ner) section for more detail.| | | 
| `validation_data` | object | **Required.** The validation data to be used within the job. <br> - The file should not start with an empty line <br> - Each line must be an empty line, or follow format `{token}` `{label}`, where there is exactly one space between the token and the label and no white space after the label <br> - All labels must start with I-, B-, or be exactly O. Case sensitive <br> - Exactly one empty line between two samples <br> - Exactly one empty line at the end of the file <br> See [data validation](./how-to-auto-train-nlp-models.md?tabs=cli#data-validation) section for more detail. | | |
| `limits` | object | Dictionary of limit configurations of the job. Parameters in this section: `max_concurrent_trials`, `max_nodes`, `max_trials`, `timeout_minutes`, `trial_timeout_minutes`. See [limits](#limits) for detail.| | |
| `training_parameters` | object | Dictionary containing training parameters for the job. Provide an object that has keys as listed in following sections. <br> For more information, see [supported hyperparameters](./how-to-auto-train-nlp-models.md?tabs=cli#supported-hyperparameters) section| | |
