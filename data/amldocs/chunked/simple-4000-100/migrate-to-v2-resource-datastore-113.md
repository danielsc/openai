
## Get datastores from your workspace

* SDK v1

    ```python
    # Get a named datastore from the current workspace
    datastore = Datastore.get(ws, datastore_name='your datastore name')
    ```
    
    ```python
    # List all datastores registered in the current workspace
    datastores = ws.datastores
    for name, datastore in datastores.items():
        print(name, datastore.datastore_type)
    ```

* SDK v2
    
    ```python
    from azure.ai.ml import MLClient
    from azure.identity import DefaultAzureCredential
    
    #Enter details of your AzureML workspace
    subscription_id = '<SUBSCRIPTION_ID>'
    resource_group = '<RESOURCE_GROUP>'
    workspace_name = '<AZUREML_WORKSPACE_NAME>'
    
    ml_client = MLClient(credential=DefaultAzureCredential(),
                         subscription_id=subscription_id, 
                         resource_group_name=resource_group)
    
    datastore = ml_client.datastores.get(name='your datastore name')
    ```

## Mapping of key functionality in SDK v1 and SDK v2

|Storage types in SDK v1|Storage types in SDK v2|
|--------------|-------------------|
|[azureml_blob_datastore](/python/api/azureml-core/azureml.data.azure_storage_datastore.azureblobdatastore?view=azure-ml-py&preserve-view=true)|[azureml_blob_datastore](/python/api/azure-ai-ml/azure.ai.ml.entities.azuredatalakegen1datastore)|
|[azureml_data_lake_gen1_datastore](/python/api/azureml-core/azureml.data.azure_data_lake_datastore.azuredatalakedatastore?view=azure-ml-py&preserve-view=true)|[azureml_data_lake_gen1_datastore](/python/api/azure-ai-ml/azure.ai.ml.entities.azuredatalakegen1datastore)|
|[azureml_data_lake_gen2_datastore](/python/api/azureml-core/azureml.data.azure_data_lake_datastore.azuredatalakegen2datastore?view=azure-ml-py&preserve-view=true)|[azureml_data_lake_gen2_datastore](/python/api/azure-ai-ml/azure.ai.ml.entities.azuredatalakegen2datastore)|
|[azuremlml_sql_database_datastore](/python/api/azureml-core/azureml.data.azure_sql_database_datastore.azuresqldatabasedatastore?view=azure-ml-py&preserve-view=true)|Will be supported via import & export functionalities|
|[azuremlml_my_sql_datastore](/python/api/azureml-core/azureml.data.azure_my_sql_datastore.azuremysqldatastore?view=azure-ml-py&preserve-view=true)|Will be supported via import & export functionalities|
|[azuremlml_postgre_sql_datastore](/python/api/azureml-core/azureml.data.azure_postgre_sql_datastore.azurepostgresqldatastore?view=azure-ml-py&preserve-view=true)|Will be supported via import & export functionalities|


## Next steps

For more information, see:

* [Create datastores](how-to-datastore.md?tabs=cli-identity-based-access%2Csdk-adls-sp%2Csdk-azfiles-sas%2Csdk-adlsgen1-sp)
* [Read and write data in a job](how-to-read-write-data-v2.md)
* [V2 datastore operations](/python/api/azure-ai-ml/azure.ai.ml.operations.datastoreoperations)

