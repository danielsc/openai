---
title: "Create jobs and input data for batch endpoints"
titleSuffix: Azure Machine Learning
description: Learn how to access data from different sources in batch endpoints jobs.
services: machine-learning
ms.service: machine-learning
ms.subservice: core
ms.topic: how-to
author: santiagxf
ms.author: fasantia
ms.date: 10/10/2022
ms.reviewer: larryfr
ms.custom: devplatv2
---

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

    ```python
    input = Input(type=AssetTypes.URI_FOLDER, path=heart_dataset_unlabeled.id)
    ```

    # [REST](#tab/rest)

    __Body__

    ```json
    {
        "properties": {
            "InputData": {
                "mnistinput": {
                    "JobInputType" : "UriFolder",
                    "Uri": "azureml://locations/<location>/workspaces/<workspace>/data/<dataset_name>/versions/labels/latest"
                }
            }
        }
    }
    ```
    ---

    > [!NOTE]
    > Data assets ID would look like `/subscriptions/<subscription>/resourcegroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/data/<data-asset>/versions/<version>`.


1. Run the deployment:

    # [Azure CLI](#tab/cli)
   
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input $DATASET_ID)
    ```

    > [!TIP]
    > You can also use `--input azureml:/<dataasset_name>@latest` as a way to indicate the input.

    # [Python](#tab/sdk)
   
    ```python
    job = ml_client.batch_endpoints.invoke(
       endpoint_name=endpoint.name,
       input=input,
    )
    ```

   # [REST](#tab/rest)

   __Request__
    
    ```http
    POST jobs HTTP/1.1
    Host: <ENDPOINT_URI>
    Authorization: Bearer <TOKEN>
    Content-Type: application/json
    ```

## Input data from data stores

Data from Azure Machine Learning registered data stores can be directly referenced by batch deployments jobs. In this example, we're going to first upload some data to the default data store in the Azure Machine Learning workspace and then run a batch deployment on it. Follow these steps to run a batch endpoint job using data stored in a data store:

1. Let's get access to the default data store in the Azure Machine Learning workspace. If your data is in a different store, you can use that store instead. There's no requirement of using the default data store. 

    # [Azure CLI](#tab/cli)

    ```azurecli
    DATASTORE_ID=$(az ml datastore show -n workspaceblobstore | jq -r '.id')
    ```
    
    > [!NOTE]
    > Data stores ID would look like `/subscriptions/<subscription>/resourceGroups/<resource-group>/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/datastores/<data-store>`.

    # [Python](#tab/sdk)

    ```python
    default_ds = ml_client.datastores.get_default()
    ```

    # [REST](#tab/rest)

    Use the Azure ML CLI, Azure ML SDK for Python, or Studio to get the data store information.
    
    ---
    
    > [!TIP]
    > The default blob data store in a workspace is called __workspaceblobstore__. You can skip this step if you already know the resource ID of the default data store in your workspace.

1. We'll need to upload some sample data to it. This example assumes you've uploaded the sample data included in the repo in the folder `sdk/python/endpoints/batch/heart-classifier/data` in the folder `heart-classifier/data` in the blob storage account. Ensure you have done that before moving forward.

1. Create a data input:

    # [Azure CLI](#tab/cli)
    
    Let's place the file path in the following variable:

    ```azurecli
    DATA_PATH="heart-disease-uci-unlabeled"
    INPUT_PATH="$DATASTORE_ID/paths/$DATA_PATH"
    ```

    # [Python](#tab/sdk)

    ```python
    data_path = "heart-classifier/data"
    input = Input(type=AssetTypes.URI_FOLDER, path=f"{default_ds.id}/paths/{data_path})
    ```

    # [REST](#tab/rest)

    __Body__

    ```json
    {
        "properties": {
            "InputData": {
                "mnistinput": {
                    "JobInputType" : "UriFolder",
                    "Uri": "azureml:/subscriptions/<subscription>/resourceGroups/<resource-group/providers/Microsoft.MachineLearningServices/workspaces/<workspace>/datastores/<data-store>/paths/<data-path>"
                }
            }
        }
    }
    ```
    ---
    
    > [!NOTE]
    > See how the path `paths` is appended to the resource id of the data store to indicate that what follows is a path inside of it.

    > [!TIP]
    > You can also use `azureml://datastores/<data-store>/paths/<data-path>` as a way to indicate the input.

1. Run the deployment:

    # [Azure CLI](#tab/cli)
   
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input $INPUT_PATH)
    ```
   
    # [Python](#tab/sdk)
   
    ```python
    job = ml_client.batch_endpoints.invoke(
       endpoint_name=endpoint.name,
       input=input,
    )
    ```

    # [REST](#tab/rest)

    __Request__
    
    ```http
    POST jobs HTTP/1.1
    Host: <ENDPOINT_URI>
    Authorization: Bearer <TOKEN>
    Content-Type: application/json
    ```

## Input data from Azure Storage Accounts

Azure Machine Learning batch endpoints can read data from cloud locations in Azure Storage Accounts, both public and private. Use the following steps to run a batch endpoint job using data stored in a storage account:

> [!NOTE]
> Check the section [Security considerations when reading data](#security-considerations-when-reading-data) for learn more about additional configuration required to successfully read data from storage accoutns.

1. Create a data input:

    # [Azure CLI](#tab/cli)

    ```azurecli
    INPUT_DATA = "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
    ```

    If your data is a file:

    ```azurecli
    INPUT_DATA = "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
    ```

    # [Python](#tab/sdk)

    ```python
    input = Input(
        type=AssetTypes.URI_FOLDER, 
        path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
    )
    ```

    If your data is a file, change `type=AssetTypes.URI_FILE`:

    ```python
    input = Input(
        type=AssetTypes.URI_FILE,
        path="https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
    )
    ```

    # [REST](#tab/rest)

    __Body__

   ```json
   {
       "properties": {
           "InputData": {
               "mnistinput": {
                   "JobInputType" : "UriFolder",
                   "Uri": "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data"
               }
           }
       }
   }
   ```

   If your data is a file, change `JobInputType`:

   __Body__

   ```json
   {
       "properties": {
           "InputData": {
               "mnistinput": {
                   "JobInputType" : "UriFolder",
                   "Uri": "https://azuremlexampledata.blob.core.windows.net/data/heart-disease-uci/data/heart.csv"
               }
           }
       }
   }
   ```

1. Run the deployment:

    # [Azure CLI](#tab/cli)
    
    If your data is a folder, use `--input-type uri_folder`:
    
    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input-type uri_folder --input $INPUT_DATA)
    ```

    If your data is a file, use `--input-type uri_file`:

    ```bash
    INVOKE_RESPONSE = $(az ml batch-endpoint invoke --name $ENDPOINT_NAME --input-type uri_file --input $INPUT_DATA)
    ```

    # [Python](#tab/sdk)
   
    ```python
    job = ml_client.batch_endpoints.invoke(
       endpoint_name=endpoint.name,
       input=input,
    )
    ```

    # [REST](#tab/rest)

    __Request__
    
    ```http
    POST jobs HTTP/1.1
    Host: <ENDPOINT_URI>
    Authorization: Bearer <TOKEN>
    Content-Type: application/json
    ```
    

