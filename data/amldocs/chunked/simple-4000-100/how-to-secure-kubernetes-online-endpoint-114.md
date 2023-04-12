For model deployment on a Kubernetes online endpoint with a custom certificate, you must update your DNS record to point to the IP address of the online endpoint. The Azure Machine Learning inference router service (`azureml-fe`) provides this IP address. For more information about `azureml-fe`, see [Managed Azure Machine Learning inference router](how-to-kubernetes-inference-routing-azureml-fe.md).

To update the DNS record for your custom domain name:

1. Get the online endpoint's IP address from the scoring URI, which is usually in the format of `http://104.214.29.152:80/api/v1/service/<service-name>/score`. In this example, the IP address is 104.214.29.152.
   
   After you configure your custom domain name, it replaces the IP address in the scoring URI. For Kubernetes clusters that use `LoadBalancer` as the inference router service, `azureml-fe` is exposed externally through a cloud provider's load balancer and TLS/SSL termination. The IP address of the Kubernetes online endpoint is the external IP address of the `azureml-fe` service deployed in the cluster. 

   If you use AKS, you can get the IP address from the [Azure portal](https://portal.azure.com/#home). Go to your AKS resource page, go to **Service and ingresses**, and then find the **azureml-fe** service under the **azuerml** namespace. Then you can find the IP address in the **External IP** column.
    
   :::image type="content" source="media/how-to-secure-kubernetes-online-endpoint/get-ip-address-from-aks-ui.png" alt-text="Screenshot of adding a new extension to the Azure Arc-enabled Kubernetes cluster from the Azure portal.":::

   In addition, you can run the Kubernetes command `kubectl describe svc azureml-fe -n azureml` in your cluster to get the IP address from the `LoadBalancer Ingress` parameter in the output.

   > [!NOTE]
   > For Kubernetes clusters that use either `nodePort` or `clusterIP` as the inference router service, you need to set up your own load-balancing solution and TLS/SSL termination for `azureml-fe`. You also need to get the IP address of the `azureml-fe` service in the cluster scope.

1. Use the tools from your domain name registrar to update the DNS record for your domain name. The record maps the FQDN (for example, `www.contoso.com`) to the IP address. The record must point to the IP address of the online endpoint.

   > [!TIP]
   > Microsoft is not responsible for updating the DNS for your custom DNS name or certificate. You must update it with your domain name registrar.

1. After the DNS record update, you can validate DNS resolution by using the `nslookup custom-domain-name` command. If the DNS record is correctly updated, the custom domain name will point to the IP address of the online endpoint.

   There can be a delay of minutes or hours before clients can resolve the domain name, depending on the registrar and the time to live (TTL) that's configured for the domain name.

For more information on DNS resolution with Azure Machine Learning, see [How to use your workspace with a custom DNS server](how-to-custom-dns.md).

## Update the TLS/SSL certificate

TLS/SSL certificates expire and must be renewed. Typically, this happens every year. Use the information in the following steps to update and renew your certificate for models deployed to Kubernetes (AKS and Azure Arc-enabled Kubernetes):

1. Use the documentation from the certificate authority to renew the certificate. This process creates new certificate files.

1. Update your Azure Machine Learning extension and specify the new certificate files by using the `az k8s-extension update` command.

   If you used a Kubernetes secret to configure TLS/SSL before, you need to first update the Kubernetes secret with the new *cert.pem* and *key.pem* configuration in your Kubernetes cluster. Then run the extension update command to update the certificate:

   ```azurecli
      az k8s-extension update --name <extension-name> --extension-type Microsoft.AzureML.Kubernetes --config inferenceRouterServiceType=LoadBalancer sslSecret=<Kubernetes secret name> sslCname=<ssl cname> --cluster-type managedClusters --cluster-name <your-AKS-cluster-name> --resource-group <your-RG-name> --scope cluster
   ``` 
