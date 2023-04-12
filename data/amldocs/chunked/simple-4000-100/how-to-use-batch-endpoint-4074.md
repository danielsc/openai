
# [Python](#tab/python)

```python
endpoint = ml_client.batch_endpoints.get(endpoint_name)
endpoint.defaults.deployment_name = deployment.name
ml_client.batch_endpoints.begin_create_or_update(endpoint)
```

# [Studio](#tab/azure-studio)

1. Navigate to the __Endpoints__ tab on the side menu.
1. Select the tab __Batch endpoints__.
1. Select the batch endpoint you want to configure.
1. Select __Update default deployment__.
    
    :::image type="content" source="./media/how-to-use-batch-endpoints-studio/update-default-deployment.png" alt-text="Screenshot of updating default deployment.":::

1. On __Select default deployment__, select the name of the deployment you want to be the default one.
1. Select __Update__.
1. The selected deployment is now the default one.


## Delete the batch endpoint and the deployment

# [Azure CLI](#tab/azure-cli)

If you aren't going to use the old batch deployment, you should delete it by running the following code. `--yes` is used to confirm the deletion.

::: code language="azurecli" source="~/azureml-examples-main/cli/batch-score.sh" ID="delete_deployment" :::

Run the following code to delete the batch endpoint and all the underlying deployments. Batch scoring jobs won't be deleted.

::: code language="azurecli" source="~/azureml-examples-main/cli/batch-score.sh" ID="delete_endpoint" :::

# [Python](#tab/python)

Delete endpoint:

```python
ml_client.batch_endpoints.begin_delete(name=batch_endpoint_name)
```

Delete compute: optional, as you may choose to reuse your compute cluster with later deployments.

```python
ml_client.compute.begin_delete(name=compute_name)
```

# [Studio](#tab/azure-studio)

1. Navigate to the __Endpoints__ tab on the side menu.
1. Select the tab __Batch endpoints__.
1. Select the batch endpoint you want to delete.
1. Select __Delete__.
1. The endpoint all along with its deployments will be deleted.
1. Notice that this won't affect the compute cluster where the deployment(s) run.


## Next steps

* [Accessing data from batch endpoints jobs](how-to-access-data-batch-endpoints-jobs.md).
* [Authentication on batch endpoints](how-to-authenticate-batch-endpoint.md).
* [Network isolation in batch endpoints](how-to-secure-batch-endpoint.md).
* [Troubleshooting batch endpoints](how-to-troubleshoot-batch-endpoints.md).
