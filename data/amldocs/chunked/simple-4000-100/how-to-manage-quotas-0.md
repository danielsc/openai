
# Manage and increase quotas for resources with Azure Machine Learning

Azure uses limits and quotas to prevent budget overruns due to fraud, and to honor Azure capacity constraints. Consider these limits as you scale for production workloads. In this article, you learn about:

> [!div class="checklist"]
> + Default limits on Azure resources related to [Azure Machine Learning](overview-what-is-azure-machine-learning.md).
> + Creating workspace-level quotas.
> + Viewing your quotas and limits.
> + Requesting quota increases.

Along with managing quotas, you can learn how to [plan and manage costs for Azure Machine Learning](concept-plan-manage-cost.md) or learn about the [service limits in Azure Machine Learning](resource-limits-capacity.md).

## Special considerations

+ A quota is a credit limit, not a capacity guarantee. If you have large-scale capacity needs, [contact Azure support to increase your quota](#request-quota-increases).

+ A quota is shared across all the services in your subscriptions, including Azure Machine Learning. Calculate usage across all services when you're evaluating capacity.
 
  Azure Machine Learning compute is an exception. It has a separate quota from the core compute quota. 

+ Default limits vary by offer category type, such as free trial, pay-as-you-go, and virtual machine (VM) series (such as Dv2, F, and G).

## Default resource quotas

In this section, you learn about the default and maximum quota limits for the following resources:

+ Azure Machine Learning assets
    + Azure Machine Learning compute
    + Azure Machine Learning managed online endpoints
    + Azure Machine Learning pipelines
+ Virtual machines
+ Azure Container Instances
+ Azure Storage

> [!IMPORTANT]
> Limits are subject to change. For the latest information, see  [Service limits in Azure Machine Learning](resource-limits-capacity.md).



### Azure Machine Learning assets
The following limits on assets apply on a per-workspace basis. 

| **Resource** | **Maximum limit** |
| --- | --- |
| Datasets | 10 million |
| Runs | 10 million |
| Models | 10 million|
| Artifacts | 10 million |

In addition, the maximum **run time** is 30 days and the maximum number of **metrics logged per run** is 1 million.

### Azure Machine Learning Compute
[Azure Machine Learning Compute](concept-compute-target.md#azure-machine-learning-compute-managed) has a default quota limit on both the number of cores (split by each VM Family and cumulative total cores) and the number of unique compute resources allowed per region in a subscription. This quota is separate from the VM core quota listed in the previous section as it applies only to the managed compute resources of Azure Machine Learning.

[Request a quota increase](#request-quota-increases) to raise the limits for various VM family core quotas, total subscription core quotas, cluster quota and resources in this section.

Available resources:
+ **Dedicated cores per region** have a default limit of 24 to 300, depending on your subscription offer type. You can increase the number of dedicated cores per subscription for each VM family. Specialized VM families like NCv2, NCv3, or ND series start with a default of zero cores.  GPUs also default to zero cores.

+ **Low-priority cores per region** have a default limit of 100 to 3,000, depending on your subscription offer type. The number of low-priority cores per subscription can be increased and is a single value across VM families.

+ **Clusters per region** have a default limit of 200. This limit is shared between training clusters, compute instances and MIR endpoint deployments. (A compute instance is considered a single-node cluster for quota purposes.) Cluster quota can be increased up to a value of 500 per region within a given subscription.

> [!TIP]
> To learn more about which VM family to request a quota increase for, check out [virtual machine sizes in Azure](../virtual-machines/sizes.md). For instance GPU VM families start with an "N" in their family name (eg. NCv3 series)
