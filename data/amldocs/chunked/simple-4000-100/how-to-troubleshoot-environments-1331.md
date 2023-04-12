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
