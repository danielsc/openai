---
title: Data concepts in Azure Machine Learning
titleSuffix: Azure Machine Learning
description: Learn key data concepts in Azure Machine Learning
services: machine-learning
ms.service: machine-learning
ms.subservice: enterprise-readiness
ms.topic: conceptual
ms.reviewer: franksolomon
author: samuel100
ms.author: samkemp
ms.date: 01/23/2023
ms.custom: devx-track-python, data4ml, event-tier1-build-2022
#Customer intent: As an experienced Python developer, I need secure access to my data in my Azure storage solutions, and I need to use that data to accomplish my machine learning tasks.
---

# Data concepts in Azure Machine Learning

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning developer platform you use:"]
> * [v1](./v1/concept-data.md)
> * [v2 (current version)](concept-data.md)

With Azure Machine Learning, you can bring data from a local machine or an existing cloud-based storage. In this article, you'll learn the main Azure Machine Learning data concepts.

## URI
A Uniform Resource Identifier (URI) represents a storage location on your local computer, Azure storage, or a publicly available http(s) location. These examples show URIs for different storage options:

|Storage location  | URI examples  |
|---------|---------|
|Local computer     | `./home/username/data/my_data`         |
|Public http(s) server    |  `https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv`    |
|Blob storage    | `wasbs://<containername>@<accountname>.blob.core.windows.net/<folder>/`|
|Azure Data Lake (gen2) | `abfss://<file_system>@<account_name>.dfs.core.windows.net/<folder>/<file>.csv`  |
| Azure Data Lake (gen1) | `adl://<accountname>.azuredatalakestore.net/<folder1>/<folder2>` 
|Azure ML [Datastore](#datastore)  |   `azureml://datastores/<data_store_name>/paths/<folder1>/<folder2>/<folder3>/<file>.parquet`      |

An Azure ML job maps URIs to the compute target filesystem. This mapping means that in a command that consumes or produces a URI, that URI works like a file or a folder. A URI uses **identity-based authentication** to connect to storage services, with either your Azure Active Directory ID (default), or Managed Identity. Azure ML [Datastore](#datastore) URIs can apply either identity-based authentication, or **credential-based** (for example, Service Principal, SAS token, account key) without exposure of secrets.

A URI can serve as either *input* or an *output* to an Azure ML job, and it can map to the compute target filesystem with one of four different *mode* options:

- **Read-*only* mount (`ro_mount`)**: The URI represents a storage location that is *mounted* to the compute target filesystem. The mounted data location supports read-only output exclusively.
- **Read-*write* mount (`rw_mount`)**: The URI represents a storage location that is *mounted* to the compute target filesystem. The mounted data location supports both read output from it *and* data writes to it.
- **Download (`download`)**: The URI represents a storage location containing data that is *downloaded* to the compute target filesystem.
- **Upload (`upload`)**: All data written to a compute target location is *uploaded* to the storage location represented by the URI.

Additionally, you can pass in the URI as a job input string with the **direct** mode. This table summarizes the combination of modes available for inputs and outputs:

Job<br>Input or Output | `upload` | `download` | `ro_mount` | `rw_mount` | `direct` | 
------ | :---: | :---: | :---: | :---: | :---: | 
Input  |   | ✓  |  ✓  |   | ✓ |  
Output  | ✓  |   |    | ✓  |  

Read [Access data in a job](how-to-read-write-data-v2.md) for more information.

## Data types

A URI (storage location) can reference a file, a folder, or a data table. A machine learning job input and output definition requires one of the following three data types:

|Type  |V2 API  |V1 API  |Canonical Scenarios | V2/V1 API Difference
|---------|---------|---------|---------|---------|
|**File**<br>Reference a single file     |    `uri_file`     |   `FileDataset`      |       Read/write a single file - the file can have any format.   |  A type new to V2 APIs. In V1 APIs, files always mapped to a folder on the compute target filesystem; this mapping required an `os.path.join`. In V2 APIs, the single file is mapped. This way, you can refer to that location in your code.   |
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

Read [Create data assets](how-to-create-data-assets.md) for more information about data assets.

## Next steps

- [Install and set up the CLI (v2)](how-to-configure-cli.md#install-and-set-up-the-cli-v2)
- [Create datastores](how-to-datastore.md#create-datastores)
- [Create data assets](how-to-create-data-assets.md#create-data-assets)
- [Access data in a job](how-to-read-write-data-v2.md)
- [Data administration](how-to-administrate-data-authentication.md#data-administration)