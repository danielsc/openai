
#### Folder asset

If you've registered a Folder asset (`uri_folder` or a V1 `FileDataset`) that you want to read into Pandas data frame - for example, a folder containing CSV file - you can achieve this using:

```python
import mltable
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset = ml_client.data.get(name="<name_of_asset>", version="<version>")

path = {
    'folder': data_asset.path
}

tbl = mltable.from_delimited_files(paths=[path])
df = tbl.to_pandas_dataframe()
df.head()
```

## A note on reading and processing large data volumes with Pandas
> [!TIP]
> Pandas is not designed to handle large datasets - you will only be able to process data that can fit into the memory of the compute instance. 
>
> For large datasets we recommend that you use AzureML managed Spark, which provides the [PySpark Pandas API](https://spark.apache.org/docs/latest/api/python/user_guide/pandas_on_spark/index.html).

You may wish to iterate quickly on a smaller subset of a large dataset before scaling up to a remote asynchronous job. `mltable` provides in-built functionality to get samples of large data using the [take_random_sample](/python/api/mltable/mltable.mltable.mltable#mltable-mltable-mltable-take-random-sample) method:

```python
import mltable

path = {
    'file': 'https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv'
}

tbl = mltable.from_delimited_files(paths=[path])
# take a random 30% sample of the data
tbl = tbl.take_random_sample(probability=.3)
df = tbl.to_pandas_dataframe()
df.head()
```

You can also take subsets of large data by using:

- [filter](/python/api/mltable/mltable.mltable.mltable#mltable-mltable-mltable-filter)
- [keep_columns](/python/api/mltable/mltable.mltable.mltable#mltable-mltable-mltable-keep-columns)
- [drop_columns](/python/api/mltable/mltable.mltable.mltable#mltable-mltable-mltable-drop-columns)


## Downloading data using the `azcopy` utility

You may want to download the data to the local SSD of your host (local machine, cloud VM, Azure ML Compute Instance) and use the local filesystem. You can do this with the `azcopy` utility, which is pre-installed on an Azure ML compute instance.  If you are **not** using an Azure ML compute instance or a Data Science Virtual Machine (DSVM), you may need to install `azcopy`. For more information please read [azcopy](../storage/common/storage-ref-azcopy.md).

> [!CAUTION]
> We do not recommend downloading data in the `/home/azureuser/cloudfiles/code` location on a compute instance. This is designed to store notebook and code artifacts, **not** data. Reading data from this location will incur significant performance overhead when training. Instead we recommend storing your data in `home/azureuser`, which is the local SSD of the compute node.

Open a terminal and create a new directory, for example:

```bash
mkdir /home/azureuser/data
```

Sign-in to azcopy using:

```bash
azcopy login
```

Next, you can copy data using a storage URI

```bash
SOURCE=https://<account_name>.blob.core.windows.net/<container>/<path>
DEST=/home/azureuser/data
azcopy cp $SOURCE $DEST
```

## Next steps

- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](interactive-data-wrangling-with-apache-spark-azure-ml.md)
- [Access data in a job](how-to-read-write-data-v2.md)
