
To delete all the resources created in this article, use the following command. Replace `<resource-group-name>` with the name of the resource group used in this example:

```azurecli
az group delete --resource-group <resource-group-name>
```

## Troubleshooting

[!INCLUDE [network isolation issues](../../includes/machine-learning-online-endpoint-troubleshooting.md)]

## Next steps

- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)
- [How to autoscale managed online endpoints](how-to-autoscale-endpoints.md)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
- [Access Azure resources with a online endpoint and managed identity](how-to-access-resources-from-endpoints-managed-identities.md)
- [Troubleshoot online endpoints deployment](how-to-troubleshoot-online-endpoints.md)