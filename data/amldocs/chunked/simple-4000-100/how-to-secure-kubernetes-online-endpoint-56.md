> Use *self-signed* certificates only for development. Don't use them in production environments. Self-signed certificates can cause problems in your client applications. For more information, see the documentation for the network libraries that your client application uses.

## Configure TLS/SSL in the Azure Machine Learning extension

For a Kubernetes online endpoint that's set to use inference HTTPS for secure connections, you can enable TLS termination with deployment configuration settings when you [deploy the Azure Machine Learning extension](how-to-deploy-online-endpoints.md) in a Kubernetes cluster. 

At deployment time for the Azure Machine Learning extension, the `allowInsecureConnections` configuration setting is `False` by default. To ensure successful extension deployment, you need to specify either the `sslSecret` configuration setting or a combination of `sslKeyPemFile` and `sslCertPemFile` configuration-protected settings. Otherwise, you can set `allowInsecureConnections=True` to support HTTP and disable TLS termination.

> [!NOTE]
> To support the HTTPS online endpoint, `allowInsecureConnections` must be set to `False`.

To enable an HTTPS endpoint for real-time inference, you need to provide a PEM-encoded TLS/SSL certificate and key. There are two ways to specify the certificate and key at deployment time for the Azure Machine Learning extension:

- Specify the `sslSecret` configuration setting.
- Specify a combination of `sslCertPemFile` and `slKeyPemFile` configuration-protected settings.

### Configure sslSecret

The best practice is to save the certificate and key in a Kubernetes secret in the `azureml` namespace.

To configure `sslSecret`, you need to save a Kubernetes secret in your Kubernetes cluster in the `azureml` namespace to store *cert.pem* (PEM-encoded TLS/SSL certificate) and *key.pem* (PEM-encoded TLS/SSL key). 

The following code is a sample YAML definition of a TLS/SSL secret:

```
apiVersion: v1
data:
  cert.pem: <PEM-encoded SSL certificate> 
  key.pem: <PEM-encoded SSL key>
kind: Secret
metadata:
  name: <secret name>
  namespace: azureml
type: Opaque
```

After you save the secret in your cluster, you can use the following Azure CLI command to specify `sslSecret` as the name of this Kubernetes secret. (This command will work only if you're using AKS.)

```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config inferenceRouterServiceType=LoadBalancer sslSecret=<Kubernetes secret name> sslCname=<ssl cname> --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
```

### Configure sslCertPemFile and sslKeyPemFile

You can specify the `sslCertPemFile` configuration setting to be the path to the PEM-encoded TLS/SSL certificate file, and the `sslKeyPemFile` configuration setting to be the path to the PEM-encoded TLS/SSL key file.

The following example demonstrates how to use the Azure CLI to specify PEM files to the Azure Machine Learning extension that uses a TLS/SSL certificate that you purchased. The example assumes that you're using AKS.

```azurecli
   az k8s-extension create --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config enableInference=True inferenceRouterServiceType=LoadBalancer sslCname=<ssl cname> --config-protected sslCertPemFile=<file-path-to-cert-PEM> sslKeyPemFile=<file-path-to-cert-KEY> --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
```

> [!NOTE]
> - A PEM file with passphrase protection is not supported.
> - Both `sslCertPemFIle` and `sslKeyPemFIle` use configuration-protected parameters. They don't configure `sslSecret` and `sslCertPemFile`/`sslKeyPemFile` at the same time.

## Update your DNS with an FQDN

For model deployment on a Kubernetes online endpoint with a custom certificate, you must update your DNS record to point to the IP address of the online endpoint. The Azure Machine Learning inference router service (`azureml-fe`) provides this IP address. For more information about `azureml-fe`, see [Managed Azure Machine Learning inference router](how-to-kubernetes-inference-routing-azureml-fe.md).
