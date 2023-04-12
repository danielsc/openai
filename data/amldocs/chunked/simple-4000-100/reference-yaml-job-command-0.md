
# CLI (v2) command job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The source JSON schema can be found at https://azuremlschemas.azureedge.net/latest/commandJob.schema.json.



[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `$schema` | string | The YAML schema. If you use the Azure Machine Learning VS Code extension to author the YAML file, including `$schema` at the top of your file enables you to invoke schema and resource completions. | | |
| `type` | const | The type of job. | `command` | `command` |
| `name` | string | Name of the job. Must be unique across all jobs in the workspace. If omitted, Azure ML will autogenerate a GUID for the name. | | |
| `display_name` | string | Display name of the job in the studio UI. Can be non-unique within the workspace. If omitted, Azure ML will autogenerate a human-readable adjective-noun identifier for the display name. | | |
| `experiment_name` | string | Experiment name to organize the job under. Each job's run record will be organized under the corresponding experiment in the studio's "Experiments" tab. If omitted, Azure ML will default it to the name of the working directory where the job was created. | | |
| `description` | string | Description of the job. | | |
| `tags` | object | Dictionary of tags for the job. | | |
| `command` | string | **Required (if not using `component` field).** The command to execute. | | |
| `code` | string | Local path to the source code directory to be uploaded and used for the job. | | |
| `environment` | string or object | **Required (if not using `component` field).** The environment to use for the job. This can be either a reference to an existing versioned environment in the workspace or an inline environment specification. <br><br> To reference an existing environment use the `azureml:<environment_name>:<environment_version>` syntax or `azureml:<environment_name>@latest` (to reference the latest version of an environment). <br><br> To define an environment inline please follow the [Environment schema](reference-yaml-environment.md#yaml-syntax). Exclude the `name` and `version` properties as they are not supported for inline environments. | | |
| `environment_variables` | object | Dictionary of environment variable key-value pairs to set on the process where the command is executed. | | |
| `distribution` | object | The distribution configuration for distributed training scenarios. One of [MpiConfiguration](#mpiconfiguration), [PyTorchConfiguration](#pytorchconfiguration), or [TensorFlowConfiguration](#tensorflowconfiguration). | | |
| `compute` | string | Name of the compute target to execute the job on. This can be either a reference to an existing compute in the workspace (using the `azureml:<compute_name>` syntax) or `local` to designate local execution. **Note:** jobs in pipeline didn't support `local` as `compute` | | `local` |
| `resources.instance_count` | integer | The number of nodes to use for the job. | | `1` |
| `resources.instance_type` | string | The instance type to use for the job. Applicable for jobs running on Azure Arc-enabled Kubernetes compute (where the compute target specified in the `compute` field is of `type: kubernentes`). If omitted, this will default to the default instance type for the Kubernetes cluster. For more information, see [Create and select Kubernetes instance types](how-to-attach-kubernetes-anywhere.md). | | |
| `limits.timeout` | integer | The maximum time in seconds the job is allowed to run. Once this limit is reached the system will cancel the job. | | |
| `inputs` | object | Dictionary of inputs to the job. The key is a name for the input within the context of the job and the value is the input value. <br><br> Inputs can be referenced in the `command` using the `${{ inputs.<input_name> }}` expression. | | |
