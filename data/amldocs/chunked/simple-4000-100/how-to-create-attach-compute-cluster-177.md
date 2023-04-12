You may also choose to use [low-priority VMs](how-to-manage-optimize-cost.md#low-pri-vm) to run some or all of your workloads. These VMs don't have guaranteed availability and may be preempted while in use. You'll have to restart a preempted job. 

Using Azure Low Priority Virtual Machines allows you to take advantage of Azure's unused capacity at a significant cost savings. At any point in time when Azure needs the capacity back, the Azure infrastructure will evict Azure Low Priority Virtual Machines. Therefore, Azure Low Priority Virtual Machines are great for workloads that can handle interruptions. The amount of available capacity can vary based on size, region, time of day, and more. When deploying Azure Low Priority Virtual Machines, Azure will allocate the VMs if there's capacity available, but there's no SLA for these VMs. An Azure Low Priority Virtual Machine offers no high availability guarantees. At any point in time when Azure needs the capacity back, the Azure infrastructure will evict Azure Low Priority Virtual Machines 

Use any of these ways to specify a low-priority VM:
    
# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.entities import AmlCompute

cluster_low_pri = AmlCompute(
    name="low-pri-example",
    size="STANDARD_DS3_v2",
    min_instances=0,
    max_instances=2,
    idle_time_before_scale_down=120,
    tier="low_priority",
)
ml_client.begin_create_or_update(cluster_low_pri).result()
```
    
# [Azure CLI](#tab/azure-cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Set the `vm-priority`:
    
```azurecli
az ml compute create -f create-cluster.yml
```

Where the file *create-cluster.yml* is:

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: low-pri-example
type: amlcompute
size: STANDARD_DS3_v2
min_instances: 0
max_instances: 2
idle_time_before_scale_down: 120
tier: low_priority

```

# [Studio](#tab/azure-studio)

In the studio, choose **Low Priority** when you create a VM.


## Set up managed identity

For information on how to configure a managed identity with your compute cluster, see [Set up authentication between Azure Machine Learning and other services](how-to-identity-based-service-authentication.md#compute-cluster).

## Troubleshooting

There's a chance that some users who created their Azure Machine Learning workspace from the Azure portal before the GA release might not be able to create AmlCompute in that workspace. You can either raise a support request against the service or create a new workspace through the portal or the SDK to unblock yourself immediately.

### Stuck at resizing

If your Azure Machine Learning compute cluster appears stuck at resizing (0 -> 0) for the node state, this may be caused by Azure resource locks.

[!INCLUDE [resource locks](../../includes/machine-learning-resource-lock.md)]

## Next steps

Use your compute cluster to:

* [Submit a training run](./how-to-train-model.md) 
* [Run batch inference](./tutorial-pipeline-batch-scoring-classification.md).
