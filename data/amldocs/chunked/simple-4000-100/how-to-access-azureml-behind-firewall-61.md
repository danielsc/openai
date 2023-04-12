| `AzureMachineLearning` | 443, 8787, 18881<br>UDP: 5831 | Using Azure Machine Learning services. |
| `BatchNodeManagement.<region>` | 443 | Communication Azure Batch. |
| `AzureResourceManager` | 443 | Creation of Azure resources with Azure Machine Learning. |
| `Storage.<region>` | 443 | Access data stored in the Azure Storage Account for compute cluster and compute instance. This outbound can be used to exfiltrate data. For more information, see [Data exfiltration protection](how-to-prevent-data-loss-exfiltration.md). |
| `AzureFrontDoor.FrontEnd`</br>* Not needed in Azure China. | 443 | Global entry point for [Azure Machine Learning studio](https://ml.azure.com). Store images and environments for AutoML. |
| `MicrosoftContainerRegistry.<region>` | 443 | Access docker images provided by Microsoft. |
| `Frontdoor.FirstParty` | 443 | Access docker images provided by Microsoft. |
| `AzureMonitor` | 443 | Used to log monitoring and metrics to Azure Monitor. |

> [!IMPORTANT]
  > If a compute instance or compute cluster is configured for no public IP, they can't access the public internet by default. However, they do need to communicate with the resources listed above. To enable outbound communication, you have two possible options:
  >
  > * __User-defined route and firewall__: Create a user-defined route in the subnet that contains the compute. The __Next hop__ for the route should reference the private IP address of the firewall, with an address prefix of 0.0.0.0/0.
  > * __Azure Virtual Network NAT with a public IP__: For more information on using Virtual Network Nat, see the [Virtual Network NAT](/azure/virtual-network/nat-gateway/nat-overview) documentation.

### Recommended configuration for training and deploying models

__Outbound traffic__

| Service tag(s) | Ports | Purpose |
| ----- |:-----:| ----- |
| `MicrosoftContainerRegistry.<region>` and `AzureFrontDoor.FirstParty` | 443 | Allows use of Docker images that Microsoft provides for training and inference. Also sets up the Azure Machine Learning router for Azure Kubernetes Service. |

__To allow installation of Python packages for training and deployment__, allow __outbound__ traffic to the following host names:

> [!NOTE]
> This is not a complete list of the hosts required for all Python resources on the internet, only the most commonly used. For example, if you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario.

| __Host name__ | __Purpose__ |
| ---- | ---- |
| `anaconda.com`<br>`*.anaconda.com` | Used to install default packages. |
| `*.anaconda.org` | Used to get repo data. |
| `pypi.org` | Used to list dependencies from the default index, if any, and the index isn't overwritten by user settings. If the index is overwritten, you must also allow `*.pythonhosted.org`. |
| `*pytorch.org` | Used by some examples based on PyTorch. |
| `*.tensorflow.org` | Used by some examples based on Tensorflow. |

## Scenario: Install RStudio on compute instance

To allow installation of RStudio on a compute instance, the firewall needs to allow outbound access to the sites to pull the Docker image from. Add the following Application rule to your Azure Firewall policy: 

* __Name__: AllowRStudioInstall 
* __Source Type__: IP Address 
* __Source IP Addresses__: The IP address range of the subnet where you will create the compute instance. For example, `172.16.0.0/24`. 
* __Destination Type__: FQDN 
* __Target FQDN__: `ghcr.io`, `pkg-containers.githubusercontent.com` 
* __Protocol__: `Https:443`
 
To allow the installation of R packages, allow __outbound__ traffic to `cloud.r-project.org`. This host is used for installing CRAN packages.

> [!NOTE]
> If you need access to a GitHub repository or other host, you must identify and add the required hosts for that scenario.

## Scenario: Using compute cluster or compute instance with a public IP

[!INCLUDE [udr info for computes](../../includes/machine-learning-compute-user-defined-routes.md)]
