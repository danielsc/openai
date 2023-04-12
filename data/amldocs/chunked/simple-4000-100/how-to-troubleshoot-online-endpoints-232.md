* [Role assignments](#role-assignment-quota)
* [Endpoints](#endpoint-quota)
* [Region-wide VM capacity](#region-wide-vm-capacity)
* [Other](#other-quota)

Additionally,  below is a list of common resources that might run out of quota only for Kubernetes online endpoint: 
* [Kubernetes](#kubernetes-quota)


#### CPU Quota

Before deploying a model, you need to have enough compute quota. This quota defines how much virtual cores are available per subscription, per workspace, per SKU, and per region. Each deployment subtracts from available quota and adds it back after deletion, based on type of the SKU.

A possible mitigation is to check if there are unused deployments that can be deleted. Or you can submit a [request for a quota increase](how-to-manage-quotas.md#request-quota-increases).

#### Disk quota

This issue happens when the size of the model is larger than the available disk space and the model is not able to be downloaded. Try a [SKU](reference-managed-online-endpoints-vm-sku-list.md) with more disk space or reducing the image and model size.

#### Memory quota
This issue happens when the memory footprint of the model is larger than the available memory. Try a [SKU](reference-managed-online-endpoints-vm-sku-list.md) with more memory.

#### Role assignment quota

When you are creating a managed online endpoint, role assignment is required for the [managed identity](../active-directory/managed-identities-azure-resources/overview.md) to access workspace resources. If you've reached the [role assignment limit](../azure-resource-manager/management/azure-subscription-service-limits.md#azure-rbac-limits), try to delete some unused role assignments in this subscription. You can check all role assignments in the Azure portal by navigating to the Access Control menu.

#### Endpoint quota

Try to delete some unused endpoints in this subscription. If all of your endpoints are actively in use, you can try [requesting an endpoint quota increase](how-to-manage-quotas.md#endpoint-quota-increases).

#### Region-wide VM capacity

Due to a lack of Azure Machine Learning capacity in the region, the service has failed to provision the specified VM size. Retry later or try deploying to a different region.

#### Kubernetes quota

This issue happens when the requested CPU, memory could not be provided. At times, nodes may be retained or unavailable, meaning that these nodes are unschedulable. When you are deploying a model to a Kubernetes compute target, Azure Machine Learning will attempt to schedule the service with the requested amount of resources. If there are no nodes available in the cluster with the appropriate amount of resources after 5 minutes, the deployment will fail. To work around this, try to delete some unused endpoints in this subscription. You can also address this error by either adding more nodes, changing the SKU of your nodes, or changing the resource requirements of your service.

The error message will typically indicate which resource you need more of. For instance, if you see an error message detailing `0/3 nodes are available: 3 Insufficient nvidia.com/gpu`, that means that the service requires GPUs and there are three nodes in the cluster that don't have sufficient GPUs. This can be addressed by adding more nodes if you're using a GPU SKU, switching to a GPU-enabled SKU if you aren't, or changing your environment to not require GPUs.

You can also try adjusting your request in the cluster, you can directly [adjust the resource request of the instance type](how-to-manage-kubernetes-instance-types.md).

#### Other quota

To run the `score.py` provided as part of the deployment, Azure creates a container that includes all the resources that the `score.py` needs, and runs the scoring script on that container.

If your container could not start, this means scoring could not happen. It might be that the container is requesting more resources than what `instance_type` can support. If so, consider updating the `instance_type` of the online deployment.
