1. Select the user identity from the list, so that it shows under **Selected members**
1. Select the appropriate user identity
1. Select **Next**

    :::image type="content" source="media/quickstart-spark-data-wrangling/add-role-assignment-choose-members.png" lightbox="media/quickstart-spark-data-wrangling/add-role-assignment-choose-members.png" alt-text="Screenshot showing the Azure add role assignment screen Members tab.":::

1. Select **Review + Assign**

    :::image type="content" source="media/quickstart-spark-data-wrangling/add-role-assignment-review-and-assign.png" lightbox="media/quickstart-spark-data-wrangling/add-role-assignment-review-and-assign.png" alt-text="Screenshot showing the Azure add role assignment screen review and assign tab.":::
1. Repeat steps 2-13 for **Contributor** role assignment.

Once the user identity has the appropriate roles assigned, data in the Azure storage account should become accessible.

## Managed (Automatic) Spark compute in Azure Machine Learning Notebooks

A Managed (Automatic) Spark compute is available in Azure Machine Learning Notebooks by default. To access it in a notebook, start in the **Compute** selection menu, and select **AzureML Spark Compute** under **Azure Machine Learning Spark**.

:::image type="content" source="media/quickstart-spark-data-wrangling/select-azure-ml-spark-compute.png" lightbox="media/quickstart-spark-data-wrangling/select-azure-ml-spark-compute.png" alt-text="Screenshot highlighting the selected Azure Machine Learning Spark option, located at the Compute selection menu.":::

## Interactive data wrangling with Titanic data

> [!TIP]
> Data wrangling with a Managed (Automatic) Spark compute, and user identity passthrough for data access in an Azure Data Lake Storage (ADLS) Gen 2 storage account, both require the lowest number of configuration steps.

The data wrangling code shown here uses the `titanic.csv` file, available [here](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/spark/data/titanic.csv). Upload this file to a container created in the Azure Data Lake Storage (ADLS) Gen 2 storage account. This Python code snippet shows interactive data wrangling with an Azure Machine Learning Managed (Automatic) Spark compute, user identity passthrough, and an input/output data URI, in the `abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<PATH_TO_DATA>` format. Here, `<FILE_SYSTEM_NAME>` matches the container name.

```python
import pyspark.pandas as pd
from pyspark.ml.feature import Imputer

df = pd.read_csv(
    "abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/titanic.csv",
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
    "abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/data/wrangled",
    index_col="PassengerId",
)
```

> [!NOTE]
> Only the Spark runtime version 3.2 supports `pyspark.pandas`, used in this Python code sample.

:::image type="content" source="media/quickstart-spark-data-wrangling/managed-spark-interactive-data-wrangling.png" lightbox="media/quickstart-spark-data-wrangling/managed-spark-interactive-data-wrangling.png" alt-text="Screenshot showing use of a Managed (Automatic) Spark compute, for interactive data wrangling.":::

## Next steps
- [Apache Spark in Azure Machine Learning (preview)](./apache-spark-azure-ml-concepts.md)
- [Quickstart: Submit Apache Spark jobs in Azure Machine Learning (preview)](./quickstart-spark-jobs.md)
- [Attach and manage a Synapse Spark pool in Azure Machine Learning (preview)](./how-to-manage-synapse-spark-pool.md)
- [Interactive Data Wrangling with Apache Spark in Azure Machine Learning (preview)](./interactive-data-wrangling-with-apache-spark-azure-ml.md)
