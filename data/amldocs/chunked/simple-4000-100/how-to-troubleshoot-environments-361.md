* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
* [Azure CLI workspace connections](/cli/azure/ml/connection)

### Secrets in base image registry
<!--issueDescription-->

**Potential causes:**

* You've specified credentials in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Specifying credentials in your environment definition is no longer supported. Delete credentials from your environment definition and use workspace connections instead.

*Applies to: Python SDK v1*

Set a workspace connection on your workspace

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.set_connection("connection1", "ACR", "<URL>", "Basic", "{'Username': '<username>', 'Password': '<password>'}")
```

*Applies to: Azure CLI extensions v1 & v2*

Create a workspace connection from a YAML specification file

```
az ml connection create --file connection.yml --resource-group my-resource-group --workspace-name my-workspace
```
 
**Resources**
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
* [Azure CLI workspace connections](/cli/azure/ml/connection)

### Deprecated Docker attribute
<!--issueDescription-->

**Potential causes:**

* You've specified Docker attributes in your environment definition that are now deprecated
* The following are deprecated:
	* `enabled`
	* `arguments`
	* `shared_volumes`
	* `gpu_support`
		* AzureML now automatically detects and uses NVIDIA Docker extension when available
	* `smh_size`

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Instead of specifying these attributes in the `DockerSection` of your environment definition, use [DockerConfiguration](https://aka.ms/azureml/environment/docker-configuration-class)
 
**Resources**
* See `DockerSection` [deprecated variables](https://aka.ms/azureml/environment/docker-section-class)

### Dockerfile length over limit
<!--issueDescription-->
**Potential causes:**
* Your specified Dockerfile exceeded the maximum size of 100 KB

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Shorten your Dockerfile to get it under this limit
 
**Resources**
* See [best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## *Docker build context issues*
### Missing Docker build context location
<!--issueDescription-->
**Potential causes:**
* You didn't provide the path of your build context directory in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Include a path in the `build_context` of your [DockerSection](https://aka.ms/azureml/environment/docker-section-class)
* See [DockerBuildContext Class](/python/api/azureml-core/azureml.core.environment.dockerbuildcontext)

*Applies to: Azure CLI & Python SDK v2*

Ensure that you include a path for your build context
* See [BuildContext class](https://aka.ms/azureml/environment/build-context-class)
* See this [sample](https://aka.ms/azureml/environment/create-env-build-context-v2)

**Resources**
* [Understand build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context)

### Missing Dockerfile path
<!--issueDescription-->
This issue can happen when AzureML fails to find your Dockerfile. As a default, AzureML will look for a Dockerfile named 'Dockerfile' at the root of your build context directory unless a Dockerfile path is specified.

**Potential causes:**
* Your Dockerfile isn't at the root of your build context directory and/or is named something other than 'Dockerfile,' and you didn't provide its path
