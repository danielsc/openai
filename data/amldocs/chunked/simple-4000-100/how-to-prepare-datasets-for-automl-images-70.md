If you have previously labeled data that you would like to use to train your model, you will first need to upload the images to the default Azure Blob Storage of your Azure ML Workspace and register it as a [data asset](how-to-create-data-assets.md). 

The following script uploads the image data on your local machine at path "./data/odFridgeObjects" to datastore in Azure Blob Storage. It then creates a new data asset with the name "fridge-items-images-object-detection" in your Azure ML Workspace. 

If there already exists a data asset with the name "fridge-items-images-object-detection" in your Azure ML Workspace, it will update the version number of the data asset and point it to the new location where the image data uploaded.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Create a .yml file with the following configuration.

```yml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: fridge-items-images-object-detection
description: Fridge-items images Object detection
path: ./data/odFridgeObjects
type: uri_folder
```

To upload the images as a data asset, you run the following CLI v2 command with the path to your .yml file, workspace name, resource group and subscription ID.

```azurecli
az ml data create -f [PATH_TO_YML_FILE] --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=upload-data)]

# [Studio](#tab/Studio)

![Animation showing how to register a dataset from local files](media\how-to-prepare-datasets-for-automl-images\ui-dataset-local.gif)


If you already have your data present in an existing datastore and want to create a data asset out of it, you can do so by providing the path to the data in the datastore, instead of providing the path of your local machine. Update the code [above](how-to-prepare-datasets-for-automl-images.md#using-pre-labeled-training-data-from-local-machine) with the following snippet.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Create a .yml file with the following configuration.

```yml
$schema: https://azuremlschemas.azureedge.net/latest/data.schema.json
name: fridge-items-images-object-detection
description: Fridge-items images Object detection
path: azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/<path_to_image_data_folder>
type: uri_folder
```

# [Python SDK](#tab/python)

 
```Python
my_data = Data(
    path="azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/<path_to_image_data_folder>",
    type=AssetTypes.URI_FOLDER,
    description="Fridge-items images Object detection",
    name="fridge-items-images-object-detection",
)
```

# [Studio](#tab/Studio)

![Animation showing how to register a dataset from data already present in datastore](media\how-to-prepare-datasets-for-automl-images\ui-dataset-datastore.gif)


Next, you will need to get the label annotations in JSONL format. The schema of labeled data depends on the computer vision task at hand. Refer to [schemas for JSONL files for AutoML computer vision experiments](reference-automl-images-schema.md) to learn more about the required JSONL schema for each task type.

If your training data is in a different format (like, pascal VOC or COCO), [helper scripts](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/image-object-detection/coco2jsonl.py) to convert the data to JSONL are available in [notebook examples](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs).
