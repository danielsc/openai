1. In the form that appears, expand the __Services__ dropdown and then enable __Microsoft.Storage__. Select __Save__ to save these changes.
1. Apply the service endpoint policy to your workspace subnet.

:::image type="content" source="media/how-to-data-exfiltration-prevention/enable-storage-endpoint-for-subnet.png" alt-text="A screenshot of the Azure portal showing how to enable storage endpoint for the subnet." lightbox="media/how-to-data-exfiltration-prevention/enable-storage-endpoint-for-subnet.png":::

## 4. Curated environments

When using Azure ML curated environments, make sure to use the latest environment version. The container registry for the environment must also be `mcr.microsoft.com`. To check the container registry, use the following steps:

1. From [Azure ML studio](https://ml.azure.com), select your workspace and then select __Environments__.
1. Verify that the __Azure container registry__ begins with a value of `mcr.microsoft.com`.

    > [!IMPORTANT]
    > If the container registry is `viennaglobal.azurecr.io` you cannot use the curated environment with the data exfiltration. Try upgrading to the latest version of the curated environment.

1. When using `mcr.microsoft.com`, you must also allow outbound configuration to the following resources. Select the configuration option that you're using:

    # [Service tag/NSG](#tab/servicetag)

    __Allow__ outbound traffic over __TCP port 443__ to the following service tags. Replace `<region>` with the Azure region that contains your compute cluster or instance.

    * `MicrosoftContainerRegistry.<region>`
    * `AzureFrontDoor.FirstParty`

    # [Firewall](#tab/firewall)

    __Allow__ outbound traffic over __TCP port 443__ to the following FQDNs:

    * `mcr.microsoft.com`
    * `*.data.mcr.microsoft.com`


## Next steps

For more information, see the following articles:

* [How to configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md)
* [Azure Batch simplified node communication](../batch/simplified-compute-node-communication.md)
