Create a single- or multi- node compute cluster for your training, batch inferencing or reinforcement learning workloads. 

1. Navigate to [Azure Machine Learning studio](https://ml.azure.com).
 
1. Under __Manage__, select __Compute__.
1. If you have no compute resources, select  **Create** in the middle of the page.
  
    :::image type="content" source="media/how-to-create-attach-studio/create-compute-target.png" alt-text="Screenshot that shows creating a compute target":::

1. If you see a list of compute resources, select **+New** above the list.

    :::image type="content" source="media/how-to-create-attach-studio/select-new.png" alt-text="Select new":::

1. In the tabs at the top, select __Compute cluster__

1. Fill out the form as follows:

    |Field  |Description  |
    |---------|---------|
    | Location | The Azure region where the compute cluster will be created. By default, this is the same location as the workspace. Setting the location to a different region than the workspace is in __preview__, and is only available for __compute clusters__, not compute instances.</br>When using a different region than your workspace or datastores, you may see increased network latency and data transfer costs. The latency and costs can occur when creating the cluster, and when running jobs on it. |
    |Virtual machine type |  Choose CPU or GPU. This type can't be changed after creation     |
    |Virtual machine priority | Choose **Dedicated** or **Low priority**.  Low priority virtual machines are cheaper but don't guarantee the compute nodes. Your job may be preempted.
    |Virtual machine size     |  Supported virtual machine sizes might be restricted in your region. Check the [availability list](https://azure.microsoft.com/global-infrastructure/services/?products=virtual-machines)     |

1. Select **Next** to proceed to **Advanced Settings** and fill out the form as follows:

    |Field  |Description  |
    |---------|---------|
    |Compute name     | * Name is required and must be between 3 to 24 characters long.<br><br> * Valid characters are upper and lower case letters, digits, and the  **-** character.<br><br> * Name must start with a letter<br><br> * Name needs to be unique across all existing computes within an Azure region. You'll see an alert if the name you choose isn't unique<br><br> * If **-**  character is used, then it needs to be followed by at least one letter later in the name    |
    |Minimum number of nodes | Minimum number of nodes that you want to provision. If you want a dedicated number of nodes, set that count here. Save money by setting the minimum to 0, so you won't pay for any nodes when the cluster is idle. |
    |Maximum number of nodes | Maximum number of nodes that you want to provision. The compute will autoscale to a maximum of this node count when a job is submitted. |
    | Idle seconds before scale down | Idle time before scaling the cluster down to the minimum node count. |
    | Enable SSH access | Use the same instructions as [Enable SSH access](#enable-ssh-access) for a compute instance (above). |
    |Advanced settings     |  Optional. Configure a virtual network. Specify the **Resource group**, **Virtual network**, and **Subnet** to create the compute instance inside an Azure Virtual Network (vnet). For more information, see these [network requirements](./how-to-secure-training-vnet.md) for vnet.   Also attach [managed identities](#set-up-managed-identity) to grant access to resources.

1. Select __Create__.


### Enable SSH access

SSH access is disabled by default.  SSH access can't be changed after creation. Make sure to enable access if you plan to debug interactively with [VS Code Remote](how-to-set-up-vs-code-remote.md).  

[!INCLUDE [enable-ssh](../../includes/machine-learning-enable-ssh.md)]

### Connect with SSH access

[!INCLUDE [ssh-access](../../includes/machine-learning-ssh-access.md)]


 ## Lower your compute cluster cost with low priority VMs

You may also choose to use [low-priority VMs](how-to-manage-optimize-cost.md#low-pri-vm) to run some or all of your workloads. These VMs don't have guaranteed availability and may be preempted while in use. You'll have to restart a preempted job. 
