If you aren't going use the deployment, you should delete it to reduce costs. The following example deletes the endpoint and all the underlying deployments:

# [Azure CLI](#tab/cli)

```azurecli
az ml online-endpoint delete --name reg-ep-1234 --yes --no-wait
```

# [Python SDK](#tab/python)

```python
ml_client_workspace.online_endpoints.begin_delete(name=online_endpoint_name)
```


## Next steps

* [How to create and manage registries](how-to-manage-registries.md)
* [How to manage environments](how-to-manage-environments-v2.md)
* [How to train models](how-to-train-cli.md)
* [How to create pipelines using components](how-to-create-component-pipeline-python.md)
