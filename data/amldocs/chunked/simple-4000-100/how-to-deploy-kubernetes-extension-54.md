   |`installPromOp`|`True` or `False`, default `True`. AzureML extension needs prometheus operator to manage prometheus. Set to `False` to reuse the existing prometheus operator. For more information about reusing the existing  prometheus operator, refer to [reusing the prometheus operator](./how-to-troubleshoot-kubernetes-extension.md#prometheus-operator)| Optional| Optional |  Optional |
   |`installVolcano`| `True` or `False`, default `True`. AzureML extension needs volcano scheduler to schedule the job. Set to `False` to reuse existing volcano scheduler. For more information about reusing the existing volcano scheduler, refer to [reusing volcano scheduler](./how-to-troubleshoot-kubernetes-extension.md#volcano-scheduler)   | Optional| N/A |  Optional |
   |`installDcgmExporter`  |`True` or `False`, default `False`. Dcgm-exporter can expose GPU metrics for AzureML workloads, which can be monitored in Azure portal. Set `installDcgmExporter`  to `True` to install dcgm-exporter. But if you want to utilize your own dcgm-exporter, refer to [DCGM exporter](./how-to-troubleshoot-kubernetes-extension.md#dcgm-exporter) |Optional |Optional |Optional |


   |Configuration Protected Setting Key Name  |Description  |Training |Inference |Training and Inference
   |--|--|--|--|--|
   | `sslCertPemFile`, `sslKeyPemFile` |Path to TLS/SSL certificate and key file (PEM-encoded), required for AzureML extension deployment with inference HTTPS endpoint support, when  ``allowInsecureConnections`` is set to False. **Note** PEM file with pass phrase protected isn't supported | N/A| Optional |  Optional |

As you can see from above configuration settings table, the combinations of different configuration settings allow you to deploy AzureML extension for different ML workload scenarios:

  * For training job and batch inference workload, specify `enableTraining=True`
  * For inference workload only, specify `enableInference=True`
  * For all kinds of ML workload, specify both `enableTraining=True` and `enableInference=True`

If you plan to deploy AzureML extension for real-time inference workload and want to specify `enableInference=True`, pay attention to following configuration settings related to real-time inference workload:

  * `azureml-fe` router service is required for real-time inference support and you need to specify `inferenceRouterServiceType` config setting for `azureml-fe`. `azureml-fe` can be deployed with one of following `inferenceRouterServiceType`:
      * Type `LoadBalancer`. Exposes `azureml-fe` externally using a cloud provider's load balancer. To specify this value, ensure that your cluster supports load balancer provisioning. Note most on-premises Kubernetes clusters might not support external load balancer.
      * Type `NodePort`. Exposes `azureml-fe` on each Node's IP at a static port. You'll be able to contact `azureml-fe`, from outside of cluster, by requesting `<NodeIP>:<NodePort>`. Using `NodePort` also allows you to set up your own load balancing solution and TLS/SSL termination for `azureml-fe`.
      * Type `ClusterIP`. Exposes `azureml-fe` on a cluster-internal IP, and it makes `azureml-fe` only reachable from within the cluster. For `azureml-fe` to serve inference requests coming outside of cluster, it requires you to set up your own load balancing solution and TLS/SSL termination for `azureml-fe`. 
   * To ensure high availability of `azureml-fe` routing service, AzureML extension deployment by default creates three replicas of `azureml-fe` for clusters having three nodes or more. If your cluster has **less than 3 nodes**, set `inferenceRouterHA=False`.
   * You also want to consider using **HTTPS** to restrict access to model endpoints and secure the data that clients submit. For this purpose, you would need to specify either `sslSecret` config setting or combination of `sslKeyPemFile` and `sslCertPemFile` config-protected settings. 
   * By default, AzureML extension deployment expects config settings for **HTTPS** support. For development or testing purposes, **HTTP** support is conveniently provided through config setting `allowInsecureConnections=True`.
