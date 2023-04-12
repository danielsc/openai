If your training data is in a different format (like, pascal VOC or COCO), [helper scripts](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/image-object-detection/coco2jsonl.py) to convert the data to JSONL are available in [notebook examples](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs).

Once you have created jsonl file following the above steps, you can register it as a data asset using UI. Make sure you select `stream` type in schema section as shown below.

![Animation showing how to register a data asset from the jsonl files](media\how-to-prepare-datasets-for-automl-images\ui-dataset-jsnol.gif)

### Using pre-labeled training data from Azure Blob storage
If you have your labeled training data present in a container in Azure Blob storage, then you can access it directly from there by [creating a datastore referring to that container](how-to-datastore.md#create-an-azure-blob-datastore). 

## Create MLTable

Once you have your labeled data in JSONL format, you can use it to create `MLTable` as shown below. MLtable packages your data into a consumable object for training.

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

You can then pass in the `MLTable` as a [data input for your AutoML training job](./how-to-auto-train-image-models.md#consume-data).

## Next steps

* [Train computer vision models with automated machine learning](how-to-auto-train-image-models.md).
* [Train a small object detection model with automated machine learning](how-to-use-automl-small-object-detect.md). 
* [Tutorial: Train an object detection model (preview) with AutoML and Python](tutorial-auto-train-image-models.md).
