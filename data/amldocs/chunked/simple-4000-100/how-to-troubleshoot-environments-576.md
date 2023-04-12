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
