
[!INCLUDE [udr info for computes](../../includes/machine-learning-compute-user-defined-routes.md)]

## Scenario: Firewall between Azure Machine Learning and Azure Storage endpoints

You must also allow __outbound__ access to `Storage.<region>` on __port 445__.

## Scenario: Workspace created with the `hbi_workspace` flag enabled

You must also allow __outbound__ access to `Keyvault.<region>`. This outbound traffic is used to access the key vault instance for the back-end Azure Batch service.

For more information on the `hbi_workspace` flag, see the [data encryption](concept-data-encryption.md) article.

## Scenario: Use Kubernetes compute

[Kubernetes Cluster](./how-to-attach-kubernetes-anywhere.md) running behind an outbound proxy server or firewall needs extra egress network configuration. 

* For Kubernetes with Azure Arc connection, configure the [Azure Arc network requirements](../azure-arc/kubernetes/quickstart-connect-cluster.md?tabs=azure-cli#meet-network-requirements) needed by Azure Arc agents. 
* For AKS cluster without Azure Arc connection, configure the [AKS extension network requirements](../aks/limit-egress-traffic.md#cluster-extensions). 

Besides above requirements, the following outbound URLs are also required for Azure Machine Learning,

| Outbound Endpoint| Port | Description|Training |Inference |
|-----|-----|-----|:-----:|:-----:|
| `*.kusto.windows.net`<br>`*.table.core.windows.net`<br>`*.queue.core.windows.net` | 443 | Required to upload system logs to Kusto. |__&check;__|__&check;__|
| `<your ACR name>.azurecr.io`<br>`<your ACR name>.<region>.data.azurecr.io` | 443 | Azure container registry, required to pull docker images used for machine learning workloads.|__&check;__|__&check;__|
| `<your storage account name>.blob.core.windows.net` | 443 | Azure blob storage, required to fetch machine learning project scripts, data or models, and upload job logs/outputs.|__&check;__|__&check;__|
| `<your workspace ID>.workspace.<region>.api.azureml.ms`<br>`<region>.experiments.azureml.net`<br>`<region>.api.azureml.ms` | 443 | Azure Machine Learning service API.|__&check;__|__&check;__|
| `pypi.org` | 443 | Python package index, to install pip packages used for training job environment initialization.|__&check;__|N/A|
| `archive.ubuntu.com`<br>`security.ubuntu.com`<br>`ppa.launchpad.net` | 80 | Required to download the necessary security patches. |__&check;__|N/A|

> [!NOTE]
> * Replace `<your workspace workspace ID>` with your workspace ID. The ID can be found in Azure portal - your Machine Learning resource page - Properties - Workspace ID.
> * Replace `<your storage account>` with the storage account name.
> * Replace `<your ACR name>` with the name of the Azure Container Registry for your workspace.
> * Replace `<region>` with the region of your workspace.

### In-cluster communication requirements

To install the Azure Machine Learning extension on Kubernetes compute, all Azure Machine Learning related components are deployed in a `azureml` namespace. The following in-cluster communication is needed to ensure the ML workloads work well in the AKS cluster.
- The components in  `azureml` namespace should be able to communicate with Kubernetes API server.
- The components in  `azureml` namespace should be able to communicate with each other.
- The components in  `azureml` namespace should be able to communicate with `kube-dns` and `konnectivity-agent` in `kube-system` namespace.
- If the cluster is used for real-time inferencing, `azureml-fe-xxx` PODs should be able to communicate with the deployed model PODs on 5001 port in other namespace. `azureml-fe-xxx` PODs should open 11001, 12001, 12101, 12201, 20000, 8000, 8001, 9001 ports for internal communication.
- If the cluster is used for real-time inferencing, the deployed model PODs should be able to communicate with `amlarc-identity-proxy-xxx` PODs on 9999 port.


## Scenario: Visual Studio Code

The hosts in this section are used to install Visual Studio Code packages to establish a remote connection between Visual Studio Code and compute instances in your Azure Machine Learning workspace.
