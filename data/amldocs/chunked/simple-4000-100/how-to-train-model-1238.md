
# [REST API](#tab/restapi)

> [!TIP]
> The name (stored in the `$run_id` variable) is used as part of the path to the model.

```bash
curl --location --request PUT "https://management.azure.com/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP/providers/Microsoft.MachineLearningServices/workspaces/$WORKSPACE/models/sklearn/versions/1?api-version=$API_VERSION" \
--header "Authorization: Bearer $TOKEN" \
--header "Content-Type: application/json" \
--data-raw "{
    \"properties\": {
        \"modelType\": \"mlflow_model\",
        \"modelUri\":\"runs:/$run_id/model\"
    }
}"
```


## Next steps

Now that you have a trained model, learn [how to deploy it using an online endpoint](how-to-deploy-online-endpoints.md).

For more examples, see the [AzureML examples](https://github.com/azure/azureml-examples) GitHub repository.

For more information on the Azure CLI commands, Python SDK classes, or REST APIs used in this article, see the following reference documentation:

* [Azure CLI `ml` extension](/cli/azure/ml)
* [Python SDK](/python/api/azure-ai-ml/azure.ai.ml)
* [REST API](/rest/api/azureml/)
