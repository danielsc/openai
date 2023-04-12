
# Plan to manage costs for Azure Machine Learning

This article describes how to plan and manage costs for Azure Machine Learning. First, you use the Azure pricing calculator to help plan for costs before you add any resources. Next, as you add the Azure resources, review the estimated costs. 

After you've started using Azure Machine Learning resources, use the cost management features to set budgets and monitor costs. Also review the forecasted costs and identify spending trends to identify areas where you might want to act.

Understand that the costs for Azure Machine Learning are only a portion of the monthly costs in your Azure bill. If you are using other Azure services, you're billed for all the Azure services and resources used in your Azure subscription, including the third-party services. This article explains how to plan for and manage costs for Azure Machine Learning. After you're familiar with managing costs for Azure Machine Learning, apply similar methods to manage costs for all the Azure services used in your subscription.

For more information on optimizing costs, see [how to manage and optimize cost in Azure Machine Learning](how-to-manage-optimize-cost.md).

## Prerequisites

Cost analysis in Cost Management supports most Azure account types, but not all of them. To view the full list of supported account types, see [Understand Cost Management data](../cost-management-billing/costs/understand-cost-mgt-data.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn). 

To view cost data, you need at least read access for an Azure account. For information about assigning access to Azure Cost Management data, see [Assign access to data](../cost-management-billing/costs/assign-access-acm-data.md?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).

## Estimate costs before using Azure Machine Learning

- Use the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) to estimate costs before you create the resources in an Azure Machine Learning workspace.
On the left, select **AI + Machine Learning**, then select **Azure Machine Learning** to begin.  

The following screenshot shows the cost estimation by using the calculator:

:::image type="content" source="media/concept-plan-manage-cost/capacity-calculator-cost-estimate.png" alt-text="Example showing estimated cost in the Azure Pricing calculator. Prices in this screenshot are examples only; your price may differ.":::

As you add new resources to your workspace, return to this calculator and add the same resource here to update your cost estimates.

For more information, see [Azure Machine Learning pricing](https://azure.microsoft.com/pricing/details/machine-learning?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).

## Understand the full billing model for Azure Machine Learning

Azure Machine Learning runs on Azure infrastructure that accrues costs along with Azure Machine Learning when you deploy the new resource. It's important to understand that additional infrastructure might accrue cost. You need to manage that cost when you make changes to deployed resources. 


### Costs that typically accrue with Azure Machine Learning

When you create resources for an Azure Machine Learning workspace, resources for other Azure services are also created. They are:

* [Azure Container Registry](https://azure.microsoft.com/pricing/details/container-registry?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn) Basic account
* [Azure Block Blob Storage](https://azure.microsoft.com/pricing/details/storage/blobs?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn) (general purpose v1)
* [Key Vault](https://azure.microsoft.com/pricing/details/key-vault?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn)
* [Application Insights](https://azure.microsoft.com/pricing/details/monitor?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn)

When you create a [compute instance](concept-compute-instance.md), the VM stays on so it is available for your work.  
