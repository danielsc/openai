
### Delete resources you no longer need

Some, but not all, resources support the DELETE verb. Check the [API Reference](/rest/api/azureml/) before committing to the REST API for deletion use-cases. To delete a model, for instance, you can use:

```bash
curl
  -X DELETE \
'https://<REGIONAL-API-SERVER>/modelmanagement/v1.0/subscriptions/<YOUR-SUBSCRIPTION-ID>/resourceGroups/<YOUR-RESOURCE-GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<YOUR-WORKSPACE-NAME>/models/<YOUR-MODEL-ID>?api-version=2022-05-01' \
  -H 'Authorization:Bearer <YOUR-ACCESS-TOKEN>' 
```

## Troubleshooting

### Resource provider errors

[!INCLUDE [machine-learning-resource-provider](../../includes/machine-learning-resource-provider.md)]

### Moving the workspace

> [!WARNING]
> Moving your Azure Machine Learning workspace to a different subscription, or moving the owning subscription to a new tenant, is not supported. Doing so may cause errors.

### Deleting the Azure Container Registry

The Azure Machine Learning workspace uses Azure Container Registry (ACR) for some operations. It will automatically create an ACR instance when it first needs one.

[!INCLUDE [machine-learning-delete-acr](../../includes/machine-learning-delete-acr.md)]

## Next steps

- Explore the complete [AzureML REST API reference](/rest/api/azureml/).
- Learn how to use the designer to [Predict automobile price with the designer](./tutorial-designer-automobile-price-train-score.md).
- Explore [Azure Machine Learning with Jupyter notebooks](..//machine-learning/samples-notebooks.md).
