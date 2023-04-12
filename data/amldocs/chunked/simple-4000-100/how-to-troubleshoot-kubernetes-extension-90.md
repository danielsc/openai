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
