
# Access data from Azure cloud storage during interactive development

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Typically the beginning of a machine learning project involves exploratory data analysis (EDA), data-preprocessing (cleaning, feature engineering), and building prototypes of ML models to validate hypotheses. This *prototyping* phase of the project is highly interactive in nature that lends itself to developing in a Jupyter notebook or an IDE with a *Python interactive console*. In this article you'll learn how to:

> [!div class="checklist"]
> * Access data from a Azure ML Datastores URI as if it were a file system.
> * Materialize data into Pandas using `mltable` Python library.
> * Materialize Azure ML data assets into Pandas using `mltable` Python library.
> * Materialize data through an explicit download with the `azcopy` utility.

## Prerequisites

* An Azure Machine Learning workspace. For more information, see [Manage Azure Machine Learning workspaces in the portal or with the Python SDK (v2)](how-to-manage-workspace.md).
* An Azure Machine Learning Datastore. For more information, see [Create datastores](how-to-datastore.md).

> [!TIP]
> The guidance in this article to access data during interactive development applies to any host that can run a Python session - for example: your local machine, a cloud VM, a GitHub Codespace, etc. We recommend using an Azure Machine Learning compute instance - a fully managed and pre-configured cloud workstation. For more information, see [Create and manage an Azure Machine Learning compute instance](how-to-create-manage-compute-instance.md).

> [!IMPORTANT]
> Ensure you have the latest `azure-fsspec` and `mltable` python libraries installed in your python environment:
> 
> ```bash
> pip install -U azureml-fsspec mltable
> ```

## Access data from a datastore URI, like a filesystem (preview)

[!INCLUDE [preview disclaimer](../../includes/machine-learning-preview-generic-disclaimer.md)]

An Azure ML datastore is a *reference* to an *existing* storage account on Azure. The benefits of creating and using a datastore include:

> [!div class="checklist"]
> * A common and easy-to-use API to interact with different storage types (Blob/Files/ADLS).
> * Easier to discover useful datastores when working as a team.
> * Supports both credential-based (for example, SAS token) and identity-based (use Azure Active Directory or Manged identity) to access data.
> * When using credential-based access, the connection information is secured so you don't expose keys in scripts.
> * Browse data and copy-paste datastore URIs in the Studio UI.

A *Datastore URI* is a Uniform Resource Identifier, which is a *reference* to a storage *location* (path) on your Azure storage account. The format of the datastore URI is:

```python
# AzureML workspace details:
subscription = '<subscription_id>'
resource_group = '<resource_group>'
workspace = '<workspace>'
datastore_name = '<datastore>'
path_on_datastore '<path>'

# long-form Datastore uri format:
uri = f'azureml://subscriptions/{subscription}/resourcegroups/{resource_group}/workspaces/{workspace}/datastores/{datastore_name}/paths/{path_on_datastore}'. 
```

These Datastore URIs are a known implementation of [Filesystem spec](https://filesystem-spec.readthedocs.io/en/latest/index.html) (`fsspec`): A unified pythonic interface to local, remote and embedded file systems and bytes storage.

The Azure ML Datastore implementation of `fsspec` automatically handles credential/identity passthrough used by the Azure ML datastore. This means you don't need to expose account keys in your scripts or do additional sign-in procedures on a compute instance.

For example, you can directly use Datastore URIs in Pandas - below is an example of reading a CSV file:

```python
import pandas as pd

df = pd.read_csv("azureml://subscriptions/<subid>/resourcegroups/<rgname>/workspaces/<workspace_name>/datastores/<datastore_name>/paths/<folder>/<filename>.csv")
df.head()
``` 
