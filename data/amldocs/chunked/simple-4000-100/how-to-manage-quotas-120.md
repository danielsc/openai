[Azure Machine Learning pipelines](concept-ml-pipelines.md) have the following limits.

| **Resource** | **Limit** |
| --- | --- |
| Steps in a pipeline | 30,000 |
| Workspaces per resource group | 800 |

### Azure Machine Learning integration with Synapse
Synapse spark clusters have a default limit of 12-2000, depending on your subscription offer type. This limit can be increased by submitting a support ticket and requesting for quota increase under the "Machine Learning Service: Spark vCore Quota" category.

:::image type="content" source="./media/how-to-manage-quotas/spark-vcore-quota-increase.png" alt-text="Screenshot of the quota increase form with the Spark vCore Quota category selected.":::

### Virtual machines
Each Azure subscription has a limit on the number of virtual machines across all services. Virtual machine cores have a regional total limit and a regional limit per size series. Both limits are separately enforced.

For example, consider a subscription with a US East total VM core limit of 30, an A series core limit of 30, and a D series core limit of 30. This subscription would be allowed to deploy 30 A1 VMs, or 30 D1 VMs, or a combination of the two that doesn't exceed a total of 30 cores.

You can't raise limits for virtual machines above the values shown in the following table.

[!INCLUDE [azure-subscription-limits-azure-resource-manager](../../includes/azure-subscription-limits-azure-resource-manager.md)]

### Container Instances

For more information, see [Container Instances limits](../azure-resource-manager/management/azure-subscription-service-limits.md#container-instances-limits).

### Storage
Azure Storage has a limit of 250 storage accounts per region, per subscription. This limit includes both Standard and Premium storage accounts.

To increase the limit, make a request through [Azure Support](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest/). The Azure Storage team will review your case and can approve up to 250 storage accounts for a region.


## Workspace-level quotas

Use workspace-level quotas to manage Azure Machine Learning compute target allocation between multiple [workspaces](concept-workspace.md) in the same subscription.

By default, all workspaces share the same quota as the subscription-level quota for VM families. However, you can set a maximum quota for individual VM families on workspaces in a subscription. This lets you share capacity and avoid resource contention issues.

1. Go to any workspace in your subscription.
1. In the left pane, select **Usages + quotas**.
1. Select the **Configure quotas** tab to view the quotas.
1. Expand a VM family.
1. Set a quota limit on any workspace listed under that VM family.

You can't set a negative value or a value higher than the subscription-level quota.

[![Screenshot that shows an Azure Machine Learning workspace-level quota.](./media/how-to-manage-quotas/azure-machine-learning-workspace-quota.png)](./media/how-to-manage-quotas/azure-machine-learning-workspace-quota.png)

> [!NOTE]
> You need subscription-level permissions to set a quota at the workspace level.

## View quotas in the studio

1. When you create a new compute resource, by default you'll see only VM sizes that you already have quota to use.  Switch the view to **Select from all options**.  

    :::image type="content" source="media/how-to-manage-quotas/select-all-options.png" alt-text="Screenshot shows select all options to see compute resources that need more quota":::

1. Scroll down until you see the list of VM sizes you don't have quota for.

    :::image type="content" source="media/how-to-manage-quotas/scroll-to-zero-quota.png" alt-text="Screenshot shows list of zero quota":::

1. Use the link to go directly to the online customer support request for more quota.

## View your usage and quotas in the Azure portal

To view your quota for various Azure resources like virtual machines, storage, or network, use the [Azure portal](https://portal.azure.com):
