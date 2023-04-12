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
