

# Troubleshoot "cannot import name 'SerializationError'"

When using Azure Machine Learning, you may receive one of the following errors:

* `cannot import name 'SerializationError'`
* `cannot import name 'SerializationError' from 'azure.core.exceptions'`

This error may occur when using an Azure Machine Learning environment. For example, when submitting a training job or using AutoML.

## Cause

This problem is caused by a bug in the Azure Machine Learning SDK version 1.42.0.

## Resolution

Update the affected environment to use SDK version 1.42.0.post1 or greater. For a local development environment or compute instance, use the following command:

```bash
pip install azureml-sdk[automl,explain,notebooks]>=1.42.0
```

For more information on updating an Azure Machine Learning environment (for training or deployment), see the following articles:

* [Manage environments in studio](how-to-manage-environments-in-studio.md#rebuild-an-environment)
* [Create & use software environments (SDK v1)](how-to-use-environments.md#update-an-existing-environment)
* [Create & manage environments (CLI v2)](how-to-manage-environments-v2.md#update)

To verify the version of your installed SDK, use the following command:

```bash
pip show azureml-core
```

## Next steps

For more information on updating an Azure Machine Learning environment (for training or deployment), see the following articles:

* [Manage environments in studio](how-to-manage-environments-in-studio.md#rebuild-an-environment)
* [Create & use software environments (SDK v1)](how-to-use-environments.md#update-an-existing-environment)
* [Create & manage environments (CLI v2)](how-to-manage-environments-v2.md#update)