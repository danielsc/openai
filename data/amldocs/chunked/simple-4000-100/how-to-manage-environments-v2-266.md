
### Update

Update mutable properties of a specific environment:

# [Azure CLI](#tab/cli)

```cli
az ml environment update --name docker-image-example --version 1 --set description="This is an updated description."
```

# [Python SDK](#tab/python)

```python
env.description="This is an updated description."
ml_client.environments.create_or_update(environment=env)
```

> [!IMPORTANT]
> For environments, only `description` and `tags` can be updated. All other properties are immutable; if you need to change any of those properties you should create a new version of the environment.

### Archive

Archiving an environment will hide it by default from list queries (`az ml environment list`). You can still continue to reference and use an archived environment in your workflows. You can archive either all versions of an environment or only a specific version.

If you don't specify a version, all versions of the environment under that given name will be archived. If you create a new environment version under an archived environment container, that new version will automatically be set as archived as well.

Archive all versions of an environment:

# [Azure CLI](#tab/cli)

```cli
az ml environment archive --name docker-image-example
```

# [Python SDK](#tab/python)

```python
ml_client.environments.archive(name="docker-image-example")
```

            
Archive a specific environment version:

# [Azure CLI](#tab/cli)

```cli
az ml environment archive --name docker-image-example --version 1
```

# [Python SDK](#tab/python)

```python
ml_client.environments.archive(name="docker-image-example", version="1")
```



## Use environments for training

# [Azure CLI](#tab/cli)

To use an environment for a training job, specify the `environment` field of the job YAML configuration. You can either reference an existing registered Azure ML environment via `environment: azureml:<environment-name>:<environment-version>` or `environment: azureml:<environment-name>@latest` (to reference the latest version of an environment), or define an environment specification inline. If defining an environment inline, don't specify the `name` and `version` fields, as these environments are treated as "unregistered" environments and aren't tracked in your environment asset registry.

# [Python SDK](#tab/python)

To use an environment for a training job, specify the `environment` property of the [command](/python/api/azure-ai-ml/azure.ai.ml#azure-ai-ml-command).

For examples of submitting jobs, see the examples at [https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs).

When you submit a training job, the building of a new environment can take several minutes. The duration depends on the size of the required dependencies. The environments are cached by the service. So as long as the environment definition remains unchanged, you incur the full setup time only once.


For more information on how to use environments in jobs, see [Train models](how-to-train-model.md).

## Use environments for model deployments

# [Azure CLI](#tab/cli)

You can also use environments for your model deployments for both online and batch scoring. To do so, specify the `environment` field in the deployment YAML configuration.

For more information on how to use environments in deployments, see [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md).

# [Python SDK](#tab/python)

You can also use environments for your model deployments. For more information, see [Deploy and score a machine learning model](how-to-deploy-managed-online-endpoint-sdk-v2.md).


## Next steps

- [Train models (create jobs)](how-to-train-model.md)
- [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md)
- [Environment YAML schema reference](reference-yaml-environment.md)
