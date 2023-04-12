    > The workspace name for this FQDN may be truncated. Truncation is done to keep `ml-<workspace-name, truncated>-<region>-<workspace-guid>` at 63 characters or less.
* `<instance-name>.<region>.instances.azureml.ms`

    > [!NOTE]
    > * Compute instances can be accessed only from within the virtual network.
    > * The IP address for this FQDN is **not** the IP of the compute instance. Instead, use the private IP address of the workspace private endpoint (the IP of the `*.api.azureml.ms` entries.)

* `<managed online endpoint name>.<region>.inference.ml.azure.com` - Used by managed online endpoints

#### Azure China region

The following FQDNs are for Azure China regions:

* `<workspace-GUID>.workspace.<region>.cert.api.ml.azure.cn`
* `<workspace-GUID>.workspace.<region>.api.ml.azure.cn`
* `ml-<workspace-name, truncated>-<region>-<workspace-guid>.<region>.notebooks.chinacloudapi.cn`

    > [!NOTE]
    > The workspace name for this FQDN may be truncated. Truncation is done to keep `ml-<workspace-name, truncated>-<region>-<workspace-guid>` at 63 characters or less.

* `<instance-name>.<region>.instances.azureml.cn`

   * The IP address for this FQDN is **not** the IP of the compute instance. Instead, use the private IP address of the workspace private endpoint (the IP of the `*.api.azureml.ms` entries.)

* `<managed online endpoint name>.<region>.inference.ml.azure.cn` - Used by managed online endpoints

#### Azure US Government

The following FQDNs are for Azure US Government regions:

* `<workspace-GUID>.workspace.<region>.cert.api.ml.azure.us`
* `<workspace-GUID>.workspace.<region>.api.ml.azure.us`
* `ml-<workspace-name, truncated>-<region>-<workspace-guid>.<region>.notebooks.usgovcloudapi.net`

    > [!NOTE]
    > The workspace name for this FQDN may be truncated. Truncation is done to keep `ml-<workspace-name, truncated>-<region>-<workspace-guid>` at 63 characters or less.
* `<instance-name>.<region>.instances.azureml.us`
    > * The IP address for this FQDN is **not** the IP of the compute instance. Instead, use the private IP address of the workspace private endpoint (the IP of the `*.api.azureml.ms` entries.)

* `<managed online endpoint name>.<region>.inference.ml.azure.us` - Used by managed online endpoints

### Find the IP addresses

To find the internal IP addresses for the FQDNs in the VNet, use one of the following methods:

> [!NOTE]
> The fully qualified domain names and IP addresses will be different based on your configuration. For example, the GUID value in the domain name will be specific to your workspace.

# [Azure CLI](#tab/azure-cli)

1. To get the ID of the private endpoint network interface, use the following command:

    ```azurecli
    az network private-endpoint show --name <endpoint> --resource-group <resource-group> --query 'networkInterfaces[*].id' --output table
    ```

1. To get the IP address and FQDN information, use the following command. Replace `<resource-id>` with the ID from the previous step:

    ```azurecli
    az network nic show --ids <resource-id> --query 'ipConfigurations[*].{IPAddress: privateIpAddress, FQDNs: privateLinkConnectionProperties.fqdns}'
    ```

    The output will be similar to the following text:

    ```json
    [
        {
            "FQDNs": [
            "fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.api.azureml.ms",
            "fb7e20a0-8891-458b-b969-55ddb3382f51.workspace.eastus.cert.api.azureml.ms"
            ],
            "IPAddress": "10.1.0.5"
        },
        {
            "FQDNs": [
            "ml-myworkspace-eastus-fb7e20a0-8891-458b-b969-55ddb3382f51.eastus.notebooks.azure.net"
            ],
            "IPAddress": "10.1.0.6"
        },
        {
            "FQDNs": [
            "*.eastus.inference.ml.azure.com"
            ],
            "IPAddress": "10.1.0.7"
        }
    ]
    ```
# [Azure PowerShell](#tab/azure-powershell)

```azurepowershell
$workspaceDns=Get-AzPrivateEndpoint -Name <endpoint> -resourcegroupname <resource-group>
$workspaceDns.CustomDnsConfigs | format-table
```
