* Use the [Azure Machine Learning SDK for Python](how-to-manage-workspace.md?tabs=python#create-a-workspace) to create a workspace on the fly from Python scripts or Jupyter notebooks.
* Use an [Azure Resource Manager template](how-to-create-workspace-template.md) or the [Azure Machine Learning CLI](how-to-configure-cli.md) when you need to automate or customize the creation with corporate security standards.
* If you work in Visual Studio Code, use the [VS Code extension](how-to-manage-resources-vscode.md#create-a-workspace).

> [!NOTE]
> The workspace name is case-insensitive.

## Sub resources

These sub resources are the main resources that are made in the AzureML workspace.

* VMs: provide computing power for your AzureML workspace and are an integral part in deploying and training models.
* Load Balancer: a network load balancer is created for each compute instance and compute cluster to manage traffic even while the compute instance/cluster is stopped.
* Virtual Network: these help Azure resources communicate with one another, the internet, and other on-premises networks.
* Bandwidth: encapsulates all outbound data transfers across regions.

## Associated resources

When you create a new workspace, it automatically creates several Azure resources that are used by the workspace:

+ [Azure Storage account](https://azure.microsoft.com/services/storage/): Is used as the default datastore for the workspace.  Jupyter notebooks that are used with your Azure Machine Learning compute instances are stored here as well. 
  
  > [!IMPORTANT]
  > By default, the storage account is a general-purpose v1 account. You can [upgrade this to general-purpose v2](../storage/common/storage-account-upgrade.md) after the workspace has been created. 
  > Do not enable hierarchical namespace on the storage account after upgrading to general-purpose v2.

  To use an existing Azure Storage account, it cannot be of type BlobStorage or a premium account (Premium_LRS and Premium_GRS). It also cannot have a hierarchical namespace (used with Azure Data Lake Storage Gen2). Neither premium storage nor hierarchical namespaces are supported with the _default_ storage account of the workspace. You can use premium storage or hierarchical namespace with _non-default_ storage accounts.
  
+ [Azure Container Registry](https://azure.microsoft.com/services/container-registry/): Registers docker containers that are used for the following components:
    * [Azure Machine Learning environments](concept-environments.md) when training and deploying models
    * [AutoML](concept-automated-ml.md) when deploying
    * [Data profiling](v1/how-to-connect-data-ui.md#data-preview-and-profile)

    To minimize costs, ACR is **lazy-loaded** until images are needed.

    > [!NOTE]
    > If your subscription setting requires adding tags to resources under it, Azure Container Registry (ACR) created by Azure Machine Learning will fail, since we cannot set tags to ACR.

+ [Azure Application Insights](https://azure.microsoft.com/services/application-insights/): Stores monitoring and diagnostics information. For more information, see [Monitor online endpoints](how-to-monitor-online-endpoints.md).

    > [!NOTE]
    > You can delete the Application Insights instance after cluster creation if you want. Deleting it limits the information gathered from the workspace, and may make it more difficult to troubleshoot problems. __If you delete the Application Insights instance created by the workspace, you cannot re-create it without deleting and recreating the workspace__.

+ [Azure Key Vault](https://azure.microsoft.com/services/key-vault/): Stores secrets that are used by compute targets and other sensitive information that's needed by the workspace.

> [!NOTE]
> You can instead use existing Azure resource instances when you create the workspace with the [Python SDK](how-to-manage-workspace.md?tabs=python#create-a-workspace) or the Azure Machine Learning CLI [using an ARM template](how-to-create-workspace-template.md).
