
# [Python (Azure ML SDK)](#tab/sdk)

```python
ml_client.online_endpoints.begin_delete(name=endpoint_name)
```

# [Python (MLflow SDK)](#tab/mlflow)

```python
deployment_client.delete_endpoint(endpoint_name)
```


> [!IMPORTANT]
> Notice that deleting an endpoint also deletes all the deployments under it.

## Next steps

- [Deploy MLflow models to Batch Endpoints](how-to-mlflow-batch.md)
- [Using MLflow models for no-code deployment](how-to-log-mlflow-models.md)
