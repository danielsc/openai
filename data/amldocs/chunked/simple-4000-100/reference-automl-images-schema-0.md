
# Data schemas to train computer vision models with automated machine learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]

> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning you are using:"]
> * [v1](v1/reference-automl-images-schema-v1.md)
> * [v2 (current version)](reference-automl-images-schema.md)


Learn how to format your JSONL files for data consumption in automated ML experiments for computer vision tasks during training and inference.


## Data schema for training 

Azure Machine Learning AutoML for Images requires input image data to be prepared in [JSONL](https://jsonlines.org/) (JSON Lines) format. This section describes input data formats or schema for image classification multi-class, image classification multi-label, object detection, and instance segmentation. We'll also provide a sample of final training or validation JSON Lines file.

### Image classification (binary/multi-class)

**Input data format/schema in each JSON Line:**
```json
{
   "image_url":"azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/<path_to_image>",
   "image_details":{
      "format":"image_format",
      "width":"image_width",
      "height":"image_height"
   },
   "label":"class_name",
}
```

| Key       | Description  | Example |
| -------- |----------|-----|
| `image_url` | Image location in AzureML datastore. <br>`my-subscription-id` needs to be replaced by the Azure subscription where images are located. More information about Azure subscriptions can be found [here](../azure-portal/get-subscription-tenant-id.md). Similarly `my-resource-group`, `my-workspace`, `my-datastore` should be replaced by [resource group name](../azure-resource-manager/management/manage-resource-groups-portal.md#what-is-a-resource-group), [workspace name]( ./concept-workspace.md) and [datastore name](./how-to-datastore.md) respectively. <br> `path_to_image` should be the full path to image on datastore.<br>`Required, String` | `"azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg"` |
| `image_details` | Image details<br>`Optional, Dictionary` | `"image_details":{"format": "jpg", "width": "400px", "height": "258px"}` |
| `format`  | Image type (all the available Image formats in [Pillow](https://pillow.readthedocs.io/en/stable/releasenotes/8.0.1.html) library are supported)<br>`Optional, String from {"jpg", "jpeg", "png", "jpe", "jfif","bmp", "tif", "tiff"}`  |  `"jpg" or "jpeg" or "png" or "jpe" or "jfif" or "bmp" or "tif" or "tiff"` |
| `width` | Width of the image<br>`Optional, String or Positive Integer`  | `"400px" or 400`|
| `height` | Height of the image<br>`Optional, String or Positive Integer` | `"200px" or 200` |
| `label` | Class/label of the image<br>`Required, String` | `"cat"` |


Example of a JSONL file for multi-class image classification:
```json
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg", "image_details":{"format": "jpg", "width": "400px", "height": "258px"}, "label": "can"}
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_02.jpg", "image_details": {"format": "jpg", "width": "397px", "height": "296px"}, "label": "milk_bottle"}
.
.
.
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_n.jpg", "image_details": {"format": "jpg", "width": "1024px", "height": "768px"}, "label": "water_bottle"}
  ```

![Image example for image classification multi-class.](media/reference-automl-images-schema/multiclass-predictions.jpg)

### Image classification multi-label

The following is an example of input data format/schema in each JSON Line for image classification.
