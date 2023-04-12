
# Upgrade datastore management to SDK v2

Azure Machine Learning Datastores securely keep the connection information to your data storage on Azure, so you don't have to code it in your scripts. V2 Datastore concept remains mostly unchanged compared with V1. The difference is we won't support SQL-like data sources via AzureML Datastores. We'll support SQL-like data sources via AzureML data import&export functionalities.

This article gives a comparison of scenario(s) in SDK v1 and SDK v2.

## Create a datastore from an Azure Blob container via account_key 

* SDK v1

    ```python
    blob_datastore_name='azblobsdk' # Name of the datastore to workspace
    container_name=os.getenv("BLOB_CONTAINER", "<my-container-name>") # Name of Azure blob container
    account_name=os.getenv("BLOB_ACCOUNTNAME", "<my-account-name>") # Storage account name
    account_key=os.getenv("BLOB_ACCOUNT_KEY", "<my-account-key>") # Storage account access key
    
    blob_datastore = Datastore.register_azure_blob_container(workspace=ws, 
                                                             datastore_name=blob_datastore_name, 
                                                             container_name=container_name, 
                                                             account_name=account_name,
                                                             account_key=account_key)
    ```


* SDK v2

    ```python
    from azure.ai.ml.entities import AzureBlobDatastore
    from azure.ai.ml import MLClient
    
    ml_client = MLClient.from_config()
    
    store = AzureBlobDatastore(
        name="blob-protocol-example",
        description="Datastore pointing to a blob container using wasbs protocol.",
        account_name="mytestblobstore",
        container_name="data-container",
        protocol="wasbs",
        credentials={
            "account_key": "XXXxxxXXXxXXXXxxXXXXXxXXXXXxXxxXxXXXxXXXxXXxxxXXxxXXXxXxXXXxxXxxXXXXxxxxxXXxxxxxxXXXxXXX"
        },
    )
    
    ml_client.create_or_update(store)
    ```


## Create a datastore from an Azure Blob container via sas_token

* SDK v1

    ```python
    blob_datastore_name='azblobsdk' # Name of the datastore to workspace
    container_name=os.getenv("BLOB_CONTAINER", "<my-container-name>") # Name of Azure blob container
    sas_token=os.getenv("BLOB_SAS_TOKEN", "<my-sas-token>") # Sas token
    
    blob_datastore = Datastore.register_azure_blob_container(workspace=ws, 
                                                             datastore_name=blob_datastore_name, 
                                                             container_name=container_name, 
                                                             sas_token=sas_token)
    ```
    
* SDK v2

    ```python
    from azure.ai.ml.entities import AzureBlobDatastore
    from azure.ai.ml import MLClient
    
    ml_client = MLClient.from_config()
    
    store = AzureBlobDatastore(
        name="blob-sas-example",
        description="Datastore pointing to a blob container using SAS token.",
        account_name="mytestblobstore",
        container_name="data-container",
        credentials=SasTokenCredentials(
            sas_token= "?xx=XXXX-XX-XX&xx=xxxx&xxx=xxx&xx=xxxxxxxxxxx&xx=XXXX-XX-XXXXX:XX:XXX&xx=XXXX-XX-XXXXX:XX:XXX&xxx=xxxxx&xxx=XXxXXXxxxxxXXXXXXXxXxxxXXXXXxxXXXXXxXXXXxXXXxXXxXX"
        ),
    )
    
    ml_client.create_or_update(store)
    ```
    
## Create a datastore from an Azure Blob container via identity-based authentication

* SDK v1

```python
blob_datastore = Datastore.register_azure_blob_container(workspace=ws,
                                                      datastore_name='credentialless_blob',
                                                      container_name='my_container_name',
                                                      account_name='my_account_name')

```

* SDK v2

    ```python
    from azure.ai.ml.entities import AzureBlobDatastore
    from azure.ai.ml import MLClient
    
    ml_client = MLClient.from_config()
    
    store = AzureBlobDatastore(
        name="",
        description="",
        account_name="",
        container_name=""
    )
    
    ml_client.create_or_update(store)
    ```
