
# What is Azure Machine Learning CLI & Python SDK v2?

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

Azure Machine Learning CLI v2 and Azure Machine Learning Python SDK v2 introduce a consistency of features and terminology across the interfaces.  In order to create this consistency, the syntax of commands differs, in some cases significantly, from the first versions (v1).

## Azure Machine Learning CLI v2

The Azure Machine Learning CLI v2 (CLI v2) is the latest extension for the [Azure CLI](/cli/azure/what-is-azure-cli). The CLI v2 provides commands in the format *az ml __\<noun\> \<verb\> \<options\>__* to create and maintain Azure ML assets and workflows. The assets or workflows themselves are defined using a YAML file. The YAML file defines the configuration of the asset or workflow – what is it, where should it run, and so on.

A few examples of CLI v2 commands:

* `az ml job create --file my_job_definition.yaml`
* `az ml environment update --name my-env --file my_updated_env_definition.yaml`
* `az ml model list`
* `az ml compute show --name my_compute`

### Use cases for CLI v2

The CLI v2 is useful in the following scenarios:

* On board to Azure ML without the need to learn a specific programming language

    The YAML file defines the configuration of the asset or workflow – what is it, where should it run, and so on. Any custom logic/IP used, say data preparation, model training, model scoring can remain in script files, which are referred to in the YAML, but not part of the YAML itself. Azure ML supports script files in python, R, Java, Julia or C#. All you need to learn is YAML format and command lines to use Azure ML. You can stick with script files of your choice.

* Ease of deployment and automation

    The use of command-line for execution makes deployment and automation simpler, since workflows can be invoked from any offering/platform, which allows users to call the command line.

* Managed inference deployments

    Azure ML offers [endpoints](concept-endpoints.md) to streamline model deployments for both real-time and batch inference deployments. This functionality is available only via CLI v2 and SDK v2.

* Reusable components in pipelines

    Azure ML introduces [components](concept-component.md) for managing and reusing common logic across pipelines. This functionality is available only via CLI v2 and SDK v2.


## Azure Machine Learning Python SDK v2

Azure ML Python SDK v2 is an updated Python SDK package, which allows users to:

* Submit training jobs
* Manage data, models, environments
* Perform managed inferencing (real time and batch)
* Stitch together multiple tasks and production workflows using Azure ML pipelines

The SDK v2 is on par with CLI v2 functionality and is consistent in how assets (nouns) and actions (verbs) are used between SDK and CLI.  For example, to list an asset, the `list` action can be used in both CLI and SDK. The same `list` action can be used to list a compute, model, environment, and so on.

### Use cases for SDK v2

The SDK v2 is useful in the following scenarios:

* Use Python functions to build a single step or a complex workflow

    SDK v2 allows you to build a single command or a chain of commands like Python functions - the command has a name, parameters, expects input, and returns output.

* Move from simple to complex concepts incrementally

    SDK v2 allows you to: 
    * Construct a single command.
    * Add a hyperparameter sweep on top of that command, 
    * Add the command with various others into a pipeline one after the other. 
    
    This construction is useful, given the iterative nature of machine learning.

* Reusable components in pipelines

    Azure ML introduces [components](concept-component.md) for managing and reusing common logic across pipelines. This functionality is available only via CLI v2 and SDK v2.

* Managed inferencing

    Azure ML offers [endpoints](concept-endpoints.md) to streamline model deployments for both real-time and batch inference deployments. This functionality is available only via CLI v2 and SDK v2.
