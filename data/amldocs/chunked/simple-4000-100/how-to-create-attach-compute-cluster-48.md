* Azure Machine Learning Compute has default limits, such as the number of cores that can be allocated. For more information, see [Manage and request quotas for Azure resources](how-to-manage-quotas.md).

* Azure allows you to place _locks_ on resources, so that they can't be deleted or are read only. __Do not apply resource locks to the resource group that contains your workspace__. Applying a lock to the resource group that contains your workspace will prevent scaling operations for Azure ML compute clusters. For more information on locking resources, see [Lock resources to prevent unexpected changes](../azure-resource-manager/management/lock-resources.md).

## Create

**Time estimate**: Approximately 5 minutes.

Azure Machine Learning Compute can be reused across runs. The compute can be shared with other users in the workspace and is retained between runs, automatically scaling nodes up or down based on the number of runs submitted, and the max_nodes set on your cluster. The min_nodes setting controls the minimum nodes available.

The dedicated cores per region per VM family quota and total regional quota, which applies to compute cluster creation, is unified and shared with Azure Machine Learning training compute instance quota. 

[!INCLUDE [min-nodes-note](../../includes/machine-learning-min-nodes.md)]

The compute autoscales down to zero nodes when it isn't used.   Dedicated VMs are created to run your jobs as needed.

The fastest way to create a compute cluster is to follow the [Quickstart: Create workspace resources you need to get started with Azure Machine Learning](quickstart-create-resources.md). 

Or use the following examples to create a compute cluster with more options:
    
# [Python SDK](#tab/python)

To create a persistent Azure Machine Learning Compute resource in Python, specify the **size** and **max_instances** properties. Azure Machine Learning then uses smart defaults for the other properties.
    
* *size**: The VM family of the nodes created by Azure Machine Learning Compute.
* **max_instances*: The max number of nodes to autoscale up to when you run a job on Azure Machine Learning Compute.

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.entities import AmlCompute

cluster_basic = AmlCompute(
    name="basic-example",
    type="amlcompute",
    size="STANDARD_DS3_v2",
    location="westus",
    min_instances=0,
    max_instances=2,
    idle_time_before_scale_down=120,
)
ml_client.begin_create_or_update(cluster_basic).result()
```

You can also configure several advanced properties when you create Azure Machine Learning Compute. The properties allow you to create a persistent cluster of fixed size, or within an existing Azure Virtual Network in your subscription.  See the [AmlCompute class](/python/api/azure-ai-ml/azure.ai.ml.entities.amlcompute) for details.

> [!WARNING]
> When setting the `location` parameter, if it is a different region than your workspace or datastores you may see increased network latency and data transfer costs. The latency and costs can occur when creating the cluster, and when running jobs on it.

# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```azurecli
az ml compute create -f create-cluster.yml
```

Where the file *create-cluster.yml* is:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: location-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
location: westus

```


> [!WARNING]
> When using a compute cluster in a different region than your workspace or datastores, you may see increased network latency and data transfer costs. The latency and costs can occur when creating the cluster, and when running jobs on it.


# [Studio](#tab/azure-studio)

Create a single- or multi- node compute cluster for your training, batch inferencing or reinforcement learning workloads. 

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com).
