  - [**Greenfield Deployment**](../application-gateway/tutorial-ingress-controller-add-on-new.md): If you are starting from scratch, refer to these instructions.
  - [**Brownfield Deployment**](../application-gateway/tutorial-ingress-controller-add-on-existing.md): If you have an existing AKS cluster and Application Gateway, refer to these instructions.
- If you want to use HTTPS on this application, you will need a x509 certificate and its private key.

### Expose services over HTTP

In order to expose the azureml-fe, we will use the following ingress resource:

```yaml
# Nginx Ingress Controller example
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: azureml-fe
  namespace: azureml
spec:
  ingressClassName: nginx
  rules:
  - http:
      paths:
      - path: /
        backend:
          service:
            name: azureml-fe
            port:
              number: 80
        pathType: Prefix
```
This ingress will expose the `azureml-fe` service and the selected deployment as a default backend of the Nginx Ingress Controller.



```yaml
# Azure Application Gateway example
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: azureml-fe
  namespace: azureml
spec:
  ingressClassName: azure-application-gateway
  rules:
  - http:
      paths:
      - path: /
        backend:
          service:
            name: azureml-fe
            port:
              number: 80
        pathType: Prefix
```
This ingress will expose the `azureml-fe` service and the selected deployment as a default backend of the Application Gateway.

Save the above ingress resource as `ing-azureml-fe.yaml`.

1. Deploy `ing-azureml-fe.yaml` by running:

    ```bash
    kubectl apply -f ing-azureml-fe.yaml
    ```

2. Check the log of the ingress controller for deployment status.

3. Now the `azureml-fe` application should be available. You can check this by visiting:
    - **Nginx Ingress Controller**: the public LoadBalancer address of Nginx Ingress Controller 
    - **Azure Application Gateway**: the public address of the Application Gateway.
4. [Create an inference job and invoke](https://github.com/Azure/AML-Kubernetes/blob/master/docs/simple-flow.md).

    >[!NOTE]
    >
    > Replace the ip in scoring_uri with public LoadBalancer address of the Nginx Ingress Controller before invoking.

### Expose services over HTTPS

1. Before deploying ingress, you need to create a kubernetes secret to host the certificate and private key. You can create a kubernetes secret by running

    ```bash
    kubectl create secret tls <ingress-secret-name> -n azureml --key <path-to-key> --cert <path-to-cert>
    ```

2. Define the following ingress. In the ingress, specify the name of the secret in the `secretName` section.

    ```yaml
    # Nginx Ingress Controller example
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: azureml-fe
      namespace: azureml
    spec:
      ingressClassName: nginx
      tls:
      - hosts:
        - <domain>
        secretName: <ingress-secret-name>
      rules:
      - host: <domain>
        http:
          paths:
          - path: /
            backend:
              service:
                name: azureml-fe
                port:
                  number: 80
            pathType: Prefix
    ```

    ```yaml
    # Azure Application Gateway example
    apiVersion: networking.k8s.io/v1
    kind: Ingress
    metadata:
      name: azureml-fe
      namespace: azureml
    spec:
      ingressClassName: azure-application-gateway
      tls:
      - hosts:
        - <domain>
        secretName: <ingress-secret-name>
      rules:
      - host: <domain>
        http:
          paths:
          - path: /
            backend:
              service:
                name: azureml-fe
                port:
                  number: 80
            pathType: Prefix
    ```

    >[!NOTE] 
    >
    > Replace `<domain>` and `<ingress-secret-name>` in the above Ingress Resource with the domain pointing to LoadBalancer of the **Nginx ingress controller/Application Gateway** and name of your secret. Store the above Ingress Resource in a file name `ing-azureml-fe-tls.yaml`.
