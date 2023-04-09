---
title: Troubleshoot environment images
titleSuffix: Azure Machine Learning
description: Learn how to troubleshoot issues with environment image builds and package installations.
services: machine-learning
ms.service: machine-learning
ms.subservice: mlops
author: edebar01
ms.author:  ericadebarge
ms.reviewer: larryfr
ms.date: 03/01/2022
ms.topic: troubleshooting
ms.custom: devx-track-python, event-tier1-build-2022, ignite-2022
---

# Troubleshooting environment image builds using troubleshooting log error messages

In this article, learn how to troubleshoot common problems you may encounter with environment image builds.

## Azure Machine Learning environments

Azure Machine Learning environments are an encapsulation of the environment where your machine learning training happens.
They specify the base docker image, Python packages, and software settings around your training and scoring scripts.
Environments are managed and versioned assets within your Machine Learning workspace that enable reproducible, auditable, and portable machine learning workflows across various compute targets.

### Types of environments

Environments can broadly be divided into three categories: curated, user-managed, and system-managed.

Curated environments are pre-created environments that are managed by Azure Machine Learning (AzureML) and are available by default in every workspace.

Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks.
These pre-created environments also allow for faster deployment time.

In user-managed environments, you're responsible for setting up your environment and installing every package that your training script needs on the compute target.
Also be sure to include any dependencies needed for model deployment.
These types of environments are represented by two subtypes. For the first type, BYOC (bring your own container), you bring an existing Docker image to AzureML. For the second type, Docker build context based environments, AzureML materializes the image from the context that you provide.

System-managed environments are used when you want conda to manage the Python environment for you.
A new isolated conda environment is materialized from your conda specification on top of a base Docker image. By default, common properties are added to the derived image.
Note that environment isolation implies that Python dependencies installed in the base image won't be available in the derived image.

### Create and manage environments

You can create and manage environments from clients like AzureML Python SDK, AzureML CLI, AzureML Studio UI, VS code extension. 

"Anonymous" environments are automatically registered in your workspace when you submit an experiment without registering or referencing an already existing environment.
They won't be listed but may be retrieved by version or label.

AzureML builds environment definitions into Docker images.
It also caches the environments in the Azure Container Registry associated with your AzureML Workspace so they can be reused in subsequent training jobs and service endpoint deployments.
Multiple environments with the same definition may result the same image, so the cached image will be reused.
Running a training script remotely requires the creation of a Docker image.

### Reproducibility and vulnerabilities

#### *Vulnerabilities*

Vulnerabilities can be addressed by upgrading to a newer version of a dependency or migrating to a different dependency that satisfies security
requirements. Mitigating vulnerabilities is time consuming and costly since it can require refactoring of code and infrastructure. With the prevalence
of open source software and the use of complicated nested dependencies, it's important to manage and keep track of vulnerabilities.

There are some ways to decrease the impact of vulnerabilities:

- Reduce your number of dependencies - use the minimal set of the dependencies for each scenario.
- Compartmentalize your environment so issues can be scoped and fixed in one place.
- Understand flagged vulnerabilities and their relevance to your scenario.

#### *Vulnerabilities vs Reproducibility*

Reproducibility is one of the foundations of software development. While developing production code, a repeated operation must guarantee the same
result. Mitigating vulnerabilities can disrupt reproducibility by changing dependencies.

AzureML's primary focus is to guarantee reproducibility. Environments can broadly be divided into three categories: curated,
user-managed, and system-managed.

**Curated environments** are pre-created environments that are managed by Azure Machine Learning (AzureML) and are available by default in every AzureML workspace provisioned.

Intended to be used as is, they contain collections of Python packages and settings to help you get started with various machine learning frameworks.
These pre-created environments also allow for faster deployment time.

In **user-managed environments**, you're responsible for setting up your environment and installing every package that your training script needs on the
compute target and for model deployment. These types of environments are represented by two subtypes:

- BYOC (bring your own container): the user provides a Docker image to AzureML
- Docker build context: AzureML materializes the image from the user provided content

Once you install more dependencies on top of a Microsoft-provided image, or bring your own base image, vulnerability
management becomes your responsibility.

You use **system-managed environments** when you want conda to manage the Python environment for you. A new isolated conda environment is materialized
from your conda specification on top of a base Docker image. While Azure Machine Learning patches base images with each release, whether you use the
latest image may be a tradeoff between reproducibility and vulnerability management. So, it's your responsibility to choose the environment version used
for your jobs or model deployments while using system-managed environments.

Associated to your Azure Machine Learning workspace is an Azure Container Registry instance that's used as a cache for container images. Any image
materialized is pushed to the container registry and used if experimentation or deployment is triggered for the corresponding environment. Azure
Machine Learning doesn't delete images from your container registry, and it's your responsibility to evaluate which images you need to maintain over time. You
can monitor and maintain environment hygiene with [Microsoft Defender for Container Registry](../defender-for-cloud/defender-for-containers-vulnerability-assessment-azure.md)
to help scan images for vulnerabilities. To
automate this process based on triggers from Microsoft Defender, see [Automate responses to Microsoft Defender for Cloud triggers](../defender-for-cloud/workflow-automation.md).

