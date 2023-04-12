
# [Python](#tab/python)
[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
mon_client.autoscale_settings.delete(
    resource_group, 
    autoscale_settings_name
)

ml_client.online_endpoints.begin_delete(endpoint_name)
```

# [Studio](#tab/azure-studio)
1. Go to the [Azure Machine Learning studio](https://ml.azure.com).
1. In the left navigation bar, select the **Endpoints** page.
1. Select an endpoint by checking the circle next to the model name.
1. Select **Delete**.

Alternatively, you can delete a managed online endpoint directly in the [endpoint details page](how-to-use-managed-online-endpoint-studio.md#view-managed-online-endpoints). 


## Next steps

To learn more about autoscale with Azure Monitor, see the following articles:

- [Understand autoscale settings](../azure-monitor/autoscale/autoscale-understanding-settings.md)
- [Overview of common autoscale patterns](../azure-monitor/autoscale/autoscale-common-scale-patterns.md)
- [Best practices for autoscale](../azure-monitor/autoscale/autoscale-best-practices.md)
- [Troubleshooting Azure autoscale](../azure-monitor/autoscale/autoscale-troubleshoot.md)
