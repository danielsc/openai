1. If the `nslookup` command returns an error, or returns a different IP address than displayed in the portal, then the custom DNS solution isn't configured correctly. For more information, see [How to use your workspace with a custom DNS server](how-to-custom-dns.md)

### Azure DNS troubleshooting

When using Azure DNS for name resolution, use the following steps to verify that the Private DNS integration is configured correctly:

1. On the Private Endpoint, select __DNS configuration__. For each entry in the __Private DNS zone__ column, there should also be an entry in the __DNS zone group__ column. 

    :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/dns-zone-group.png" alt-text="Screenshot of the DNS configuration with Private DNS zone and group highlighted.":::

    * If there's a Private DNS zone entry, but __no DNS zone group entry__, delete and recreate the Private Endpoint. When recreating the private endpoint, __enable Private DNS zone integration__.
    * If __DNS zone group__ isn't empty, select the link for the __Private DNS zone__ entry.
    
        From the Private DNS zone, select __Virtual network links__. There should be a link to the VNet. If there isn't one, then delete and recreate the private endpoint. When recreating it, select a Private DNS Zone linked to the VNet or create a new one that is linked to it.

        :::image type="content" source="./media/how-to-troubleshoot-secure-connection-workspace/virtual-network-links.png" alt-text="Screenshot of the virtual network links for the Private DNS zone.":::

1. Repeat the previous steps for the rest of the Private DNS zone entries.

## Browser configuration (DNS over HTTPS)

Check if DNS over HTTP is enabled in your web browser. DNS over HTTP can prevent Azure DNS from responding with the IP address of the Private Endpoint.

* Mozilla Firefox: For more information, see [Disable DNS over HTTPS in Firefox](https://support.mozilla.org/en-US/kb/firefox-dns-over-https).
* Microsoft Edge:
    1. Search for DNS in Microsoft Edge settings: image.png
    2. Disable __Use secure DNS to specify how to look up the network address for websites__.

## Proxy configuration

If you use a proxy, it may prevent communication with a secured workspace. To test, use one of the following options:

* Temporarily disable the proxy setting and see if you can connect.
* Create a [Proxy auto-config (PAC)](https://wikipedia.org/wiki/Proxy_auto-config) file that allows direct access to the FQDNs listed on the private endpoint. It should also allow direct access to the FQDN for any compute instances.
* Configure your proxy server to forward DNS requests to Azure DNS.



