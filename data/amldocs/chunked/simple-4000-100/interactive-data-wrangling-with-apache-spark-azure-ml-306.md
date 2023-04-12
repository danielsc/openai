To access data from [Azure Machine Learning Datastore](how-to-datastore.md), define a path to data on the datastore with [URI format](how-to-create-data-assets.md?tabs=cli#supported-paths) `azureml://datastores/<DATASTORE_NAME>/paths/<PATH_TO_DATA>`. To wrangle data from an Azure Machine Learning Datastore in a Notebooks session interactively:

1. Select the Managed (Automatic) Spark compute **AzureML Spark Compute** under **Azure Machine Learning Spark** from the **Compute** selection menu, or select an attached Synapse Spark pool under **Synapse Spark pool (Preview)** from the **Compute** selection menu.
2. This code sample shows how to read and wrangle Titanic data from an Azure Machine Learning Datastore, using `azureml://` datastore URI, `pyspark.pandas` and `pyspark.ml.feature.Imputer`.

    ```python
    import pyspark.pandas as pd
    from pyspark.ml.feature import Imputer

    df = pd.read_csv(
        "azureml://datastores/workspaceblobstore/paths/data/titanic.csv",
        index_col="PassengerId",
    )
    imputer = Imputer(inputCols=["Age"], outputCol="Age").setStrategy(
        "mean"
    )  # Replace missing values in Age column with the mean value
    df.fillna(
        value={"Cabin": "None"}, inplace=True
    )  # Fill Cabin column with value "None" if missing
    df.dropna(inplace=True)  # Drop the rows which still have any missing value
    df.to_csv(
        "azureml://datastores/workspaceblobstore/paths/data/wrangled",
        index_col="PassengerId",
    )
    ```

    > [!NOTE]
    > This Python code sample uses `pyspark.pandas`, which is only supported by Spark runtime version 3.2.

The Azure Machine Learning datastores can access data using Azure storage account credentials 

- access key
- SAS token 
- service principal

or provide credential-less data access. Depending on the datastore type and the underlying Azure storage account type, adopt an appropriate authentication mechanism to ensure data access. This table summarizes the authentication mechanisms to access data in the Azure Machine Learning datastores:

|Storage account type|Credential-less data access|Data access mechanism|Role assignments|
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
|Azure Blob|No|Access key or SAS token|No role assignments needed|
|Azure Blob|Yes|User identity passthrough<sup><b>*</b></sup>|User identity should have [appropriate role assignments](#add-role-assignments-in-azure-storage-accounts) in the Azure Blob storage account|
|Azure Data Lake Storage (ADLS) Gen 2|No|Service principal|Service principal should have [appropriate role assignments](#add-role-assignments-in-azure-storage-accounts) in the Azure Data Lake Storage (ADLS) Gen 2 storage account|
|Azure Data Lake Storage (ADLS) Gen 2|Yes|User identity passthrough|User identity should have [appropriate role assignments](#add-role-assignments-in-azure-storage-accounts) in the Azure Data Lake Storage (ADLS) Gen 2 storage account|

<sup><b>*</b></sup> user identity passthrough works for credential-less datastores that point to Azure Blob storage accounts, only if [soft delete](../storage/blobs/soft-delete-blob-overview.md) is not enabled.

## Accessing data on the default file share

The default file share is mounted to both Managed (Automatic) Spark compute and attached Synapse Spark pools.

:::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/default-file-share.png" alt-text="Screenshot showing use of a file share.":::

In Azure Machine Learning studio, files in the default file share are shown in the directory tree under the **Files** tab. Notebook code can directly access files stored in this file share with `file://` protocol, along with the absolute path of the file, without any additional configurations. This code snippet shows how to access a file stored on the default file share:

```python
import os
import pyspark.pandas as pd
from pyspark.ml.feature import Imputer

abspath = os.path.abspath(".")
file = "file://" + abspath + "/Users/<USER>/data/titanic.csv"
print(file)
df = pd.read_csv(file, index_col="PassengerId")
imputer = Imputer(
    inputCols=["Age"],
    outputCol="Age").setStrategy("mean") # Replace missing values in Age column with the mean value
df.fillna(value={"Cabin" : "None"}, inplace=True) # Fill Cabin column with value "None" if missing
df.dropna(inplace=True) # Drop the rows which still have any missing value
output_path = "file://" + abspath + "/Users/<USER>/data/wrangled"
df.to_csv(output_path, index_col="PassengerId")
```
