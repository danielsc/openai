
# Access data in a job

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you use:"]
> * [v1](v1/how-to-train-with-datasets.md)
> * [v2 (current version)](how-to-read-write-data-v2.md)

Learn how to read and write data for your jobs with the Azure Machine Learning Python SDK v2 and the Azure Machine Learning CLI extension v2.

## Prerequisites

- An Azure subscription. If you don't have an Azure subscription, create a free account before you begin. Try the [free or paid version of Azure Machine Learning](https://azure.microsoft.com/free/).

- The [Azure Machine Learning SDK for Python v2](https://aka.ms/sdk-v2-install).

- An Azure Machine Learning workspace

## Supported paths

When you provide a data input/output to a Job, you must specify a `path` parameter that points to the data location. This table shows both the different data locations that Azure Machine Learning supports, and examples for the `path` parameter:


|Location  | Examples  |
|---------|---------|
|A path on your local computer     | `./home/username/data/my_data`         |
|A path on a public http(s) server    |  `https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv`    |
|A path on Azure Storage     |   `https://<account_name>.blob.core.windows.net/<container_name>/<path>` <br> `abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>`    |
|A path on a Datastore   |   `azureml://datastores/<data_store_name>/paths/<path>`      |
|A path to a Data Asset  |  `azureml:<my_data>:<version>`  |

## Supported modes

When you run a job with data inputs/outputs, you can specify the *mode* - for example, whether the data should be read-only mounted, or downloaded to the compute target. This table shows the possible modes for different type/mode/input/output combinations:

Type | Input/Output | `upload` | `download` | `ro_mount` | `rw_mount` | `direct` | `eval_download` | `eval_mount` 
------ | ------ | :---: | :---: | :---: | :---: | :---: | :---: | :---:
`uri_folder` | Input  |   | ✓  |  ✓  |   | ✓  |  | 
`uri_file`   | Input |   | ✓  |  ✓  |   | ✓  |  | 
`mltable`   | Input |   | ✓  |  ✓  |   | ✓  | ✓ | ✓
`uri_folder` | Output  | ✓  |   |    | ✓  |   |  | 
`uri_file`   | Output | ✓  |   |    | ✓  |   |  | 
`mltable`   | Output | ✓  |   |    | ✓  | ✓  |  | 

> [!NOTE]
> `eval_download` and `eval_mount` are unique to `mltable`. The `ro_mount` is the default mode for MLTable. In some scenarios, however, an MLTable can yield files that are not necessarily co-located with the MLTable file in storage. Alternately, an `mltable` can subset or shuffle the data located in the storage resource. That view becomes visible only if the engine actually evaluates the MLTable file. These modes provide that view of the files.


## Read data in a job

# [Azure CLI](#tab/cli)

Create a job specification YAML file (`<file-name>.yml`). In the `inputs` section of the job, specify:

1. The `type`; whether the data is a specific file (`uri_file`), a folder location (`uri_folder`), or an `mltable`.
1. The `path` of your data location; any of the paths outlined in the [Supported Paths](#supported-paths) section will work.

```yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

# Possible Paths for Data:
# Blob: https://<account_name>.blob.core.windows.net/<container_name>/<folder>/<file>
# Datastore: azureml://datastores/paths/<folder>/<file>
# Data Asset: azureml:<my_data>:<version>

command: |
  ls ${{inputs.my_data}}
code: <folder where code is located>
inputs:
  my_data:
    type: <type> # uri_file, uri_folder, mltable
    path: <path>
environment: azureml:AzureML-sklearn-1.0-ubuntu20.04-py38-cpu@latest
compute: azureml:cpu-cluster
```

Next, run in the CLI

```azurecli
az ml job create -f <file-name>.yml
```

# [Python SDK](#tab/python)

Use the `Input` class to define:

1. The `type`; whether the data is a specific file (`uri_file`), a folder location (`uri_folder`), or an `mltable`.
