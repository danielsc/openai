| amlarc resource group| 	ml.azure.com/resource-group | \<resource group name> | `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| Only machine learning workload pods created from the specific resource group would tolerate this `amlarc resource group` taint.|
| amlarc workspace | 	ml.azure.com/workspace |	\<workspace name>	| `NoSchddule`, `NoExecute`  or `PreferNoSchedule`|Only machine learning workload pods created from the specific workspace would tolerate this `amlarc workspace` taint. |
| amlarc compute| 	ml.azure.com/compute| \<compute name>	| `NoSchddule`, `NoExecute`  or `PreferNoSchedule`| Only machine learning workload pods created with the specific compute target would tolerate this `amlarc compute` taint.|

> [!TIP]
> 1. For Azure Kubernetes Service(AKS), you can follow the example in [Best practices for advanced scheduler features in Azure Kubernetes Service (AKS)](../aks/operator-best-practices-advanced-scheduler.md#provide-dedicated-nodes-using-taints-and-tolerations) to apply taints to node pools.
> 1. For Arc Kubernetes clusters, such as on premises Kubernetes clusters, you can use `kubectl taint` command to add taints to nodes. For more examples,see the [Kubernetes Documentation](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

### Best practices

According to your scheduling requirements of the Azureml-dedicated nodes, you can add **multiple amlarc-specific taints** to restrict what Azureml workloads can run on nodes. We list best practices for using amlarc taints:

- **To prevent non-azureml workloads from running on azureml-dedicated nodes/node pools**, you can just add the `aml overall` taint to these nodes.
- **To prevent non-system pods from running on azureml-dedicated nodes/node pools**, you have to add the following taints: 
  - `amlarc overall` taint
  - `amlarc system` taint
- **To prevent non-ml workloads from running on azureml-dedicated nodes/node pools**, you have to add the following taints: 
  - `amlarc overall` taint
  - `amlarc workloads` taint
- **To prevent workloads not created from *workspace X* from running on azureml-dedicated nodes/node pools**, you have to add the following taints: 
  - `amlarc overall` taint
  - `amlarc resource group (has this <workspace X>)` taint 
  - `amlarc <workspace X>` taint
- **To prevent workloads not created by *compute target X* from running on azureml-dedicated nodes/node pools**, you have to add the following taints: 
  - `amlarc overall` taint
  - `amlarc resource group (has this <workspace X>)` taint 
  - `amlarc workspace (has this <compute X>)` taint
  - `amlarc <compute X>` taint

  
## Integrate other load balancers with AzureML extension over HTTP or HTTPS

In addition to the default AzureML inference load balancer [azureml-fe](../machine-learning/how-to-kubernetes-inference-routing-azureml-fe.md), you can also integrate other load balancers with AzureML extension over HTTP or HTTPS. 

This tutorial helps illustrate how to integrate the [Nginx Ingress Controller](https://github.com/kubernetes/ingress-nginx) or the [Azure Application Gateway](../application-gateway/overview.md).

### Prerequisites

- [Deploy the AzureML extension](../machine-learning/how-to-deploy-kubernetes-extension.md) with `inferenceRouterServiceType=ClusterIP` and `allowInsecureConnections=True`, so that the Nginx Ingress Controller can handle TLS termination by itself instead of handing it over to [azureml-fe](../machine-learning/how-to-kubernetes-inference-routing-azureml-fe.md) when service is exposed over HTTPS.
- For integrating with **Nginx Ingress Controller**, you will need a Kubernetes cluster setup with Nginx Ingress Controller.
  - [**Create a basic controller**](../aks/ingress-basic.md): If you are starting from scratch, refer to these instructions.
- For integrating with **Azure Application Gateway**, you will need a Kubernetes cluster setup with Azure Application Gateway Ingress Controller.
  - [**Greenfield Deployment**](../application-gateway/tutorial-ingress-controller-add-on-new.md): If you are starting from scratch, refer to these instructions.
