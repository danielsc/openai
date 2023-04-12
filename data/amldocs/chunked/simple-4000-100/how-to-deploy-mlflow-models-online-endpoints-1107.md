
# [Python (Azure ML SDK)](#tab/sdk)
    
```python
ml_client.online_endpoints.begin_delete(endpoint_name)
```

# [Python (MLflow SDK)](#tab/mlflow)

```python
deployment_client.delete_endpoint(endpoint_name)
```

# [Studio](#tab/studio)

1. Navigate to the __Endpoints__ tab on the side menu.
1. Select the tab __Online endpoints__.
1. Select the endpoint you want to delete.
1. Click on __Delete__.
1. The endpoint all along with its deployments will be deleted.


## Next steps

To learn more, review these articles:

- [Deploy models with REST](how-to-deploy-with-rest.md)
- [Create and use online endpoints in the studio](how-to-use-managed-online-endpoint-studio.md)
- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)
- [How to autoscale managed online endpoints](how-to-autoscale-endpoints.md)
- [Use batch endpoints for batch scoring](batch-inference/how-to-use-batch-endpoint.md)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
- [Access Azure resources with an online endpoint and managed identity](how-to-access-resources-from-endpoints-managed-identities.md)
- [Troubleshoot online endpoint deployment](how-to-troubleshoot-managed-online-endpoints.md)
