    The client will first start by querying On-premises DNS Server for the address of the following FQDNs:

    **Azure Public regions**:
    - ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.azureml.ms```
    - ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.azure.net```
    - ```<managed online endpoint name>.<region>.inference.ml.azure.com``` - Used by managed online endpoints

    **Azure China regions**:
    - ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.ml.azure.cn```
    - ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.chinacloudapi.cn```
    - ```<managed online endpoint name>.<region>.inference.ml.azure.cn``` - Used by managed online endpoints

    **Azure US Government regions**:
    - ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.ml.azure.us```
    - ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.usgovcloudapi.net```
    - ```<managed online endpoint name>.<region>.inference.ml.azure.us``` - Used by managed online endpoints

6. **On-premises DNS server recursively resolves workspace domain**:

    The on-premises DNS Server will resolve the FQDNs from step 5 from the DNS Server. Because there is a conditional forwarder (step 4), the on-premises DNS Server will send the request to the DNS Server for resolution.

7. **DNS Server resolves workspace domain to CNAME from Azure DNS**:

    The DNS server will resolve the FQDNs from step 5 from the Azure DNS. Azure DNS will respond with one of the domains listed in step 1.

8. **On-premises DNS Server recursively resolves workspace domain CNAME record from DNS Server**:

    On-premises DNS Server will proceed to recursively resolve the CNAME received in step 7. Because there was a conditional forwarder setup in step 4, On-premises DNS Server will send the request to DNS Server for resolution.

9. **DNS Server recursively resolves workspace domain CNAME record from Azure DNS**:

    DNS Server will proceed to recursively resolve the CNAME received in step 7. Because there was a conditional forwarder setup in step 3, DNS Server will send the request to the Azure DNS Virtual Server IP address for resolution.

10. **Azure DNS returns records from Private DNS zone**:

    The corresponding records stored in the Private DNS Zones will be returned to DNS Server, which will mean the Azure DNS Virtual Server returns the IP addresses of the Private Endpoint.

11. **On-premises DNS Server resolves workspace domain name to private endpoint address**:

    The query from On-premises DNS Server to DNS Server in step 8 ultimately returns the IP addresses associated with the Private Endpoint to the Azure Machine Learning workspace. These IP addresses are returned to the original client, which will now communicate with the Azure Machine Learning workspace over the Private Endpoint configured in step 1.

<a id="hosts"></a>
## Example: Hosts file

The `hosts` file is a text document that Linux, macOS, and Windows all use to override name resolution for the local computer. The file contains a list of IP addresses and the corresponding host name. When the local computer tries to resolve a host name, if the host name is listed in the `hosts` file, the name is resolved to the corresponding IP address.

> [!IMPORTANT]
> The `hosts` file only overrides name resolution for the local computer. If you want to use a `hosts` file with multiple computers, you must modify it individually on each computer.

The following table lists the location of the `hosts` file:

| Operating system | Location |
| ----- | ----- |
| Linux | `/etc/hosts` |
| macOS | `/etc/hosts` |
| Windows | `%SystemRoot%\System32\drivers\etc\hosts` |

> [!TIP]
> The name of the file is `hosts` with no extension. When editing the file, use administrator access. For example, on Linux or macOS you might use `sudo vi`. On Windows, run notepad as an administrator.
