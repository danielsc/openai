The reason you might run into this error when creating/updating a Kubernetes online endpoint/deployment is because the [Azureml-fe](how-to-kubernetes-inference-routing-azureml-fe.md) that is the system service running in the cluster is not found or unhealthy.

To trouble shoot this issue, you can re-install or update the Azure Machine Learning extension in your cluster.

### ERROR: ACRSecretError 

Below is a list of reasons you might run into this error when creating/updating the Kubernetes online deployments:

* Role assignment has not yet been completed. In this case, please wait for a few seconds and try again later. 
* The Azure ARC (For Azure Arc Kubernetes cluster) or Azure Machine Learning extension (For AKS) is not properly installed or configured. Please try to check the Azure ARC or Azure Machine Learning extension configuration and status. 
* The Kubernetes cluster has improper network configuration, please check the proxy, network policy or certificate.
  * If you are using a private AKS cluster, it is necessary to set up private endpoints for ACR, storage account, workspace in the AKS vnet. 

### ERROR: EndpointNotFound

The reason you might run into this error when creating/updating Kubernetes online deployments is because the system can't find the endpoint resource for the deployment in the cluster. You should create the deployment in an exist endpoint or create this endpoint first in your cluster.

### ERROR: ValidateScoringFailed

The reason you might run into this error when creating/updating Kubernetes online deployments is because the scoring request URL validation failed when processing the model deploying. 

In this case, you can first check the endpoint URL and then try to re-deploy the deployment.

### ERROR: InvalidDeploymentSpec

The reason you might run into this error when creating/updating Kubernetes online deployments is because the deployment spec is invalid.

In this case, you can check the error message.
* Make sure the `instance count` is valid.
* If you have enabled auto scaling, make sure the `minimum instance count` and `maximum instance count` are both valid.

### ERROR: ImagePullLoopBackOff

The reason you might run into this error when creating/updating Kubernetes online deployments is because the images can't be downloaded from the container registry, resulting in the images pull failure. 

In this case, you can check the cluster network policy and the workspace container registry if cluster can pull image from the container registry.

### ERROR: KubernetesCrashLoopBackOff

Below is a list of reasons you might run into this error when creating/updating the Kubernetes online endpoints/deployments:
* One or more pod(s) stuck in CrashLoopBackoff status, you can check if the deployment log exists, and check if there are error messages in the log.
* There is an error in `score.py` and the container crashed when init your score code, please following [ERROR: ResourceNotReady](#error-resourcenotready) part. 
* Your scoring process needs more memory that your deployment config limit is insufficient, you can try to update the deployment with a larger memory limit. 

### ERROR: PodUnschedulable

Below is a list of reasons you might run into this error when creating/updating the Kubernetes online endpoints/deployments:
* Unable to schedule pod to nodes, due to insufficient resources in your cluster.
* No node match node affinity/selector.

To mitigate this error, refer to the following steps: 
* Check the `node selector` definition of the `instance type` you used, and `node label` configuration of your cluster nodes. 
* Check `instance type` and the node SKU size for AKS cluster or the node resource for Arc-Kubernetes cluster.
  * If the cluster is under-resourced, you can reduce the instance type resource requirement or use another instance type with smaller resource required. 
* If the cluster has no more resource to meet the requirement of the deployment, delete some deployment to release resources.
