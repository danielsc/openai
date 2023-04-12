
# CLI (v2) pipeline job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](v1/reference-pipeline-yaml.md)
> * [v2 (current version)](reference-yaml-job-pipeline.md)

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json.

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `type` | const | **Required.** The type of job. | `pipeline` | |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `settings` | object | Default settings for the pipeline job. See [Attributes of the `settings` key](#attributes-of-the-settings-key) for the set of configurable properties. | | |
| `jobs` | object | **Required.** Dictionary of the set of individual jobs to run as steps within the pipeline. These jobs are considered child jobs of the parent pipeline job. <br><br> The key is the name of the step within the context of the pipeline job. This name is different from the unique job name of the child job. The value is the job specification, which can follow the [command job schema](reference-yaml-job-command.md#yaml-syntax) or [sweep job schema](reference-yaml-job-sweep.md#yaml-syntax). Currently only command jobs and sweep jobs can be run in a pipeline. Later releases will have support for other job types. | | |
| `inputs` | object | Dictionary of inputs to the pipeline job. The key is a name for the input within the context of the job and the value is the input value. <br><br> These pipeline inputs can be referenced by the inputs of an individual step job in the pipeline using the `${{ parent.inputs.<input_name> }}` expression. For more information on how to bind the inputs of a pipeline step to the inputs of the top-level pipeline job, see the [Expression syntax for binding inputs and outputs between steps in a pipeline job](reference-yaml-core-syntax.md#binding-inputs-and-outputs-between-steps-in-a-pipeline-job). | | |
| `inputs.<input_name>` | number, integer, boolean, string or object | One of a literal value (of type number, integer, boolean, or string) or an object containing a [job input data specification](#job-inputs). | | |
| `outputs` | object | Dictionary of output configurations of the pipeline job. The key is a name for the output within the context of the job and the value is the output configuration. <br><br> These pipeline outputs can be referenced by the outputs of an individual step job in the pipeline using the `${{ parents.outputs.<output_name> }}` expression. For more information on how to bind the inputs of a pipeline step to the inputs of the top-level pipeline job, see the [Expression syntax for binding inputs and outputs between steps in a pipeline job](reference-yaml-core-syntax.md#binding-inputs-and-outputs-between-steps-in-a-pipeline-job). | |
