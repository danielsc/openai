    The next step is to create a Private Endpoint to the Azure Machine Learning workspace. The private endpoint targets both Private DNS Zones created in step 1. This ensures all communication with the workspace is done via the Private Endpoint in the Azure Machine Learning Virtual Network.

    > [!IMPORTANT]
    > The private endpoint must have Private DNS integration enabled for this example to function correctly.

3. **Create conditional forwarder in DNS Server to forward to Azure DNS**:

    Next, create a conditional forwarder to the Azure DNS Virtual Server. The conditional forwarder ensures that the DNS server always queries the Azure DNS Virtual Server IP address for FQDNs related to your workspace. This means that the DNS Server will return the corresponding record from the Private DNS Zone.

    The zones to conditionally forward are listed below. The Azure DNS Virtual Server IP address is 168.63.129.16.

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

4. **Create conditional forwarder in On-premises DNS Server to forward to DNS Server**:

    Next, create a conditional forwarder to the DNS Server in the DNS Server Virtual Network. This forwarder is for the zones listed in step 1. This is similar to step 3, but, instead of forwarding to the Azure DNS Virtual Server IP address, the On-premises DNS Server will be targeting the IP address of the DNS Server. As the On-premises DNS Server is not in Azure, it is not able to directly resolve records in Private DNS Zones. In this case the DNS Server proxies requests from the On-premises DNS Server to the Azure DNS Virtual Server IP. This allows the On-premises DNS Server to retrieve records in the Private DNS Zones linked to the DNS Server Virtual Network.

    The zones to conditionally forward are listed below. The IP addresses to forward to are the IP addresses of your DNS Servers:

    **Azure Public regions**:
    - ```api.azureml.ms```
    - ```notebooks.azure.net```
    - ```instances.azureml.ms```
    - ```inference.ml.azure.com``` - Used by managed online endpoints

    **Azure China regions**:
    - ```api.ml.azure.cn```
    - ```notebooks.chinacloudapi.cn```
    - ```instances.azureml.cn```
    - ```inference.ml.azure.cn``` - Used by managed online endpoints

    **Azure US Government regions**:
    - ```api.ml.azure.us```
    - ```notebooks.usgovcloudapi.net```
    - ```instances.azureml.us```
    - ```inference.ml.azure.us``` - Used by managed online endpoints

    > [!IMPORTANT]
    > Configuration steps for the DNS Server are not included here, as there are many DNS solutions available that can be used as a custom DNS Server. Refer to the documentation for your DNS solution for how to appropriately configure conditional forwarding.

5. **Resolve workspace domain**:

    At this point, all setup is done. Any client that uses on-premises DNS Server for name resolution, and has a route to the Azure Machine Learning Private Endpoint, can proceed to access the workspace.

    The client will first start by querying On-premises DNS Server for the address of the following FQDNs:
