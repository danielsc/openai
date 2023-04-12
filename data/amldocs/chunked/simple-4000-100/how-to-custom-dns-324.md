    At this point, all setup is done. Now any client that uses DNS Server for name resolution and has a route to the Azure Machine Learning Private Endpoint can proceed to access the workspace.
    The client will first start by querying DNS Server for the address of the following FQDNs:

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

5. **Azure DNS recursively resolves workspace domain to CNAME**:

    The DNS Server will resolve the FQDNs from step 4 from Azure DNS. Azure DNS will respond with one of the domains listed in step 1.

6. **DNS Server recursively resolves workspace domain CNAME record from Azure DNS**:

    DNS Server will proceed to recursively resolve the CNAME received in step 5. Because there was a conditional forwarder setup in step 3, DNS Server will send the request to the Azure DNS Virtual Server IP address for resolution.

7. **Azure DNS returns records from Private DNS zone**:

    The corresponding records stored in the Private DNS Zones will be returned to DNS Server, which will mean Azure DNS Virtual Server returns the IP addresses of the Private Endpoint.

8. **Custom DNS Server resolves workspace domain name to private endpoint address**:

    Ultimately the Custom DNS Server now returns the IP addresses of the Private Endpoint to the client from step 4. This ensures that all traffic to the Azure Machine Learning workspace is via the Private Endpoint.

#### Troubleshooting

If you cannot access the workspace from a virtual machine or jobs fail on compute resources in the virtual network, use the following steps to identify the cause:

1. **Locate the workspace FQDNs on the Private Endpoint**:

    Navigate to the Azure portal using one of the following links:
    - [Azure Public regions](https://portal.azure.com/?feature.privateendpointmanagedns=false)
    - [Azure China regions](https://portal.azure.cn/?feature.privateendpointmanagedns=false)
    - [Azure US Government regions](https://portal.azure.us/?feature.privateendpointmanagedns=false)

    Navigate to the Private Endpoint to the Azure Machine Learning workspace. The workspace FQDNs will be listed on the “Overview” tab.

1. **Access compute resource in Virtual Network topology**:

    Proceed to access a compute resource in the Azure Virtual Network topology. This will likely require accessing a Virtual Machine in a Virtual Network that is peered with the Hub Virtual Network.

1. **Resolve workspace FQDNs**:

    Open a command prompt, shell, or PowerShell. Then for each of the workspace FQDNs, run the following command:

    `nslookup <workspace FQDN>`

    The result of each nslookup should return one of the two private IP addresses on the Private Endpoint to the Azure Machine Learning workspace. If it does not, then there is something misconfigured in the custom DNS solution.

    Possible causes:
    - The compute resource running the troubleshooting commands is not using DNS Server for DNS resolution
