    - Make sure that the subnet contains enough free IP addresses. Each compute instance requires one IP address. Each *node* within a compute cluster requires one IP address.

+ If you have your own DNS server, we recommend using DNS forwarding to resolve the fully qualified domain names (FQDN) of compute instances and clusters. For more information, see [Use a custom DNS with Azure Machine Learning](how-to-custom-dns.md).

+ To deploy resources into a virtual network or subnet, your user account must have permissions to the following actions in Azure role-based access control (Azure RBAC):

    - "Microsoft.Network/virtualNetworks/*/read" on the virtual network resource. This permission isn't needed for Azure Resource Manager (ARM) template deployments.
    - "Microsoft.Network/virtualNetworks/subnet/join/action" on the subnet resource.

    For more information on Azure RBAC with networking, see the [Networking built-in roles](../role-based-access-control/built-in-roles.md#networking)

## Limitations

* __Compute clusters__ can be created in a different region than your workspace. This functionality is in __preview__, and is only available for __compute clusters__, not compute instances. When using a different region for the cluster, the following limitations apply:

    * If your workspace associated resources, such as storage, are in a different virtual network than the cluster, set up global virtual network peering between the networks. For more information, see [Virtual network peering](../virtual-network/virtual-network-peering-overview.md).
    * You may see increased network latency and data transfer costs. The latency and costs can occur when creating the cluster, and when running jobs on it.

    Guidance such as using NSG rules, user-defined routes, and input/output requirements, apply as normal when using a different region than the workspace.

    > [!WARNING]
    > If you are using a __private endpoint-enabled workspace__, creating the cluster in a different region is __not supported__.

* Compute cluster/instance deployment in virtual network isn't supported with Azure Lighthouse.

## Compute instance/cluster with no public IP

> [!IMPORTANT]
> If you have been using compute instances or compute clusters configured for no public IP without opting-in to the preview, you will need to delete and recreate them after January 20, 2023 (when the feature is generally available).
> 
> If you were previously using the preview of no public IP, you may also need to modify what traffic you allow inbound and outbound, as the requirements have changed for general availability:
> * Outbound requirements - Two additional outbound, which are only used for the management of compute instances and clusters. The destination of these service tags are owned by Microsoft:
>     - `AzureMachineLearning` service tag on UDP port 5831.
>     - `BatchNodeManagement` service tag on TCP port 443.

The following configurations are in addition to those listed in the [Prerequisites](#prerequisites) section, and are specific to **creating** a compute instances/clusters configured for no public IP:

+ You must use a workspace private endpoint for the compute resource to communicate with Azure Machine Learning services from the VNet. For more information, see [Configure a private endpoint for Azure Machine Learning workspace](how-to-configure-private-link.md).

+ In your VNet, allow **outbound** traffic to the following service tags or fully qualified domain names (FQDN):

    | Service tag | Protocol | Port | Notes |
    | ----- |:-----:|:-----:| ----- |
    | `AzureMachineLearning` | TCP<br>UDP | 443/8787/18881<br>5831 | Communication with the Azure Machine Learning service.|
    | `BatchNodeManagement.<region>` | ANY | 443| Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. Communication with Azure Batch. Compute instance and compute cluster are implemented using the Azure Batch service.|
    | `Storage.<region>` | TCP | 443 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. This service tag is used to communicate with the Azure Storage account used by Azure Batch. |
