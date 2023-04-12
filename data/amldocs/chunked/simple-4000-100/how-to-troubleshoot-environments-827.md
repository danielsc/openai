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
