   
   If you directly configured the PEM files in the extension deployment command before, you need to run the extension update command and specify the new PEM file's path:

   ```azurecli
      az k8s-extension update --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config sslCname=<ssl cname> --config-protected sslCertPemFile=<file-path-to-cert-PEM> sslKeyPemFile=<file-path-to-cert-KEY> --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```

## Disable TLS

To disable TLS for a model deployed to Kubernetes:

1. Update the Azure Machine Learning extension with `allowInsercureconnection` set to `True`.
1. Remove the `sslCname` configuration setting, along with the `sslSecret` or `sslPem` configuration settings.
1. Run the following Azure CLI command in your Kubernetes cluster, and then perform an update. This command assumes that you're using AKS.

   ```azurecli
      az k8s-extension update --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableInference=True inferenceRouterServiceType=LoadBalancer allowInsercureconnection=True --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
   ```

> [!WARNING]
> By default, the Azure Machine Learning extension deployment expects configuration settings for HTTPS support. We recommend HTTP support only for development or testing purposes. The `allowInsecureConnections=True` configuration setting provides HTTP support.

## Next steps

Learn how to:
- [Consume a machine learning model deployed as an online endpoint](how-to-deploy-online-endpoints.md#invoke-the-local-endpoint-to-score-data-by-using-your-model)
- [Secure a Kubernetes inferencing environment](how-to-secure-kubernetes-inferencing-environment.md)
- [Use your workspace with a custom DNS server](how-to-custom-dns.md)
