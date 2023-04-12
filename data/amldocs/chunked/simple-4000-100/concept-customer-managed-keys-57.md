These Microsoft-managed resources are located in a new Azure resource group is created in your subscription. This group is in addition to the resource group for your workspace. This resource group will contain the Microsoft-managed resources that your key is used with. The resource group will be named using the formula of `<Azure Machine Learning workspace resource group name><GUID>`.

> [!TIP]
> * The [__Request Units__](../cosmos-db/request-units.md) for the Azure Cosmos DB automatically scale as needed.
> * If your Azure Machine Learning workspace uses a private endpoint, this resource group will also contain a Microsoft-managed Azure Virtual Network. This VNet is used to secure communications between the managed services and the workspace. You __cannot provide your own VNet for use with the Microsoft-managed resources__. You also __cannot modify the virtual network__. For example, you cannot change the IP address range that it uses.

> [!IMPORTANT]
> If your subscription does not have enough quota for these services, a failure will occur.

> [!WARNING]
> __Don't delete the resource group__ that contains this Azure Cosmos DB instance, or any of the resources automatically created in this group. If you need to delete the resource group or Microsoft-managed services in it, you must delete the Azure Machine Learning workspace that uses it. The resource group resources are deleted when the associated workspace is deleted.

## How compute data is stored

Azure Machine Learning uses compute resources to train and deploy machine learning models. The following table describes the compute options and how data is encrypted by each one:

| Compute | Encryption |
| ----- | ----- |
| Azure Container Instance | Data is encrypted by a Microsoft-managed key or a customer-managed key.</br>For more information, see [Encrypt data with a customer-managed key](../container-instances/container-instances-encrypt-data.md). |
| Azure Kubernetes Service | Data is encrypted by a Microsoft-managed key or a customer-managed key.</br>For more information, see [Bring your own keys with Azure disks in Azure Kubernetes Services](../aks/azure-disk-customer-managed-keys.md). |
| Azure Machine Learning compute instance | Local scratch disk is encrypted if the `hbi_workspace` flag is enabled for the workspace. |
| Azure Machine Learning compute cluster | OS disk encrypted in Azure Storage with Microsoft-managed keys. Temporary disk is encrypted if the `hbi_workspace` flag is enabled for the workspace. |

**Compute cluster**
The OS disk for each compute node stored in Azure Storage is encrypted with Microsoft-managed keys in Azure Machine Learning storage accounts. This compute target is ephemeral, and clusters are typically scaled down when no jobs are queued. The underlying virtual machine is de-provisioned, and the OS disk is deleted. Azure Disk Encryption isn't supported for the OS disk. 

Each virtual machine also has a local temporary disk for OS operations. If you want, you can use the disk to stage training data. If the workspace was created with the `hbi_workspace` parameter set to `TRUE`, the temporary disk is encrypted. This environment is short-lived (only during your job) and encryption support is limited to system-managed keys only.

**Compute instance**
The OS disk for compute instance is encrypted with Microsoft-managed keys in Azure Machine Learning storage accounts. If the workspace was created with the `hbi_workspace` parameter set to `TRUE`, the local temporary disk on compute instance is encrypted with Microsoft managed keys. Customer managed key encryption isn't supported for OS and temp disk.

### HBI_workspace flag

* The `hbi_workspace` flag can only be set when a workspace is created. It can’t be changed for an existing workspace.
* When this flag is set to True, it may increase the difficulty of troubleshooting issues because less telemetry data is sent to Microsoft. There’s less visibility into success rates or problem types. Microsoft may not be able to react as proactively when this flag is True.
