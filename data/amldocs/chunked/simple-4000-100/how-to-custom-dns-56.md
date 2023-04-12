- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.ml.azure.cn```
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.cert.api.ml.azure.cn```
- ```<compute instance name>.<region the workspace was created in>.instances.azureml.cn```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.chinacloudapi.cn```
- ```<managed online endpoint name>.<region>.inference.ml.azure.cn``` - Used by managed online endpoints

**Azure US Government regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.api.ml.azure.us```
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.cert.api.ml.azure.us```
- ```<compute instance name>.<region the workspace was created in>.instances.azureml.us```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.notebooks.usgovcloudapi.net```
- ```<managed online endpoint name>.<region>.inference.ml.azure.us``` - Used by managed online endpoints

The Fully Qualified Domains resolve to the following Canonical Names (CNAMEs) called the workspace Private Link FQDNs:

**Azure Public regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.privatelink.api.azureml.ms```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.privatelink.notebooks.azure.net```
- ```<managed online endpoint name>.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.azureml.ms``` - Used by managed online endpoints

**Azure China regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.privatelink.api.ml.azure.cn```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.privatelink.notebooks.chinacloudapi.cn```
- ```<managed online endpoint name>.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.ml.azure.cn``` - Used by managed online endpoints

**Azure US Government regions**:
- ```<per-workspace globally-unique identifier>.workspace.<region the workspace was created in>.privatelink.api.ml.azure.us```
- ```ml-<workspace-name, truncated>-<region>-<per-workspace globally-unique identifier>.<region>.privatelink.notebooks.usgovcloudapi.net```
- ```<managed online endpoint name>.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.ml.azure.us``` - Used by managed online endpoints

The FQDNs resolve to the IP addresses of the Azure Machine Learning workspace in that region. However, resolution of the workspace Private Link FQDNs can be overridden by using a custom DNS server hosted in the virtual network. For an example of this architecture, see the [custom DNS server hosted in a vnet](#example-custom-dns-server-hosted-in-vnet) example.

> [!NOTE]
> Managed online endpoints share the workspace private endpoint. If you are manually adding DNS records to the private DNS zone `privatelink.api.azureml.ms`, an A record with wildcard
> `*.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.azureml.ms` should be added to route all endpoints under the workspace to the private endpoint.

## Manual DNS server integration

This section discusses which Fully Qualified Domains to create A records for in a DNS Server, and which IP address to set the value of the A record to.

### Retrieve Private Endpoint FQDNs

#### Azure Public region

The following list contains the fully qualified domain names (FQDNs) used by your workspace if it is in the Azure Public Cloud:

* `<workspace-GUID>.workspace.<region>.cert.api.azureml.ms`
* `<workspace-GUID>.workspace.<region>.api.azureml.ms`
* `ml-<workspace-name, truncated>-<region>-<workspace-guid>.<region>.notebooks.azure.net`

    > [!NOTE]
    > The workspace name for this FQDN may be truncated. Truncation is done to keep `ml-<workspace-name, truncated>-<region>-<workspace-guid>` at 63 characters or less.
