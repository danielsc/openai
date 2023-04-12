
# Upgrade data management to SDK v2

In V1, an AzureML dataset can either be a `Filedataset` or a `Tabulardataset`.
In V2, an AzureML data asset can be a `uri_folder`, `uri_file` or `mltable`.
You can conceptually map `Filedataset` to `uri_folder` and `uri_file`, `Tabulardataset` to `mltable`.

* URIs (`uri_folder`, `uri_file`) - a Uniform Resource Identifier that is a reference to a storage location on your local computer or in the cloud that makes it easy to access data in your jobs.
* MLTable - a method to abstract the schema definition for tabular data so that it's easier for consumers of the data to materialize the table into a Pandas/Dask/Spark dataframe.

This article gives a comparison of data scenario(s) in SDK v1 and SDK v2.

## Create a `filedataset`/ uri type of data asset

* SDK v1 - Create a `Filedataset`

    ```python
    from azureml.core import Workspace, Datastore, Dataset
    
    # create a FileDataset pointing to files in 'animals' folder and its subfolders recursively
    datastore_paths = [(datastore, 'animals')]
    animal_ds = Dataset.File.from_files(path=datastore_paths)
    
    # create a FileDataset from image and label files behind public web urls
    web_paths = ['https://azureopendatastorage.blob.core.windows.net/mnist/train-images-idx3-ubyte.gz',
                 'https://azureopendatastorage.blob.core.windows.net/mnist/train-labels-idx1-ubyte.gz']
    mnist_ds = Dataset.File.from_files(path=web_paths)
    ```
    
* SDK v2
    * Create a `URI_FOLDER` type data asset

        ```python
        from azure.ai.ml.entities import Data
        from azure.ai.ml.constants import AssetTypes
        
        # Supported paths include:
        # local: './<path>'
        # blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>'
        # ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/'
        # Datastore: 'azureml://datastores/<data_store_name>/paths/<path>'
        
        my_path = '<path>'
        
        my_data = Data(
            path=my_path,
            type=AssetTypes.URI_FOLDER,
            description="<description>",
            name="<name>",
            version='<version>'
        )
        
        ml_client.data.create_or_update(my_data)
        ```

    * Create a `URI_FILE` type data asset.
        ```python
        from azure.ai.ml.entities import Data
        from azure.ai.ml.constants import AssetTypes
        
        # Supported paths include:
        # local: './<path>/<file>'
        # blob:  'https://<account_name>.blob.core.windows.net/<container_name>/<path>/<file>'
        # ADLS gen2: 'abfss://<file_system>@<account_name>.dfs.core.windows.net/<path>/<file>'
        # Datastore: 'azureml://datastores/<data_store_name>/paths/<path>/<file>'
        my_path = '<path>'
        
        my_data = Data(
            path=my_path,
            type=AssetTypes.URI_FILE,
            description="<description>",
            name="<name>",
            version="<version>"
        )
        
        ml_client.data.create_or_update(my_data)
        ```

## Create a tabular dataset/data asset

* SDK v1

    ```python
    from azureml.core import Workspace, Datastore, Dataset
    
    datastore_name = 'your datastore name'
    
    # get existing workspace
    workspace = Workspace.from_config()
        
    # retrieve an existing datastore in the workspace by name
    datastore = Datastore.get(workspace, datastore_name)
    
    # create a TabularDataset from 3 file paths in datastore
    datastore_paths = [(datastore, 'weather/2018/11.csv'),
                       (datastore, 'weather/2018/12.csv'),
                       (datastore, 'weather/2019/*.csv')]
    
    weather_ds = Dataset.Tabular.from_delimited_files(path=datastore_paths)
    ```

* SDK v2 - Create `mltable` data asset via yaml definition

    ```yaml
    type: mltable
    
    paths:
      - pattern: ./*.txt
    transformations:
      - read_delimited:
          delimiter: ,
          encoding: ascii
          header: all_files_same_headers
    ```
