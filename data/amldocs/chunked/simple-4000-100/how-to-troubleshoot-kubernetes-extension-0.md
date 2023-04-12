
# Troubleshoot AzureML extension

In this article, learn how to troubleshoot common problems you may encounter with [AzureML extension](./how-to-deploy-kubernetes-extension.md) deployment in your AKS or Arc-enabled Kubernetes.

## How is AzureML extension installed
AzureML extension is released as a helm chart and installed by Helm V3. All components of AzureML extension are installed in `azureml` namespace. You can use the following commands to check the extension status. 
```bash
# get the extension status
az k8s-extension show --name <extension-name>

# check status of all pods of AzureML extension
kubectl get pod -n azureml

# get events of the extension
kubectl get events -n azureml --sort-by='.lastTimestamp'
```

## Troubleshoot AzureML extension deployment error

### Error: can't reuse a name that is still in use
This error means the extension name you specified already exists. If the name is used by Azureml extension, you need to wait for about an hour and try again. If the name is used by other helm charts, you need to use another name. Run ```helm list -Aa``` to list all helm charts in your cluster. 

### Error: earlier operation for the helm chart is still in progress
You need to wait for about an hour and try again after the unknown operation is completed.

### Error: unable to create new content in namespace azureml because it's being terminated
This error happens when an uninstallation operation isn't finished and another installation operation is triggered. You can run ```az k8s-extension show``` command to check the provisioning status of the extension and make sure the extension has been uninstalled before taking other actions.

### Error: failed in download the Chart path not found 
This error happens when you specify a wrong extension version. You need to make sure the specified version exists. If you want to use the latest version, you don't need to specify ```--version```  .

### Error: can't be imported into the current release: invalid ownership metadata 
This error means there's a conflict between existing cluster resources and AzureML extension. A full error message could be like the following text: 
```
CustomResourceDefinition "jobs.batch.volcano.sh" in namespace "" exists and cannot be imported into the current release: invalid ownership metadata; label validation error: missing key "app.kubernetes.io/managed-by": must be set to "Helm"; annotation validation error: missing key "meta.helm.sh/release-name": must be set to "amlarc-extension"; annotation validation error: missing key "meta.helm.sh/release-namespace": must be set to "azureml"
```

Use the following steps to mitigate the issue.

* Check who owns the problematic resources and if the resource can be deleted or modified. 
* If the resource is used only by AzureML extension and can be deleted, you can manually add labels to mitigate the issue. Taking the previous error message as an example, you can run commands as follows,

    ```bash 
    kubectl label crd jobs.batch.volcano.sh "app.kubernetes.io/managed-by=Helm" 
    kubectl annotate crd jobs.batch.volcano.sh "meta.helm.sh/release-namespace=azureml" "meta.helm.sh/release-name=<extension-name>"
    ``` 
    By setting the labels and annotations to the resource, it means the resource is managed by helm and owned by AzureML extension. 
* If the resource is also used by other components in your cluster and can't be modified. Refer to [deploy AzureML extension](./how-to-deploy-kubernetes-extension.md#review-azureml-extension-configuration-settings) to see if there's a configuration setting to disable the conflict resource. 

## HealthCheck of extension
When the installation failed and didn't hit any of the above error messages, you can use the built-in health check job to make a comprehensive check on the extension. Azureml extension contains a `HealthCheck` job to pre-check your cluster readiness when you try to install, update or delete the extension. The HealthCheck job will output a report, which is saved in a configmap named `arcml-healthcheck` in `azureml` namespace. The error codes and possible solutions for the report are listed in [Error Code of HealthCheck](#error-code-of-healthcheck). 
