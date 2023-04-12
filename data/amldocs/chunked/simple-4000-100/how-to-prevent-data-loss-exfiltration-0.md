
# Azure Machine Learning data exfiltration prevention

<!-- Learn how to use a [Service Endpoint policy](../virtual-network/virtual-network-service-endpoint-policies-overview.md) to prevent data exfiltration from storage accounts in your Azure Virtual Network that are used by Azure Machine Learning. -->

Azure Machine Learning has several inbound and outbound dependencies. Some of these dependencies can expose a data exfiltration risk by malicious agents within your organization. This document explains how to minimize data exfiltration risk by limiting inbound and outbound requirements.

* __Inbound__: If your compute instance or cluster uses a public IP address, you have an inbound on `azuremachinelearning` (port 44224) service tag. You can control this inbound traffic by using a network security group (NSG) and service tags. It's difficult to disguise Azure service IPs, so there's low data exfiltration risk. You can also configure the compute to not use a public IP, which removes inbound requirements.

* __Outbound__: If malicious agents don't have write access to outbound destination resources, they can't use that outbound for data exfiltration. Azure Active Directory, Azure Resource Manager, Azure Machine Learning, and Microsoft Container Registry belong to this category. On the other hand, Storage and AzureFrontDoor.frontend can be used for data exfiltration.

    * __Storage Outbound__: This requirement comes from compute instance and compute cluster. A malicious agent can use this outbound rule to exfiltrate data by provisioning and saving data in their own storage account. You can remove data exfiltration risk by using an Azure Service Endpoint Policy and Azure Batch's simplified node communication architecture.

    * __AzureFrontDoor.frontend outbound__: Azure Front Door is used by the Azure Machine Learning studio UI and AutoML. Instead of allowing outbound to the service tag (AzureFrontDoor.frontend), switch to the following fully qualified domain names (FQDN). Switching to these FQDNs removes unnecessary outbound traffic included in the service tag and allows only what is needed for Azure Machine Learning studio UI and AutoML.

        - `ml.azure.com`
        - `automlresources-prod.azureedge.net`

## Prerequisites

* An Azure subscription
* An Azure Virtual Network (VNet)
* An Azure Machine Learning workspace with a private endpoint that connects to the VNet.
    * The storage account used by the workspace must also connect to the VNet using a private endpoint.
* You need to recreate compute instance or scale down compute cluster to zero node.
    * Not required if you have joined preview.
    * Not required if you have new compute instance and compute cluster created after December 2022.

## Why do I need to use the service endpoint policy

Service endpoint policies allow you to filter egress virtual network traffic to Azure Storage accounts over service endpoint and allow data exfiltration to only specific Azure Storage accounts. Azure Machine Learning compute instance and compute cluster requires access to Microsoft-managed storage accounts for its provisioning. The Azure Machine learning alias in service endpoint policies includes Microsoft-managed storage accounts. We use service endpoint policies with the Azure Machine Learning alias to prevent data exfiltration or control the destination storage accounts. You can learn more in [Service Endpoint policy documentation](../virtual-network/virtual-network-service-endpoint-policies-overview.md).

## 1. Create the service endpoint policy

1. From the [Azure portal](https://portal.azure.com), add a new __Service Endpoint Policy__. On the __Basics__ tab, provide the required information and then select __Next__.
1. On the __Policy definitions__ tab, perform the following actions:
    1. Select __+ Add a resource__, and then provide the following information:
    
        <!-- > [!TIP]
        > * At least one storage account resource must be listed in the policy.
