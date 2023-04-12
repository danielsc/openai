    **Azure Public regions**:
    - ```privatelink.api.azureml.ms```
    - ```privatelink.notebooks.azure.net```

    **Azure China regions**:
    - ```privatelink.api.ml.azure.cn```
    - ```privatelink.notebooks.chinacloudapi.cn```

    **Azure US Government regions**:
    - ```privatelink.api.ml.azure.us```
    - ```privatelink.notebooks.usgovcloudapi.net```

    > [!NOTE]
    > Managed online endpoints share the workspace private endpoint. If you are manually adding DNS records to the private DNS zone `privatelink.api.azureml.ms`, an A record with wildcard
    > `*.<per-workspace globally-unique identifier>.inference.<region>.privatelink.api.azureml.ms` should be added to route all endpoints under the workspace to the private endpoint.

    Following creation of the Private DNS Zone, it needs to be linked to the DNS Server Virtual Network. The Virtual Network that contains the DNS Server.

    A Private DNS Zone overrides name resolution for all names within the scope of the root of the zone. This override applies to all Virtual Networks the Private DNS Zone is linked to. For example, if a Private DNS Zone rooted at `privatelink.api.azureml.ms` is linked to Virtual Network foo, all resources in Virtual Network foo that attempt to resolve `bar.workspace.westus2.privatelink.api.azureml.ms` will receive any record that is listed in the `privatelink.api.azureml.ms` zone.

    However, records listed in Private DNS Zones are only returned to devices resolving domains using the default Azure DNS Virtual Server IP address. So the custom DNS Server will resolve domains for devices spread throughout your network topology. But the custom DNS Server will need to resolve Azure Machine Learning-related domains against the Azure DNS Virtual Server IP address.

2. **Create private endpoint with private DNS integration targeting Private DNS Zone linked to DNS Server Virtual Network**:

    The next step is to create a Private Endpoint to the Azure Machine Learning workspace. The private endpoint targets both Private DNS Zones created in step 1. This ensures all communication with the workspace is done via the Private Endpoint in the Azure Machine Learning Virtual Network.

    > [!IMPORTANT]
    > The private endpoint must have Private DNS integration enabled for this example to function correctly.

3. **Create conditional forwarder in DNS Server to forward to Azure DNS**:

    Next, create a conditional forwarder to the Azure DNS Virtual Server. The conditional forwarder ensures that the DNS server always queries the Azure DNS Virtual Server IP address for FQDNs related to your workspace. This means that the DNS Server will return the corresponding record from the Private DNS Zone.

    The zones to conditionally forward are listed below. The Azure DNS Virtual Server IP address is 168.63.129.16:

    **Azure Public regions**:
    - ```api.azureml.ms```
    - ```notebooks.azure.net```
    - ```instances.azureml.ms```
    - ```aznbcontent.net```
    - ```inference.ml.azure.com``` - Used by managed online endpoints

    **Azure China regions**:
    - ```api.ml.azure.cn```
    - ```notebooks.chinacloudapi.cn```
    - ```instances.azureml.cn```
    - ```aznbcontent.net```
    - ```inference.ml.azure.cn``` - Used by managed online endpoints

    **Azure US Government regions**:
    - ```api.ml.azure.us```
    - ```notebooks.usgovcloudapi.net```
    - ```instances.azureml.us```
    - ```aznbcontent.net```
    - ```inference.ml.azure.us``` - Used by managed online endpoints

    > [!IMPORTANT]
    > Configuration steps for the DNS Server are not included here, as there are many DNS solutions available that can be used as a custom DNS Server. Refer to the documentation for your DNS solution for how to appropriately configure conditional forwarding.

4. **Resolve workspace domain**:

    At this point, all setup is done. Now any client that uses DNS Server for name resolution and has a route to the Azure Machine Learning Private Endpoint can proceed to access the workspace.
