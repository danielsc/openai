---
title: Troubleshooting online endpoints deployment
titleSuffix: Azure Machine Learning
description: Learn how to troubleshoot some common deployment and scoring errors with online endpoints.
services: machine-learning
ms.service: machine-learning
ms.subservice: mlops
author: dem108
ms.author: sehan
ms.reviewer: mopeakande
ms.date: 01/27/2023
ms.topic: troubleshooting
ms.custom: devplatv2, devx-track-azurecli, cliv2, event-tier1-build-2022, sdkv2, ignite-2022
#Customer intent: As a data scientist, I want to figure out why my online endpoint deployment failed so that I can fix it.
---

# Troubleshooting online endpoints deployment and scoring

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]


Learn how to resolve common issues in the deployment and scoring of Azure Machine Learning online endpoints.

This document is structured in the way you should approach troubleshooting:

1. Use [local deployment](#deploy-locally) to test and debug your models locally before deploying in the cloud.
1. Use [container logs](#get-container-logs) to help debug issues.
1. Understand [common deployment errors](#common-deployment-errors) that might arise and how to fix them.

The section [HTTP status codes](#http-status-codes) explains how invocation and prediction errors map to HTTP status codes when scoring endpoints with REST requests.

## Prerequisites

* An **Azure subscription**. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).
* The [Azure CLI](/cli/azure/install-azure-cli).
* For Azure Machine Learning CLI v2, see [Install, set up, and use the CLI (v2)](how-to-configure-cli.md).
* For Azure Machine Learning Python SDK v2, see [Install the Azure Machine Learning SDK v2 for Python](/python/api/overview/azure/ai-ml-readme).

## Deploy locally

Local deployment is deploying a model to a local Docker environment. Local deployment is useful for testing and debugging before deployment to the cloud.

> [!TIP]
> You can also use [Azure Machine Learning inference HTTP server Python package](how-to-inference-server-http.md) to debug your scoring script locally. Debugging with the inference server helps you to debug the scoring script before deploying to local endpoints so that you can debug without being affected by the deployment container configurations.


Local deployment supports creation, update, and deletion of a local endpoint. It also allows you to invoke and get logs from the endpoint. 

## [Azure CLI](#tab/cli)

To use local deployment, add `--local` to the appropriate CLI command:

```azurecli
az ml online-deployment create --endpoint-name <endpoint-name> -n <deployment-name> -f <spec_file.yaml> --local
```

## [Python SDK](#tab/python)

To use local deployment, add  `local=True` parameter in the command:

```python
ml_client.begin_create_or_update(online_deployment, local=True)
```

* `ml_client` is the instance for `MLCLient` class, and `online_deployment` is the instance for either `ManagedOnlineDeployment` class or `KubernetesOnlineDeployment` class.

## [Studio](#tab/studio)

The studio doesn't support local endpoints/deployments. See the Azure CLI or Python tabs for steps to perform deployment locally.

---

As a part of local deployment the following steps take place:

- Docker either builds a new container image or pulls an existing image from the local Docker cache. An existing image is used if there's one that matches the environment part of the specification file.
- Docker starts a new container with mounted local artifacts such as model and code files.

For more, see [Deploy locally in Deploy and score a machine learning model](how-to-deploy-managed-online-endpoint-sdk-v2.md#create-local-endpoint-and-deployment).

> [!TIP]
> Use Visual Studio Code to test and debug your endpoints locally. For more information, see [debug online endpoints locally in Visual Studio Code](how-to-debug-managed-online-endpoints-visual-studio-code.md).

## Conda installation
 
Generally, issues with MLflow deployment stem from issues with the installation of the user environment specified in the `conda.yaml` file. 

To debug conda installation problems, try the following:

1. Check the logs for conda installation. If the container crashed or taking too long to start up, it is likely that conda environment update has failed to resolve correctly.

1. Install the mlflow conda file locally with the command `conda env create -n userenv -f <CONDA_ENV_FILENAME>`. 

1. If there are errors locally, try resolving the conda environment and creating a functional one before redeploying. 

1. If the container crashes even if it resolves locally, the SKU size used for deployment may be too small. 
    1. Conda package installation occurs at runtime, so if the SKU size is too small to accommodate all of the packages detailed in the `conda.yaml` environment file, then the container may crash. 
    1. A Standard_F4s_v2 VM is a good starting SKU size, but larger ones may be needed depending on which dependencies are specified in the conda file.
    1. For Kubernetes online endpoint, the Kubernetes cluster must have minimum of 4 vCPU cores and 8-GB memory.

## Get container logs

You can't get direct access to the VM where the model is deployed. However, you can get logs from some of the containers that are running on the VM. The amount of information you get depends on the provisioning status of the deployment. If the specified container is up and running, you'll see its console output; otherwise, you'll get a message to try again later.

There are two types of containers that you can get the logs from:
- Inference server: Logs include the console log (from [the inference server](how-to-inference-server-http.md)) which contains the output of print/logging functions from your scoring script (`score.py` code). 
- Storage initializer: Logs contain information on whether code and model data were successfully downloaded to the container. The container will run before the inference server container starts to run.

# [Azure CLI](#tab/cli)

To see log output from a container, use the following CLI command:

```azurecli
az ml online-deployment get-logs -e <endpoint-name> -n <deployment-name> -l 100
```

or

```azurecli
az ml online-deployment get-logs --endpoint-name <endpoint-name> --name <deployment-name> --lines 100
```

Add `--resource-group` and `--workspace-name` to the commands above if you have not already set these parameters via `az configure`.

To see information about how to set these parameters, and if current values are already set, run:

```azurecli
az ml online-deployment get-logs -h
```

By default the logs are pulled from the inference server. 

> [!NOTE]
> If you use Python logging, ensure you use the correct logging level order for the messages to be published to logs. For example, INFO.

You can also get logs from the storage initializer container by passing `–-container storage-initializer`. 

Add `--help` and/or `--debug` to commands to see more information. 

# [Python SDK](#tab/python)

To see log output from container, use the `get_logs` method as follows:

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100
)
```

To see information about how to set these parameters, see
[reference for get-logs](/python/api/azure-ai-ml/azure.ai.ml.operations.onlinedeploymentoperations#azure-ai-ml-operations-onlinedeploymentoperations-get-logs)

By default the logs are pulled from the inference server.

> [!NOTE]
> If you use Python logging, ensure you use the correct logging level order for the messages to be published to logs. For example, INFO.

You can also get logs from the storage initializer container by adding `container_type="storage-initializer"` option. 

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100, container_type="storage-initializer"
)
```

# [Studio](#tab/studio)

To see log output from a container, use the **Endpoints** in the studio:

1. In the left navigation bar, select Endpoints.
1. (Optional) Create a filter on compute type to show only managed compute types.
1. Select an endpoint's name to view the endpoint's details page.
1. Select the **Deployment logs** tab in the endpoint's details page.
1. Use the dropdown to select the deployment whose log you want to see.

:::image type="content" source="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" lightbox="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" alt-text="A screenshot of observing deployment logs in the studio.":::

The logs are pulled from the inference server. 

To get logs from the storage initializer container, use the Azure CLI or Python SDK (see each tab for details). 

---

For Kubernetes online endpoint, the administrators are able to directly access the cluster where the model is deployed, which is more flexible for them to check the log in Kubernetes. For example:

```bash
kubectl -n <compute-namespace> logs <container-name>
```

## Request tracing

There are two supported tracing headers:

- `x-request-id` is reserved for server tracing. We override this header to ensure it's a valid GUID.

   > [!Note]
   > When you create a support ticket for a failed request, attach the failed request ID to expedite the investigation.
   
- `x-ms-client-request-id` is available for client tracing scenarios. This header is sanitized to only accept alphanumeric characters, hyphens and underscores, and is truncated to a maximum of 40 characters.

## Common deployment errors

Below is a list of common deployment errors that are reported as part of the deployment operation status.

* [ImageBuildFailure](#error-imagebuildfailure)
* [OutOfQuota](#error-outofquota)
* [BadArgument](#error-badargument)
* [ResourceNotReady](#error-resourcenotready)
* [ResourceNotFound](#error-resourcenotfound)
* [OperationCanceled](#error-operationcanceled)
* [NamespaceNotFound](#error-namespacenotfound)
* [KubernetesCrashLoopBackOff](#error-kubernetescrashloopbackoff)
* [ACRSecretError](#error-acrsecreterror)
* [InferencingClientCallFailed](#error-inferencingclientcallfailed )


### ERROR: ImageBuildFailure

This error is returned when the environment (docker image) is being built. You can check the build log for more information on the failure(s). The build log is located in the default storage for your Azure Machine Learning workspace. The exact location may be returned as part of the error. For example, "The build log is available in the workspace blob store '[storage-account-name]' under the path '/azureml/ImageLogs/your-image-id/build.log'". In this case, "azureml" is the name of the blob container in the storage account.

Below is a list of common image build failure scenarios:

* [Azure Container Registry (ACR) authorization failure](#container-registry-authorization-failure)
* [Generic or unknown failure](#generic-image-build-failure)

#### Container registry authorization failure

If the error message mentions `"container registry authorization failure"` that means the container registry could not be accessed with the current credentials.
This can be caused by desynchronization of a workspace resource's keys and it takes some time to automatically synchronize.
However, you can [manually call for a synchronization of keys](/cli/azure/ml/workspace#az-ml-workspace-sync-keys) which may resolve the authorization failure.

Container registries that are behind a virtual network may also encounter this error if set up incorrectly. You must verify that the virtual network has been set up properly.

#### Generic image build failure

As stated above, you can check the build log for more information on the failure.
If no obvious error is found in the build log and the last line is `Installing pip dependencies: ...working...`, then the error may be caused by a dependency. Pinning version dependencies in your conda file can fix this problem.

We also recommend [deploying locally](#deploy-locally) to test and debug your models locally before deploying to the cloud.

### ERROR: OutOfQuota

Below is a list of common resources that might run out of quota when using Azure services:

* [CPU](#cpu-quota)
* [Disk](#disk-quota)
* [Memory](#memory-quota)
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

To get the exact reason for an error, run: 

#### [Azure CLI](#tab/cli)

```azurecli
az ml online-deployment get-logs -e <endpoint-name> -n <deployment-name> -l 100
```

#### [Python SDK](#tab/python)

```python
ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100
)
```

#### [Studio](#tab/studio)

Use the **Endpoints** in the studio:

1. In the left navigation bar, select **Endpoints**.
1. (Optional) Create a filter on compute type to show only managed compute types.
1. Select an endpoint name to view the endpoint's details page.
1. Select the **Deployment logs** tab in the endpoint's details page.
1. Use the dropdown to select the deployment whose log you want to see.

---

### ERROR: BadArgument

Below is a list of reasons you might run into this error when using either managed online endpoint or Kubernetes online endpoint:

* [Subscription does not exist](#subscription-does-not-exist)
* [Startup task failed due to authorization error](#authorization-error)
* [Startup task failed due to incorrect role assignments on resource](#authorization-error)
* [Unable to download user container image](#unable-to-download-user-container-image)
* [Unable to download user model](#unable-to-download-user-model)


Additionally, below is a list of reasons you might run into this error only when using Kubernetes online endpoint:

* [Resource request was greater than limits](#resource-requests-greater-than-limits)
* [azureml-fe for kubernetes online endpoint is not ready](#azureml-fe-not-ready)


#### Subscription does not exist

The Azure subscription that is entered must be existing. This error occurs when we cannot find the Azure subscription that was referenced. This is likely due to a typo in the subscription ID. Please double-check that the subscription ID was correctly typed and that it is currently active.

For more information about Azure subscriptions, refer to the [prerequisites section](#prerequisites).

#### Authorization error

After you've provisioned the compute resource (while creating a deployment), Azure tries to pull the user container image from the workspace Azure Container Registry (ACR) and mount the user model and code artifacts into the user container from the workspace storage account.

To do these, Azure uses [managed identities](../active-directory/managed-identities-azure-resources/overview.md) to access the storage account and the container registry.

- If you created the associated endpoint with System Assigned Identity, Azure role-based access control (RBAC) permission is automatically granted, and no further permissions are needed.

- If you created the associated endpoint with User Assigned Identity, the user's managed identity must have Storage blob data reader permission on the storage account for the workspace, and AcrPull permission on the Azure Container Registry (ACR) for the workspace. Make sure your User Assigned Identity has the right permission.

For more information, please see [Container Registry Authorication Error](#container-registry-authorization-error).

#### Unable to download user container image

It's possible that the user container couldn't be found. Check [container logs](#get-container-logs) to get more details.

Make sure container image is available in workspace ACR.

For example, if image is `testacr.azurecr.io/azureml/azureml_92a029f831ce58d2ed011c3c42d35acb:latest` check the repository with
`az acr repository show-tags -n testacr --repository azureml/azureml_92a029f831ce58d2ed011c3c42d35acb --orderby time_desc --output table`.

#### Unable to download user model

It is possible that the user's model can't be found. Check [container logs](#get-container-logs) to get more details.

Make sure the model is registered to the same workspace as the deployment. To show details for a model in a workspace: 
  
#### [Azure CLI](#tab/cli)

```azurecli
az ml model show --name <model-name> --version <version>
```

#### [Python SDK](#tab/python)

```python
ml_client.models.get(name="<model-name>", version=<version>)
```

#### [Studio](#tab/studio)

See the **Models** page in the studio:

1. In the left navigation bar, select Models.
1. Select a model's name to view the model's details page.

---

> [!WARNING]
> You must specify either version or label to get the model's information.

You can also check if the blobs are present in the workspace storage account.

- For example, if the blob is `https://foobar.blob.core.windows.net/210212154504-1517266419/WebUpload/210212154504-1517266419/GaussianNB.pkl`, you can use this command to check if it exists:
   
  ```azurecli
  az storage blob exists --account-name foobar --container-name 210212154504-1517266419 --name WebUpload/210212154504-1517266419/GaussianNB.pkl --subscription <sub-name>`
  ```
  
- If the blob is present, you can use this command to obtain the logs from the storage initializer:

  #### [Azure CLI](#tab/cli)

  ```azurecli
  az ml online-deployment get-logs --endpoint-name <endpoint-name> --name <deployment-name> –-container storage-initializer`
  ```

  #### [Python SDK](#tab/python)

  ```python
  ml_client.online_deployments.get_logs(
    name="<deployment-name>", endpoint_name="<endpoint-name>", lines=100, container_type="storage-initializer"
  )
  ```

  #### [Studio](#tab/studio)

  You can't see logs from the storage initializer in the studio. Use the Azure CLI or Python SDK (see each tab for details). 

  ---

#### Resource requests greater than limits

Requests for resources must be less than or equal to limits. If you don't set limits, we set default values when you attach your compute to an Azure Machine Learning workspace. You can check limits in the Azure portal or by using the `az ml compute show` command.

#### azureml-fe not ready
The front-end component (azureml-fe) that routes incoming inference requests to deployed services automatically scales as needed. It's installed during your k8s-extension installation.

This component should be healthy on cluster, at least one healthy replica. You will get this error message if it's not available when you trigger kubernetes online endpoint and deployment creation/update request.

Please check the pod status and logs to fix this issue, you can also try to update the k8s-extension installed on the cluster.


### ERROR: ResourceNotReady

To run the `score.py` provided as part of the deployment, Azure creates a container that includes all the resources that the `score.py` needs, and runs the scoring script on that container. The error in this scenario is that this container is crashing when running, which means scoring can't happen. This error happens when:

- There's an error in `score.py`. Use `get-logs` to help diagnose common problems:
    - A package that was imported but isn't in the conda environment.
    - A syntax error.
    - A failure in the `init()` method.
- If `get-logs` isn't producing any logs, it usually means that the container has failed to start. To debug this issue, try [deploying locally](#deploy-locally) instead.
- Readiness or liveness probes aren't set up correctly.
- There's an error in the environment set up of the container, such as a missing dependency.
- When you face `TypeError: register() takes 3 positional arguments but 4 were given` error, the error may be caused by the dependency between flask v2 and `azureml-inference-server-http`. See [FAQs for inference HTTP server](how-to-inference-server-http.md#1-i-encountered-the-following-error-during-server-startup) for more details.

### ERROR: ResourceNotFound

Below is a list of reasons you might run into this error only when using either managed online endpoint or Kubernetes online endpoint:

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


### ERROR: InferencingClientCallFailed 

The reason you might run into this error when creating/updating Kubernetes online endpoints/deployments is because the k8s-extension of the Kubernetes cluster is not connectable.

In this case, you can detach and then **re-attach** your compute. 

> [!]
>
> To troubleshoot errors by re-attaching, please guarantee to re-attach with the exact same configuration as previously detached compute, such as the same compute name and namespace, otherwise you may encounter other errors.

If it is still not working, please ask the administrator who can access the cluster to use `kubectl get po -n azureml` to check whether the *relay server* pods are running.


### ERROR: InternalServerError

Although we do our best to provide a stable and reliable service, sometimes things don't go according to plan. If you get this error, it means that something isn't right on our side, and we need to fix it. Submit a [customer support ticket](https://portal.azure.com/#blade/Microsoft_Azure_Support/HelpAndSupportBlade/newsupportrequest) with all related information and we'll address the issue. 

## Autoscaling issues

If you're having trouble with autoscaling, see [Troubleshooting Azure autoscale](../azure-monitor/autoscale/autoscale-troubleshoot.md).

For Kubernetes online endpoint, there is **AzureML inference router** which is a front-end component to handle autoscaling for all model deployments on the Kubernetes cluster, you can find more information in [Autoscaling of Kubernetes inference routing](how-to-kubernetes-inference-routing-azureml-fe.md#autoscaling)

## Common model consumption errors

Below is a list of common model consumption errors resulting from the endpoint `invoke` operation status.

* [Bandwidth limit issues](#bandwidth-limit-issues)
* [HTTP status codes](#http-status-codes)
* [Blocked by CORS policy](#blocked-by-cors-policy)

### Bandwidth limit issues

Managed online endpoints have bandwidth limits for each endpoint. You find the limit configuration in [Manage and increase quotas for resources with Azure Machine Learning](how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints). If your bandwidth usage exceeds the limit, your request will be delayed. To monitor the bandwidth delay:

- Use metric “Network bytes” to understand the current bandwidth usage. For more information, see [Monitor managed online endpoints](how-to-monitor-online-endpoints.md).
- There are two response trailers will be returned if the bandwidth limit enforced: 
    - `ms-azureml-bandwidth-request-delay-ms`: delay time in milliseconds it took for the request stream transfer.
    - `ms-azureml-bandwidth-response-delay-ms`: delay time in milliseconds it took for the response stream transfer.

### HTTP status codes

When you access online endpoints with REST requests, the returned status codes adhere to the standards for [HTTP status codes](https://aka.ms/http-status-codes). Below are details about how endpoint invocation and prediction errors map to HTTP status codes.

#### Common error codes for managed online endpoints
Below are common error codes when consuming managed online endpoints with REST requests:

| Status code | Reason phrase             | Why this code might get returned                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 200         | OK                        | Your model executed successfully, within your latency bound.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 401         | Unauthorized              | You don't have permission to do the requested action, such as score, or your token is expired.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 404         | Not found                 | The endpoint doesn't have any valid deployment with positive weight.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 408         | Request timeout           | The model execution took longer than the timeout supplied in `request_timeout_ms` under `request_settings` of your model deployment config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 424         | Model Error               | If your model container returns a non-200 response, Azure returns a 424. Check the `Model Status Code` dimension under the `Requests Per Minute` metric on your endpoint's [Azure Monitor Metric Explorer](../azure-monitor/essentials/metrics-getting-started.md). Or check response headers `ms-azureml-model-error-statuscode` and `ms-azureml-model-error-reason` for more information.                                                                                                                                                                                                                                                                                                                                                          |
| 429         | Too many pending requests | Your model is getting more requests than it can handle. AzureML allows maximum 2 * `max_concurrent_requests_per_instance` * `instance_count` requests in parallel at any time and rejects additional requests. You can confirm these settings in your model deployment config under `request_settings` and `scale_settings`, respectively. If you're using auto-scaling, this error means that your model is getting requests faster than the system can scale up. With auto-scaling, you can try to resend requests with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff). Doing so can give the system time to adjust. Apart from enabling auto-scaling, you could also increase the number of instances by using the [code to calculate instance count](#how-to-calculate-instance-count). |
| 429         | Rate-limiting             | The number of requests per second reached the [limit](./how-to-manage-quotas.md#azure-machine-learning-managed-online-endpoints) of managed online endpoints.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 500         | Internal server error     | Azure ML-provisioned infrastructure is failing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### Common error codes for kubernetes online endpoints

Below are common error codes when consuming Kubernetes online endpoints with REST requests:

| Status code | Reason phrase                                                                 | Why this code might get returned                                                                                                                                                                                                                                                                                                                                                                       |
| ----------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 409         | Conflict error                                                                | When an operation is already in progress, any new operation on that same online endpoint will respond with 409 conflict error. For example, If create or update online endpoint operation is in progress and if you trigger a new Delete operation it will throw an error.                                                                                                                             |
| 502         | Has thrown an exception or crashed in the `run()` method of the score.py file | When there's an error in `score.py`, for example an imported package does not exist in the conda environment, a syntax error, or a failure in the `init()` method. You can follow [here](#error-resourcenotready) to debug the file.                                                                                                                                                                   |
| 503         | Receive large spikes in requests per second                                   | The autoscaler is designed to handle gradual changes in load. If you receive large spikes in requests per second, clients may receive an HTTP status code 503. Even though the autoscaler reacts quickly, it takes AKS a significant amount of time to create more containers. You can follow [here](#how-to-prevent-503-status-codes) to prevent 503 status codes.                                    |
| 504         | Request has timed out                                                         | A 504 status code indicates that the request has timed out. The default timeout setting is 5 seconds. You can increase the timeout or try to speed up the endpoint by modifying the score.py to remove unnecessary calls. If these actions don't correct the problem, you can follow [here](#error-resourcenotready) to debug the score.py file. The code may be in a non-responsive state or an infinite loop. |
| 500         | Internal server error                                                         | Azure ML-provisioned infrastructure is failing.                                                                                                                                                                                                                                                                                                                                                        |


### How to prevent 503 status codes
Kubernetes online deployments support autoscaling, which allows replicas to be added to support extra load, more information you can find in [AzureML inference router](how-to-kubernetes-inference-routing-azureml-fe.md). Decisions to scale up/down is based off of utilization of the current container replicas.

There are two things that can help prevent 503 status codes:
> [!TIP]
> These two approaches can be used individually or in combination.

* Change the utilization level at which autoscaling creates new replicas. You can adjust the utilization target by setting the `autoscale_target_utilization` to a lower value.

    > [!IMPORTANT]
    > This change does not cause replicas to be created *faster*. Instead, they are created at a lower utilization threshold. Instead of waiting until the service is 70% utilized, changing the value to 30% causes replicas to be created when 30% utilization occurs.
    
    If the Kubernetes online endpoint is already using the current max replicas and you're still seeing 503 status codes, increase the `autoscale_max_replicas` value to increase the maximum number of replicas.

* Change the minimum number of replicas. Increasing the minimum replicas provides a larger pool to handle the incoming spikes.

    To increase the number of instances, you could calculate the required replicas following below code.

    ```python
    from math import ceil
    # target requests per second
    target_rps = 20
    # time to process the request (in seconds, choose appropriate percentile)
    request_process_time = 10
    # Maximum concurrent requests per instance
    max_concurrent_requests_per_instance = 1
    # The target CPU usage of the model container. 70% in this example
    target_utilization = .7
    
    concurrent_requests = target_rps * request_process_time / target_utilization
    
    # Number of instance count
    instance_count = ceil(concurrent_requests / max_concurrent_requests_per_instance)
    ```

    > [!NOTE]
    > If you receive request spikes larger than the new minimum replicas can handle, you may receive 503 again. For example, as traffic to your endpoint increases, you may need to increase the minimum replicas.

#### How to calculate instance count
To increase the number of instances, you can calculate the required replicas by using the following code:
```python
from math import ceil
# target requests per second
target_rps = 20
# time to process the request (in seconds, choose appropriate percentile)
request_process_time = 10
# Maximum concurrent requests per instance
max_concurrent_requests_per_instance = 1
# The target CPU usage of the model container. 70% in this example
target_utilization = .7

concurrent_requests = target_rps * request_process_time / target_utilization

# Number of instance count
instance_count = ceil(concurrent_requests / max_concurrent_requests_per_instance)
```

### Blocked by CORS policy

Online endpoints (v2) currently do not support [Cross-Origin Resource Sharing](https://developer.mozilla.org/docs/Web/HTTP/CORS) (CORS) natively. If your web application tries to invoke the endpoint without proper handling of the CORS preflight requests, you'll see the following error message: 

```
Access to fetch at 'https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score' from origin http://{your-url} has been blocked by CORS policy: Response to preflight request doesn't pass access control check. No 'Access-control-allow-origin' header is present on the request resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with the CORS disabled.
```
We recommend that you use Azure Functions, Azure Application Gateway, or any service as an interim layer to handle CORS preflight requests.

## Common network isolation issues

[!INCLUDE [network isolation issues](../../includes/machine-learning-online-endpoint-troubleshooting.md)]

## Troubleshoot inference server
In this section, we'll provide basic troubleshooting tips for [Azure Machine Learning inference HTTP server](how-to-inference-server-http.md). 

[!INCLUDE [inference server TSGs](../../includes/machine-learning-inference-server-troubleshooting.md)]

## Next steps

- [Deploy and score a machine learning model by using an online endpoint](how-to-deploy-online-endpoints.md)
- [Safe rollout for online endpoints](how-to-safely-rollout-online-endpoints.md)
- [Online endpoint YAML reference](reference-yaml-endpoint-online.md)
- [Troubleshoot kubernetes compute ](how-to-troubleshoot-kubernetes-compute.md)
