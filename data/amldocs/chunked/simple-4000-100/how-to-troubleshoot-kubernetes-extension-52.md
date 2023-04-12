When the installation failed and didn't hit any of the above error messages, you can use the built-in health check job to make a comprehensive check on the extension. Azureml extension contains a `HealthCheck` job to pre-check your cluster readiness when you try to install, update or delete the extension. The HealthCheck job will output a report, which is saved in a configmap named `arcml-healthcheck` in `azureml` namespace. The error codes and possible solutions for the report are listed in [Error Code of HealthCheck](#error-code-of-healthcheck). 

Run this command to get the HealthCheck report,
```bash
kubectl describe configmap -n azureml arcml-healthcheck
```
The health check is triggered whenever you install, update or delete the extension. The health check report is structured with several parts `pre-install`, `pre-rollback`, `pre-upgrade` and `pre-delete`.

- If the extension is installed failed, you should look into `pre-install` and `pre-delete`.
- If the extension is updated failed, you should look into `pre-upgrade` and `pre-rollback`.
- If the extension is deleted failed, you should look into `pre-delete`.

When you request support, we recommend that you run the following command and send the```healthcheck.logs``` file to us, as it can facilitate us to better locate the problem.
```bash
kubectl logs healthcheck -n azureml
```

### Error Code of HealthCheck 
This table shows how to troubleshoot the error codes returned by the HealthCheck report. 

|Error Code |Error Message | Description |
|--|--|--|
|E40001 | LOAD_BALANCER_NOT_SUPPORT | Load balancer isn't supported in your cluster. You need to configure the load balancer in your cluster or consider to  set `inferenceRouterServiceType` to `nodePort` or `clusterIP`. |
|E40002 | INSUFFICIENT_NODE | You have enabled `inferenceRouterHA` that requires at least three nodes in your cluster. Disable the HA if you've fewer than three nodes. |
|E40003 | INTERNAL_LOAD_BALANCER_NOT_SUPPORT | Currently, internal load balancer is only supported by AKS. Don't set  `internalLoadBalancerProvider` if you don't have an AKS cluster.|
|E40007 | INVALID_SSL_SETTING | The SSL key or certificate isn't valid. The CNAME should be compatible with the certificate. |
|E45002 | PROMETHEUS_CONFLICT | The Prometheus Operator installed is conflict with your existing Prometheus Operator. For more information, see [Prometheus operator](#prometheus-operator) |
|E45003 | BAD_NETWORK_CONNECTIVITY | You need to meet [network-requirements](./how-to-access-azureml-behind-firewall.md#scenario-use-kubernetes-compute).|
|E45004 | AZUREML_FE_ROLE_CONFLICT |AzureML extension isn't supported in the [legacy AKS](./how-to-attach-kubernetes-anywhere.md#kubernetescompute-and-legacy-akscompute). To install AzureML extension, you need to [delete the legacy azureml-fe components](v1/how-to-create-attach-kubernetes.md#delete-azureml-fe-related-resources).|
|E45005 | AZUREML_FE_DEPLOYMENT_CONFLICT | AzureML extension isn't supported in the [legacy AKS](./how-to-attach-kubernetes-anywhere.md#kubernetescompute-and-legacy-akscompute). To install AzureML extension, you need to [delete the legacy azureml-fe components](v1/how-to-create-attach-kubernetes.md#delete-azureml-fe-related-resources).|

## Open Source components integration

AzureML extension uses some open source components, including Prometheus Operator, Volcano Scheduler, and DCGM exporter. If the Kubernetes cluster already has some of them installed, you can read following sections to integrate your existing components with AzureML extension.

### Prometheus operator
[Prometheus operator](https://github.com/prometheus-operator/prometheus-operator) is an open source framework to help build metric monitoring system in kubernetes. AzureML extension also utilizes Prometheus operator to help monitor resource utilization of jobs.

If the Prometheus operator has already been installed in cluster by other service, you can specify ```installPromOp=false``` to disable the Prometheus operator in AzureML extension to avoid a conflict between two Prometheus operators.
