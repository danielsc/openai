| [Use Docker images managed by Azure Machine Learning](#scenario-use-docker-images-managed-by-azure-ml) | NA | <ul><li>Microsoft Container Registry</li><li>`viennaglobal.azurecr.io` global container registry</li></ul> | If the Azure Container Registry for your workspace is behind the VNet, configure the workspace to use a compute cluster to build images. For more information, see [How to secure a workspace in a virtual network](how-to-secure-workspace-vnet.md#enable-azure-container-registry-acr). | 

> [!IMPORTANT]
> Azure Machine Learning uses multiple storage accounts. Each stores different data, and has a different purpose:
>
> * __Your storage__: The Azure Storage Account(s) in your Azure subscription are used to store your data and artifacts such as models, training data, training logs, and Python scripts. For example, the _default_ storage account for your workspace is in your subscription. The Azure Machine Learning compute instance and compute clusters access __file__ and __blob__ data in this storage over ports 445 (SMB) and 443 (HTTPS).
> 
>    When using a __compute instance__ or __compute cluster__, your storage account is mounted as a __file share__ using the SMB protocol. The compute instance and cluster use this file share to store the data, models, Jupyter notebooks, datasets, etc. The compute instance and cluster use the private endpoint when accessing the storage account.
>
> * __Microsoft storage__: The Azure Machine Learning compute instance and compute clusters rely on Azure Batch, and access storage located in a Microsoft subscription. This storage is used only for the management of the compute instance/cluster. None of your data is stored here. The compute instance and compute cluster access the __blob__, __table__, and __queue__ data in this storage, using port 443 (HTTPS).
>
> Machine Learning also stores metadata in an Azure Cosmos DB instance. By default, this instance is hosted in a Microsoft subscription and managed by Microsoft. You can optionally use an Azure Cosmos DB instance in your Azure subscription. For more information, see [Data encryption with Azure Machine Learning](concept-data-encryption.md#azure-cosmos-db).

## Scenario: Access workspace from studio

> [!NOTE]
> The information in this section is specific to using the workspace from the Azure Machine Learning studio. If you use the Azure Machine Learning SDK, REST API, CLI, or Visual Studio Code, the information in this section does not apply to you.

When accessing your workspace from studio, the network traffic flows are as follows:

* To authenticate to resources, __Azure Active Directory__ is used.
* For management and deployment operations, __Azure Resource Manager__ is used.
* For Azure Machine Learning specific tasks, __Azure Machine Learning service__ is used
* For access to Azure Machine Learning studio (https://ml.azure.com), __Azure FrontDoor__ is used.
* For most storage operations, traffic flows through the private endpoint of the default storage for your workspace. Exceptions are discussed in the [Use AutoML, designer, dataset, and datastore](#scenario-use-automl-designer-dataset-and-datastore-from-studio) section.
* You also need to configure a DNS solution that allows you to resolve the names of the resources within the VNet. For more information, see [Use your workspace with a custom DNS](how-to-custom-dns.md).

:::image type="content" source="./media/concept-secure-network-traffic-flow/workspace-traffic-studio.png" alt-text="Diagram of network traffic between client and workspace when using studio":::

## Scenario: Use AutoML, designer, dataset, and datastore from studio

The following features of Azure Machine Learning studio use _data profiling_:

* Dataset: Explore the dataset from studio.
* Designer: Visualize module output data.
* AutoML: View a data preview/profile and choose a target column.
* Labeling

Data profiling depends on the Azure Machine Learning managed service being able to access the default Azure Storage Account for your workspace. The managed service _doesn't exist in your VNet_, so can’t directly access the storage account in the VNet. Instead, the workspace uses a service principal to access storage.
