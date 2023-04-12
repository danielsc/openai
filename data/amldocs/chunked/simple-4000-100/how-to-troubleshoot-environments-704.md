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
