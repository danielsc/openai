utilization_percentage = (The number of replicas that are busy processing a request + The number of requests queued in azureml-fe) / The total number of current replicas
```
If this number exceeds `target_utilization_percentage`, then more replicas are created. If it's lower, then replicas are reduced. By default, the target utilization is 70%.

Decisions to add replicas are eager and fast (around 1 second). Decisions to remove replicas are conservative (around 1 minute).

For example, if you want to deploy a model service and want to know many instances (pods/replicas) should be configured for target requests per second (RPS) and target response time. You can calculate the required replicas by using the following code:

```python
from math import ceil
# target requests per second
targetRps = 20
# time to process the request (in seconds)
reqTime = 10
# Maximum requests per container
maxReqPerContainer = 1
# target_utilization. 70% in this example
targetUtilization = .7

concurrentRequests = targetRps * reqTime / targetUtilization

# Number of container replicas
replicas = ceil(concurrentRequests / maxReqPerContainer)
```

### Performance of azureml-fe

The `azureml-fe` can reach 5K requests per second (QPS) with good latency, having an overhead not exceeding 3ms on average and 15ms at 99% percentile.


>[!Note]
>
>If you have RPS requirements higher than 10K, consider the following options:
>
>* Increase resource requests/limits for `azureml-fe` pods; by default it has 2 vCPU and 1.2G memory resource limit.
>* Increase the number of instances for `azureml-fe`. By default, AzureML creates 3 or 1 `azureml-fe` instances per cluster.
>   * This instance count depends on your configuration of `inferenceRouterHA` of the [AzureML entension](how-to-deploy-kubernetes-extension.md#review-azureml-extension-configuration-settings).
>   * The increased instance count cannot be persisted, since it will be overwritten with your configured value once the extension is upgraded.
>* Reach out to Microsoft experts for help.

## Understand connectivity requirements for AKS inferencing cluster

AKS cluster is deployed with one of the following two network models:
* Kubenet networking - The network resources are typically created and configured as the AKS cluster is deployed.
* Azure Container Networking Interface (CNI) networking - The AKS cluster is connected to an existing virtual network resource and configurations.

For Kubenet networking, the network is created and configured properly for Azure Machine Learning service. For the CNI networking, you need to understand the connectivity requirements and ensure DNS resolution and outbound connectivity for AKS inferencing. For example, you may be using a firewall to block network traffic.

The following diagram shows the connectivity requirements for AKS inferencing. Black arrows represent actual communication, and blue arrows represent the domain names. You may need to add entries for these hosts to your firewall or to your custom DNS server.

![Diagram of the connectivity requirements for inferencing with Azure Kubernetes Services.](./media/how-to-attach-kubernetes-to-workspace/azureml-kubernetes-network.png)

For general AKS connectivity requirements, see [Control egress traffic for cluster nodes in Azure Kubernetes Service](../aks/limit-egress-traffic.md).

For accessing Azure ML services behind a firewall, see [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).

### Overall DNS resolution requirements

DNS resolution within an existing VNet is under your control. For example, a firewall or custom DNS server. The following hosts must be reachable:

| Host name | Used by |
| ----- | ----- |
| `<cluster>.hcp.<region>.azmk8s.io` | AKS API server |
| `mcr.microsoft.com` | Microsoft Container Registry (MCR) |
| `<ACR name>.azurecr.io` | Your Azure Container Registry (ACR) |
| `<account>.blob.core.windows.net` | Azure Storage Account (blob storage) |
| `api.azureml.ms` | Azure Active Directory (Azure AD) authentication |
