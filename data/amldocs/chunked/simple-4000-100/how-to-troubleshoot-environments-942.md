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