## Security considerations when reading data

Batch endpoints ensure that only authorized users are able to invoke batch deployments and generate jobs. However, depending on how the input data is configured, other credentials may be used to read the underlying data. Use the following table to understand which credentials are used and any additional requirements.

| Data input type              | Credential in store             | Credentials used                                              | Access granted by |
|------------------------------|---------------------------------|---------------------------------------------------------------|-------------------|
| Data store                   | Yes                             | Data store's credentials in the workspace                     | Credentials       |
| Data store                   | No                              | Identity of the job                                           | Depends on type   |
| Data asset                   | Yes                             | Data store's credentials in the workspace                     | Credentials       |
| Data asset                   | No                              | Identity of the job                                           | Depends on store  |
| Azure Blob Storage           | Not apply                       | Identity of the job + Managed identity of the compute cluster | RBAC              |
| Azure Data Lake Storage Gen1 | Not apply                       | Identity of the job + Managed identity of the compute cluster | POSIX             |
| Azure Data Lake Storage Gen2 | Not apply                       | Identity of the job + Managed identity of the compute cluster | POSIX and RBAC    |

The managed identity of the compute cluster is used for mounting and configuring external data storage accounts. However, the identity of the job is still used to read the underlying data allowing you to achieve granular access control. That means that in order to successfully read data from external storage services, the managed identity of the compute cluster where the deployment is running must have at least [Storage Blob Data Reader](../role-based-access-control/built-in-roles.md#storage-blob-data-reader) access to the storage account. Only storage account owners can [change your access level via the Azure portal](../storage/blobs/assign-azure-role-data-access.md).

> [!NOTE]
> To assign an identity to the compute used by a batch deployment, follow the instructions at [Set up authentication between Azure ML and other services](how-to-identity-based-service-authentication.md#compute-cluster). Configure the identity on the compute cluster associated with the deployment. Notice that all the jobs running on such compute are affected by this change. However, different deployments (even under the same deployment) can be configured to run under different clusters so you can administer the permissions accordingly depending on your requirements.

## Next steps

* [Troubleshooting batch endpoints](how-to-troubleshoot-batch-endpoints.md).
* [Customize outputs in batch deployments](how-to-deploy-model-custom-output.md).
* [Invoking batch endpoints from Azure Data Factory](how-to-use-batch-azure-data-factory.md).
