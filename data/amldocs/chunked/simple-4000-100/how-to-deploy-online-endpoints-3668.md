
The `update` command also works with local deployments. Use the same `az ml online-deployment update` command with the `--local` flag.

# [Python](#tab/python)

If you want to update the code, model, or environment, update the configuration, and then run the `MLClient`'s [`online_deployments.begin_create_or_update`](/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations#azure-ai-ml-operations-onlinedeploymentoperations-begin-create-or-update) module/method. 

> [!NOTE]
> If you update instance count and along with other model settings (code, model, or environment) in a single `begin_create_or_update` method: first the scaling operation will be performed, then the other updates will be applied. In production environment is a good practice to perform these operations separately.

To understand how `begin_create_or_update` works:

1. Open the file *online/model-1/onlinescoring/score.py*.
2. Change the last line of the `init()` function: After `logging.info("Init complete")`, add `logging.info("Updated successfully")`. 
3. Save the file.
4. Run the method:

    ```python
    ml_client.online_deployments.begin_create_or_update(blue_deployment)
    ```

5. Because you modified the `init()` function (`init()` runs when the endpoint is created or updated), the message `Updated successfully` will be in the logs. Retrieve the logs by running:

    ```python
    ml_client.online_deployments.get_logs(
        name="blue", endpoint_name=online_endpoint_name, lines=50
    )
    ```

The `begin_create_or_update` method also works with local deployments. Use the same method with the `local=True` flag.

# [ARM template](#tab/arm)

There currently is not an option to update the deployment using an ARM template.


> [!Note]
> The above is an example of inplace rolling update.
> * For managed online endpoint, the same deployment is updated with the new configuration, with 20% nodes at a time, i.e. if the deployment has 10 nodes, 2 nodes at a time will be updated. 
> * For Kubernetes online endpoint, the system will iterately create a new deployment instance with the new configuration and delete the old one.
> * For production usage, you might want to consider [blue-green deployment](how-to-safely-rollout-online-endpoints.md), which offers a safer alternative.

### (Optional) Configure autoscaling

Autoscale automatically runs the right amount of resources to handle the load on your application. Managed online endpoints support autoscaling through integration with the Azure monitor autoscale feature. To configure autoscaling, see [How to autoscale online endpoints](how-to-autoscale-endpoints.md).

### (Optional) Monitor SLA by using Azure Monitor

To view metrics and set alerts based on your SLA, complete the steps that are described in [Monitor online endpoints](how-to-monitor-online-endpoints.md).

### (Optional) Integrate with Log Analytics

The `get-logs` command for CLI or the `get_logs` method for SDK provides only the last few hundred lines of logs from an automatically selected instance. However, Log Analytics provides a way to durably store and analyze logs. For more information on using logging, see [Monitor online endpoints](how-to-monitor-online-endpoints.md#logs)

[!INCLUDE [Email Notification Include](../../includes/machine-learning-email-notifications.md)]

## Delete the endpoint and the deployment

If you aren't going use the deployment, you should delete it by running the following code (it deletes the endpoint and all the underlying deployments):

# [Azure CLI](#tab/azure-cli)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="delete_endpoint" :::

# [Python](#tab/python)

```python
ml_client.online_endpoints.begin_delete(name=online_endpoint_name)
```

# [ARM template](#tab/arm)

::: code language="azurecli" source="~/azureml-examples-main/cli/deploy-managed-online-endpoint.sh" ID="delete_endpoint" :::


## Next steps

Try safe rollout of your models as a next step:
