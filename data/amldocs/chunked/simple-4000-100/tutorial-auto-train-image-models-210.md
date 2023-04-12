
Using the above helper functions, for any given image, you can run the following code to display the bounding boxes.

```python
image_file = "./odFridgeObjects/images/31.jpg"
jsonl_file = "./odFridgeObjects/train_annotations.jsonl"

plot_ground_truth_boxes_jsonl(image_file, jsonl_file)
```

## Upload data and create MLTable
In order to use the data for training, upload data to default Blob Storage of your Azure ML Workspace and register it as an asset. The benefits of registering data are:
- Easy to share with other members of the team
- Versioning of the metadata (location, description, etc.)
- Lineage tracking

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


Next step is to create `MLTable` from your data in jsonl format as shown below. MLtable package your data into a consumable object for training.

```yaml
paths:
  - file: ./train_annotations.jsonl
transformations:
  - read_json_lines:
        encoding: utf8
        invalid_lines: error
        include_path_column: false
  - convert_column_types:
      - columns: image_url
        column_type: stream_info
```

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

The following configuration creates training and validation data from the MLTable.

```yaml
target_column_name: label
training_data:
  path: data/training-mltable-folder
  type: mltable
validation_data:
  path: data/validation-mltable-folder
  type: mltable
```

# [Python SDK](#tab/python)
 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


You can create data inputs from training and validation MLTable with the following code:

[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=data-load)]


## Configure your object detection experiment

To configure automated ML jobs for image-related tasks, create a task specific AutoML job.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
task: image_object_detection
primary_metric: mean_average_precision
```

# [Python SDK](#tab/python)
 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]


[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=image-object-detection-configuration)]


### Automatic hyperparameter sweeping for image tasks (AutoMode)

> [!IMPORTANT]
> This feature is currently in public preview. This preview version is provided without a service-level agreement. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

In your AutoML job, you can perform an automatic hyperparameter sweep in order to find the optimal model (we call this functionality AutoMode). You only specify the number of trials; the hyperparameter search space, sampling method and early termination policy are not needed. The system will automatically determine the region of the hyperparameter space to sweep based on the number of trials. A value between 10 and 20 will likely work well on many datasets.
