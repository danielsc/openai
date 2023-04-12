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
