
# Troubleshoot automated ML experiments in Python

[!INCLUDE [sdk v1](../../includes/machine-learning-sdk-v1.md)]

In this guide, learn how to identify and resolve known issues in your automated machine learning experiments with the [Azure Machine Learning SDK](/python/api/overview/azure/ml/intro).

## Version dependencies

**`AutoML` dependencies to newer package versions break compatibility**. After SDK version 1.13.0, models aren't loaded in older SDKs due to incompatibility between the older versions pinned in previous `AutoML` packages, and the newer versions pinned today.

Expect errors such as:

* Module not found errors such as,

  `No module named 'sklearn.decomposition._truncated_svd'`

* Import errors such as,

  `ImportError: cannot import name 'RollingOriginValidator'`,
* Attribute errors such as,

  `AttributeError: 'SimpleImputer' object has no attribute 'add_indicator'`

Resolutions depend on your `AutoML` SDK training version:

* If your `AutoML` SDK training version is greater than 1.13.0, you need `pandas == 0.25.1` and `scikit-learn==0.22.1`.

    * If there is a version mismatch, upgrade scikit-learn and/or pandas to correct version with the following,

      ```bash
          pip install --upgrade pandas==0.25.1
          pip install --upgrade scikit-learn==0.22.1
      ```

* If your `AutoML` SDK training version is less than or equal to 1.12.0, you need `pandas == 0.23.4` and `sckit-learn==0.20.3`.
  * If there is a version mismatch, downgrade scikit-learn and/or pandas to correct version with the following,
  
    ```bash
      pip install --upgrade pandas==0.23.4
      pip install --upgrade scikit-learn==0.20.3
    ```

## Setup

`AutoML` package changes since version 1.0.76 require the previous version to be uninstalled before updating to the new version.

* **`ImportError: cannot import name AutoMLConfig`**

    If you encounter this error after upgrading from an SDK version before v1.0.76 to v1.0.76 or later, resolve the error by running: `pip uninstall azureml-train automl` and then `pip install azureml-train-automl`. The automl_setup.cmd script does this automatically.

* **automl_setup fails**

  * On Windows, run automl_setup from an Anaconda Prompt. [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html).

  * Ensure that conda 64-bit version  4.4.10 or later is installed. You can check the bit with the `conda info` command. The `platform` should be `win-64` for Windows or `osx-64` for Mac. To check the version use the command `conda -V`. If you have a previous version installed, you can update it by using the command: `conda update conda`. To check  32-bit by running 

  * Ensure that conda  is installed. 

  * Linux - `gcc: error trying to exec 'cc1plus'`

    1. If the `gcc: error trying to exec 'cc1plus': execvp: No such file or directory` error is encountered, install the GCC build tools for your Linux distribution. For example, on Ubuntu, use the command `sudo apt-get install build-essential`.

    1. Pass a new name as the first parameter to automl_setup to create a new conda environment. View existing conda environments using `conda env list` and remove them with `conda env remove -n <environmentname>`.

* **automl_setup_linux.sh fails**: If automl_setup_linus.sh fails on Ubuntu Linux with the error: `unable to execute 'gcc': No such file or directory`

  1. Make sure that outbound ports 53 and 80 are enabled. On an Azure virtual machine, you can do this from the Azure portal by selecting the VM and clicking on **Networking**.
  1. Run the command: `sudo apt-get update`
  1. Run the command: `sudo apt-get install build-essential --fix-missing`
  1. Run `automl_setup_linux.sh` again

* **configuration.ipynb fails**:

  * For local conda, first ensure that `automl_setup` has successfully run.
  * Ensure that the subscription_id is correct. Find the subscription_id in the Azure portal by selecting All Service and then Subscriptions. The characters "<" and ">" should not be included in the subscription_id value. For example, `subscription_id = "12345678-90ab-1234-5678-1234567890abcd"` has the valid format.
