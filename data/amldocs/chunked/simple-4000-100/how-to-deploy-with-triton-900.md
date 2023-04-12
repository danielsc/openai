
1. Use the following command to archive your model:

    ```azurecli
    az ml model archive --name $MODEL_NAME --version $MODEL_VERSION
    ```

# [Python](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

1. Delete the endpoint. Deleting the endpoint also deletes any child deployments, however it will not archive associated Environments or Models. 

    ```python
    ml_client.online_endpoints.begin_delete(name=endpoint_name)
    ```

1. Archive the model with the following code.

    ```python 
    ml_client.models.archive(name=model_name, version=model_version)
    ```

# [Studio](#tab/azure-studio)

1. From the endpoint's page, click `Delete` in the second row below the endpoint's name. 

1. From the model's page, click `Delete` in the first row below the model's name. 


## Next steps

To learn more, review these articles:

- [Deploy models with REST](how-to-deploy-with-rest.md)
- [Create and use managed online endpoints in the studio](how-to-use-managed-online-endpoint-studio.md)
- [Safe rollout for online endpoints ](how-to-safely-rollout-online-endpoints.md)
- [How to autoscale managed online endpoints](how-to-autoscale-endpoints.md)
- [View costs for an Azure Machine Learning managed online endpoint](how-to-view-online-endpoints-costs.md)
- [Access Azure resources with a managed online endpoint and managed identity](how-to-access-resources-from-endpoints-managed-identities.md)
- [Troubleshoot managed online endpoints deployment](how-to-troubleshoot-managed-online-endpoints.md)