## **Environment definition problems**

## *Environment name issues*
### Curated prefix not allowed
<!--issueDescription-->
This issue can happen when the name of your custom environment uses terms reserved only for curated environments. *Curated* environments are environments that Microsoft maintains. *Custom* environments are environments that you create and maintain.
 
**Potential causes:**
* Your environment name starts with *Microsoft* or *AzureML*
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

 Update your environment name to exclude the reserved prefix you're currently using
 
**Resources**
* [Create and manage reusable environments](https://aka.ms/azureml/environment/create-and-manage-reusable-environments)

### Environment name is too long
<!--issueDescription-->
 
**Potential causes:**
* Your environment name is longer than 255 characters
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

 Update your environment name to be 255 characters or less

## *Docker issues*

*Applies to: Azure CLI & Python SDK v1*

To create a new environment, you must use one of the following approaches (see [DockerSection](https://aka.ms/azureml/environment/environment-docker-section)):
* Base image
    * Provide base image name, repository from which to pull it, and credentials if needed
    * Provide a conda specification
* Base Dockerfile 
    * Provide a Dockerfile
    * Provide a conda specification
* Docker build context
    * Provide the location of the build context (URL)
    * The build context must contain at least a Dockerfile, but may contain other files as well

*Applies to: Azure CLI & Python SDK v2*

To create a new environment, you must use one of the following approaches:
* Docker image
    * Provide the image URI of the image hosted in a registry such as Docker Hub or Azure Container Registry
    * [Sample here](https://aka.ms/azureml/environment/create-env-docker-image-v2)
* Docker build context
    * Specify the directory that will serve as the build context
    * The directory should contain a Dockerfile and any other files needed to build the image
    * [Sample here](https://aka.ms/azureml/environment/create-env-build-context-v2)
* Conda specification 
    * You must specify a base Docker image for the environment; the conda environment will be built on top of the Docker image provided
    * Provide the relative path to the conda file
    * [Sample here](https://aka.ms/azureml/environment/create-env-conda-spec-v2)

### Missing Docker definition
*Applies to: Python SDK v1*
<!--issueDescription-->
This issue can happen when your environment definition is missing a `DockerSection.` This section configures settings related to the final Docker image built from your environment specification.
 
**Potential causes:**
* The `DockerSection` of your environment definition isn't defined (null)
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

 Add a `DockerSection` to your environment definition, specifying either a base image, base dockerfile, or docker build context.

```python
from azureml.core import Environment
myenv = Environment(name="myenv")
# Specify docker steps as a string.
dockerfile = r'''
FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
RUN echo "Hello from custom container!"
'''

myenv.docker.base_dockerfile = dockerfile
```
 
**Resources**
* [DockerSection](https://aka.ms/azureml/environment/environment-docker-section)

### Too many Docker options
<!--issueDescription-->
 
**Potential causes:**

*Applies to: Python SDK v1*

You have more than one of these Docker options specified in your environment definition
* `base_image`
* `base_dockerfile`
* `build_context`
* See [DockerSection](https://aka.ms/azureml/environment/docker-section-class)

*Applies to: Azure CLI & Python SDK v2*

You have more than one of these Docker options specified in your environment definition
* `image`
* `build`
* See [azure.ai.ml.entities.Environment](https://aka.ms/azureml/environment/environment-class-v2)
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

Choose which Docker option you'd like to use to build your environment. Then set all other specified options to None.

*Applies to: Python SDK v1*

```python
from azureml.core import Environment
myenv = Environment(name="myEnv")
dockerfile = r'''
FROM mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
RUN echo "Hello from custom container!"
'''
myenv.docker.base_dockerfile = dockerfile
myenv.docker.base_image = "pytorch/pytorch:latest"

# Having both base dockerfile and base image set will cause failure. Delete the one you won't use.
myenv.docker.base_image = None
```

### Missing Docker option
<!--issueDescription-->
 
**Potential causes:**

*Applies to: Python SDK v1*

You didn't specify one of the following options in your environment definition
* `base_image`
* `base_dockerfile`
* `build_context`
* See [DockerSection](https://aka.ms/azureml/environment/docker-section-class)

*Applies to: Azure CLI & Python SDK v2*

You didn't specify one of the following options in your environment definition
* `image`
* `build`
* See [azure.ai.ml.entities.Environment](https://aka.ms/azureml/environment/environment-class-v2)
 
**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->
 
**Troubleshooting steps**

Choose which Docker option you'd like to use to build your environment, then populate that option in your environment definition.

*Applies to: Python SDK v1*

```python
from azureml.core import Environment
myenv = Environment(name="myEnv")
myenv.docker.base_image = "pytorch/pytorch:latest"
```

*Applies to: Python SDK v2*

```python
env_docker_image = Environment(
    image="pytorch/pytorch:latest",
    name="docker-image-example",
    description="Environment created from a Docker image.",
)
ml_client.environments.create_or_update(env_docker_image)
```

**Resources**
* [Create and manage reusable environments v2](https://aka.ms/azureml/environment/create-and-manage-reusable-environments)
* [Environment class v1](https://aka.ms/azureml/environment/environment-class-v1)

### Container registry credentials missing either username or password
<!--issueDescription-->

**Potential causes:**

* You've specified either a username or a password for your container registry in your environment definition, but not both

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Add the missing username or password to your environment definition to fix the issue

```python
myEnv.docker.base_image_registry.username = "username"
```

Alternatively, provide authentication via [workspace connections](https://aka.ms/azureml/environment/set-connection-v1)

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

> [!NOTE]
> * Providing credentials in your environment definition is no longer supported. Use workspace connections instead.
 
**Resources**
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
* [Python SDK v2 workspace connections](/python/api/azure-ai-ml/azure.ai.ml.entities.workspaceconnection)
* [Azure CLI workspace connections](/cli/azure/ml/connection)

### Multiple credentials for base image registry
<!--issueDescription-->

**Potential causes:**

* You've specified more than one set of credentials for your base image registry

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

If you're using workspace connections, view the connections you have set, and delete whichever one(s) you don't want to use

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.list_connections()
ws.delete_connection("myConnection2")
```

If you've specified credentials in your environment definition, choose one set of credentials to use, and set all others to null

```python
myEnv.docker.base_image_registry.registry_identity = None
```

> [!NOTE]
> * Providing credentials in your environment definition is no longer supported. Use workspace connections instead.
 
**Resources**
* [Delete a workspace connection v1](https://aka.ms/azureml/environment/delete-connection-v1)
* [Python SDK v1 workspace connections](https://aka.ms/azureml/environment/set-connection-v1)
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
* You used a deprecated base image
	* AzureML can't provide troubleshooting support for failed builds with deprecated images
	* These images aren't updated or maintained, so they're at risk of vulnerabilities

The following base images are deprecated:
* `azureml/base`
* `azureml/base-gpu`
* `azureml/base-lite`
* `azureml/intelmpi2018.3-cuda10.0-cudnn7-ubuntu16.04`
* `azureml/intelmpi2018.3-cuda9.0-cudnn7-ubuntu16.04`
* `azureml/intelmpi2018.3-ubuntu16.04`
* `azureml/o16n-base/python-slim`
* `azureml/openmpi3.1.2-cuda10.0-cudnn7-ubuntu16.04`
* `azureml/openmpi3.1.2-ubuntu16.04`
* `azureml/openmpi3.1.2-cuda10.0-cudnn7-ubuntu18.04`
* `azureml/openmpi3.1.2-cuda10.1-cudnn7-ubuntu18.04`
* `azureml/openmpi3.1.2-cuda10.2-cudnn7-ubuntu18.04`
* `azureml/openmpi3.1.2-cuda10.2-cudnn8-ubuntu18.04`
* `azureml/openmpi3.1.2-ubuntu18.04`
* `azureml/openmpi4.1.0-cuda11.0.3-cudnn8-ubuntu18.04`
* `azureml/openmpi4.1.0-cuda11.1-cudnn8-ubuntu18.04`

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Upgrade your base image to a latest version of supported images
* See available [base images](https://github.com/Azure/AzureML-Containers/tree/master/base)

### No tag or digest
<!--issueDescription-->
**Potential causes:**
* You didn't include a version tag or a digest on your specified base image
* Without one of these, the environment isn't reproducible

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Include at least one of the following on your specified base image
* Version tag
* Digest
* See [image with immutable identifier](https://aka.ms/azureml/environment/pull-image-by-digest)

## *Environment variable issues*
### Misplaced runtime variables
<!--issueDescription-->
**Potential causes:**
* You specified runtime variables in your environment definition 

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Use the `environment_variables` attribute on the [RunConfiguration object](https://aka.ms/azureml/environment/environment-variables-on-run-config) instead

## *Python issues*
### Python section missing
<!--issueDescription-->
**Potential causes:**
* Your environment definition doesn't have a Python section

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Populate the Python section of your environment definition
* See [PythonSection class](https://aka.ms/azureml/environment/environment-python-section)

### Python version missing
<!--issueDescription-->
**Potential causes:**
* You haven't specified a Python version in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Add Python as a conda package and specify the version

```python
from azureml.core.environment import CondaDependencies

myenv = Environment(name="myenv")
conda_dep = CondaDependencies()
conda_dep.add_conda_package("python==3.8")
env.python.conda_dependencies = conda_dep
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, include Python as a dependency

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip:
      - azureml-defaults
channels:
  - anaconda
```

**Resources**
* [Add conda package v1](https://aka.ms/azureml/environment/add-conda-package-v1)

### Multiple Python versions
<!--issueDescription-->
**Potential causes:**
* You've specified more than one Python version in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Choose which Python version you want to use, and remove all other versions 

```python
myenv.python.conda_dependencies.remove_conda_package("python=3.6")
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, include only one Python version as a dependency

**Resources**
* [CondaDependencies Class v1](https://aka.ms/azureml/environment/conda-dependencies-class)

### Python version not supported
<!--issueDescription-->
**Potential causes:**
* You've specified a Python version that is at or near its end-of-life and is no longer supported

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Specify a [python version](https://aka.ms/azureml/environment/python-versions) that hasn't reached and isn't nearing its [end-of-life](https://aka.ms/azureml/environment/python-end-of-life)

### Python version not recommended
<!--issueDescription-->
**Potential causes:**
* You've specified a Python version that is at or near its end-of-life

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Specify a [python version](https://aka.ms/azureml/environment/python-versions) that hasn't reached and isn't nearing its [end-of-life](https://aka.ms/azureml/environment/python-end-of-life)

### Failed to validate Python version
<!--issueDescription-->
**Potential causes:**
* The provided Python version was formatted improperly or specified with incorrect syntax

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Use correct syntax to specify a Python version using the SDK

```python
myenv.python.conda_dependencies.add_conda_package("python=3.8")
```

*Applies to: all scenarios*

Use correct syntax to specify a Python version in a conda YAML

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip:
      - azureml-defaults
channels:
  - anaconda
```

**Resources**
* See [conda package pinning](https://aka.ms/azureml/environment/how-to-pin-conda-packages)

## *Conda issues*
### Missing conda dependencies
<!--issueDescription-->
**Potential causes:**
* You haven't provided a conda specification in your environment definition, and `user_managed_dependencies` is set to `False` (the default)

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

If you don't want AzureML to create a Python environment for you based on `conda_dependencies,` set `user_managed_dependencies` to `True`

```python
env.python.user_managed_dependencies = True
```
* You're responsible for ensuring that all necessary packages are available in the Python environment in which you choose to run the script

If you want AzureML to create a Python environment for you based on a conda specification, `conda_dependencies` needs to be populated in your environment definition 

```python
from azureml.core.environment import CondaDependencies

env = Environment(name="env")
conda_dep = CondaDependencies()
conda_dep.add_conda_package("python==3.8")
env.python.conda_dependencies = conda_dep
```

*Applies to: Azure CLI & Python SDK v2*

You must specify a base Docker image for the environment, and the conda environment will be built on top of that image
* Provide the relative path to the conda file
* See how to [create an environment from a conda specification](https://aka.ms/azureml/environment/create-env-conda-spec-v2)

**Resources**
* See [how to create a conda file manually](https://aka.ms/azureml/environment/how-to-create-conda-file)
* See [CondaDependencies class](https://aka.ms/azureml/environment/conda-dependencies-class)
* See [how to set a conda specification on the environment definition](https://aka.ms/azureml/environment/set-conda-spec-on-environment-definition)

### Invalid conda dependencies
<!--issueDescription-->
**Potential causes:**
* The conda dependencies specified in your environment definition aren't formatted correctly

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Ensure that `conda_dependencies` is a JSONified version of the conda dependencies YAML structure

```json
"condaDependencies": {
    "channels": [
	"anaconda",
        "conda-forge"
    ],
    "dependencies": [
        "python=3.8",
        {
            "pip": [
                "azureml-defaults"
            ]
        }
    ],
    "name": "project_environment"
}
```

Conda dependencies can also be specified using the `add_conda_package` method

```python
from azureml.core.environment import CondaDependencies

env = Environment(name="env")
conda_dep = CondaDependencies()
conda_dep.add_conda_package("python==3.8")
env.python.conda_dependencies = conda_dep
```

*Applies to: Azure CLI & Python SDK v2*

You must specify a base Docker image for the environment, and the conda environment will be built on top of that image
* Provide the relative path to the conda file
* See how to [create an environment from a conda specification](https://aka.ms/azureml/environment/create-env-conda-spec-v2)

**Resources**
* See [more extensive examples](https://github.com/Azure/MachineLearningNotebooks/blob/9b1e130d18d3c61d41dc225488a4575904897c85/how-to-use-azureml/training/using-environments/using-environments.ipynb)
* See [how to create a conda file manually](https://aka.ms/azureml/environment/how-to-create-conda-file)
* See [CondaDependencies class](https://aka.ms/azureml/environment/conda-dependencies-class)
* See [how to set a conda specification on the environment definition](https://aka.ms/azureml/environment/set-conda-spec-on-environment-definition)

### Missing conda channels
<!--issueDescription-->
**Potential causes:**
* You haven't specified conda channels in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

For reproducibility of your environment, specify channels from which to pull dependencies. If no conda channel is specified, conda will use defaults that might change.

*Applies to: Python SDK v1*

Add a conda channel using the Python SDK

```python
from azureml.core.environment import CondaDependencies

env = Environment(name="env")
conda_dep = CondaDependencies()
conda_dep.add_channel("conda-forge")
env.python.conda_dependencies = conda_dep
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, include the conda channel(s) you'd like to use

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip:
      - azureml-defaults
channels:
  - anaconda
  - conda-forge
```

**Resources**
* See [how to set a conda specification on the environment definition v1](https://aka.ms/azureml/environment/set-conda-spec-on-environment-definition)
* See [CondaDependencies class](https://aka.ms/azureml/environment/conda-dependencies-class)
* See how to [create an environment from a conda specification v2](https://aka.ms/azureml/environment/create-env-conda-spec-v2)
* See [how to create a conda file manually](https://aka.ms/azureml/environment/how-to-create-conda-file)

### Base conda environment not recommended
<!--issueDescription-->
**Potential causes:**
* You specified a base conda environment in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Partial environment updates can lead to dependency conflicts and/or unexpected runtime errors, so the use of base conda environments isn't recommended. 

*Applies to: Python SDK v1*

Remove your base conda environment, and specify all packages needed for your environment in the `conda_dependencies` section of your environment definition

```python
from azureml.core.environment import CondaDependencies

env = Environment(name="env")
env.python.base_conda_environment = None
conda_dep = CondaDependencies()
conda_dep.add_conda_package("python==3.8")
env.python.conda_dependencies = conda_dep
```

*Applies to: Azure CLI & Python SDK v2*

Define an environment using a standard conda YAML configuration file
* See [how to create an environment from a conda specification](https://aka.ms/azureml/environment/create-env-conda-spec-v2)

**Resources**
* See [how to set a conda specification on the environment definition v1](https://aka.ms/azureml/environment/set-conda-spec-on-environment-definition)
* See [CondaDependencies class](https://aka.ms/azureml/environment/conda-dependencies-class)
* See [how to create a conda file manually](https://aka.ms/azureml/environment/how-to-create-conda-file)

### Unpinned dependencies
<!--issueDescription-->
**Potential causes:**
* You didn't specify versions for certain packages in your conda specification

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

If a dependency version isn't specified, the conda package resolver may choose a different version of the package on subsequent builds of the same environment. This breaks reproducibility of the environment and can lead to unexpected errors.

*Applies to: Python SDK v1*

Include version numbers when adding packages to your conda specification

```python
from azureml.core.environment import CondaDependencies

conda_dep = CondaDependencies()
conda_dep.add_conda_package("numpy==1.24.1")
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, specify versions for your dependencies

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip:
      - numpy=1.24.1
channels:
  - anaconda
  - conda-forge
```

**Resources**
* See [conda package pinning](https://aka.ms/azureml/environment/how-to-pin-conda-packages)

## *Pip issues*
### Pip not specified
<!--issueDescription-->
**Potential causes:**
* You didn't specify pip as a dependency in your conda specification

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

For reproducibility, pip should be specified as a dependency in your conda specification, and it should be pinned.

*Applies to: Python SDK v1*

Specify pip as a dependency, along with its version

```python
env.python.conda_dependencies.add_conda_package("pip==22.3.1")
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, specify pip as a dependency

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip=22.3.1
  - pip:
      - numpy=1.24.1
channels:
  - anaconda
  - conda-forge
```

**Resources**
* See [conda package pinning](https://aka.ms/azureml/environment/how-to-pin-conda-packages)

### Pip not pinned
<!--issueDescription-->
**Potential causes:**
* You didn't specify a version for pip in your conda specification

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

If a pip version isn't specified, a different version may be used on subsequent builds of the same environment. This can cause reproducibility issues and other unexpected errors if different versions of pip resolve your packages differently.

*Applies to: Python SDK v1*

Specify a pip version in your conda dependencies

```python
env.python.conda_dependencies.add_conda_package("pip==22.3.1")
```

*Applies to: all scenarios*

If you're using a YAML for your conda specification, specify a version for pip

```yaml
name: project_environment
dependencies:
  - python=3.8
  - pip=22.3.1
  - pip:
      - numpy=1.24.1
channels:
  - anaconda
  - conda-forge
```

**Resources**
* See [conda package pinning](https://aka.ms/azureml/environment/how-to-pin-conda-packages)

## *Miscellaneous environment issues*
### R section is deprecated
<!--issueDescription-->
**Potential causes:**
* You specified an R section in your environment definition

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

The AzureML SDK for R was deprecated at the end of 2021 to make way for an improved R training and deployment experience using the Azure CLI v2

*Applies to: Python SDK v1*

Remove the R section from your environment definition

```python
env.r = None
```

*Applies to: all scenarios*

See the [samples repository](https://aka.ms/azureml/environment/train-r-models-cli-v2) to get started training R models using the Azure CLI v2

### No definition exists for environment
<!--issueDescription-->
**Potential causes:**
* You specified an environment that doesn't exist or hasn't been registered
* There was a misspelling or syntactical error in the way you specified your environment name or environment version

**Affected areas (symptoms):**
* Failure in registering your environment
<!--/issueDescription-->

**Troubleshooting steps**

Ensure that you are specifying your environment name correctly, along with the correct version
* `path-to-resource:version-number`

The 'latest' version of your environment is specified in a slightly different way
* `path-to-resource@latest`

## **Image build problems**

## *ACR issues*
### ACR unreachable
<!--issueDescription-->
This issue can happen by failing to access a workspace's associated Azure Container Registry (ACR) resource.

**Potential causes:**
* Workspace's ACR is behind a virtual network (VNet) (private endpoint or service endpoint), and no compute cluster is used to build images.
* Workspace's ACR is behind a virtual network (private endpoint or service endpoint), and the compute cluster used for building images have no access to the workspace's ACR.

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
* Pipeline job failures.
* Model deployment failures.
<!--/issueDescription-->

**Troubleshooting steps**

*Applies to: Python SDK v1*

Update the workspace image build compute property using SDK:

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.update(image_build_compute = 'mycomputecluster')
```

*Applies to: Azure CLI extensions v1 & v2*

Update the workspace image build compute property using Azure CLI:

```
az ml workspace update --name myworkspace --resource-group myresourcegroup --image-build-compute mycomputecluster
```

> [!NOTE]
> * Only Azure Machine Learning compute clusters are supported. Compute, Azure Kubernetes Service (AKS), or other instance types are not supported for image build compute.
> * Make sure the compute cluster's VNet that's used for the image build compute has access to the workspace's ACR.
> * Make sure the compute cluster is CPU based.

**Resources**
* [Enable Azure Container Registry (ACR)](https://aka.ms/azureml/environment/acr-private-endpoint)
* [How To Use Environments](https://aka.ms/azureml/environment/how-to-use-environments)

## *Docker pull issues*
### Failed to pull Docker image
<!--issueDescription-->
This issue can happen when a Docker image pull fails during an image build.

**Potential causes:**
* The path name to the container registry is incorrect
* A container registry behind a virtual network is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* The image you're trying to reference doesn't exist in the container registry you specified 
* You haven't provided credentials for a private registry you're trying to pull the image from, or the provided credentials are incorrect

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

If you suspect that the path name to your container registry is incorrect
* For a registry `my-registry.io` and image `test/image` with tag `3.2`, a valid image path would be `my-registry.io/test/image:3.2`
* See [registry path documentation](https://aka.ms/azureml/environment/docker-registries)

If your container registry is behind a virtual network or is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* Configure the container registry by using the service endpoint (public access) from the portal and retry
* After you put the container registry behind a virtual network, run the [Azure Resource Manager template](https://aka.ms/azureml/environment/secure-resources-using-vnet) so the workspace can communicate with the container registry instance

If the image you're trying to reference doesn't exist in the container registry you specified
* Check that the correct tag is used and that `user_managed_dependencies` is set to `True`. Setting [user_managed_dependencies](https://aka.ms/azureml/environment/environment-python-section) to `True` disables conda and uses the user's installed packages

If you haven't provided credentials for a private registry you're trying to pull from, or the provided credentials are incorrect
* Set [workspace connections](https://aka.ms/azureml/environment/set-connection-v1) for the container registry if needed

### I/O Error
<!--issueDescription-->
This issue can happen when a Docker image pull fails due to a network issue.  

**Potential causes:**
* Network connection issue, which could be temporary
* Firewall is blocking the connection
* ACR is unreachable and there's network isolation. For more details, see [ACR unreachable](#acr-unreachable). 

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**  

Add the host to the firewall rules  
* See [configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md) to learn how to use Azure Firewall for your workspace and resources behind a VNet

Assess your workspace set-up. Are you using a virtual network, or are any of the resources you're trying to access during your image build behind a virtual network?
* Ensure that you've followed the steps in this article on [securing a workspace with virtual networks](https://aka.ms/azureml/environment/acr-private-endpoint)
* Azure Machine Learning requires both inbound and outbound access to the public internet. If there's a problem with your virtual network setup, there might be an issue with accessing certain repositories required during your image build  

If you aren't using a virtual network, or if you've configured it correctly
* Try rebuilding your image. If the timeout was due to a network issue, the problem might be transient, and a rebuild could fix the problem

## *Conda issues during build*
### Bad spec
<!--issueDescription-->
This issue can happen when a package listed in your conda specification is invalid or when a conda command is executed incorrectly.

**Potential causes:**
* The syntax you used in your conda specification is incorrect
* You're executing a conda command incorrectly

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Conda spec errors can happen when the conda create command is used incorrectly
* Read the [documentation](https://aka.ms/azureml/environment/conda-create) and ensure that you're using valid options and syntax
* There's known confusion regarding `conda env create` versus `conda create`. You can read more about conda's response and other users' known solutions [here](https://aka.ms/azureml/environment/conda-env-create-known-issue)

To ensure a successful build, ensure that you're using proper syntax and valid package specification in your conda yaml
* See [package match specifications](https://aka.ms/azureml/environment/conda-package-match-specifications) and [how to create a conda file manually](https://aka.ms/azureml/environment/how-to-create-conda-file)

### Communications error
<!--issueDescription-->
This issue can happen when there's a failure in communicating with the entity from which you wish to download packages listed in your conda specification.

**Potential causes:**
* Failed to communicate with a conda channel or a package repository
* These failures may be due to transient network failures 

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Ensure that the conda channels/repositories you're using in your conda specification are correct
* Check that they exist and are spelled correctly

If the conda channels/repositories are correct
* Try to rebuild the image--there's a chance that the failure is transient, and a rebuild might fix the issue
* Check to make sure that the packages listed in your conda specification exist in the channels/repositories you specified

### Compile error
<!--issueDescription-->
This issue can happen when there's a failure building a package required for the conda environment due to a compiler error.

**Potential causes:**
* A package was spelled incorrectly and therefore wasn't recognized
* There's something wrong with the compiler

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

If you're using a compiler
* Ensure that the compiler you're using is recognized
* If needed, add an installation step to your Dockerfile
* Verify the version of your compiler and check that all commands or options you're using are compatible with the compiler version
* If necessary, upgrade your compiler version

Ensure that all packages you've listed are spelled correctly and that any pinned versions are correct

**Resources**
* [Dockerfile reference on running commands](https://docs.docker.com/engine/reference/builder/#run)
* [Example compiler issue](https://stackoverflow.com/questions/46504700/gcc-compiler-not-recognizing-fno-plt-option)

### Missing command
<!--issueDescription-->
This issue can happen when a command isn't recognized during an image build.

**Potential causes:**
* The command wasn't spelled correctly
* The command can't be executed because a required package isn't installed

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

* Ensure that the command is spelled correctly
* Ensure that any package needed to execute the command you're trying to perform is installed
* If needed, add an installation step to your Dockerfile

**Resources**
* [Dockerfile reference on running commands](https://docs.docker.com/engine/reference/builder/#run)

### Conda timeout
<!--issueDescription-->
This issue can happen when conda package resolution takes too long to complete.

**Potential causes:**
* There's a large number of packages listed in your conda specification and unnecessary packages are included
* You haven't pinned your dependencies (you included tensorflow instead of tensorflow=2.8)
* You've listed packages for which there's no solution (you included package X=1.3 and Y=2.8, but X's version is incompatible with Y's version)

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**
* Remove any packages from your conda specification that are unnecessary
* Pin your packages--environment resolution will be faster
* If you're still having issues, review this article for an in-depth look at [understanding and improving conda's performance](https://aka.ms/azureml/environment/improve-conda-performance)

### Out of memory
<!--issueDescription-->
This issue can happen when conda package resolution fails due to available memory being exhausted.

**Potential causes:**
* There's a large number of packages listed in your conda specification and unnecessary packages are included
* You haven't pinned your dependencies (you included tensorflow instead of tensorflow=2.8)
* You've listed packages for which there's no solution (you included package X=1.3 and Y=2.8, but X's version is incompatible with Y's version)

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**
* Remove any packages from your conda specification that are unnecessary
* Pin your packages--environment resolution will be faster
* If you're still having issues, review this article for an in-depth look at [understanding and improving conda's performance](https://aka.ms/azureml/environment/improve-conda-performance)

### Package not found
<!--issueDescription-->
This issue can happen when one or more conda packages listed in your specification can't be found in a channel/repository.

**Potential causes:**
* The package's name or version was listed incorrectly in your conda specification 
* The package exists in a conda channel that you didn't list in your conda specification

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**
* Ensure that the package is spelled correctly and that the specified version exists
* Ensure that the package exists on the channel you're targeting
* Ensure that the channel/repository is listed in your conda specification so the package can be pulled correctly during package resolution

Specify channels in your conda specification:

```yaml
channels:
  - conda-forge
  - anaconda
dependencies:
  - python=3.8
  - tensorflow=2.8
Name: my_environment
```

**Resources**
* [Managing channels](https://aka.ms/azureml/environment/managing-conda-channels)

### Missing Python module
<!--issueDescription-->
This issue can happen when a Python module listed in your conda specification doesn't exist or isn't valid.

**Potential causes:**
* The module was spelled incorrectly
* The module isn't recognized

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**
* Ensure that the module is spelled correctly and exists
* Check to make sure that the module is compatible with the Python version you've specified in your conda specification
* If you haven't listed a specific Python version in your conda specification, make sure to list a specific version that's compatible with your module otherwise a default may be used that isn't compatible

Pin a Python version that's compatible with the pip module you're using:
```yaml
channels:
  - conda-forge
  - anaconda
dependencies:
  - python=3.8
  - pip:
    - dataclasses
Name: my_environment
```

### No matching distribution 
<!--issueDescription-->
This issue can happen when there's no package found that matches the version you specified.

**Potential causes:**
* The package name was spelled incorrectly
* The package and version can't be found on the channels or feeds that you specified
* The version you specified doesn't exist

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

* Ensure that the package is spelled correctly and exists
* Ensure that the version you specified for the package exists
* Ensure that you've specified the channel from which the package will be installed. If you don't specify a channel, defaults will be used and those defaults may or may not have the package you're looking for

How to list channels in a conda yaml specification:

```yaml
channels:
  - conda-forge
  - anaconda
dependencies:
  - python = 3.8
  - tensorflow = 2.8
Name: my_environment
```

**Resources**
* [Managing channels](https://aka.ms/azureml/environment/managing-conda-channels)
* [pypi](https://aka.ms/azureml/environment/pypi)

### Can't build mpi4py
<!--issueDescription-->
This issue can happen when building wheels for mpi4py fails.

**Potential causes:**
* Requirements for a successful mpi4py installation aren't met
* There's something wrong with the method you've chosen to install mpi4py

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Ensure that you have a working MPI installation (preference for MPI-3 support and for MPI being built with shared/dynamic libraries) 
* See [mpi4py installation](https://aka.ms/azureml/environment/install-mpi4py)
* If needed, follow these [steps on building MPI](https://mpi4py.readthedocs.io/en/stable/appendix.html#building-mpi-from-sources)

Ensure that you're using a compatible python version
* Python 2.5 or 3.5+ is required, but Python 3.7+ is recommended
* See [mpi4py installation](https://aka.ms/azureml/environment/install-mpi4py)

**Resources**
* [mpi4py installation](https://aka.ms/azureml/environment/install-mpi4py)

### Interactive auth was attempted
<!--issueDescription-->
This issue can happen when pip attempts interactive authentication during package installation.

**Potential causes:**
* You've listed a package that requires authentication, but you haven't provided credentials
* During the image build, pip tried to prompt you to authenticate which failed the build
because you can't provide interactive authentication during a build

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Provide authentication via workspace connections

*Applies to: Python SDK v1*

```python
from azureml.core import Workspace
ws = Workspace.from_config()
ws.set_connection("connection1", "PythonFeed", "<URL>", "Basic", "{'Username': '<username>', 'Password': '<password>'}")
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
This issue can happen when there's a package specified in your conda environment that isn't compatible with your specified Python version.

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Use a different version of the package that's compatible with your specified Python version

Alternatively, use a different version of Python that's compatible with the package you've specified
* If you're changing your Python version, use a version that's supported and that isn't nearing its end-of-life soon
* See Python [end-of-life dates](https://aka.ms/azureml/environment/python-end-of-life)

**Resources**
* [Python documentation by version](https://aka.ms/azureml/environment/python-versions)

### Conda bare redirection
<!--issueDescription-->
This issue can happen when a package is specified on the command line using "<" or ">" without using quotes, causing conda environment creation or update to fail.

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Add quotes around the package specification
* For example, change `conda install -y pip<=20.1.1` to `conda install -y "pip<=20.1.1"`

### UTF-8 decoding error
<!--issueDescription-->
This issue can happen when there's a failure decoding a character in your conda specification. 

**Potential causes:**
* Your conda YAML file contains characters that aren't compatible with UTF-8.

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

## *Pip issues during build*
### Failed to install packages
<!--issueDescription-->
This issue can happen when your image build fails during Python package installation.

**Potential causes:**
* There are many issues that could cause this error
* This is a generic message that's surfaced when the error you're encountering isn't yet covered by AzureML analysis

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Review your Build log for more information on your image build failure 

Leave feedback for the AzureML team to analyze the error you're experiencing
* [File a problem or suggestion](https://github.com/Azure/azureml-assets/issues/new?assignees=&labels=environmentLogs&template=environmentLogsFeedback.yml)

### Can't uninstall package
<!--issueDescription-->
This can happen when pip fails to uninstall a Python package that was installed via the operating system's package manager.

**Potential causes:**
* An existing pip problem or a problematic pip version
* An issue arising from not using an isolated environment

**Affected areas (symptoms):**
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

Read the following and determine if your failure is caused by an existing pip problem
* [Cannot uninstall while creating Docker image](https://stackoverflow.com/questions/63383400/error-cannot-uninstall-ruamel-yaml-while-creating-docker-image-for-azure-ml-a)
* [pip 10 disutils partial uninstall issue](https://github.com/pypa/pip/issues/5247)
* [pip 10 no longer uninstalls disutils packages](https://github.com/pypa/pip/issues/4805)

Try the following

```
pip install --ignore-installed [package]
```

Try creating a separate environment using conda

## *Docker push issues*
### Failed to store Docker image
<!--issueDescription-->
This issue can happen when a Docker image fails to be stored (pushed) to a container registry.  

**Potential causes:**
* A transient issue has occurred with the ACR associated with the workspace
* A container registry behind a virtual network is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)

**Affected areas (symptoms):**
* Failure in building environments from the UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**  

Retry the environment build if you suspect this is a transient issue with the workspace's Azure Container Registry (ACR)  

If your container registry is behind a virtual network or is using a private endpoint in an [unsupported region](https://aka.ms/azureml/environment/private-link-availability)
* Configure the container registry by using the service endpoint (public access) from the portal and retry
* After you put the container registry behind a virtual network, run the [Azure Resource Manager template](https://aka.ms/azureml/environment/secure-resources-using-vnet) so the workspace can communicate with the container registry instance

If you aren't using a virtual network, or if you've configured it correctly, test that your credentials are correct for your ACR by attempting a simple local build
* Get credentials for your workspace ACR from the Azure portal
* Log in to your ACR using `docker login <myregistry.azurecr.io> -u "username" -p "password"`
* For an image "helloworld", test pushing to your ACR by running `docker push helloworld`
* See [Quickstart: Build and run a container image using Azure Container Registry Tasks](../container-registry/container-registry-quickstart-task-cli.md)

## *Miscellaneous build issues*
### Build log unavailable
<!--issueDescription-->
**Potential causes:**
* AzureML isn't authorized to store your build logs in your storage account
* A transient error occurred while saving your build logs
* A system error occurred before an image build was triggered

**Affected areas (symptoms):**
* A successful build, but no available logs.
* Failure in building environments from UI, SDK, and CLI.
* Failure in running jobs because it will implicitly build the environment in the first step.
<!--/issueDescription-->

**Troubleshooting steps**

A rebuild may fix the issue if it's transient
