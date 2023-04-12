- `request_file` - File with request data
- `deployment_name` - Name of the specific deployment to test in an endpoint

We'll send a sample request using a json file. The sample json is in the [example repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/endpoints/online/custom-container).

```python
# test the blue deployment with some sample data
ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="blue",
    request_file="sample-request.json",
)
```


### Delete the endpoint

Now that you've successfully scored with your endpoint, you can delete it:

# [Azure CLI](#tab/cli)

```azurecli
az ml online-endpoint delete --name tfserving-endpoint
```

# [Python SDK](#tab/python)

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```


## Next steps

- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)
- [Troubleshooting online endpoints deployment](./how-to-troubleshoot-online-endpoints.md)
- [Torch serve sample](https://github.com/Azure/azureml-examples/blob/main/cli/deploy-custom-container-torchserve-densenet.sh)
