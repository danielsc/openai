
# Create jobs and input data for batch endpoints

Batch endpoints can be used to perform batch scoring on large amounts of data. Such data can be placed in different places. In this tutorial we'll cover the different places where batch endpoints can read data from and how to reference it.

## Prerequisites

* This example assumes that you've a model correctly deployed as a batch endpoint. Particularly, we're using the *heart condition classifier* created in the tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).

## Supported data inputs

Batch endpoints support reading files located in the following storage options:

* [Azure Machine Learning Data Assets](#input-data-from-a-data-asset). The following types are supported:
    * Data assets of type Folder (`uri_folder`).
    * Data assets of type File (`uri_file`).
    * Datasets of type `FileDataset` (Deprecated).
* [Azure Machine Learning Data Stores](#input-data-from-data-stores). The following stores are supported:
    * Azure Blob Storage
    * Azure Data Lake Storage Gen1
    * Azure Data Lake Storage Gen2
* [Azure Storage Accounts](#input-data-from-azure-storage-accounts). The following storage containers are supported:
    * Azure Data Lake Storage Gen1
    * Azure Data Lake Storage Gen2
    * Azure Blob Storage

> [!TIP]
> Local data folders/files can be used when executing batch endpoints from the Azure ML CLI or Azure ML SDK for Python. However, that operation will result in the local data to be uploaded to the default Azure Machine Learning Data Store of the workspace you are working on.

> [!IMPORTANT]
> __Deprecation notice__: Datasets of type `FileDataset` (V1) are deprecated and will be retired in the future. Existing batch endpoints relying on this functionality will continue to work but batch endpoints created with GA CLIv2 (2.4.0 and newer) or GA REST API (2022-05-01 and newer) will not support V1 dataset.


## Input data from a data asset

Azure Machine Learning data assets (formerly known as datasets) are supported as inputs for jobs. Follow these steps to run a batch endpoint job using data stored in a registered data asset in Azure Machine Learning:

> [!WARNING]
> Data assets of type Table (`MLTable`) aren't currently supported.

1. Let's create the data asset first. This data asset consists of a folder with multiple CSV files that we want to process in parallel using batch endpoints. You can skip this step is your data is already registered as a data asset.

    # [Azure CLI](#tab/cli)
   
    Create a data asset definition in `YAML`:
   
    __heart-dataset-unlabeled.yml__
    ```yaml
    $schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
    name: heart-dataset-unlabeled
    description: An unlabeled dataset for heart classification.
    type: uri_folder
    path: heart-classifier-mlflow/data
    ```
   
    Then, create the data asset:
   
    ```bash
    az ml data create -f heart-dataset-unlabeled.yml
    ```
   
    # [Python](#tab/sdk)
   
    ```python
    data_path = "heart-classifier-mlflow/data"
    dataset_name = "heart-dataset-unlabeled"
 
    heart_dataset_unlabeled = Data(
        path=data_path,
        type=AssetTypes.URI_FOLDER,
        description="An unlabeled dataset for heart classification",
        name=dataset_name,
    )
    ```
    
    Then, create the data asset:
    
    ```python
    ml_client.data.create_or_update(heart_dataset_unlabeled)
    ```
    
    To get the newly created data asset, use:
    
    ```python
    heart_dataset_unlabeled = ml_client.data.get(name=dataset_name, label="latest")
    ```

    # [REST](#tab/rest)

    Use the Azure ML CLI, Azure ML SDK for Python, or Studio to get the location (region), workspace, and data asset name and version. You will need them later.


1. Create a data input:

    # [Azure CLI](#tab/cli)
    
    ```azurecli
    DATASET_ID=$(az ml data show -n heart-dataset-unlabeled --label latest --query id)
    ```

    # [Python](#tab/sdk)
