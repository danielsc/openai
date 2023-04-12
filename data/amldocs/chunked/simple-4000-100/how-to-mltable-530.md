
# [Python](#tab/Python-SDK)

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

my_path = './data'

my_data = Data(
    path=my_path,
    type=AssetTypes.MLTABLE,
    name="green-sample",
    version='1'
)

ml_client.data.create_or_update(my_data)
```

> [!NOTE]
> Your local data folder - containing the parquet file and MLTable - will automatically upload to cloud storage (default Azure ML datastore) on asset create.

### Step 4: Create a job

Create a Python script called `read-mltable.py` in an `src` folder that contains:

```python
# ./src/read-mltable.py
import argparse
import mltable

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', help='mltable artifact to read')
args = parser.parse_args()

# load mltable
tbl = mltable.load(args.input)

# show table
print(tbl.show())
```

To keep things simple, we only show how to read the table into Pandas, and print the first few records.

Your job will need a Conda file that includes the Python package dependencies. Save that Conda file as `conda_dependencies.yml`:

```yml
# ./conda_dependencies.yml
dependencies:
  - python=3.10
  - pip=21.2.4
  - pip:
      - mltable
      - azureml-dataprep[pandas]
```

Next, submit the job:

# [CLI](#tab/cli)

Create the following job YAML file:

```yml
# mltable-job.yml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json

code: ./src

command: python read-mltable.py --input ${{inputs.my_mltable}}
inputs:
    my_mltable:
      type: mltable
      path: azureml:green-sample:1

compute: cpu-cluster

environment:
  image: mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04
  conda_file: conda_dependencies.yml
```

In the CLI, create the job:

```azurecli
az ml job create -f mltable-job.yml
```

# [Python](#tab/Python-SDK)

```python
from azure.ai.ml import MLClient, command, Input
from azure.ai.ml.entities import Environment
from azure.identity import DefaultAzureCredential

# Create a client
ml_client = MLClient.from_config(credential=DefaultAzureCredential())

# get the data asset
data_asset = ml_client.data.get(name="green-sample", version="1")

job = command(
    command="python read-mltable.py --input ${{inputs.my_mltable}}",
    inputs={
        "my_mltable": Input(type="mltable",path=data_asset.id)
    },
    compute="cpu-cluster",
    environment=Environment(
        image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04",
        conda_file="./conda_dependencies.yml"
    ),
    code="./src"
)

ml_client.jobs.create_or_update(job)
```


## `MLTable` file examples

### Delimited Text (a CSV file)

This example assumes you have a CSV file stored in the following Azure Data Lake location:

- `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/<file-name>.csv`

> [!NOTE]
> You must update the `<>` placeholders for your Azure Data Lake filesystem and account name, along with the path on Azure Data lake to your CSV file.

# [CLI](#tab/cli)
Create an `MLTable` file in the `abfss://<filesystem>@<account_name>.dfs.core.windows.net/<folder>/` location:
    
```yaml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable

paths:
  - file: ./<file-name>.csv

transformations:
  - read_delimited:
      delimiter: ',' 
      empty_as_string: false 
      encoding: utf8 
      header: all_files_same_headers
      include_path_column: false 
      infer_column_types: true 
      support_multi_line: false
```

If you don't already use [Option 1: Directly author `MLTable` in cloud storage with VSCode](#option-1-directly-author-mltable-in-cloud-storage-with-vscode), then you can upload your `MLTable` file with `azcopy`:

```bash
SOURCE=<local_path-to-mltable-file>
DEST=https://<account_name>.blob.core.windows.net/<filesystem>/<folder>
azcopy cp $SOURCE $DEST
```

# [Python](#tab/Python-SDK)

```python
import mltable
from mltable import MLTableHeaders, MLTableFileEncoding
from azure.storage.blob import BlobClient
from azure.identity import DefaultAzureCredential

# update the file name
my_path = {
    'file': './<file_name>.csv'
}

tbl = mltable.from_delimited_files(
    paths=[my_path],
    header=MLTableHeaders.all_files_same_headers,
    delimiter=',',
    encoding=MLTableFileEncoding.utf8,
    empty_as_string=False,
    include_path_column=False,
    infer_column_types=True,
    support_multi_line=False)

# save the table to the local file system
local_folder = "local"
tbl.save(local_folder)

# upload the MLTable file to your storage account so that you have an artifact
storage_account_url = "https://<account_name>.blob.core.windows.net"
container_name = "<filesystem>"
data_folder_on_storage = '<folder>'

# get a blob client using default credential
blob_client = BlobClient(
    credential=DefaultAzureCredential(), 
    account_url=storage_account_url, 
    container_name=container_name,
    blob_name=f'{data_folder_on_storage}/MLTable'
)

# upload to cloud storage
with open(f'{local_folder}/MLTable', "rb") as mltable_file:
    blob_client.upload_blob(mltable_file)

```
