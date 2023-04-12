When you create a [compute instance](concept-compute-instance.md), the VM stays on so it is available for your work.  
* [Enable idle shutdown (preview)](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview) to save on cost when the VM has been idle for a specified time period.
* Or [set up a schedule](how-to-create-manage-compute-instance.md#schedule-automatic-start-and-stop) to automatically start and stop the compute instance (preview) to save cost when you aren't planning to use it.

 
### Costs might accrue before resource deletion

Before you delete an Azure Machine Learning workspace in the Azure portal or with Azure CLI, the following sub resources are common costs that accumulate even when you are not actively working in the workspace. If you are planning on returning to your Azure Machine Learning workspace at a later time, these resources may continue to accrue costs.

* VMs
* Load Balancer
* Virtual Network
* Bandwidth

Each VM is billed per hour it is running. Cost depends on VM specifications. VMs that are running but not actively working on a dataset will still be charged via the load balancer. For each compute instance, one load balancer will be billed per day. Every 50 nodes of a compute cluster will have one standard load balancer billed. Each load balancer is billed around $0.33/day. To avoid load balancer costs on stopped compute instances and compute clusters, delete the compute resource. One virtual network will be billed per subscription and per region. Virtual networks cannot span regions or subscriptions. Setting up private endpoints in vNet setups may also incur charges. Bandwidth is charged by usage; the more data transferred, the more you are charged.

### Costs might accrue after resource deletion

After you delete an Azure Machine Learning workspace in the Azure portal or with Azure CLI, the following resources continue to exist. They continue to accrue costs until you delete them.

* Azure Container Registry
* Azure Block Blob Storage
* Key Vault
* Application Insights

To delete the workspace along with these dependent resources, use the SDK:

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
```python
from azure.ai.ml.entities import Workspace
ml_client.workspaces.begin_delete(name=ws.name, delete_dependent_resources=True)
```

If you create Azure Kubernetes Service (AKS) in your workspace, or if you attach any compute resources to your workspace you must delete them separately in [Azure portal](https://portal.azure.com).

### Using Azure Prepayment credit with Azure Machine Learning

You can pay for Azure Machine Learning charges with your Azure Prepayment credit. However, you can't use Azure Prepayment credit to pay for charges for third party products and services including those from the Azure Marketplace.

## Review estimated costs in the Azure portal

<!-- Note for Azure service writer: If your service shows estimated costs when a user is creating resources in the Azure portal, at a minimum, insert this section as a brief walkthrough that steps through creating a Azure Machine Learning resource where the estimated cost is shown to the user, updated for your service. Add a screenshot where the estimated costs or subscription credits are shown.

If your service doesn't show costs as they create a resource or if estimated costs aren't shown to users before they use your service, then omit this section.

For example, you might start with the following (modify for your service):
-->

As you create compute resources for Azure Machine Learning, you see estimated costs.

To create a *compute instance *and view the estimated price:

1. Sign into the [Azure Machine Learning studio](https://ml.azure.com)
1. On the left side, select **Compute**.
1. On the top toolbar, select **+New**.
1. Review the estimated price shown in for each available virtual machine size.
1. Finish creating the resource.


:::image type="content" source="media/concept-plan-manage-cost/create-resource.png" alt-text="Example showing estimated costs while creating a compute instance." lightbox="media/concept-plan-manage-cost/create-resource.png" :::
