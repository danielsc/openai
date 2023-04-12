    - The compute resource running the troubleshooting commands is not using DNS Server for DNS resolution
    - The Private DNS Zones chosen when creating the Private Endpoint are not linked to the DNS Server VNet
    - Conditional forwarders to Azure DNS Virtual Server IP were not configured correctly

<a id='dns-on-premises'></a>

## Example: Custom DNS Server hosted on-premises

This architecture uses the common Hub and Spoke virtual network topology. ExpressRoute is used to connect from your on-premises network to the Hub virtual network. The Custom DNS server is hosted on-premises. A separate virtual network contains the private endpoint to the Azure Machine Learning workspace and associated resources. With this topology, there needs to be another virtual network hosting a DNS server that can send requests to the Azure DNS Virtual Server IP address.

:::image type="content" source="./media/how-to-custom-dns/custom-dns-express-route.svg" alt-text="Diagram of custom DNS hosted on-premises topology" lightbox ="./media/how-to-custom-dns/custom-dns-express-route-expanded.png" :::

The following steps describe how this topology works:

1. **Create Private DNS Zone and link to DNS Server Virtual Network**:

    The first step in ensuring a Custom DNS solution works with your Azure Machine Learning workspace is to create two Private DNS Zones rooted at the following domains:

    **Azure Public regions**:
    - ``` privatelink.api.azureml.ms```
    - ``` privatelink.notebooks.azure.net```

    **Azure China regions**:
    - ```privatelink.api.ml.azure.cn```
    - ```privatelink.notebooks.chinacloudapi.cn```

    **Azure US Government regions**:
    - ```privatelink.api.ml.azure.us```
    - ```privatelink.notebooks.usgovcloudapi.net```

    > [!NOTE]
    > Managed online endpoints share the workspace private endpoint. If you are manually adding DNS records to the private DNS zone `privatelink.api.azureml.ms`, an A record with wildcard
    > `*.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.azureml.ms` should be added to route all endpoints under the workspace to the private endpoint.

    Following creation of the Private DNS Zone, it needs to be linked to the DNS Server VNet – the Virtual Network that contains the DNS Server.

    > [!NOTE]
    > The DNS Server in the virtual network is separate from the On-premises DNS Server.

    A Private DNS Zone overrides name resolution for all names within the scope of the root of the zone. This override applies to all Virtual Networks the Private DNS Zone is linked to. For example, if a Private DNS Zone rooted at `privatelink.api.azureml.ms` is linked to Virtual Network foo, all resources in Virtual Network foo that attempt to resolve `bar.workspace.westus2.privatelink.api.azureml.ms` will receive any record that is listed in the privatelink.api.azureml.ms zone.

    However, records listed in Private DNS Zones are only returned to devices resolving domains using the default Azure DNS Virtual Server IP address. The Azure DNS Virtual Server IP address is only valid within the context of a Virtual Network. When using an on-premises DNS server, it is not able to query the Azure DNS Virtual Server IP address to retrieve records.

    To get around this behavior, create an intermediary DNS Server in a virtual network. This DNS server can query the Azure DNS Virtual Server IP address to retrieve records for any Private DNS Zone linked to the virtual network.

    While the On-premises DNS Server will resolve domains for devices spread throughout your network topology, it will resolve Azure Machine Learning-related domains against the DNS Server. The DNS Server will resolve those domains from the Azure DNS Virtual Server IP address.

2. **Create private endpoint with private DNS integration targeting Private DNS Zone linked to DNS Server Virtual Network**:

    The next step is to create a Private Endpoint to the Azure Machine Learning workspace. The private endpoint targets both Private DNS Zones created in step 1. This ensures all communication with the workspace is done via the Private Endpoint in the Azure Machine Learning Virtual Network.
