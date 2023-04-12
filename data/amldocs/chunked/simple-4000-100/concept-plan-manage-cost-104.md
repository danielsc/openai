:::image type="content" source="media/concept-plan-manage-cost/create-resource.png" alt-text="Example showing estimated costs while creating a compute instance." lightbox="media/concept-plan-manage-cost/create-resource.png" :::

If your Azure subscription has a spending limit, Azure prevents you from spending over your credit amount. As you create and use Azure resources, your credits are used. When you reach your credit limit, the resources that you deployed are disabled for the rest of that billing period. You can't change your credit limit, but you can remove it. For more information about spending limits, see [Azure spending limit](../cost-management-billing/manage/spending-limit.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).

## Monitor costs

As you use Azure resources with Azure Machine Learning, you incur costs. Azure resource usage unit costs vary by time intervals (seconds, minutes, hours, and days) or by unit usage (bytes, megabytes, and so on.) As soon as Azure Machine Learning use starts, costs are incurred and you can see the costs in [cost analysis](../cost-management-billing/costs/quick-acm-cost-analysis.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).

When you use cost analysis, you view Azure Machine Learning costs in graphs and tables for different time intervals. Some examples are by day, current and prior month, and year. You also view costs against budgets and forecasted costs. Switching to longer views over time can help you identify spending trends. And you see where overspending might have occurred. If you've created budgets, you can also easily see where they're exceeded.

To view Azure Machine Learning costs in cost analysis:

1. Sign in to the Azure portal.
2. Open the scope in the Azure portal and select **Cost analysis** in the menu. For example, go to **Subscriptions**, select a subscription from the list, and then select  **Cost analysis** in the menu. Select **Scope** to switch to a different scope in cost analysis.
3. By default, cost for services are shown in the first donut chart. Select the area in the chart labeled Azure Machine Learning.

Actual monthly costs are shown when you initially open cost analysis. Here's an example showing all monthly usage costs.

:::image type="content" source="media/concept-plan-manage-cost/all-costs.png" alt-text="Example showing accumulated costs for a subscription." lightbox="media/concept-plan-manage-cost/all-costs.png" :::


To narrow costs for a single service, like Azure Machine Learning, select **Add filter** and then select **Service name**. Then, select **virtual machines**.

Here's an example showing costs for just Azure Machine Learning.

:::image type="content" source="media/concept-plan-manage-cost/vm-specific-cost.png" alt-text="Example showing accumulated costs for ServiceName." lightbox="media/concept-plan-manage-cost/vm-specific-cost.png" :::

<!-- Note to Azure service writer: The image shows an example for Azure Storage. Replace the example image with one that shows costs for your service. -->

In the preceding example, you see the current cost for the service. Costs by Azure regions (locations) and Azure Machine Learning costs by resource group are also shown. From here, you can explore costs on your own.
## Create budgets

You can create [budgets](../cost-management-billing/costs/tutorial-acm-create-budgets.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn) to manage costs and create [alerts](../cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn) that automatically notify stakeholders of spending anomalies and overspending risks. Alerts are based on spending compared to budget and cost thresholds. Budgets and alerts are created for Azure subscriptions and resource groups, so they're useful as part of an overall cost monitoring strategy. 

Budgets can be created with filters for specific resources or services in Azure if you want more granularity present in your monitoring. Filters help ensure that you don't accidentally create new resources that cost you additional money. For more about the filter options when you when create a budget, see [Group and filter options](../cost-management-billing/costs/group-filter.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).
