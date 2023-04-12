
*Applies to: Azure CLI extensions v1 & v2*

Create a workspace connection from a YAML specification file

```
az ml connection create --file connection.yml --resource-group my-resource-group --workspace-name my-workspace
```

**Resources**
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
* [Azure CLI workspace connections](/cli/azure/ml/connection)

### Forbidden blob
<!--issueDescription-->
This issue can happen when an attempt to access a blob in a storage account is rejected.

**Potential causes:**
* The authorization method you're using to access the storage account is invalid
* You're attempting to authorize via shared access signature (SAS), but the SAS token is expired or invalid

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Read the following to understand [how to authorize access to blob data in the Azure portal](../storage/blobs/authorize-data-operations-portal.md)

Read the following to understand [how to authorize access to data in Azure storage](../storage/common/authorize-data-access.md)

Read the following if you're interested in [using SAS to access Azure storage resources](../storage/common/storage-sas-overview.md)

### Horovod build
<!--issueDescription-->
This issue can happen when the conda environment fails to be created or updated because horovod failed to build.

**Potential causes:**
* Horovod installation requires other modules that you haven't installed
* Horovod installation requires certain libraries that you haven't included

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Many issues could cause a horovod failure, and there's a comprehensive list of them in horovod's documentation
* Review the [horovod troubleshooting guide](https://horovod.readthedocs.io/en/stable/troubleshooting_include.html#) 
* Review your Build log to see if there's an error message that surfaced when horovod failed to build
* It's possible that the problem you're encountering is detailed in the horovod troubleshooting guide, along with a solution

**Resources**
* [horovod installation](https://aka.ms/azureml/environment/install-horovod)

### Conda command not found
<!--issueDescription-->
This issue can happen when the conda command isn't recognized during conda environment creation or update.

**Potential causes:**
* conda isn't installed in the base image you're using
* conda isn't installed via your Dockerfile before you try to execute the conda command
* conda isn't included in or wasn't added to your path

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Ensure that you have a conda installation step in your Dockerfile before trying to execute any conda commands
* Review this [list of conda installers](https://docs.conda.io/en/latest/miniconda.html) to determine what you need for your scenario

If you've tried installing conda and are experiencing this issue, ensure that you've added conda to your path
* Review this [example](https://stackoverflow.com/questions/58269375/how-to-install-packages-with-miniconda-in-dockerfile) for guidance
* Review how to set [environment variables in a Dockerfile](https://docs.docker.com/engine/reference/builder/#env)

**Resources**
* All available conda distributions are found in the [conda repository](https://repo.anaconda.com/miniconda/)

### Incompatible Python version
<!--issueDescription-->
