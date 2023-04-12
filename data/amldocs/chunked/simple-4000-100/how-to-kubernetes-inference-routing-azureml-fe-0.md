
# AzureML inference router and connectivity requirements

AzureML inference router is a critical component for real-time inference with Kubernetes cluster. In this article, you can learn about:

  * What is AzureML inference router
  * How autoscaling works
  * How to configure and meet inference request performance (# of requests per second and latency)
  * Connectivity requirements for AKS inferencing cluster

## What is AzureML inference router

AzureML inference router is the front-end component (`azureml-fe`) which is deployed on AKS or Arc Kubernetes cluster at AzureML extension deployment time. It has following functions:
  
  * Routes incoming inference requests from cluster load balancer or ingress controller to corresponding model pods.
  * Load-balance all incoming inference requests with smart coordinated routing.
  * Manages model pods auto-scaling.
  * Fault-tolerant and failover capability, ensuring inference requests is always served for critical business application.

The following steps are how requests are processed by the front-end:

1. Client sends request to the load balancer.
1. Load balancer sends to one of the front-ends.
1. The front-end locates the service router (the front-end instance acting as coordinator) for the service.
1. The service router selects a back-end and returns it to the front-end.
1. The front-end forwards the request to the back-end.
1. After the request has been processed, the back-end sends a response to the front-end component.
1. The front-end propagates the response back to the client.
1. The front-end informs the service router that the back-end has finished processing and is available for other requests.

The following diagram illustrates this flow:

:::image type="content" source="./media/how-to-attach-kubernetes-to-workspace/request-handling-architecture.png" alt-text="Diagram illustrating the flow of requests between components.":::

As you can see from above diagram, by default 3 `azureml-fe` instances are created during AzureML extension deployment, one instance acts as coordinating role, and the other instances serve incoming inference requests. The coordinating instance has all information about model pods and makes decision about which model pod to serve incoming request, while the serving `azureml-fe` instances are responsible for routing the request to selected model pod and propagate the response back to the original user.

## Autoscaling

AzureML inference router handles autoscaling for all model deployments on the Kubernetes cluster. Since all inference requests go through it, it has the necessary data to automatically scale the deployed model(s).

> [!IMPORTANT]
> * **Do not enable Kubernetes Horizontal Pod Autoscaler (HPA) for model deployments**. Doing so would cause the two auto-scaling components to compete with each other. Azureml-fe is designed to auto-scale models deployed by AzureML, where HPA would have to guess or approximate model utilization from a generic metric like CPU usage or a custom metric configuration.
> 
> * **Azureml-fe does not scale the number of nodes in an AKS cluster**, because this could lead to unexpected cost increases. Instead, **it scales the number of replicas for the model** within the physical cluster boundaries. If you need to scale the number of nodes within the cluster, you can manually scale the cluster or [configure the AKS cluster autoscaler](../aks/cluster-autoscaler.md).

Autoscaling can be controlled by `scale_settings` property in deployment YAML. The following example demonstrates how to enable autoscaling:

```yaml
# deployment yaml
# other properties skipped
scale_setting:
  type: target_utilization
  min_instances: 3
  max_instances: 15
  target_utilization_percentage: 70
  polling_interval: 10
# other deployment properties continue
```

The decision to scale up or down is based off of ``utilization of the current container replicas``. 

```
utilization_percentage = (The number of replicas that are busy processing a request + The number of requests queued in azureml-fe) / The total number of current replicas
