
# Configure inbound and outbound network traffic

Azure Machine Learning requires access to servers and services on the public internet. When implementing network isolation, you need to understand what access is required and how to enable it.

> [!NOTE]
> The information in this article applies to Azure Machine Learning workspace configured with a private endpoint.

## Common terms and information

The following terms and information are used throughout this article:

* __Azure service tags__: A service tag is an easy way to specify the IP ranges used by an Azure service. For example, the `AzureMachineLearning` tag represents the IP addresses used by the Azure Machine Learning service.

    > [!IMPORTANT]
    > Azure service tags are only supported by some Azure services. For a list of service tags supported with network security groups and Azure Firewall, see the [Virtual network service tags](/azure/virtual-network/service-tags-overview) article.
    > 
    > If you are using a non-Azure solution such as a 3rd party firewall, download a list of [Azure IP Ranges and Service Tags](https://www.microsoft.com/download/details.aspx?id=56519). Extract the file and search for the service tag within the file. The IP addresses may change periodically.

* __Region__: Some service tags allow you to specify an Azure region. This limits access to the service IP addresses in a specific region, usually the one that your service is in. In this article, when you see `<region>`, substitute your Azure region instead. For example, `BatchNodeManagement.<region>` would be `BatchNodeManagement.uswest` if your Azure Machine Learning workspace is in the US West region.

* __Azure Batch__: Azure Machine Learning compute clusters and compute instances rely on a back-end Azure Batch instance. This back-end service is hosted in a Microsoft subscription.

* __Ports__: The following ports are used in this article. If a port range isn't listed in this table, it's specific to the service and may not have any published information on what it's used for:

    | Port | Description |
    | ----- | ----- | 
    | 80 | Unsecured web traffic (HTTP) |
    | 443 | Secured web traffic (HTTPS) |
    | 445 | SMB traffic used to access file shares in Azure File storage |
    | 8787 | Used when connecting to RStudio on a compute instance |
    | 18881 | Used to connect to the language server to enable IntelliSense for notebooks on a compute instance. |

* __Protocol__: Unless noted otherwise, all network traffic mentioned in this article uses __TCP__.

## Basic configuration

This configuration makes the following assumptions:

* You're using docker images provided by a container registry that you provide, and won't be using images provided by Microsoft.
* You're using a private Python package repository, and won't be accessing public package repositories such as `pypi.org`, `*.anaconda.com`, or `*.anaconda.org`.
* The private endpoints can communicate directly with each other within the VNet. For example, all services have a private endpoint in the same VNet:
    * Azure Machine Learning workspace
    * Azure Storage Account (blob, file, table, queue)

__Inbound traffic__

| Source | Source<br>ports | Destination | Destination<b>ports| Purpose |
| ----- |:-----:| ----- |:-----:| ----- |
| `AzureLoadBalancer` | Any | `VirtualNetwork` | 44224 | Inbound to compute instance/cluster. __Only needed if the instance/cluster is configured to use a public IP address__. |

> [!TIP]
> A network security group (NSG) is created by default for this traffic. For more information, see [Default security rules](/azure/virtual-network/network-security-groups-overview#inbound).

__Outbound traffic__

| Service tag(s) | Ports | Purpose |
| ----- |:-----:| ----- |
| `AzureActiveDirectory` | 80, 443 | Authentication using Azure AD. |
| `AzureMachineLearning` | 443, 8787, 18881<br>UDP: 5831 | Using Azure Machine Learning services. |
| `BatchNodeManagement.<region>` | 443 | Communication Azure Batch. |
