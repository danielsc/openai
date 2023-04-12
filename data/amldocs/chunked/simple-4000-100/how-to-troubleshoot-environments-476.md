* Your Dockerfile isn't at the root of your build context directory and/or is named something other than 'Dockerfile,' and you didn't provide its path

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

In the `build_context` of your [DockerSection](https://aka.ms/azureml/environment/docker-section-class), include a `dockerfile_path`
* See [DockerBuildContext Class](/python/api/azureml-core/azureml.core.environment.dockerbuildcontext)

*Applies to: Azure CLI & Python SDK v2*

Specify a Dockerfile path
* [See BuildContext class](https://aka.ms/azureml/environment/build-context-class)
* See this [sample](https://aka.ms/azureml/environment/create-env-build-context-v2)

**Resources**
* [Understand build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context)

### Not allowed to specify attribute with Docker build context
<!--issueDescription-->
This issue can happen when you've specified properties in your environment definition that can't be included with a Docker build context.

**Potential causes:**
* You specified a Docker build context, along with at least one of the following in your environment definition:
	* Environment variables
	* Conda dependencies
	* R
	* Spark

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

If any of the above-listed properties are specified in your environment definition, remove them
* If you're using a Docker build context and want to specify conda dependencies, your conda specification should reside in your build context directory

**Resources**
* [Understand build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context)
* Python SDK v1 [Environment Class](https://aka.ms/azureml/environment/environment-class-v1)

### Location type not supported/Unknown location type
<!--issueDescription-->
**Potential causes:**
* You specified a location type for your Docker build context that isn't supported or is unknown

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

The following are accepted location types:
* Git
	* Git URLs can be provided to AzureML, but images can't yet be built using them. Use a storage account until builds have Git support
* Storage account
	* See this [storage account overview](../storage/common/storage-account-overview.md)
	* See how to [create a storage account](../storage/common/storage-account-create.md)
	
**Resources**
* See [DockerBuildContext Class](/python/api/azureml-core/azureml.core.environment.dockerbuildcontext)
* [Understand build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context)

### Invalid location
<!--issueDescription-->
**Potential causes:**
* The specified location of your Docker build context is invalid

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

For scenarios in which you're storing your Docker build context in a storage account
* The path of the build context must be specified as 

	`https://<storage-account>.blob.core.windows.net/<container>/<path>`
* Ensure that the location you provided is a valid URL
* Ensure that you've specified a container and a path
	
**Resources**
* See [DockerBuildContext Class](/python/api/azureml-core/azureml.core.environment.dockerbuildcontext)
* [Python SDK/Azure CLI v2 sample](https://aka.ms/azureml/environment/create-env-build-context-v2)
* [Understand build context](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#understand-build-context)

## *Base image issues*
### Base image is deprecated
<!--issueDescription-->
**Potential causes:**
