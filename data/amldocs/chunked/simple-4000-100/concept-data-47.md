|**Folder**<br> Reference a single folder     |     `uri_folder`    |   `FileDataset`      |  You must read/write a folder of parquet/CSV files into Pandas/Spark.<br><br>Deep-learning with images, text, audio, video files located in a folder.       | In V1 APIs, `FileDataset` had an associated engine that could take a file sample from a folder. In V2 APIs, a Folder is a simple mapping to the compute target filesystem. |
|**Table**<br> Reference a data table    |   `mltable`      |     `TabularDataset`    |    You have a complex schema subject to frequent changes, or you need a subset of large tabular data.<br><br>AutoML with Tables.     | In V1 APIs, the Azure ML back-end stored the data materialization blueprint. As a result, `TabularDataset` only worked if you had an Azure ML workspace. `mltable` stores the data materialization blueprint in *your* storage. This storage location means you can use it *disconnected to Azure ML* - for example, local, on-premises. In V2 APIs, you'll find it easier to transition from local to remote jobs. Read [Working with tables in Azure Machine Learning](how-to-mltable.md) for more information. |

## Data runtime capability
Azure ML uses its own *data runtime* for mounts/uploads/downloads, to map storage URIs to the compute target filesystem, or to materialize tabular data into pandas/spark with Azure ML tables (`mltable`). The Azure ML data runtime is designed for machine learning task *high speed and high efficiency*. Its key benefits include:

> [!div class="checklist"]
> - [Rust](https://www.rust-lang.org/) language architecture. The Rust language is known for high speed and high memory efficiency.
> - Light weight; the Azure ML data runtime has *no* dependencies on other technologies - JVM, for example - so the runtime installs quickly on compute targets.
> - Multi-process (parallel) data loading.
> - Data pre-fetches operate as background task on the CPU(s), to enhance utilization of the GPU(s) in deep-learning operations.
> - Seamless authentication to cloud storage.

## Datastore

An Azure ML datastore serves as a *reference* to an *existing* Azure storage account. The benefits of Azure ML datastore creation and use include:

1. A common, easy-to-use API that interacts with different storage types (Blob/Files/ADLS).
1. Easier discovery of useful datastores in team operations.
1. For credential-based access (service principal/SAS/key), Azure ML datastore secures connection information. This way, you won't need to place that information in your scripts.

When you create a datastore with an existing Azure storage account, you can choose between two different authentication methods:

- **Credential-based** - authenticate data access with a service principal, shared access signature (SAS) token, or account key. Users with *Reader* workspace access can access the credentials.
- **Identity-based** - use your Azure Active Directory identity or managed identity to authenticate data access.

The following table summarizes the Azure cloud-based storage services that an Azure Machine Learning datastore can create. Additionally, the table summarizes the authentication types that can access those services:

Supported storage service | Credential-based authentication | Identity-based authentication
|---|:----:|:---:|
Azure Blob Container| ✓ | ✓|
Azure File Share| ✓ | |
Azure Data Lake Gen1 | ✓ | ✓|
Azure Data Lake Gen2| ✓ | ✓|

Read [Create datastores](how-to-datastore.md) for more information about datastores.

## Data asset

An Azure ML data asset resembles web browser bookmarks (favorites). Instead of remembering long storage paths (URIs) that point to your most frequently used data, you can create a data asset, and then access that asset with a friendly name.

Data asset creation also creates a *reference* to the data source location, along with a copy of its metadata. Because the data remains in its existing location, you incur no extra storage cost, and you don't risk data source integrity. You can create Data assets from Azure ML datastores, Azure Storage, public URLs, or local files.
