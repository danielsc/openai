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
