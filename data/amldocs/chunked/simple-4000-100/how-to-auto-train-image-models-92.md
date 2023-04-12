> Creation of `MLTable` from data in JSONL format is supported using the SDK and CLI only, for this capability. Creating the `MLTable` via UI is not supported at this time. 


### JSONL schema samples

The structure of the TabularDataset depends upon the task at hand. For computer vision task types, it consists of the following fields:

Field| Description
---|---
`image_url`| Contains filepath as a StreamInfo object
`image_details`|Image metadata information consists of height, width, and format. This field is optional and hence may or may not exist.
`label`| A json representation of the image label, based on the task type.

The following is a sample JSONL file for image classification:

```json
{
      "image_url": "azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/image_data/Image_01.png",
      "image_details":
      {
          "format": "png",
          "width": "2230px",
          "height": "4356px"
      },
      "label": "cat"
  }
  {
      "image_url": "azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/image_data/Image_02.jpeg",
      "image_details":
      {
          "format": "jpeg",
          "width": "3456px",
          "height": "3467px"
      },
      "label": "dog"
  }
  ```

  The following code is a sample JSONL file for object detection:

  ```json
  {
      "image_url": "azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/image_data/Image_01.png",
      "image_details":
      {
          "format": "png",
          "width": "2230px",
          "height": "4356px"
      },
      "label":
      {
          "label": "cat",
          "topX": "1",
          "topY": "0",
          "bottomX": "0",
          "bottomY": "1",
          "isCrowd": "true",
      }
  }
  {
      "image_url": "azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/image_data/Image_02.png",
      "image_details":
      {
          "format": "jpeg",
          "width": "1230px",
          "height": "2356px"
      },
      "label":
      {
          "label": "dog",
          "topX": "0",
          "topY": "1",
          "bottomX": "0",
          "bottomY": "1",
          "isCrowd": "false",
      }
  }
  ```


### Consume data

Once your data is in JSONL format, you can create training and validation `MLTable` as shown below.

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

Automated ML doesn't impose any constraints on training or validation data size for computer vision tasks. Maximum dataset size is only limited by the storage layer behind the dataset (i.e. blob store). There's no minimum number of images or labels. However, we recommend starting with a minimum of 10-15 samples per label to ensure the output model is sufficiently trained. The higher the total number of labels/classes, the more samples you need per label.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Training data is a required parameter and is passed in using the `training_data` key. You can optionally specify another MLtable as a validation data with the `validation_data` key. If no validation data is specified, 20% of your training data will be used for validation by default, unless you pass `validation_data_size` argument with a different value.

Target column name is a required parameter and used as target for supervised ML task. It's passed in using the `target_column_name` key. For example,

```yaml
target_column_name: label
training_data:
  path: data/training-mltable-folder
  type: mltable
validation_data:
  path: data/validation-mltable-folder
  type: mltable
```
