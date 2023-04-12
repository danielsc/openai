
# Network traffic flow when using a secured workspace

When your Azure Machine Learning workspace and associated resources are secured in an Azure Virtual Network, it changes the network traffic between resources. Without a virtual network, network traffic flows over the public internet or within an Azure data center. Once a virtual network (VNet) is introduced, you may also want to harden network security. For example, blocking inbound and outbound communications between the VNet and public internet. However, Azure Machine Learning requires access to some resources on the public internet. For example, Azure Resource Management is used for deployments and management operations.

This article lists the required traffic to/from the public internet. It also explains how network traffic flows between your client development environment and a secured Azure Machine Learning workspace in the following scenarios:

* Using Azure Machine Learning __studio__ to work with:

    * Your workspace
    * AutoML
    * Designer
    * Datasets and datastores

    > [!TIP]
    > Azure Machine Learning studio is a web-based UI that runs partially in your web browser, and makes calls to Azure services to perform tasks such as training a model, using designer, or viewing datasets. Some of these calls use a different communication flow than if you are using the SDK, CLI, REST API, or VS Code.

* Using Azure Machine Learning __studio__, __SDK__, __CLI__, or __REST API__ to work with:

    * Compute instances and clusters
    * Azure Kubernetes Service
    * Docker images managed by Azure Machine Learning

> [!TIP]
> If a scenario or task is not listed here, it should work the same with or without a secured workspace.

## Assumptions

This article assumes the following configuration:

* Azure Machine Learning workspace using a private endpoint to communicate with the VNet.
* The Azure Storage Account, Key Vault, and Container Registry used by the workspace also use a private endpoint to communicate with the VNet.
* A VPN gateway or Express Route is used by the client workstations to access the VNet.

## Inbound and outbound requirements


| __Scenario__ | __Required inbound__ | __Required outbound__ | __Additional configuration__ | 
| ----- | ----- | ----- | ----- |
| [Access workspace from studio](#scenario-access-workspace-from-studio) | NA | <ul><li>Azure Active Directory</li><li>Azure Front Door</li><li>Azure Machine Learning service</li></ul> | You may need to use a custom DNS server. For more information, see [Use your workspace with a custom DNS](how-to-custom-dns.md). | 
| [Use AutoML, designer, dataset, and datastore from studio](#scenario-use-automl-designer-dataset-and-datastore-from-studio) | NA | NA | <ul><li>Workspace service principal configuration</li><li>Allow access from trusted Azure services</li></ul>For more information, see [How to secure a workspace in  a virtual network](how-to-secure-workspace-vnet.md#secure-azure-storage-accounts). | 
| [Use compute instance and compute cluster](#scenario-use-compute-instance-and-compute-cluster) | <ul><li>Azure Machine Learning service on port 44224</li><li>Azure Batch Management service on ports 29876-29877</li></ul> | <ul><li>Azure Active Directory</li><li>Azure Resource Manager</li><li>Azure Machine Learning service</li><li>Azure Storage Account</li><li>Azure Key Vault</li></ul> | If you use a firewall, create user-defined routes. For more information, see [Configure inbound and outbound traffic](how-to-access-azureml-behind-firewall.md). | 
| [Use Azure Kubernetes Service](#scenario-use-azure-kubernetes-service) | NA | For information on the outbound configuration for AKS, see [How to secure Kubernetes inference](how-to-secure-kubernetes-inferencing-environment.md). | | 
| [Use Docker images managed by Azure Machine Learning](#scenario-use-docker-images-managed-by-azure-ml) | NA | <ul><li>Microsoft Container Registry</li><li>`viennaglobal.azurecr.io` global container registry</li></ul> | If the Azure Container Registry for your workspace is behind the VNet, configure the workspace to use a compute cluster to build images. For more information, see [How to secure a workspace in a virtual network](how-to-secure-workspace-vnet.md#enable-azure-container-registry-acr). | 
