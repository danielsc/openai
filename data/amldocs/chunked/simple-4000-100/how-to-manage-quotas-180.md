To view your quota for various Azure resources like virtual machines, storage, or network, use the [Azure portal](https://portal.azure.com):

1. On the left pane, select **All services** and then select **Subscriptions** under the **General** category.

2. From the list of subscriptions, select the subscription whose quota you're looking for.

3. Select **Usage + quotas** to view your current quota limits and usage. Use the filters to select the provider and locations. 

You manage the Azure Machine Learning compute quota on your subscription separately from other Azure quotas: 

1. Go to your **Azure Machine Learning** workspace in the Azure portal.

2. On the left pane, in the **Support + troubleshooting** section, select **Usage + quotas** to view your current quota limits and usage.

3. Select a subscription to view the quota limits. Filter to the region you're interested in.

4. You can switch between a subscription-level view and a workspace-level view.

## Request quota increases

To raise the limit or VM quota above the default limit, [open an online customer support request](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest/) at no charge.

You can't raise limits above the maximum values shown in the preceding tables. If there's no maximum limit, you can't adjust the limit for the resource.

When you're requesting a quota increase, select the service that you have in mind. For example, select Machine Learning Service, Container Instances, or Storage. For Azure Machine Learning endpoint, you can select the **Request Quota** button while viewing the quota in the preceding steps.
 
1. Scroll to **Machine Learning Service: Virtual Machine Quota**.
 
    :::image type="content" source="./media/how-to-manage-quotas/virtual-machine-quota.png" lightbox="./media/how-to-manage-quotas/virtual-machine-quota.png" alt-text="Screenshot of the VM quota details form.":::

2. Under **Additonal Details** specify the request details with the number of additional vCPUs required to run your Machine Learning Endpoint.
 
    :::image type="content" source="./media/how-to-manage-quotas/vm-quota-request-additional-info.png" lightbox="./media/how-to-manage-quotas/vm-quota-request-additional-info.png" alt-text="Screenshot of the VM quota additional details form.":::

> [!NOTE]
> [Free trial subscriptions](https://azure.microsoft.com/offers/ms-azr-0044p) are not eligible for limit or quota increases. If you have a free trial subscription, you can upgrade to a [pay-as-you-go](https://azure.microsoft.com/offers/ms-azr-0003p/) subscription. For more information, see [Upgrade Azure free trial to pay-as-you-go](../cost-management-billing/manage/upgrade-azure-subscription.md) and [Azure free account FAQ](https://azure.microsoft.com/free/free-account-faq).

### Endpoint quota increases

When requesting the quota increase, provide the following information:

1. When opening the support request, select __Machine Learning Service: Endpoint Limits__ as the __Quota type__.
1. On the __Additional details__ tab, select __Enter details__ and then provide the quota you'd like to increase and the new value, the reason for the quota increase request, and __location(s)__ where you need the quota increase. Finally, select __Save and continue__ to continue.

    :::image type="content" source="./media/how-to-manage-quotas/quota-details.png" lightbox="./media/how-to-manage-quotas/quota-details.png" alt-text="Screenshot of the endpoint quota details form.":::

## Next steps

+ [Plan and manage costs for Azure Machine Learning](concept-plan-manage-cost.md)
+ [Service limits in Azure Machine Learning](resource-limits-capacity.md)
+ [Troubleshooting managed online endpoints deployment and scoring](./how-to-troubleshoot-online-endpoints.md)
