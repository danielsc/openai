        <!-- > [!TIP]
        > * At least one storage account resource must be listed in the policy.
        > * If you are adding multiple storage accounts, and the _default storage account_ for your workspace is configured with a private endpoint, you do not need to include it in the policy. -->

        * __Service__: Microsoft.Storage
        * __Scope__: Select the scope as __Single account__ to limit the network traffic to one storage account.
        * __Subscription__: The Azure subscription that contains the storage account.
        * __Resource group__: The resource group that contains the storage account.
        * __Resource__: The default storage account of your workspace.
    
        Select __Add__ to add the resource information.

        :::image type="content" source="media/how-to-data-exfiltration-prevention/create-service-endpoint-policy.png" alt-text="A screenshot showing how to create a service endpoint policy." lightbox="media/how-to-data-exfiltration-prevention/create-service-endpoint-policy.png":::

    1. Select __+ Add an alias__, and then select `/services/Azure/MachineLearning` as the __Server Alias__ value. Select __Add__ to add the alias.
    
        > [!NOTE]
        > The Azure CLI and Azure PowerShell do not provide support for adding an alias to the policy.

1. Select __Review + Create__, and then select __Create__.

> [!IMPORTANT]
> If your compute instance and compute cluster need access to additional storage accounts, your service endpoint policy should include the additional storage accounts in the resources section. Note that it is not required if you use Storage private endpoints. Service endpoint policy and private endpoint are independent.

## 2. Allow inbound and outbound network traffic

### Inbound

> [!IMPORTANT]
> The following information __modifies__ the guidance provided in the [How to secure training environment](how-to-secure-training-vnet.md) article.

When using Azure Machine Learning __compute instance__ _with a public IP address_, allow inbound traffic from Azure Batch management (service tag `BatchNodeManagement.<region>`). A compute instance _with no public IP_ __doesn't__ require this inbound communication.

### Outbound 

> [!IMPORTANT]
> The following information is __in addition__ to the guidance provided in the [Secure training environment with virtual networks](how-to-secure-training-vnet.md) and [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md) articles.

Select the configuration that you're using:

# [Service tag/NSG](#tab/servicetag)

__Allow__ outbound traffic over __TCP port 443__ to the following __service tags__. Replace `<region>` with the Azure region that contains your compute cluster or instance:

* `BatchNodeManagement.<region>`
* `AzureMachineLearning`
* `Storage.<region>` - A Service Endpoint Policy will be applied in a later step to limit outbound traffic. 

# [Firewall](#tab/firewall)

__Allow__ outbound traffic over __TCP port 443__ to the following FQDNs. Replace instances of `<region>` with the Azure region that contains your compute cluster or instance:

* `<region>.batch.azure.com`
* `<region>.service.batch.com`

> [!WARNING]
> If you enable the service endpoint on the subnet used by your firewall, you must open outbound traffic to the following hosts:
> * `*.blob.core.windows.net`
> * `*.queue.core.windows.net`
> * `*.table.core.windows.net`


For more information, see [How to secure training environments](how-to-secure-training-vnet.md) and [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).

## 3. Enable storage endpoint for the subnet

1. From the [Azure portal](https://portal.azure.com), select the __Azure Virtual Network__ for your Azure ML workspace.
1. From the left of the page, select __Subnets__ and then select the subnet that contains your compute cluster/instance resources.
1. In the form that appears, expand the __Services__ dropdown and then enable __Microsoft.Storage__. Select __Save__ to save these changes.
