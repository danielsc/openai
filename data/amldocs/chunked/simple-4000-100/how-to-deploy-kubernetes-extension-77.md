   * By default, AzureML extension deployment expects config settings for **HTTPS** support. For development or testing purposes, **HTTP** support is conveniently provided through config setting `allowInsecureConnections=True`.

## AzureML extension deployment - CLI examples and Azure portal

### [Azure CLI](#tab/deploy-extension-with-cli)
To deploy AzureML extension with CLI, use `az k8s-extension create` command passing in values for the mandatory parameters.

We list four typical extension deployment scenarios for reference. To deploy extension for your production usage, carefully read the complete list of [configuration settings](#review-azureml-extension-configuration-settings).

- **Use AKS cluster in Azure for a quick proof of concept to run all kinds of ML workload, i.e., to run training jobs or to deploy models as online/batch endpoints**

   For AzureML extension deployment on AKS cluster, make sure to specify `managedClusters` value for `--cluster-type` parameter. Run the following Azure CLI command to deploy AzureML extension:
   ```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableTraining=True enableInference=True inferenceRouterServiceType=LoadBalancer allowInsecureConnections=True inferenceLoadBalancerHA=False --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```

- **Use Arc Kubernetes cluster outside of Azure for a quick proof of concept, to run training jobs only**

   For AzureML extension deployment on [Arc Kubernetes](../azure-arc/kubernetes/overview.md) cluster, you would need to specify `connectedClusters` value for `--cluster-type` parameter. Run the following Azure CLI command to deploy AzureML extension:
   ```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableTraining=True --cluster-type connectedClusters --cluster-name <your-connected-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```

- **Enable an AKS cluster in Azure for production training and inference workload**
   For AzureML extension deployment on AKS, make sure to specify `managedClusters` value for `--cluster-type` parameter. Assuming your cluster has more than three nodes, and you'll use an Azure public load balancer and HTTPS for inference workload support. Run the following Azure CLI command to deploy AzureML extension:
   ```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableTraining=True enableInference=True inferenceRouterServiceType=LoadBalancer sslCname=<ssl cname> --config-protected sslCertPemFile=<file-path-to-cert-PEM> sslKeyPemFile=<file-path-to-cert-KEY> --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```
- **Enable an [Arc Kubernetes](../azure-arc/kubernetes/overview.md) cluster anywhere for production training and inference workload using NVIDIA GPUs**

   For AzureML extension deployment on [Arc Kubernetes](../azure-arc/kubernetes/overview.md) cluster, make sure to specify `connectedClusters` value for `--cluster-type` parameter. Assuming your cluster has more than three nodes, you'll use a NodePort service type and HTTPS for inference workload support, run following Azure CLI command to deploy AzureML extension:
   ```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableTraining=True enableInference=True inferenceRouterServiceType=NodePort sslCname=<ssl cname> installNvidiaDevicePlugin=True installDcgmExporter=True --config-protected sslCertPemFile=<file-path-to-cert-PEM> sslKeyPemFile=<file-path-to-cert-KEY> --cluster-type connectedClusters --cluster-name <your-connected-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```

### [Azure portal](#tab/portal)

The UI experience to deploy extension is only available for **[Arc Kubernetes](../azure-arc/kubernetes/overview.md)**. If you have an AKS cluster without Azure Arc connection, you need to use CLI to deploy AzureML extension.
