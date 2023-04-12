    | `Storage.<region>` | TCP | 443 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. This service tag is used to communicate with the Azure Storage account used by Azure Batch. |

    > [!IMPORTANT]
    > The outbound access to `Storage.<region>` could potentially be used to exfiltrate data from your workspace. By using a Service Endpoint Policy, you can mitigate this vulnerability. For more information, see the [Azure Machine Learning data exfiltration prevention](how-to-prevent-data-loss-exfiltration.md) article.

    | FQDN | Protocol | Port | Notes |
    | ---- |:----:|:----:| ---- |
    | `<region>.tundra.azureml.ms` | UDP | 5831 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. |
    | `graph.windows.net` | TCP | 443 | Communication with the Microsoft Graph API.|
    | `*.instances.azureml.ms` | TCP | 443/8787/18881 | Communication with Azure Machine Learning. |
    | `<region>.batch.azure.com` | ANY | 443 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. Communication with Azure Batch. |
    | `<region>.service.batch.com` | ANY | 443 | Replace `<region>` with the Azure region that contains your Azure Machine learning workspace. Communication with Azure Batch. |
    | `*.blob.core.windows.net` | TCP | 443 | Communication with Azure Blob storage. |
    | `*.queue.core.windows.net` | TCP | 443 | Communication with Azure Queue storage. |
    | `*.table.core.windows.net` | TCP | 443 | Communication with Azure Table storage. |


+ Create either a firewall and outbound rules or a NAT gateway and network service groups to allow outbound traffic. Since the compute has no public IP address, it can't communicate with resources on the public internet without this configuration. For example, it wouldn't be able to communicate with Azure Active Directory or Azure Resource Manager. Installing Python packages from public sources would also require this configuration. 

    For more information on the outbound traffic that is used by Azure Machine Learning, see the following articles:
    - [Configure inbound and outbound network traffic](how-to-access-azureml-behind-firewall.md).
    - [Azure's outbound connectivity methods](/azure/load-balancer/load-balancer-outbound-connections#scenarios).

    For more information on service tags that can be used with Azure Firewall, see the [Virtual network service tags](/azure/virtual-network/service-tags-overview) article.

Use the following information to create a compute instance or cluster with no public IP address:

# [Azure CLI](#tab/cli)

In the `az ml compute create` command, replace the following values:

* `rg`: The resource group that the compute will be created in.
* `ws`: The Azure Machine Learning workspace name.
* `yourvnet`: The Azure Virtual Network.
* `yoursubnet`: The subnet to use for the compute.
* `AmlCompute` or `ComputeInstance`: Specifying `AmlCompute` creates a *compute cluster*. `ComputeInstance` creates a *compute instance*.

```azurecli
# create a compute cluster with no public IP
az ml compute create --name cpu-cluster --resource-group rg --workspace-name ws --vnet-name yourvnet --subnet yoursubnet --type AmlCompute --set enable_node_public_ip=False

# create a compute instance with no public IP
az ml compute create --name myci --resource-group rg --workspace-name ws --vnet-name yourvnet --subnet yoursubnet --type ComputeInstance --set enable_node_public_ip=False
```

# [Python](#tab/python)

> [!IMPORTANT]
> The following code snippet assumes that `ml_client` points to an Azure Machine Learning workspace that uses a private endpoint to participate in a VNet. For more information on using `ml_client`, see the tutorial [Azure Machine Learning in a day](tutorial-azure-ml-in-a-day.md).

```python
from azure.ai.ml.entities import AmlCompute

# specify aml compute name.
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4,
        vnet_name="yourvnet", subnet_name="yoursubnet", enable_node_public_ip=False
    )
    ml_client.compute.begin_create_or_update(compute).result()
```
