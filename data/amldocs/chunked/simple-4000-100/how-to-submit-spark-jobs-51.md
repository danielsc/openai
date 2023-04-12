If the CLI or SDK code defines an option to use managed identity, Azure Machine Learning Managed (Automatic) Spark compute uses user-assigned managed identity attached to the workspace. You can attach a user-assigned managed identity to an existing Azure Machine Learning workspace using Azure Machine Learning CLI v2, or with `ARMClient`.

### Attach user assigned managed identity using CLI v2
1. Create a YAML file that defines the user-assigned managed identity that should be attached to the workspace:
    ```yaml
    identity:
      type: system_assigned,user_assigned
      tenant_id: <TENANT_ID>
      user_assigned_identities:
        '/subscriptions/<SUBSCRIPTION_ID/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID>':
          {}
    ```
1. With the `--file` parameter, use the YAML file in the `az ml workspace update` command to attach the user assigned managed identity:
    ```azurecli
    az ml workspace update --subscription <SUBSCRIPTION_ID> --resource-group <RESOURCE_GROUP> --name <AML_WORKSPACE_NAME> --file <YAML_FILE_NAME>.yaml
    ```

### Attach user assigned managed identity using `ARMClient`
1. Install [ARMClient](https://github.com/projectkudu/ARMClient), a simple command line tool that invokes the Azure Resource Manager API.
1. Create a JSON file that defines the user-assigned managed identity that should be attached to the workspace:
    ```json
    {
        "properties":{
        },
        "location": "<AZURE_REGION>",
        "identity":{
            "type":"SystemAssigned,UserAssigned",
            "userAssignedIdentities":{
                "/subscriptions/<SUBSCRIPTION_ID/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<AML_USER_MANAGED_ID>": { }
            }
        }
    }
    ```
1. Execute the following command in the PowerShell prompt or the command prompt, to attach the user-assigned managed identity to the workspace.
    ```cmd
    armclient PATCH https://management.azure.com/subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP>/providers/Microsoft.MachineLearningServices/workspaces/<AML_WORKSPACE_NAME>?api-version=2022-05-01 '@<JSON_FILE_NAME>.json'
    ```

> [!NOTE]
> - To ensure successful execution of the Spark job, assign the **Contributor** and **Storage Blob Data Contributor** roles, on the Azure storage account used for data input and output, to the identity that the Spark job uses
> - If an [attached Synapse Spark pool](./how-to-manage-synapse-spark-pool.md) points to a Synapse Spark pool, in an Azure Synapse workspace that has a managed virtual network associated with it, [a managed private endpoint to storage account should be configured](../synapse-analytics/security/connect-to-a-secure-storage-account.md) to ensure data access.

## Submit a standalone Spark job
A Python script developed by [interactive data wrangling](./interactive-data-wrangling-with-apache-spark-azure-ml.md) can be used to submit a batch job to process a larger volume of data, after making necessary changes for Python script parameterization. A simple data wrangling batch job can be submitted as a standalone Spark job.

A Spark job requires a Python script that takes arguments, which can be developed with modification of the Python code developed from [interactive data wrangling](./interactive-data-wrangling-with-apache-spark-azure-ml.md). A sample Python script is shown here.

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
