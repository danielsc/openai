
# Create data assets
[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning SDK you are using:"]
> * [v1](./v1/how-to-create-register-datasets.md)
> * [v2 (current version)](how-to-create-data-assets.md)

In this article, you'll learn how to create a data asset in Azure ML. An Azure ML data asset is similar to web browser bookmarks (favorites). Instead of remembering long storage paths (URIs) that point to your most frequently used data, you can create a data asset, and then access that asset with a friendly name.

Data asset creation also creates a *reference* to the data source location, along with a copy of its metadata. Because the data remains in its existing location, you incur no extra storage cost, and don't risk data source integrity. You can create Data assets from Azure ML datastores, Azure Storage, public URLs, and local files.

## Prerequisites

To create and work with data assets, you need:

* An Azure subscription. If you don't have one, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

* An Azure Machine Learning workspace. [Create workspace resources](quickstart-create-resources.md).

* The [Azure Machine Learning CLI/SDK installed](how-to-configure-cli.md).

## Do I *need* to create a data asset to access my data?

No. If you just want to access your data in an interactive session (for example, a notebook) or a job, you are **not** required to create a data asset first. You can use the storage URI to access the data.

Data assets can "bookmark" your frequently used data, to avoid the need to remember long storage URIs.

> [!TIP]
> For more information about accessing your data in a notebook, please see [Access data from Azure cloud storage for interactive development](how-to-access-data-interactive.md).<br><br>For more information about accessing your data - both local and cloud storage - in a job, please see [Access data in a job](how-to-read-write-data-v2.md).

## Data asset types

> [!NOTE]
> Make sure to check out the **canonical scenarios** below when deciding if you want to use uri_file, uri_folder or mltable for your use case.

You can create three data asset types:

|Type  |V2 API  |V1 API  |V2/V1 API Difference  |**Canonical Scenarios**
|---------|---------|---------|---------|---------|
|**File**<br>Reference a single file     |    `uri_file`     |   `FileDataset`      |  A type new to V2 APIs. In V1 APIs, files always mapped to a folder on the compute target filesystem; this mapping required an `os.path.join`. In V2 APIs, the single file is mapped. This way, you can refer to that location in your code.   |       Read/write a single file - the file can have any format. |  
|**Folder**<br> Reference a single folder     |     `uri_folder`    |   `FileDataset`       | In V1 APIs, `FileDataset` had an associated engine that could take a file sample from a folder. In V2 APIs, a Folder is a simple mapping to the compute target filesystem. |      You must read/write a folder of parquet/CSV files into Pandas/Spark.<br><br>Deep-learning with images, text, audio, video files located in a folder. |
|**Table**<br> Reference a data table    |   `mltable`      |     `TabularDataset`     | In V1 APIs, the Azure ML back-end stored the data materialization blueprint. This storage location meant that `TabularDataset` only worked if you had an Azure ML workspace. `mltable` stores the data materialization blueprint in *your* storage. This storage location means you can use it *disconnected to Azure ML* - for example, local, on-premises. In V2 APIs, you'll find it easier to transition from local to remote jobs. Read [Working with tables in Azure Machine Learning](how-to-mltable.md) for more information. |    You have a complex schema subject to frequent changes, or you need a subset of large tabular data.<br><br>AutoML with Tables. |

## Supported paths
