> The name of the file is `hosts` with no extension. When editing the file, use administrator access. For example, on Linux or macOS you might use `sudo vi`. On Windows, run notepad as an administrator.

The following is an example of `hosts` file entries for Azure Machine Learning:

```
# For core Azure Machine Learning hosts
10.1.0.5    fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.api.azureml.ms
10.1.0.5    fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.cert.api.azureml.ms
10.1.0.6    ml-myworkspace-eastus-fb7e20a0-8891-458b-b969-55ddb3382f51.eastus.notebooks.azure.net

# For a managed online/batch endpoint named 'mymanagedendpoint'
10.1.0.7    mymanagedendpoint.eastus.inference.ml.azure.com

# For a compute instance named 'mycomputeinstance'
10.1.0.5    mycomputeinstance.eastus.instances.azureml.ms
```

For more information on the `hosts` file, see [https://wikipedia.org/wiki/Hosts_(file)](https://wikipedia.org/wiki/Hosts_(file)).

## Dependency services DNS resolution

The services that your workspace relies on may also be secured using a private endpoint. If so, then you may need to create a custom DNS record if you need to directly communicate with the service. For example, if you want to directly work with the data in an Azure Storage Account used by your workspace.

> [!NOTE]
> Some services have multiple private-endpoints for sub-services or features. For example, an Azure Storage Account may have individual private endpoints for Blob, File, and DFS. If you need to access both Blob and File storage, then you must enable resolution for each specific private endpoint.

For more information on the services and DNS resolution, see [Azure Private Endpoint DNS configuration](../private-link/private-endpoint-dns.md).

## Troubleshooting

If after running through the above steps you are unable to access the workspace from a virtual machine or jobs fail on compute resources in the Virtual Network containing the Private Endpoint to the Azure Machine learning workspace, follow the below steps to try to identify the cause.

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

    The result of each nslookup should yield one of the two private IP addresses on the Private Endpoint to the Azure Machine Learning workspace. If it does not, then there is something misconfigured in the custom DNS solution.

    Possible causes:
    - The compute resource running the troubleshooting commands is not using DNS Server for DNS resolution
    - The Private DNS Zones chosen when creating the Private Endpoint are not linked to the DNS Server VNet
    - Conditional forwarders from DNS Server to Azure DNS Virtual Server IP were not configured correctly
    - Conditional forwarders from On-premises DNS Server to DNS Server were not configured correctly

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the workspace resources](how-to-secure-workspace-vnet.md)
