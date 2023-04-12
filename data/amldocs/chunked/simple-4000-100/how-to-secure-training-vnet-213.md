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

Use the following information to create a compute instance or cluster with a public IP address in the VNet:

# [Azure CLI](#tab/cli)

In the `az ml compute create` command, replace the following values:

* `rg`: The resource group that the compute will be created in.
* `ws`: The Azure Machine Learning workspace name.
* `yourvnet`: The Azure Virtual Network.
* `yoursubnet`: The subnet to use for the compute.
* `AmlCompute` or `ComputeInstance`: Specifying `AmlCompute` creates a *compute cluster*. `ComputeInstance` creates a *compute instance*.

```azurecli
# create a compute cluster with a public IP
az ml compute create --name cpu-cluster --resource-group rg --workspace-name ws --vnet-name yourvnet --subnet yoursubnet --type AmlCompute

# create a compute instance with a public IP
az ml compute create --name myci --resource-group rg --workspace-name ws --vnet-name yourvnet --subnet yoursubnet --type ComputeInstance
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
    # Replace "yourvnet" and "yoursubnet" with your VNet and subnet.
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4,
        vnet_name="yourvnet", subnet_name="yoursubnet"
    )
    ml_client.compute.begin_create_or_update(compute).result()
```

# [Studio](#tab/azure-studio)

1. Sign in to the [Azure Machine Learning studio](https://ml.azure.com), and then select your subscription and workspace.
1. Select the **Compute** page from the left navigation bar.
1. Select the **+ New** from the navigation bar of compute instance or compute cluster.
1. Configure the VM size and configuration you need, then select **Next**.
1. From the **Advanced Settings**, Select **Enable virtual network** and then select your virtual network and subnet.

    :::image type="content" source="./media/how-to-secure-training-vnet/with-public-ip.png" alt-text="A screenshot of how to configure a compute instance/cluster in a VNet with a public IP." lightbox="./media/how-to-secure-training-vnet/with-public-ip.png":::
