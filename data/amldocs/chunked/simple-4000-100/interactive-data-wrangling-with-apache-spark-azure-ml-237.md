
1. Import and wrangle data using data URI in format `abfss://<FILE_SYSTEM_NAME>@<STORAGE_ACCOUNT_NAME>.dfs.core.windows.net/<PATH_TO_DATA>` as shown in the code sample using the Titanic data.

### Import and wrangle data from Azure Blob storage

You can access Azure Blob storage data with either the storage account access key or a shared access signature (SAS) token. You should [store these credentials in the Azure Key Vault as a secret](#store-azure-storage-account-credentials-as-secrets-in-azure-key-vault), and set them as properties in the session configuration.

To start interactive data wrangling:
1. At the Azure Machine Learning studio left panel, select **Notebooks**.
1. At the **Compute** selection menu, select the Managed (Automatic) Spark compute **AzureML Spark Compute** under **Azure Machine Learning Spark**, or select an attached Synapse Spark pool under **Synapse Spark pool (Preview)** from the **Compute** selection menu.
1. To configure the storage account access key or a shared access signature (SAS) token for data access in Azure Machine Learning Notebooks:

     - For the access key, set property `fs.azure.account.key.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net` as shown in this code snippet:

        ```python
        from pyspark.sql import SparkSession

        sc = SparkSession.builder.getOrCreate()
        token_library = sc._jvm.com.microsoft.azure.synapse.tokenlibrary.TokenLibrary
        access_key = token_library.getSecret("<KEY_VAULT_NAME>", "<ACCESS_KEY_SECRET_NAME>")
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.account.key.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net", access_key
        )
        ```
     - For the SAS token, set property `fs.azure.sas.<BLOB_CONTAINER_NAME>.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net` as shown in this code snippet:
   
        ```python
        from pyspark.sql import SparkSession

        sc = SparkSession.builder.getOrCreate()
        token_library = sc._jvm.com.microsoft.azure.synapse.tokenlibrary.TokenLibrary
        sas_token = token_library.getSecret("<KEY_VAULT_NAME>", "<SAS_TOKEN_SECRET_NAME>")
        sc._jsc.hadoopConfiguration().set(
            "fs.azure.sas.<BLOB_CONTAINER_NAME>.<STORAGE_ACCOUNT_NAME>.blob.core.windows.net",
            sas_token,
        )
        ```
        > [!NOTE]
        > The `get_secret()` calls in the above code snippets require the name of the Azure Key Vault, and the names of the secrets created for the Azure Blob storage account access key or SAS token

2. Execute the data wrangling code in the same notebook. Format the data URI as `wasbs://<BLOB_CONTAINER_NAME>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/<PATH_TO_DATA>` similar to this code snippet

    ```python
    import pyspark.pandas as pd
    from pyspark.ml.feature import Imputer

    df = pd.read_csv(
        "wasbs://<BLOB_CONTAINER_NAME>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/data/titanic.csv",
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
        "wasbs://<BLOB_CONTAINER_NAME>@<STORAGE_ACCOUNT_NAME>.blob.core.windows.net/data/wrangled",
        index_col="PassengerId",
    )
    ```

    > [!NOTE]
    > This Python code sample uses `pyspark.pandas`, which is only supported by Spark runtime version 3.2.

### Import and wrangle data from Azure Machine Learning Datastore

To access data from [Azure Machine Learning Datastore](how-to-datastore.md), define a path to data on the datastore with [URI format](how-to-create-data-assets.md?tabs=cli#supported-paths) `azureml://datastores/<DATASTORE_NAME>/paths/<PATH_TO_DATA>`. To wrangle data from an Azure Machine Learning Datastore in a Notebooks session interactively:
