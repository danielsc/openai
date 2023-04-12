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
