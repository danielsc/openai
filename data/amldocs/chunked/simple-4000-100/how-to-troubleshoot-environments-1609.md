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
