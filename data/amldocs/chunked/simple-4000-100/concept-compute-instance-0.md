
# What is an Azure Machine Learning compute instance?

An Azure Machine Learning compute instance is a managed cloud-based workstation for data scientists.  Each compute instance has only one owner, although you can share files between multiple compute instances. 

Compute instances make it easy to get started with Azure Machine Learning development and provide management and enterprise readiness capabilities for IT administrators.

Use a compute instance as your fully configured and managed development environment in the cloud for machine learning. They can also be used as a compute target for training and inferencing for development and testing purposes.

For compute instance Jupyter functionality to work, ensure that web socket communication isn't disabled. Ensure your network allows websocket connections to *.instances.azureml.net and *.instances.azureml.ms.

> [!IMPORTANT]
> Items marked (preview) in this article are currently in public preview.
> The preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities.
> For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

## Why use a compute instance?

A compute instance is a fully managed cloud-based workstation optimized for your machine learning development environment. It provides the following benefits:

|Key benefits|Description|
|----|----|
|Productivity|You can build and deploy models using integrated notebooks and the following tools in Azure Machine Learning studio:<br/>-  Jupyter<br/>-  JupyterLab<br/>-  VS Code (preview)<br/>Compute instance is fully integrated with Azure Machine Learning workspace and studio. You can share notebooks and data with other data scientists in the workspace.<br/> 
|Managed & secure|Reduce your security footprint and add compliance with enterprise security requirements. Compute instances  provide robust management policies and secure networking configurations such as:<br/><br/>- Autoprovisioning from Resource Manager templates or Azure Machine Learning SDK<br/>- [Azure role-based access control (Azure RBAC)](../role-based-access-control/overview.md)<br/>- [Virtual network support](./how-to-secure-training-vnet.md)<br/> - Azure policy to disable SSH access<br/> - Azure policy to enforce creation in a virtual network <br/> - Auto-shutdown/auto-start based on schedule <br/>- TLS 1.2 enabled |
|Preconfigured&nbsp;for&nbsp;ML|Save time on setup tasks with pre-configured and up-to-date ML packages, deep learning frameworks, GPU drivers.|
|Fully customizable|Broad support for Azure VM types including GPUs and persisted low-level customization such as installing packages and drivers makes advanced scenarios a breeze. You can also use setup scripts to automate customization |

* Secure your compute instance with **[No public IP](./how-to-secure-training-vnet.md)**.
* The compute instance is also a secure training compute target similar to [compute clusters](how-to-create-attach-compute-cluster.md), but it's single node. 
* You can [create a compute instance](how-to-create-manage-compute-instance.md?tabs=python#create) yourself, or an administrator can **[create a compute instance on your behalf](how-to-create-manage-compute-instance.md?tabs=python#create-on-behalf-of-preview)**.
* You can also **[use a setup script (preview)](how-to-customize-compute-instance.md)**  for an automated way to customize and configure the compute instance as per your needs.
* To save on costs, **[create  a schedule](how-to-create-manage-compute-instance.md#schedule-automatic-start-and-stop)** to automatically start and stop the compute instance, or [enable idle shutdown](how-to-create-manage-compute-instance.md#enable-idle-shutdown-preview)


## Tools and environments

Azure Machine Learning compute instance enables you to author, train, and deploy models in a fully integrated notebook experience in your workspace.
