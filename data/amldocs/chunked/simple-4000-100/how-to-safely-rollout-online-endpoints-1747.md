
# [Python](#tab/python)

If you aren't going use the deployment, you should delete it with:

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```


## Next steps
- [Explore online endpoint samples](https://github.com/Azure/azureml-examples/tree/v2samplesreorg/sdk/python/endpoints)
- [Deploy models with REST](how-to-deploy-with-rest.md)
- [Create and use online endpoints  in the studio](how-to-use-managed-online-endpoint-studio.md)
- [Access Azure resources with a online endpoint and managed identity](how-to-access-resources-from-endpoints-managed-identities.md)
- [Monitor managed online endpoints](how-to-monitor-online-endpoints.md)
- [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
- [Managed online endpoints SKU list](reference-managed-online-endpoints-vm-sku-list.md)
- [Troubleshooting  online endpoints deployment and scoring](how-to-troubleshoot-managed-online-endpoints.md)
- [Online endpoint YAML reference](reference-yaml-endpoint-online.md)
