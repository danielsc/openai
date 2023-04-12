
# CLI (v2) core YAML syntax

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Every Azure Machine Learning entity has a schematized YAML representation. You can create a new entity from a YAML configuration file with a `.yml` or `.yaml` extension.

This article provides an overview of core syntax concepts you will encounter while configuring these YAML files.



## Referencing an Azure ML entity

Azure ML provides a reference syntax (consisting of a shorthand and longhand format) for referencing an existing Azure ML entity when configuring a YAML file. For example, you can reference an existing registered environment in your workspace to use as the environment for a job.

### Referencing an Azure ML asset

There are two options for referencing an Azure ML asset (environments, models, data, and components):
* Reference an explicit version of an asset:
  * Shorthand syntax: `azureml:<asset_name>:<asset_version>`
  * Longhand syntax, which includes the Azure Resource Manager (ARM) resource ID of the asset:
  ```
  azureml:/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>/environments/<environment-name>/versions/<environment-version>
  ```
* Reference the latest version of an asset:

  In some scenarios you may want to reference the latest version of an asset without having to explicitly look up and specify the actual version string itself. The latest    version is defined as the latest (also known as most recently) created version of an asset under a given name. 

  You can reference the latest version using the following syntax: `azureml:<asset_name>@latest`. Azure ML will resolve the reference to an explicit asset version in the workspace.

### Reference an Azure ML resource

To reference an Azure ML resource (such as compute), you can use either of the following syntaxes:
* Shorthand syntax: `azureml:<resource_name>`
* Longhand syntax, which includes the ARM resource ID of the resource:
```
azureml:/subscriptions/<subscription-id>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace-name>/computes/<compute-name>
```

## Azure ML data reference URI

Azure ML offers a convenience data reference URI format to point to data in an Azure storage service. This can be used for scenarios where you need to specify a cloud storage location in your YAML file, such as creating an Azure ML model from file(s) in storage, or pointing to data to pass as input to a job.

To use this data URI format, the storage service you want to reference must first be registered as a datastore in your workspace. Azure ML will handle the data access using the credentials you provided during datastore creation.

The format consists of a datastore in the current workspace and the path on the datastore to the file or folder you want to point to:

```
azureml://datastores/<datastore-name>/paths/<path-on-datastore>/
```

For example:

* `azureml://datastores/workspaceblobstore/paths/example-data/`
* `azureml://datastores/workspaceblobstore/paths/example-data/iris.csv`

In addition to the Azure ML data reference URI, Azure ML also supports the following direct storage URI protocols: `https`, `wasbs`, `abfss`, and `adl`, as well as public `http` and `https` URIs.

## Expression syntax for configuring Azure ML jobs and components

v2 job and component YAML files allow for the use of expressions to bind to contexts for different scenarios. The essential use case is using an expression for a value that might not be known at the time of authoring the configuration, but must be resolved at runtime.

Use the following syntax to tell Azure ML to evaluate an expression rather than treat it as a string:

`${{ <expression> }}`

The supported scenarios are covered below.

### Parameterizing the `command` with the `inputs` and `outputs` contexts of a job

You can specify literal values, URI paths, and registered Azure ML data assets as inputs to a job. The `command` can then be parameterized with references to those input(s) using the `${{inputs.<input_name>}}` syntax. References to literal inputs will get resolved to the literal value at runtime, while references to data inputs will get resolved to the download path or mount path (depending on the `mode` specified).
