
# CLI (v2) parallel job YAML schema

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](v1/reference-pipeline-yaml.md)
> * [v2 (current version)](reference-yaml-job-pipeline.md)

> [!IMPORTANT]
> Parallel job can only be used as a single step inside an Azure ML pipeline job. Thus, there is no source JSON schema for parallel job at this time. This document lists the valid keys and their values when creating a parallel job in a pipeline.

[!INCLUDE [schema note](../../includes/machine-learning-preview-old-json-schema-note.md)]

## YAML syntax

| Key | Type | Description | Allowed values | Default value |
| --- | ---- | ----------- | -------------- | ------------- |
| `type` | const | **Required.** The type of job. | `parallel` | |
| `inputs` | object | Dictionary of inputs to the parallel job. The key is a name for the input within the context of the job and the value is the input value. <br><br> Inputs can be referenced in the `program_arguments` using the `${{ inputs.<input_name> }}` expression. <br><br> Parallel job inputs can be referenced by pipeline inputs using the `${{ parent.inputs.<input_name> }}` expression. For how to bind the inputs of a parallel step to the pipeline inputs, see the [Expression syntax for binding inputs and outputs between steps in a pipeline job](reference-yaml-core-syntax.md#binding-inputs-and-outputs-between-steps-in-a-pipeline-job). | | |
| `inputs.<input_name>` | number, integer, boolean, string or object | One of a literal value (of type number, integer, boolean, or string) or an object containing a [job input data specification](#job-inputs). | | |
| `outputs` | object | Dictionary of output configurations of the parallel job. The key is a name for the output within the context of the job and the value is the output configuration. <br><br> Parallel job outputs can be referenced by pipeline outputs using the `${{ parents.outputs.<output_name> }}` expression. For how to bind the outputs of a parallel step to the pipeline outputs, see the [Expression syntax for binding inputs and outputs between steps in a pipeline job](reference-yaml-core-syntax.md#binding-inputs-and-outputs-between-steps-in-a-pipeline-job). | |
| `outputs.<output_name>` | object | You can leave the object empty, in which case by default the output will be of type `uri_folder` and Azure ML will system-generate an output location for the output based on the following templatized path: `{settings.datastore}/azureml/{job-name}/{output-name}/`. File(s) to the output directory will be written via read-write mount. If you want to specify a different mode for the output, provide an object containing the [job output specification](#job-outputs). | |
| `compute` | string | Name of the compute target to execute the job on. The value can be either a reference to an existing compute in the workspace (using the `azureml:<compute_name>` syntax) or `local` to designate local execution. <br><br> When using parallel job in pipeline, you can leave this setting empty, in which case the compute will be auto-selected by the `default_compute` of pipeline.| | `local` |
| `task` | object | **Required.** The template for defining the distributed tasks for parallel job. See [Attributes of the `task` key](#attributes-of-the-task-key).|||
|`input_data`| object | **Required.**  Define which input data will be split into mini-batches to run the parallel job. Only applicable for referencing one of the parallel job `inputs` by using the `${{ inputs.<input_name> }}` expression|||
| `mini_batch_size` | string | Define the size of each mini-batch to split the input.<br><br> If the input_data is a folder or set of files, this number defines the **file count** for each mini-batch. For example, 10, 100.<br>If the input_data is a tabular data from `mltable`, this number defines the proximate physical size for each mini-batch. For example, 100 kb, 100 mb. ||1|
