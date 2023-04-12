One of the key methods of optimizing cost and performance is by parallelizing the workload with the help of a parallel run step in Azure Machine Learning. This step allows you to use many smaller nodes to execute the task in parallel, hence allowing you to scale horizontally. There is an overhead for parallelization. Depending on the workload and the degree of parallelism that can be achieved, this may or may not be an option. For further information, see the [ParallelRunStep](xref:azureml.contrib.pipeline.steps.ParallelRunStep) documentation.

## Set data retention & deletion policies

Every time a pipeline is executed, intermediate datasets are generated at each step. Over time, these intermediate datasets take up space in your storage account. Consider setting up policies to manage your data throughout its lifecycle to archive and delete your datasets. For more information, see [optimize costs by automating Azure Blob Storage access tiers](../storage/blobs/lifecycle-management-overview.md).

## Deploy resources to the same region

Computes located in different regions may experience network latency and increased data transfer costs. Azure network costs are incurred from outbound bandwidth from Azure data centers. To help reduce network costs, deploy all your resources in the region. Provisioning your Azure Machine Learning workspace and dependent resources in the same region as your data can help lower cost and improve performance.

For hybrid cloud scenarios like those using ExpressRoute, it can sometimes be more cost effective to move all resources to Azure to optimize network costs and latency.

## Next steps

- [Plan to manage costs for Azure Machine Learning](concept-plan-manage-cost.md)
- [Manage budgets, costs, and quota for Azure Machine Learning at organizational scale](/azure/cloud-adoption-framework/ready/azure-best-practices/optimize-ai-machine-learning-cost)
