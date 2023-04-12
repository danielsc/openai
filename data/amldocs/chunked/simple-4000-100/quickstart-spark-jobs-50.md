    :::image type="content" source="media/quickstart-spark-jobs/find-storage-accounts-service.png" lightbox="media/quickstart-spark-jobs/find-storage-accounts-service.png" alt-text="Expandable screenshot showing search for and selection of Storage accounts service, in Microsoft Azure portal.":::

1. On the **Storage accounts** page, select the Azure Data Lake Storage (ADLS) Gen 2 storage account from the list. A page showing **Overview** of the storage account opens.

    :::image type="content" source="media/quickstart-spark-jobs/storage-accounts-list.png" lightbox="media/quickstart-spark-jobs/storage-accounts-list.png" alt-text="Expandable screenshot showing selection of Azure Data Lake Storage (ADLS) Gen 2 storage account  Storage account.":::

1. Select **Access Control (IAM)** from the left panel.
1. Select **Add role assignment**.

    :::image type="content" source="media/quickstart-spark-jobs/storage-account-add-role-assignment.png" lightbox="media/quickstart-spark-jobs/storage-account-add-role-assignment.png" alt-text="Expandable screenshot showing the Azure access keys screen.":::

1. Search for the role **Storage Blob Data Contributor**.
1. Select the role: **Storage Blob Data Contributor**.
1. Select **Next**.

    :::image type="content" source="media/quickstart-spark-jobs/add-role-assignment-choose-role.png" lightbox="media/quickstart-spark-jobs/add-role-assignment-choose-role.png" alt-text="Expandable screenshot showing the Azure add role assignment screen.":::

1. Select **User, group, or service principal**.
1. Select **+ Select members**.
1. In the textbox under **Select**, search for the user identity.
1. Select the user identity from the list so that it shows under **Selected members**.
1. Select the appropriate user identity.
1. Select **Next**.

    :::image type="content" source="media/quickstart-spark-jobs/add-role-assignment-choose-members.png" lightbox="media/quickstart-spark-jobs/add-role-assignment-choose-members.png" alt-text="Expandable screenshot showing the Azure add role assignment screen Members tab.":::

1. Select **Review + Assign**.

    :::image type="content" source="media/quickstart-spark-jobs/add-role-assignment-review-and-assign.png" lightbox="media/quickstart-spark-jobs/add-role-assignment-review-and-assign.png" alt-text="Expandable screenshot showing the Azure add role assignment screen review and assign tab.":::
1. Repeat steps 2-13 for **Contributor** role assignment.

Data in the Azure Data Lake Storage (ADLS) Gen 2 storage account should become accessible once the user identity has appropriate roles assigned.

## Create parametrized Python code
A Spark job requires a Python script that takes arguments, which can be developed by modifying the Python code developed from [interactive data wrangling](./interactive-data-wrangling-with-apache-spark-azure-ml.md). A sample Python script is shown here.

```python
# titanic.py
import argparse
from operator import add
import pyspark.pandas as pd
from pyspark.ml.feature import Imputer

parser = argparse.ArgumentParser()
parser.add_argument("--titanic_data")
parser.add_argument("--wrangled_data")

args = parser.parse_args()
print(args.wrangled_data)
print(args.titanic_data)

df = pd.read_csv(args.titanic_data, index_col="PassengerId")
imputer = Imputer(inputCols=["Age"], outputCol="Age").setStrategy(
    "mean"
)  # Replace missing values in Age column with the mean value
df.fillna(
    value={"Cabin": "None"}, inplace=True
)  # Fill Cabin column with value "None" if missing
df.dropna(inplace=True)  # Drop the rows which still have any missing value
df.to_csv(args.wrangled_data, index_col="PassengerId")
```

> [!NOTE]
>  - This Python code sample uses `pyspark.pandas`, which is only supported by Spark runtime version 3.2.
>  - Please ensure that `titanic.py` file is uploaded to a folder named `src`. The `src` folder should be located in the same directory where you have created the Python script/notebook or the YAML specification file defining the standalone Spark job.
