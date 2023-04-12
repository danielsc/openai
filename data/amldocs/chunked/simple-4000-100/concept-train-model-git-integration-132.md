> To check if the git command is available on your development environment, open a shell session, command prompt, PowerShell or other command line interface and type the following command:
>
> ```
> git --version
> ```
>
> If installed, and in the path, you receive a response similar to `git version 2.4.1`. For more information on installing git on your development environment, see the [Git website](https://git-scm.com/).

## View the logged information

The git information is stored in the properties for a training job. You can view this information using the Azure portal or Python SDK.

### Azure portal

1. From the [studio portal](https://ml.azure.com), select your workspace.
1. Select __Jobs__, and then select one of your experiments.
1. Select one of the jobs from the __Display name__ column.
1. Select __Outputs + logs__, and then expand the __logs__ and __azureml__ entries. Select the link that begins with __###\_azure__.

The logged information contains text similar to the following JSON:

```json
"properties": {
    "_azureml.ComputeTargetType": "batchai",
    "ContentSnapshotId": "5ca66406-cbac-4d7d-bc95-f5a51dd3e57e",
    "azureml.git.repository_uri": "git@github.com:azure/machinelearningnotebooks",
    "mlflow.source.git.repoURL": "git@github.com:azure/machinelearningnotebooks",
    "azureml.git.branch": "master",
    "mlflow.source.git.branch": "master",
    "azureml.git.commit": "4d2b93784676893f8e346d5f0b9fb894a9cf0742",
    "mlflow.source.git.commit": "4d2b93784676893f8e346d5f0b9fb894a9cf0742",
    "azureml.git.dirty": "True",
    "AzureML.DerivedImageName": "azureml/azureml_9d3568242c6bfef9631879915768deaf",
    "ProcessInfoFile": "azureml-logs/process_info.json",
    "ProcessStatusFile": "azureml-logs/process_status.json"
}
```

### View properties

After submitting a training run, a [Job](/python/api/azure-ai-ml/azure.ai.ml.entities.job) object is returned. The `properties` attribute of this object contains the logged git information. For example, the following code retrieves the commit hash:

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
job.properties["azureml.git.commit"]
```

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml job show --name my_job_id --query "{GitCommit:properties."""azureml.git.commit"""}"
```


## Next steps

* [Access a compute instance terminal in your workspace](how-to-access-terminal.md)
