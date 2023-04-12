  - Fixed a bug in batch endpoint list-jobs output.
- `az ml component`
  - The command group is marked as GA.
  - Added an option to list only archived components.
- `az ml code`
  - This command group is removed.

## 2022-03-14

### Azure Machine Learning CLI (v2) v2.2.1

- `az ml job`
  - For all job types, flattened the `code` section of the YAML schema. Instead of `code.local_path` to specify the path to the source code directory, it is now just `code`
  - For all job types, changed the schema for defining data inputs to the job in the job YAML. Instead of specifying the data path using either the `file` or `folder` fields, use the `path` field to specify either a local path, a URI to a cloud path containing the data, or a reference to an existing registered Azure ML data asset via `path: azureml:<data_name>:<data_version>`. Also specify the `type` field to clarify whether the data source is a single file (`uri_file`) or a folder (`uri_folder`). If `type` field is omitted, it defaults to `type: uri_folder`. For more information, see the section of any of the [job YAML references](reference-yaml-job-command.md) that discuss the schema for specifying input data.
  - In the [sweep job YAML schema](reference-yaml-job-sweep.md), changed the `sampling_algorithm` field from a string to an object in order to support additional configurations for the random sampling algorithm type
  - Removed the component job YAML schema. With this release, if you want to run a command job inside a pipeline that uses a component, just specify the component to the `component` field of the command job YAML definition. 
  - For all job types, added support for referencing the latest version of a nested asset in the job YAML configuration. When referencing a registered environment or data asset to use as input in a job, you can alias by latest version rather than having to explicitly specify the version. For example: `environment: azureml:AzureML-Minimal@latest`
  - For pipeline jobs, introduced the `${{ parent }}` context for binding inputs and outputs between steps in a pipeline. For more information, see [Expression syntax for binding inputs and outputs between steps in a pipeline job](reference-yaml-core-syntax.md#binding-inputs-and-outputs-between-steps-in-a-pipeline-job).
  - Added support for downloading named outputs of job via the `--output-name` argument for the `az ml job download` command
- `az ml data`
  - Deprecated the `az ml dataset` subgroup, now using `az ml data` instead
  - There are two types of data that can now be created, either from a single file source (`type: uri_file`) or a folder (`type: uri_folder`). When creating the data asset, you can either specify the data source from a local file / folder or from a URI to a cloud path location. See the [data YAML schema](reference-yaml-data.md) for the full schema
- `az ml environment`
  - In the [environment YAML schema](reference-yaml-environment.md), renamed the `build.local_path` field to `build.path`
  - Removed the `build.context_uri` field, the URI of the uploaded build context location will be accessible via `build.path` when the environment is returned
- `az ml model`
  - In the [model YAML schema](reference-yaml-model.md), `model_uri` and `local_path` fields removed and consolidated to one `path` field that can take either a local path or a cloud path URI. `model_format` field renamed to `type`; the default type is `custom_model`, but you can specify one of the other types (`mlflow_model`, `triton_model`) to use the model in no-code deployment scenarios
  - For `az ml model create`, `--model-uri` and `--local-path` arguments removed and consolidated to one `--path` argument that can take either a local path or a cloud path URI 
  - Added the `az ml model download` command to download a model's artifact files
- `az ml online-deployment`
  - In the [online deployment YAML schema](reference-yaml-deployment-managed-online.md), flattened the `code` section of the `code_configuration` field. Instead of `code_configuration.code.local_path` to specify the path to the source code directory containing the scoring files, it is now just `code_configuration.code`
