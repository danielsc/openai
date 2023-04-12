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
