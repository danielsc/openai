
## Create a deployment with your configuration

Create a deployment that's associated with the online endpoint. [Learn more about deploying to online endpoints](how-to-deploy-online-endpoints.md).

>[!WARNING]
> This deployment can take approximately 8-14 minutes depending on whether the underlying environment/image is being built for the first time. Subsequent deployments using the same environment will go quicker.

# [System-assigned (CLI)](#tab/system-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="deploy" :::

>[!NOTE]
> The value of the `--name` argument may override the `name` key inside the YAML file.

Check the status of the deployment.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="check_deploy_Status" :::

To refine the above query to only return specific data, see [Query Azure CLI command output](/cli/azure/query-azure-cli).

> [!NOTE]
> The init method in the scoring script reads the file from your storage account using the system-assigned managed identity token.

To check the init method output, see the deployment log with the following code. 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-sai.sh" id="check_deployment_log" :::


# [User-assigned (CLI)](#tab/user-identity-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="create_endpoint" :::

>[!Note]
> The value of the `--name` argument may override the `name` key inside the YAML file.

Once the command executes, you can check the status of the deployment.

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="check_endpoint_Status" :::

To refine the above query to only return specific data, see [Query Azure CLI command output](/cli/azure/query-azure-cli).

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="check_deployment_log" :::

> [!NOTE]
> The init method in the scoring script reads the file from your storage account using the user-assigned managed identity token.

To check the init method output, see the deployment log with the following code. 

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint-access-resource-uai.sh" id="check_deployment_log" :::

# [System-assigned (Python)](#tab/system-identity-python)

First, create the deployment:  

```python
ml_client.online_deployments.begin_create_or_update(deployment).result()
```

Once deployment completes, check its status and confirm its identity details: 

```python
deployment = ml_client.online_deployments.get(
    endpoint_name=endpoint_name, name=deployment.name
)
print(deployment)
```

> [!NOTE]
> The init method in the scoring script reads the file from your storage account using the system-assigned managed identity token.

To check the init method output, see the deployment log with the following code. 

```python
ml_client.online_deployments.get_logs(deployment.name, deployment.endpoint_name, 1000)
```

Now that the deployment is confirmed, set the traffic to 100%: 

```python
endpoint.traffic = {str(deployment.name): 100}
ml_client.begin_create_or_update(endpoint).result()
```

# [User-assigned (Python)](#tab/user-identity-python)

Before we deploy, update the `UAI_CLIENT_ID` environment variable placeholder. 

```python
deployment.environment_variables["UAI_CLIENT_ID"] = uai_client_id
```

Now, create the deployment: 

```python
ml_client.online_deployments.begin_create_or_update(deployment).result()
```

Once deployment completes, check its status and confirm its identity details: 

```python
deployment = ml_client.online_deployments.get(
    endpoint_name=endpoint_name, name=deployment.name
)
print(deployment)
```
