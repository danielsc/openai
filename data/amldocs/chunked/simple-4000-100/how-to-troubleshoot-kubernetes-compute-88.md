There is a compute target validation process when deploying models to your Kubernetes cluster. This error should occur when the compute information is invalid when validating, for example the compute target is not found, or the configuration of Azure Machine Learning extension has been updated in your Kubernetes cluster. 

You can check the following items to troubleshoot the issue:
* Check whether the compute target you used is correct and existing in your workspace.
* Try to detach and reattach the compute to the workspace. Pay attention to more notes on [reattach](#error-genericcomputeerror).

#### ERROR: InvalidComputeNoKubernetesConfiguration

The error message is as follows:

```bash
The compute kubeconfig is invalid.
```

This error should occur when the system failed to find any configuration to connect to cluster, such as:
* For Arc-Kubernetes cluster, there is no Azure Relay configuration can be found.
* For AKS cluster, there is no AKS configuration can be found.

To rebuild the configuration of compute connection in your cluster, you can try to detach and reattach the compute to the workspace. Pay attention to more notes on [reattach](#error-genericcomputeerror).

### Kubernetes cluster error

Below is a list of error types in **cluster scope** that you might encounter when using Kubernetes compute to create online endpoints and online deployments for real-time model inference, which you can trouble shoot by following the guideline:

* [ERROR: GenericClusterError](#error-genericclustererror)
* [ERROR: ClusterNotReachable](#error-clusternotreachable)
* [ERROR: ClusterNotFound](#error-clusternotfound)

#### ERROR: GenericClusterError

The error message is as follows:

```bash
Failed to connect to Kubernetes cluster: <message>
```

This error should occur when the system  failed to connect to the Kubernetes cluster for an unknown reason. You can check the following items to troubleshoot the issue:

For AKS clusters:
* Check if the AKS cluster is shut down. 
    * If the cluster isn't running, you need to start the cluster first.
* Check if the AKS cluster has enabled selected network by using authorized IP ranges. 
    * If the AKS cluster has enabled authorized IP ranges, please make sure all the **AzureML control plane IP ranges** have been enabled for the AKS cluster. More information you can see this [document](how-to-deploy-kubernetes-extension.md#limitations).


For an AKS cluster or an Azure Arc enabled Kubernetes cluster:
* Check if the Kubernetes API server is accessible by running `kubectl` command in cluster. 

#### ERROR: ClusterNotReachable 

The error message is as follows:

```bash
The Kubernetes cluster is not reachable. 
```

This error should occur when the system can't connect to a cluster. You can check the following items to troubleshoot the issue:


For AKS clusters:
* Check if the AKS cluster is shut down. 
    *  If the cluster isn't running, you need to start the cluster first.

For an AKS cluster or an Azure Arc enabled Kubernetes cluster:
* Check if the Kubernetes API server is accessible by running `kubectl` command in cluster. 

#### ERROR: ClusterNotFound

The error message is as follows:

```bash
Cannot found Kubernetes cluster. 
```

This error should occur when the system cannot find the AKS/Arc-Kubernetes cluster.

You can check the following items to troubleshoot the issue:
* First, check the cluster resource ID in the Azure portal to verify whether Kubernetes cluster resource still exists and is running normally.
* If the cluster exists and is running, then you can try to detach and reattach the compute to the workspace. Pay attention to more notes on [reattach](#error-genericcomputeerror).

> [!TIP]
   > More troubleshoot guide of common errors when creating/updating the Kubernetes online endpoints and deployments, you can find in [How to troubleshoot online endpoints](how-to-troubleshoot-online-endpoints.md).


## Training guide

### UserError

#### AzureML Kubernetes job failed. E45004
