
# Configure a secure online endpoint with TLS/SSL

This article shows you how to secure a Kubernetes online endpoint that's created through Azure Machine Learning.

You use [HTTPS](https://en.wikipedia.org/wiki/HTTPS) to restrict access to online endpoints and help secure the data that clients submit. HTTPS encrypts communications between a client and an online endpoint by using [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security). TLS is sometimes still called *Secure Sockets Layer* (SSL), which was the predecessor of TLS.

> [!TIP]
> * Specifically, Kubernetes online endpoints support TLS version 1.2 for Azure Kubernetes Service (AKS) and Azure Arc-enabled Kubernetes.
> * TLS version 1.3 for Azure Machine Learning Kubernetes inference is unsupported.

TLS and SSL both rely on *digital certificates*, which help with encryption and identity verification. For more information on how digital certificates work, see the Wikipedia topic [public_key_infrastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure).

> [!WARNING]
> If you don't use HTTPS for your online endpoints, data that's sent to and from the service might be visible to others on the internet.
>
> HTTPS also enables the client to verify the authenticity of the server that it's connecting to. This feature protects clients against [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) attacks.

The following is the general process to secure an online endpoint:

1. [Get a domain name](#get-a-domain-name).

1. [Get a digital certificate](#get-a-tlsssl-certificate).

1. [Configure TLS/SSL in the Azure Machine Learning extension](#configure-tlsssl-in-the-azure-machine-learning-extension).

1. [Update your DNS with a fully qualified domain name (FQDN) to point to the online endpoint](#update-your-dns-with-an-fqdn).

> [!IMPORTANT]
> You need to purchase your own certificate to get a domain name or TLS/SSL certificate, and then configure them in the Azure Machine Learning extension. For more detailed information, see the following sections of this article.

## Get a domain name

If you don't already own a domain name, purchase one from a *domain name registrar*. The process and price differ among registrars. The registrar provides tools to manage the domain name. You use these tools to map an FQDN (such as `www.contoso.com`) to the IP address that hosts your online endpoint. 

For more information on how to get the IP address of your online endpoints, see the [Update your DNS with an FQDN](#update-your-dns-with-an-fqdn) section of this article.

## Get a TLS/SSL certificate

There are many ways to get a TLS/SSL certificate (digital certificate). The most common is to purchase one from a *certificate authority*. Regardless of where you get the certificate, you need the following files:

- A certificate that contains the full certificate chain and is PEM encoded
- A key that's PEM encoded

> [!NOTE]
> An SSL key in a PEM file with passphrase protection is not supported.

When you request a certificate, you must provide the FQDN of the address that you plan to use for the online endpoint (for example, `www.contoso.com`). The address that's stamped into the certificate and the address that the clients use are compared to verify the identity of the online endpoint. If those addresses don't match, the client gets an error message.

For more information on how to configure IP banding with an FQDN, see the [Update your DNS with an FQDN](#update-your-dns-with-an-fqdn) section of this article.

> [!TIP]
> If the certificate authority can't provide the certificate and key as PEM-encoded files, you can use a tool like [OpenSSL](https://www.openssl.org/) to change the format.

> [!WARNING]
> Use *self-signed* certificates only for development. Don't use them in production environments. Self-signed certificates can cause problems in your client applications. For more information, see the documentation for the network libraries that your client application uses.
