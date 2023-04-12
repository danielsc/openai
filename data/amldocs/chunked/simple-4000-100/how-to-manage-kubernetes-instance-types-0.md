
# Create and manage instance types for efficient compute resource utilization

## What are instance types?

Instance types are an Azure Machine Learning concept that allows targeting certain types of compute nodes for training and inference workloads.  For an Azure VM, an example for an instance type is `STANDARD_D2_V3`.

In Kubernetes clusters, instance types are represented in a custom resource definition (CRD) that is installed with the AzureML extension. Instance types are represented by two elements in AzureML extension: 
[nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector)
and [resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).

In short, a `nodeSelector` lets you specify which node a pod should run on.  The node must have a corresponding label.  In the `resources` section, you can set the compute resources (CPU, memory and NVIDIA GPU) for the pod.

>[!IMPORTANT]
> 
> If you have [specified a nodeSelector when deploying the AzureML extension](./how-to-deploy-kubernetes-extension.md#review-azureml-extension-configuration-settings), the nodeSelector will be applied to all instance types.  This means that:
> - For each instance type creating, the specified nodeSelector should be a subset of the extension-specified nodeSelector. 
> - If you use an instance type **with nodeSelector**, the workload will run on any node matching both the extension-specified nodeSelector and the instance type-specified nodeSelector.
> - If you use an instance type **without a nodeSelector**, the workload will run on any node mathcing the extension-specified nodeSelector.


## Default instance type

By default, a `defaultinstancetype` with the following definition is created when you attach a Kubernetes cluster to an AzureML workspace:
- No `nodeSelector` is applied, meaning the pod can get scheduled on any node.
- The workload's pods are assigned default resources with 0.1 cpu cores, 500Mi memory and 0 GPU for request.
- Resource use by the workload's pods is limited to 2 cpu cores and 8 GB memory:

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "500MB"
  limits:
    cpu: "2"
    memory: "8Gi"
    nvidia.com/gpu: null
```

> [!NOTE] 
> - The default instance type purposefully uses little resources.  To ensure all ML workloads run with appropriate resources, for example GPU resource, it is highly recommended to create custom instance types.
> - `defaultinstancetype` will not appear as an InstanceType custom resource in the cluster when running the command ```kubectl get instancetype```, but it will appear in all clients (UI, CLI, SDK).
> - `defaultinstancetype` can be overridden with a custom instance type definition having the same name as `defaultinstancetype` (see [Create custom instance types](#create-custom-instance-types) section)

### Create custom instance types

To create a new instance type, create a new custom resource for the instance type CRD.  For example:

```bash
kubectl apply -f my_instance_type.yaml
```

With `my_instance_type.yaml`:
```yaml
apiVersion: amlarc.azureml.com/v1alpha1
kind: InstanceType
metadata:
  name: myinstancetypename
spec:
  nodeSelector:
    mylabel: mylabelvalue
  resources:
    limits:
      cpu: "1"
      nvidia.com/gpu: 1
      memory: "2Gi"
    requests:
      cpu: "700m"
      memory: "1500Mi"
```

The following steps will create an instance type with the labeled behavior:
- Pods will be scheduled only on nodes with label `mylabel: mylabelvalue`.
- Pods will be assigned resource requests of `700m` CPU and `1500Mi` memory.
- Pods will be assigned resource limits of `1` CPU, `2Gi` memory and `1` NVIDIA GPU.

Creation of custom instance types must meet the following parameters and definition rules, otherwise the instance type creation will fail:

| Parameter | Required | Description |
| --- | --- | --- |
| name | required | String values, which must be unique in cluster.|
| CPU request | required | String values, which cannot be 0 or empty. <br>CPU can be specified in millicores; for example, `100m`. Can also be specified as full numbers; for example, `"1"` is equivalent to `1000m`.|
