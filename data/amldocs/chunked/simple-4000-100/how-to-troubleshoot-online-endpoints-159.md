:::image type="content" source="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" lightbox="media/how-to-troubleshoot-online-endpoints/deployment-logs.png" alt-text="A screenshot of observing deployment logs in the studio.":::

The logs are pulled from the inference server. 

To get logs from the storage initializer container, use the Azure CLI or Python SDK (see each tab for details). 


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
