
# Troubleshoot connection to a workspace with a private endpoint

When connecting to a workspace that has been configured with a private endpoint, you may encounter a 403 or a messaging saying that access is forbidden. Use the information in this article to check for common configuration problems that can cause this error.

> [!TIP]
> Before using the steps in this article, try the Azure Machine Learning workspace diagnostic API. It can help identify configuration problems with your workspace. For more information, see [How to use workspace diagnostics](how-to-workspace-diagnostic-api.md).

## DNS configuration

The troubleshooting steps for DNS configuration differ based on whether you're using Azure DNS or a custom DNS. Use the following steps to determine which one you're using:

1. In the [Azure portal](https://portal.azure.com), select the private endpoint for your Azure Machine Learning workspace.
1. From the __Overview__ page, select the __Network Interface__ link.

    :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/private-endpoint-overview.png" alt-text="Screenshot of the private endpoint overview with network interface link highlighted.":::

1. Under __Settings__, select __IP Configurations__ and then select the __Virtual network__ link.

    :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/network-interface-ip-configurations.png" alt-text="Screenshot of the IP configuration with virtual network link highlighted.":::

1. From the __Settings__ section on the left of the page, select the __DNS servers__ entry.

    :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/dns-servers.png" alt-text="Screenshot of the DNS servers configuration.":::

    * If this value is __Default (Azure-provided)__ or __168.63.129.16__, then the VNet is using Azure DNS. Skip to the [Azure DNS troubleshooting](#azure-dns-troubleshooting) section.
    * If there's a different IP address listed, then the VNet is using a custom DNS solution. Skip to the [Custom DNS troubleshooting](#custom-dns-troubleshooting) section.

### Custom DNS troubleshooting

Use the following steps to verify if your custom DNS solution is correctly resolving names to IP addresses:

1. From a virtual machine, laptop, desktop, or other compute resource that has a working connection to the private endpoint, open a web browser. In the browser, use the URL for your Azure region:

    | Azure region | URL |
    | ----- | ----- |
    | Azure Government | https://portal.azure.us/?feature.privateendpointmanagedns=false |
    | Azure China 21Vianet | https://portal.azure.cn/?feature.privateendpointmanagedns=false |
    | All other regions | https://portal.azure.com/?feature.privateendpointmanagedns=false |

1. In the portal, select the private endpoint for the workspace. Make a list of FQDNs listed for the private endpoint.

    :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/custom-dns-settings.png" alt-text="Screenshot of the private endpoint with custom DNS settings highlighted.":::

1. Open a command prompt, PowerShell, or other command line and run the following command for each FQDN returned from the previous step. Each time you run the command, verify that the IP address returned matches the IP address listed in the portal for the FQDN: 

    `nslookup <fqdn>`

    For example, running the command `nslookup 29395bb6-8bdb-4737-bf06-848a6857793f.workspace.eastus.api.azureml.ms` would return a value similar to the following text:

    ```
    Server: yourdnsserver
    Address: yourdnsserver-IP-address

    Name:   29395bb6-8bdb-4737-bf06-848a6857793f.workspace.eastus.api.azureml.ms
    Address: 10.3.0.5
    ```

1. If the `nslookup` command returns an error, or returns a different IP address than displayed in the portal, then the custom DNS solution isn't configured correctly. For more information, see [How to use your workspace with a custom DNS server](how-to-custom-dns.md)
