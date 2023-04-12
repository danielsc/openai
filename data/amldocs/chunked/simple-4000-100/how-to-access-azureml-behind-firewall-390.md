| Your storage account | `<storage>.blob.core.chinacloudapi.cn` | TCP | 443 |
| Azure Key Vault | `*.vault.azure.cn` | TCP | 443 |


__Docker images maintained by by Azure Machine Learning__

| __Required for__ | __Hosts__ | __Protocol__ | __Ports__ |
| ----- | ----- | ----- | ----- |
| Microsoft Container Registry | mcr.microsoft.com</br>\*.data.mcr.microsoft.com | TCP | 443 |

> [!TIP]
> * __Azure Container Registry__ is required for any custom Docker image. This includes small modifications (such as additional packages) to base images provided by Microsoft. It is also required by the internal training job submission process of Azure Machine Learning.
> * __Microsoft Container Registry__ is only needed if you plan on using the _default Docker images provided by Microsoft_, and _enabling user-managed dependencies_.
> * If you plan on using federated identity, follow the [Best practices for securing Active Directory Federation Services](/windows-server/identity/ad-fs/deployment/best-practices-securing-ad-fs) article.

Also, use the information in the [compute with public IP](#scenario-using-compute-cluster-or-compute-instance-with-a-public-ip) section to add IP addresses for `BatchNodeManagement` and `AzureMachineLearning`.

For information on restricting access to models deployed to AKS, see [Restrict egress traffic in Azure Kubernetes Service](../aks/limit-egress-traffic.md).

__Monitoring, metrics, and diagnostics__

To support logging of metrics and other monitoring information to Azure Monitor and Application Insights, allow outbound traffic to the following hosts:

> [!NOTE]
> The information logged to these hosts is also used by Microsoft Support to be able to diagnose any problems you run into with your workspace.

* `dc.applicationinsights.azure.com`
* `dc.applicationinsights.microsoft.com`
* `dc.services.visualstudio.com`
* `*.in.applicationinsights.azure.com`

For a list of IP addresses for these hosts, see [IP addresses used by Azure Monitor](../azure-monitor/app/ip-addresses.md).

## Next steps

This article is part of a series on securing an Azure Machine Learning workflow. See the other articles in this series:

* [Virtual network overview](how-to-network-security-overview.md)
* [Secure the workspace resources](how-to-secure-workspace-vnet.md)
* [Secure the training environment](how-to-secure-training-vnet.md)
* [Secure the inference environment](how-to-secure-inferencing-vnet.md)
* [Enable studio functionality](how-to-enable-studio-virtual-network.md)
* [Use custom DNS](how-to-custom-dns.md)

For more information on configuring Azure Firewall, see [Tutorial: Deploy and configure Azure Firewall using the Azure portal](../firewall/tutorial-firewall-deploy-portal.md).