  * Ensure that the subscription_id is correct. Find the subscription_id in the Azure portal by selecting All Service and then Subscriptions. The characters "<" and ">" should not be included in the subscription_id value. For example, `subscription_id = "12345678-90ab-1234-5678-1234567890abcd"` has the valid format.
  * Ensure Contributor or Owner access to the subscription.
  * Check that the region is one of the supported regions: `eastus2`, `eastus`, `westcentralus`, `southeastasia`, `westeurope`, `australiaeast`, `westus2`, `southcentralus`.
  * Ensure access to the region using the Azure portal.
  
* **workspace.from_config fails**:

  If the call `ws = Workspace.from_config()` fails:

  1. Ensure that the configuration.ipynb notebook has run successfully.
  1. If the notebook is being run from a folder that is not under the folder where the `configuration.ipynb` was run, copy the folder aml_config and the file config.json that it contains to the new folder. Workspace.from_config reads the config.json for the notebook folder or its parent folder.
  1. If a new subscription, resource group, workspace, or region, is being used, make sure that you run the `configuration.ipynb` notebook again. Changing config.json directly will only work if the workspace already exists in the specified resource group under the specified subscription.
  1. If you want to change the region, change the workspace, resource group, or subscription. `Workspace.create` will not create or update a workspace if it already exists, even if the region specified is different.

## TensorFlow

As of version 1.5.0 of the SDK, automated machine learning does not install TensorFlow models by default. To install TensorFlow and use it with your automated ML experiments, install `tensorflow==1.12.0` via `CondaDependencies`.

```python
  from azureml.core.runconfig import RunConfiguration
  from azureml.core.conda_dependencies import CondaDependencies
  run_config = RunConfiguration()
  run_config.environment.python.conda_dependencies = CondaDependencies.create(conda_packages=['tensorflow==1.12.0'])
```

## Numpy failures

* **`import numpy` fails in Windows**: Some Windows environments see an error loading numpy with the latest Python version 3.6.8. If you see this issue, try with Python version 3.6.7.

* **`import numpy` fails**: Check the TensorFlow version in the automated ml conda environment. Supported versions are < 1.13. Uninstall TensorFlow from the environment if version is >= 1.13.

You can check the version of TensorFlow and uninstall as follows:

  1. Start a command shell, activate conda environment where automated ml packages are installed.
  1. Enter `pip freeze` and look for `tensorflow`, if found, the version listed should be < 1.13
  1. If the listed version is not a supported version, `pip uninstall tensorflow` in the command shell and enter y for confirmation.

## `jwt.exceptions.DecodeError`

Exact error message: `jwt.exceptions.DecodeError: It is required that you pass in a value for the "algorithms" argument when calling decode()`.

For SDK versions <= 1.17.0, installation might result in an unsupported version of PyJWT. Check that the PyJWT version in the automated ml conda environment is a supported version. That is PyJWT version < 2.0.0.

You may check the version of PyJWT as follows:

1. Start a command shell and activate conda environment where automated ML packages are installed.

1. Enter `pip freeze` and look for `PyJWT`, if found, the version listed should be < 2.0.0

If the listed version is not a supported version:

1. Consider upgrading to the latest version of AutoML SDK: `pip install -U azureml-sdk[automl]`

1. If that is not viable, uninstall PyJWT from the environment and install the right version as follows:

    1. `pip uninstall PyJWT` in the command shell and enter `y` for confirmation.
    1. Install using `pip install 'PyJWT<2.0.0'`.
  

## Data access
 
For automated ML jobs, you need to ensure the file datastore that connects to your AzureFile storage has the appropriate authentication credentials. Otherwise, the following message results. Learn how to [update your data access authentication credentials](v1/how-to-train-with-datasets.md#azurefile-storage).
