
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
