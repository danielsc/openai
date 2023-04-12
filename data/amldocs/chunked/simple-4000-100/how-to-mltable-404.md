|`take_random_sample`     |    Adds a transformation step to randomly select each row of this MLTable with a probability chance. The probability must be in the range [0, 1]. May optionally set a random seed.     | <code>- take_random_sample:<br>&emsp; &emsp;probability: 0.10<br>&emsp; &emsp;seed:123</code><br> Take a 10 percent random sample of rows using a random seed of 123.

## Create a Data asset

An Azure ML data asset resembles web browser bookmarks (favorites). Instead of remembering long storage paths (URIs) that point to your most frequently used data, you can create a data asset, and then access that asset with a friendly name.

You can create a Table data asset using:

# [CLI](#tab/cli)

```azurecli
az ml data create --name <name_of_asset> --version 1 --path <folder_with_MLTable> --type mltable
```

> [!NOTE]
> The path points to the **folder** that contains the `MLTable` file. The path can be local or remote (a cloud storage URI). If the path is a local folder, then the folder will automatically be uploaded to the default Azure ML datastore in the cloud.

Only the data in the *same* folder as the `MLTable` file will upload when you create data assets from a local folder. That upload will go to the default Azure ML datastore located in the cloud. Then, the asset is created. If any relative path in the `MLTable` `path` section exists, and the data *isn't* in the same folder, the data won't upload, and the relative path won't work.

# [Python](#tab/Python-SDK)

You can create a data asset in Azure Machine Learning with this Python Code:

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# my_path must point to folder containing MLTable artifact (MLTable file + data
# Supported paths include:
# local: './<path>'
# blob:  'wasbs://<container_name>@<account_name>.blob.core.windows.net/<path>'
# ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>'
# Datastore: 'azureml://datastores/<data_store_name>/paths/<path>'

my_path = '<path>'

my_data = Data(
    path=my_path,
    type=AssetTypes.MLTABLE,
    description="<description>",
    name="<name>",
    version='<version>'
)

ml_client.data.create_or_update(my_data)
```
> [!NOTE]
> The path points to the **folder** containing the MLTable artifact.


## An end-to-end example

In this example, you'll author an MLTable file locally, create an asset, and then use the data asset in an Azure ML job.

### Step 1: Download the data for the example
To complete this end-to-end example, first download a sample of the Green Taxi data from *Azure Open Datasets* into a local data folder:

```bash
mkdir data
cd data
wget https://azureopendatastorage.blob.core.windows.net/nyctlc/green/puYear%3D2013/puMonth%3D8/part-00172-tid-4753095944193949832-fee7e113-666d-4114-9fcb-bcd3046479f3-2742-1.c000.snappy.parquet
```

### Step 2: Create the `MLTable` file

Create an `MLTable` file in the data folder:

# [CLI](#tab/cli)

```bash
cd data
touch MLTable
```

Save the following contents to the `MLTable` file:

```yml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

paths:
    - pattern: ./*.parquet

transformations:
    - read_parquet
    - take_random_sample:
          probability: 0.5
          seed: 154
```

# [Python](#tab/Python-SDK)

```python
import mltable
import os

# change the working directory to the data directory
os.chdir("./data")

# define the path to the parquet files using a glob pattern
path = {
    'pattern': './*.parquet'
}

# load from parquet files
tbl = mltable.from_parquet_files(paths=[path])

# create a new table with a random sample of 50% of the rows
new_tbl = tbl.take_random_sample(0.5, 154)

# show the first few records
new_tbl.show()

# save MLTable file in the data directory
new_tbl.save(".")
```


Next, create a Data asset:

# [CLI](#tab/cli)

Execute the following command

```azurecli
cd .. # come up one level from the data directory
az ml data create --name green-sample --version 1 --type mltable --path ./data
```
