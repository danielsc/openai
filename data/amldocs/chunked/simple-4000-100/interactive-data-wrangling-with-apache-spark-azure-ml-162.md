    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/select-azure-machine-learning-spark.png" alt-text="Screenshot showing use of a Managed (Automatic) Spark compute.":::

- To use an attached Synapse Spark pool, select an attached Synapse Spark pool under **Synapse Spark pool (Preview)** from the **Compute** selection menu.

    :::image type="content" source="media/interactive-data-wrangling-with-apache-spark-azure-ml/select-synapse-spark-pools-preview.png" alt-text="Screenshot showing use of an attached spark pool.":::

- This Titanic data wrangling code sample shows use of a data URI in format `abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<PATH_TO_DATA>` with `pyspark.pandas` and `pyspark.ml.feature.Imputer`.

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
    > This Python code sample uses `pyspark.pandas`, which is only supported by Spark runtime version 3.2.

To wrangle data by access through a service principal:

1. Verify that the service principal has **Contributor** and **Storage Blob Data Contributor** [role assignments](#add-role-assignments-in-azure-storage-accounts) in the Azure Data Lake Storage (ADLS) Gen 2 storage account.
1. [Create Azure Key Vault secrets](#store-azure-storage-account-credentials-as-secrets-in-azure-key-vault) for the service principal tenant ID, client ID and client secret values.
1. Select Managed (Automatic) Spark compute **AzureML Spark Compute** under **Azure Machine Learning Spark** from the **Compute** selection menu, or select an attached Synapse Spark pool under **Synapse Spark pool (Preview)** from the **Compute** selection menu
1. To set the service principal tenant ID, client ID and client secret in the configuration, execute the following code sample. 
     - Note that the `get_secret()` call in the code depends on name of the Azure Key Vault, and the names of the Azure Key Vault secrets created for the service principal tenant ID, client ID and client secret. The corresponding property name/values to set in the configuration are as follows:
       - Client ID property: `fs.azure.account.oauth2.client.id.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net`
       - Client secret property: `fs.azure.account.oauth2.client.secret.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net`
       - Tenant ID property: `fs.azure.account.oauth2.client.endpoint.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net`
       - Tenant ID value: `https://login.microsoftonline.com/<TENANT_ID>/oauth2/token`

        ```python
        from pyspark.sql import SparkSession

        sc = SparkSession.builder.getOrCreate()
        token_library = sc._jvm.com.microsoft.azure.synapse.tokenlibrary.TokenLibrary

        # Set up service principal tenant ID, client ID and secret from Azure Key Vault
        client_id = token_library.getSecret("<KEY_VAULT_NAME>", "<CLIENT_ID_SECRET_NAME>")
        tenant_id = token_library.getSecret("<KEY_VAULT_NAME>", "<TENANT_ID_SECRET_NAME>")
        client_secret = token_library.getSecret("<KEY_VAULT_NAME>", "<CLIENT_SECRET_NAME>")

        # Set up service principal which has access of the data
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.auth.type.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net", "OAuth"
        )
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.oauth.provider.type.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net",
            "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
        )
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.oauth2.client.id.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net",
            client_id,
        )
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.oauth2.client.secret.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net",
            client_secret,
        )
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.oauth2.client.endpoint.<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net",
            "https://login.microsoftonline.com/" + tenant_id + "/oauth2/token",
        )
        ```
