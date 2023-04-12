  - In the [online deployment YAML schema](reference-yaml-deployment-managed-online.md), flattened the `code` section of the `code_configuration` field. Instead of `code_configuration.code.local_path` to specify the path to the source code directory containing the scoring files, it is now just `code_configuration.code`
  - Added an `environment_variables` field to the online deployment YAML schema to support configuring environment variables for an online deployment
- `az ml batch-deployment`
  - In the [batch deployment YAML schema](reference-yaml-deployment-batch.md), flattened the `code` section of the `code_configuration` field. Instead of `code_configuration.code.local_path` to specify the path to the source code directory containing the scoring files, it is now just `code_configuration.code`
- `az ml component`
  - Flattened the `code` section of the [command component YAML schema](reference-yaml-component-command.md). Instead of `code.local_path` to specify the path to the source code directory, it is now just `code`
  -  Added support for referencing the latest version of a registered environment to use in the component YAML configuration. When referencing a registered environment, you can alias by latest version rather than having to explicitly specify the version. For example: `environment: azureml:AzureML-Minimal@latest`
  -  Renamed the component input and output type value from `path` to `uri_folder` for the `type` field when defining a component input or output
- Removed the `delete` commands for assets (model, component, data, environment). The existing delete functionality is only a soft delete, so the `delete` commands will be reintroduced in a later release once hard delete is supported
- Added support for archiving and restoring assets (model, component, data, environment) and jobs, e.g. `az ml model archive` and `az ml model restore`. You can now archive assets and jobs, which will hide the archived entity from list queries (e.g. `az ml model list`).

## 2021-10-04

### Azure Machine Learning CLI (v2) v2.0.2

- `az ml workspace`
  - Updated [workspace YAML schema](reference-yaml-workspace.md)
- `az ml compute`
  - Updated YAML schemas for [AmlCompute](reference-yaml-compute-aml.md) and [Compute Instance](reference-yaml-compute-instance.md)
  - Removed support for legacy AKS attach via `az ml compute attach`. Azure Arc-enabled Kubernetes attach will be supported in the next release
- `az ml datastore`
  - Updated YAML schemas for [Azure blob](reference-yaml-datastore-blob.md), [Azure file](reference-yaml-datastore-files.md), [Azure Data Lake Gen1](reference-yaml-datastore-data-lake-gen1.md), and [Azure Data Lake Gen2](reference-yaml-datastore-data-lake-gen2.md) datastores
  - Added support for creating Azure Data Lake Storage Gen1 and Gen2 datastores
- `az ml job`
  - Updated YAML schemas for [command job](reference-yaml-job-command.md) and [sweep job](reference-yaml-job-sweep.md)
  - Added support for running pipeline jobs ([pipeline job YAML schema](reference-yaml-job-pipeline.md))
  - Added support for job input literals and input data URIs for all job types
  - Added support for job outputs for all job types
  - Changed the expression syntax from `{ <expression> }` to `${{ <expression> }}`. For more information, see [Expression syntax for configuring Azure ML jobs](reference-yaml-core-syntax.md#expression-syntax-for-configuring-azure-ml-jobs-and-components)
- `az ml environment`
  - Updated [environment YAML schema](reference-yaml-environment.md)
  - Added support for creating environments from Docker build context
- `az ml model`
  - Updated [model YAML schema](reference-yaml-model.md)
  - Added new `model_format` property to Model for no-code deployment scenarios
- `az ml dataset`
  - Renamed `az ml data` subgroup to `az ml dataset`
  - Updated dataset YAML schema
- `az ml component`
  - Added the `az ml component` commands for managing Azure ML components
  - Added support for command components ([command component YAML schema](reference-yaml-component-command.md))
