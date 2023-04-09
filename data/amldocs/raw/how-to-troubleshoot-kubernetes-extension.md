---
title: Troubleshoot AzureML extension
description: Learn how to troubleshoot some common AzureML extension deployment or update errors. 
titleSuffix: Azure Machine Learning
author: zhongj
ms.author: jinzhong
ms.reviewer: larryfr ssalgado
ms.service: machine-learning
ms.subservice: core
ms.date: 10/10/2022
ms.topic: how-to
ms.custom: build-spring-2022, cliv2, sdkv2, event-tier1-build-2022
---

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
In this case, all Prometheus instances will be managed by the existing prometheus operator. To make sure Prometheus works properly, the following things need to be paid attention to when you disable prometheus operator in Azureml extension.
1. Check if prometheus in azureml namespace is managed by the Prometheus operator. In some scenarios, prometheus operator is set to only monitor some specific namespaces. If so, make sure azureml namespace is in the allowlist. For more information, see [command flags](https://github.com/prometheus-operator/prometheus-operator/blob/b475b655a82987eca96e142fe03a1e9c4e51f5f2/cmd/operator/main.go#L165).
2. Check if kubelet-service is enabled in prometheus operator. Kubelet-service contains all the endpoints of kubelet. For more information, see [command flags](https://github.com/prometheus-operator/prometheus-operator/blob/b475b655a82987eca96e142fe03a1e9c4e51f5f2/cmd/operator/main.go#L149). And also need to make sure that kubelet-service has a label`k8s-app=kubelet`.
3. Create ServiceMonitor for kubelet-service. Run the following command with variables replaced:
    ```bash
    cat << EOF | kubectl apply -f -
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: prom-kubelet
      namespace: azureml
      labels:
        release: "<extension-name>"     # Please replace to your Azureml extension name
    spec:
      endpoints:
      - port: https-metrics
        scheme: https
        path: /metrics/cadvisor
        honorLabels: true
        tlsConfig:
          caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
          insecureSkipVerify: true
        bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
        relabelings:
        - sourceLabels:
          - __metrics_path__
          targetLabel: metrics_path
      jobLabel: k8s-app
      namespaceSelector:
        matchNames:
        - "<namespace-of-your-kubelet-service>"  # Please change this to the same namespace of your kubelet-service
      selector:
        matchLabels:
          k8s-app: kubelet    # Please make sure your kubelet-service has a label named k8s-app and it's value is kubelet

    EOF
    ```

### DCGM exporter
[Dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter) is the official tool recommended by NVIDIA for collecting GPU metrics. We've integrated it into Azureml extension. But, by default, dcgm-exporter isn't enabled, and no GPU metrics are collected. You can specify ```installDcgmExporter``` flag to ```true``` to enable it. As it's NVIDIA's official tool, you may already have it installed in your GPU cluster. If so, you can set ```installDcgmExporter```  to ```false``` and follow the steps below to integrate your dcgm-exporter into Azureml extension. Another thing to note is that dcgm-exporter allows user to config which metrics to expose. For Azureml extension, make sure ```DCGM_FI_DEV_GPU_UTIL```, ```DCGM_FI_DEV_FB_FREE``` and ```DCGM_FI_DEV_FB_USED``` metrics are exposed. 

1. Make sure you have Aureml extension and dcgm-exporter installed successfully. Dcgm-exporter can be installed by [Dcgm-exporter helm chart](https://github.com/NVIDIA/dcgm-exporter) or [Gpu-operator helm chart](https://github.com/NVIDIA/gpu-operator)

1. Check if there's a service for dcgm-exporter. If it doesn't exist or you don't know how to check, run the following command to create one.
    ```bash
    cat << EOF | kubectl apply -f -
    apiVersion: v1
    kind: Service
    metadata:
      name: dcgm-exporter-service
      namespace: "<namespace-of-your-dcgm-exporter>" # Please change this to the same namespace of your dcgm-exporter
      labels:
        app.kubernetes.io/name: dcgm-exporter
        app.kubernetes.io/instance: "<extension-name>" # Please replace to your Azureml extension name
        app.kubernetes.io/component: "dcgm-exporter"
      annotations:
        prometheus.io/scrape: 'true'
    spec:
      type: "ClusterIP"
      ports:
      - name: "metrics"
        port: 9400  # Please replace to the correct port of your dcgm-exporter. It's 9400 by default
        targetPort: 9400  # Please replace to the correct port of your dcgm-exporter. It's 9400 by default
        protocol: TCP
      selector:
        app.kubernetes.io/name: dcgm-exporter  # Those two labels are used to select dcgm-exporter pods. You can change them according to the actual label on the service
        app.kubernetes.io/instance: "<dcgm-exporter-helm-chart-name>" # Please replace to the helm chart name of dcgm-exporter
    EOF
    ```
1. Check if the service in previous step is set correctly
    ```bash
    kubectl -n <namespace-of-your-dcgm-exporter> port-forward service/dcgm-exporter-service 9400:9400
    # run this command in a separate terminal. You will get a lot of dcgm metrics with this command.
    curl http://127.0.0.1:9400/metrics
    ```
1. Set up ServiceMonitor to expose dcgm-exporter service to Azureml extension. Run the following command and it will take effect in a few minutes.
    ```bash
    cat << EOF | kubectl apply -f -
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: dcgm-exporter-monitor
      namespace: azureml
      labels:
        app.kubernetes.io/name: dcgm-exporter
        release: "<extension-name>"   # Please replace to your Azureml extension name
        app.kubernetes.io/component: "dcgm-exporter"
    spec:
      selector:
        matchLabels:
          app.kubernetes.io/name: dcgm-exporter
          app.kubernetes.io/instance: "<extension-name>"   # Please replace to your Azureml extension name
          app.kubernetes.io/component: "dcgm-exporter"
      namespaceSelector:
        matchNames:
        - "<namespace-of-your-dcgm-exporter>"  # Please change this to the same namespace of your dcgm-exporter
      endpoints:
      - port: "metrics"
        path: "/metrics"
    EOF
    ```

### Volcano Scheduler
If your cluster already has the volcano suite installed, you can set `installVolcano=false`, so the extension won't install the volcano scheduler. Volcano scheduler and volcano controller are required for training job submission and scheduling.

The volcano scheduler config used by AzureML extension is:

```yaml
volcano-scheduler.conf: |
    actions: "enqueue, allocate, backfill"
    tiers:
    - plugins:
        - name: task-topology
        - name: priority
        - name: gang
        - name: conformance
    - plugins:
        - name: overcommit
        - name: drf
        - name: predicates
        - name: proportion
        - name: nodeorder
        - name: binpack
```
You need to use the same config settings as above, and you need to disable `job/validate` webhook in the volcano admission if your **volcano version is lower than 1.6**, so that AzureML training workloads can perform properly.

#### Volcano scheduler integration supporting cluster autoscaler
As discussed in this [thread](https://github.com/volcano-sh/volcano/issues/2558) , the **gang plugin** is not working well with the cluster autoscaler(CA) and also the node autoscaler in AKS. 

If you use the volcano that comes with the AzureML extension via setting `installVolcano=true`, the extension will have a scheduler config by default, which configures the **gang** plugin to prevent job deadlock. Therefore, the cluster autoscaler(CA) in AKS cluster will not be supported with the volcano installed by extension.

For the case above, if you prefer the AKS cluster autoscaler could work normally, you can configure this `volcanoScheduler.schedulerConfigMap` parameter through updating extension, and specify a custom config of **no gang** volcano scheduler to it, for example:

```yaml
volcano-scheduler.conf: |
    actions: "enqueue, allocate, backfill"
    tiers:
    - plugins:
      - name: sla 
        arguments:
        sla-waiting-time: 1m
    - plugins:
      - name: conformance
    - plugins:
        - name: overcommit
        - name: drf
        - name: predicates
        - name: proportion
        - name: nodeorder
        - name: binpack
```

To use this config in your AKS cluster, you need to follow the steps below:  
1. Create a configmap file with the above config in the azureml namespace. This namespace will generally be created when you install the AzureML extension.
1. Set `volcanoScheduler.schedulerConfigMap=<configmap name>` in the extension config to apply this configmap. And you need to skip the resource validation when installing the extension by configuring `amloperator.skipResourceValidation=true`. For example:
    ```azurecli
    az k8s-extension update --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config volcanoScheduler.schedulerConfigMap=<configmap name> amloperator.skipResourceValidation=true --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
    ```

> [!NOTE]
> Since the gang plugin is removed, there's potential that the deadlock happens when volcano schedules the job. 
> 
> * To avoid this situation, you can **use same instance type across the jobs**.
>
> Note that you need to disable `job/validate` webhook in the volcano admission if your **volcano version is lower than 1.6**.



