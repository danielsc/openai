
> [!NOTE]
> The init method in the scoring script reads the file from your storage account using the user-assigned managed identity token.

To check the init method output, see the deployment log with the following code. 

```python
ml_client.online_deployments.get_logs(deployment.name, deployment.endpoint_name, 1000)
```

Now that the deployment is confirmed, set the traffic to 100%: 

```python
endpoint.traffic = {str(deployment.name): 100}
ml_client.begin_create_or_update(endpoint).result()
```


When your deployment completes,  the model, the environment, and the endpoint are registered to your Azure Machine Learning workspace.

## Test the endpoint

Once your online endpoint is deployed, test and confirm its operation with a request. Details of inferencing vary from model to model. For this guide, the JSON query parameters look like: 

```json
{"data": [
    [1,2,3,4,5,6,7,8,9,10], 
    [10,9,8,7,6,5,4,3,2,1]
]}
```

To call your endpoint, run:

# [System-assigned (CLI)](#tab/system-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="test_endpoint" :::

# [User-assigned (CLI)](#tab/user-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="test_endpoint" :::

# [System-assigned (Python)](#tab/system-identity-python)

```python
sample_data = "../../model-1/sample-request.json"
ml_client.online_endpoints.invoke(endpoint_name=endpoint_name, request_file=sample_data)
```

# [User-assigned (Python)](#tab/user-identity-python)


```python
sample_data = "../../model-1/sample-request.json"
ml_client.online_endpoints.invoke(endpoint_name=endpoint_name, request_file=sample_data)
```


## Delete the endpoint and storage account

If you don't plan to continue using the deployed online endpoint and storage, delete them to reduce costs. When you delete the endpoint, all of its associated deployments are deleted as well.

# [System-assigned (CLI)](#tab/system-identity-cli)
 
::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="delete_endpoint" :::
::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="delete_storage_account" :::

# [User-assigned (CLI)](#tab/user-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="delete_endpoint" :::
::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="delete_storage_account" :::
::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="delete_user_identity" :::

# [System-assigned (Python)](#tab/system-identity-python)

Delete the endpoint: 

```python
ml_client.online_endpoints.begin_delete(endpoint_name)
```

Delete the storage account: 

```python
storage_client.storage_accounts.delete(
    resource_group_name=resource_group, account_name=storage_account_name
)
```

# [User-assigned (Python)](#tab/user-identity-python)

Delete the endpoint: 

```python
ml_client.online_endpoints.begin_delete(endpoint_name)
```


Delete the storage account: 

```python
storage_client.storage_accounts.delete(
    resource_group_name=resource_group, account_name=storage_account_name
)
```

Delete the User-assigned managed identity: 

```python
msi_client.user_assigned_identities.delete(
    resource_group_name=resource_group, resource_name=uai_name
)
```


## Next steps

* [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md).
* For more on deployment, see [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md).
* For more information on using the CLI, see [Use the CLI extension for Azure Machine Learning](reference-azure-machine-learning-cli.md).
