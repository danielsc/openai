* [Azure Resource Manager cannot find a required resource](#resource-manager-cannot-find-a-resource)
* [Azure Container Registry is private or otherwise inaccessible](#container-registry-authorization-error)

#### Resource Manager cannot find a resource

This error occurs when Azure Resource Manager can't find a required resource. For example, you'll receive this error if a storage account was referred to but can't be found at the path on which it was specified. Be sure to double check resources that might have been supplied by exact path or the spelling of their names.

For more information, see [Resolve Resource Not Found Errors](../azure-resource-manager/troubleshooting/error-not-found.md).

#### Container registry authorization error

This error occurs when an image belonging to a private or otherwise inaccessible container registry was supplied for deployment. 
At this time, our APIs cannot accept private registry credentials. 

To mitigate this error, either ensure that the container registry is **not private** or follow the following steps:
1. Grant your private registry's `acrPull` role to the system identity of your online endpoint.
1. In your environment definition, specify the address of your private image as well as the additional instruction to not modify (build) the image.

If the mitigation is successful, the image will not require any building and the final image address will simply be the given image address.
At deployment time, your online endpoint's system identity will pull the image from the private registry.

For more diagnostic information, see [How To Use the Workspace Diagnostic API](../machine-learning/how-to-workspace-diagnostic-api.md).

### ERROR: OperationCanceled

Below is a list of reasons you might run into this error when using either managed online endpoint or Kubernetes online endpoint:

* [Operation was canceled by another operation that has a higher priority](#operation-canceled-by-another-higher-priority-operation)
* [Operation was canceled due to a previous operation waiting for lock confirmation](#operation-canceled-waiting-for-lock-confirmation)

#### Operation canceled by another higher priority operation

Azure operations have a certain priority level and are executed from highest to lowest. This error happens when your operation happened to be overridden by another operation that has a higher priority.

Retrying the operation might allow it to be performed without cancellation.

#### Operation canceled waiting for lock confirmation

Azure operations have a brief waiting period after being submitted during which they retrieve a lock to ensure that we don't run into race conditions. This error happens when the operation you submitted is the same as another operation that is currently still waiting for confirmation that it has received the lock to proceed. It may indicate that you've submitted a very similar request too soon after the initial request.

Retrying the operation after waiting several seconds up to a minute may allow it to be performed without cancellation.

### ERROR: NamespaceNotFound

The reason you might run into this error when creating/updating the Kubernetes online endpoints is because the namespace your Kubernetes compute used is unavailable in your cluster. 

You can check the Kubernetes compute in your workspace portal and check the namespace in your Kubernetes cluster. If the namespace is not available, you can detach the legacy compute and re-attach to create a new one, specifying a namespace that already exists in your cluster.    

### ERROR: EndpointAlreadyExists

The reason you might run into this error when creating a Kubernetes online endpoint is because the creating endpoint already exists in your cluster.

The endpoint name should be unique per workspace and per cluster, so in this case, you should create endpoint with another name. 

### ERROR: ScoringFeUnhealthy

The reason you might run into this error when creating/updating a Kubernetes online endpoint/deployment is because the [Azureml-fe](how-to-kubernetes-inference-routing-azureml-fe.md) that is the system service running in the cluster is not found or unhealthy.
