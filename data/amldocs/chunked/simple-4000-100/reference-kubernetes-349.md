    > Replace `<domain>` and `<ingress-secret-name>` in the above Ingress Resource with the domain pointing to LoadBalancer of the **Nginx ingress controller/Application Gateway** and name of your secret. Store the above Ingress Resource in a file name `ing-azureml-fe-tls.yaml`.

1. Deploy ing-azureml-fe-tls.yaml by running

    ```bash
    kubectl apply -f ing-azureml-fe-tls.yaml
    ```

2. Check the log of the ingress controller for deployment status.

3. Now the `azureml-fe` application will be available on HTTPS. You can check this by visiting the public LoadBalancer address of the Nginx Ingress Controller.

4. [Create an inference job and invoke](../machine-learning/how-to-deploy-online-endpoints.md).

    >[!NOTE]
    >
    > Replace the protocol and IP in scoring_uri with https and domain pointing to LoadBalancer of the Nginx Ingress Controller  or the Application Gateway before invoking.

## Use ARM Template to Deploy Extension
Extension on managed cluster can be deployed with ARM template. A sample template can be found from [deployextension.json](https://github.com/Azure/AML-Kubernetes/blob/master/files/deployextension.json), with a demo parameter file [deployextension.parameters.json](https://github.com/Azure/AML-Kubernetes/blob/master/files/deployextension.parameters.json) 

To leverage the sample deployment template, edit the parameter file with correct value, then run the following command:

```azurecli
az deployment group create --name <ARM deployment name> --resource-group <resource group name> --template-file deployextension.json --parameters deployextension.parameters.json
```
More information about how to use ARM template can be found from [ARM template doc](../azure-resource-manager/templates/overview.md)


## Azureml extension release note
> [!NOTE]
 >
 > New features are released at a biweekly calendar.

| Date | Version |Version description |
|---|---|---|
| Dec 27, 2022 | 1.1.17 | Move the Fluent-bit from DaemonSet to sidecars. Add MDC support. Refine error messages. Support cluster mode (windows, linux) jobs. Bug fixes|
| Nov 29, 2022 | 1.1.16 |Add instance type validation by new CRD. Support Tolerance. Shorten SVC Name. Workload Core hour. Multiple Bug fixes and improvements. |
| Sep 13, 2022 | 1.1.10 | Bug fixes.|
| Aug 29, 2022 | 1.1.9 | Improved health check logic. Bug fixes.|
| Jun 23, 2022 | 1.1.6 | Bug fixes. |
| Jun 15, 2022 | 1.1.5 | Updated training to use new common runtime to run jobs. Removed Azure Relay usage for AKS extension. Removed service bus usage from the extension. Updated security context usage. Updated inference azureml-fe to v2. Updated to use Volcano as training job scheduler. Bug fixes. |
| Oct 14, 2021 | 1.0.37 | PV/PVC volume mount support in AMLArc training job. |
| Sept 16, 2021 | 1.0.29 | New regions available, WestUS, CentralUS, NorthCentralUS, KoreaCentral. Job queue explainability. See job queue details in AML Workspace Studio. Auto-killing policy. Support max_run_duration_seconds in ScriptRunConfig. The system will attempt to automatically cancel the run if it took longer than the setting value. Performance improvement on cluster auto scaling support. Arc agent and ML extension deployment from on premises container registry.|
| August 24, 2021 | 1.0.28 | Compute instance type is supported in job YAML. Assign Managed Identity to AMLArc compute.|
| August 10, 2021 | 1.0.20 |New Kubernetes distribution support, K3S - Lightweight Kubernetes. Deploy AzureML extension to your AKS cluster without connecting via Azure Arc. Automated Machine Learning (AutoML) via Python SDK. Use 2.0 CLI to attach the Kubernetes cluster to AML Workspace. Optimize AzureML extension components CPU/memory resources utilization.|
| July 2, 2021 | 1.0.13 | New Kubernetes distributions support, OpenShift Kubernetes and GKE (Google Kubernetes Engine). Autoscale support. If the user-managed Kubernetes cluster enables the autoscale, the cluster will be automatically scaled out or scaled in according to the volume of active runs and deployments. Performance improvement on job launcher, which shortens the job execution time to a great deal.|
