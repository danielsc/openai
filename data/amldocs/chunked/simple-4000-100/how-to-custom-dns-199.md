
# [Azure portal](#tab/azure-portal)

1. In the [Azure portal](https://portal.azure.com), select your Azure Machine Learning __workspace__.
1. From the __Settings__ section, select __Private endpoint connections__.
1. Select the link in the __Private endpoint__ column that is displayed.
1. A list of the fully qualified domain names (FQDN) and IP addresses for the workspace private endpoint are at the bottom of the page.

    :::image type="content" source="./media/how-to-custom-dns/private-endpoint-custom-dns.png" alt-text="List of FQDNs in the portal":::

    > [!TIP]
    > If the DNS settings do not appear at the bottom of the page, use the __DNS configuration__ link from the left side of the page to view the FQDNs.


The information returned from all methods is the same; a list of the FQDN and private IP address for the resources. The following example is from the Azure Public Cloud:

| FQDN | IP Address |
| ----- | ----- |
| `fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.api.azureml.ms` | `10.1.0.5` |
| `fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.cert.api.azureml.ms` | `10.1.0.5` |
| `ml-myworkspace-eastus-fb7e20a0-8891-458b-b969-55ddb3382f51.eastus.notebooks.azure.net` | `10.1.0.6` |
| `*.eastus.inference.ml.azure.com` | `10.1.0.7` |

The following table shows example IPs from Azure China regions:

| FQDN | IP Address |
| ----- | ----- |
| `52882c08-ead2-44aa-af65-08a75cf094bd.workspace.chinaeast2.api.ml.azure.cn` | `10.1.0.5` |
| `52882c08-ead2-44aa-af65-08a75cf094bd.workspace.chinaeast2.cert.api.ml.azure.cn` | `10.1.0.5` |
| `ml-mype-pltest-chinaeast2-52882c08-ead2-44aa-af65-08a75cf094bd.chinaeast2.notebooks.chinacloudapi.cn` | `10.1.0.6` |
| `*.chinaeast2.inference.ml.azure.cn` | `10.1.0.7` |

The following table shows example IPs from Azure US Government regions:

| FQDN | IP Address |
| ----- | ----- |
| `52882c08-ead2-44aa-af65-08a75cf094bd.workspace.chinaeast2.api.ml.azure.us` | `10.1.0.5` |
| `52882c08-ead2-44aa-af65-08a75cf094bd.workspace.chinaeast2.cert.api.ml.azure.us` | `10.1.0.5` |
| `ml-mype-plt-usgovvirginia-52882c08-ead2-44aa-af65-08a75cf094bd.usgovvirginia.notebooks.usgovcloudapi.net` | `10.1.0.6` |
| `*.usgovvirginia.inference.ml.azure.us` | `10.1.0.7` |

> [!NOTE]
> Managed online endpoints share the workspace private endpoint. If you are manually adding DNS records to the private DNS zone `privatelink.api.azureml.ms`, an A record with wildcard
> `*.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.azureml.ms` should be added to route all endpoints under the workspace to the private endpoint.

<a id='dns-vnet'></a>

### Create A records in custom DNS server

Once the list of FQDNs and corresponding IP addresses are gathered, proceed to create A records in the configured DNS Server. Refer to the documentation for your DNS server to determine how to create A records. Note it is recommended to create a unique zone for the entire FQDN, and create the A record in the root of the zone.

## Example: Custom DNS Server hosted in VNet

This architecture uses the common Hub and Spoke virtual network topology. One virtual network contains the DNS server and one contains the private endpoint to the Azure Machine Learning workspace and associated resources. There must be a valid route between both virtual networks. For example, through a series of peered virtual networks.

:::image type="content" source="./media/how-to-custom-dns/custom-dns-topology.svg" alt-text="Diagram of custom DNS hosted in Azure topology"  lightbox ="./media/how-to-custom-dns/custom-dns-topology-expanded.png":::

The following steps describe how this topology works:

1. **Create Private DNS Zone and link to DNS Server Virtual Network**:

    The first step in ensuring a Custom DNS solution works with your Azure Machine Learning workspace is to create two Private DNS Zones rooted at the following domains:

    **Azure Public regions**:
    - ```privatelink.api.azureml.ms```
    - ```privatelink.notebooks.azure.net```
