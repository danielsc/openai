The following is an example of input data format/schema in each JSON Line for image classification.


```json
{
   "image_url":"azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/<path_to_image>",
   "image_details":{
      "format":"image_format",
      "width":"image_width",
      "height":"image_height"
   },
   "label":[
      "class_name_1",
      "class_name_2",
      "class_name_3",
      "...",
      "class_name_n"
        
   ]
}
```

| Key       | Description  | Example |
| -------- |----------|-----|
| `image_url` | Image location in AzureML datastore. <br>`my-subscription-id` needs to be replaced by the Azure subscription where images are located. More information about Azure subscriptions can be found [here](../azure-portal/get-subscription-tenant-id.md). Similarly `my-resource-group`, `my-workspace`, `my-datastore` should be replaced by [resource group name](../azure-resource-manager/management/manage-resource-groups-portal.md#what-is-a-resource-group), [workspace name]( ./concept-workspace.md) and [datastore name](./how-to-datastore.md) respectively. <br> `path_to_image` should be the full path to image on datastore.<br>`Required, String` | `"azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg"` |
| `image_details` | Image details<br>`Optional, Dictionary` | `"image_details":{"format": "jpg", "width": "400px", "height": "258px"}` |
| `format`  | Image type (all the Image formats available in [Pillow](https://pillow.readthedocs.io/en/stable/releasenotes/8.0.1.html) library are supported)<br>`Optional, String from {"jpg", "jpeg", "png", "jpe", "jfif", "bmp", "tif", "tiff"}`  |  `"jpg" or "jpeg" or "png" or "jpe" or "jfif" or "bmp" or "tif" or "tiff"` |
| `width` | Width of the image<br>`Optional, String or Positive Integer`  | `"400px" or 400`|
| `height` | Height of the image<br>`Optional, String or Positive Integer` | `"200px" or 200` |
| `label` | List of classes/labels in the image<br>`Required, List of Strings` | `["cat","dog"]` |


Example of a JSONL file for Image Classification Multi-label:

```json
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg", "image_details":{"format": "jpg", "width": "400px", "height": "258px"}, "label": ["can"]}
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_02.jpg", "image_details": {"format": "jpg", "width": "397px", "height": "296px"}, "label": ["can","milk_bottle"]}
.
.
.
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_n.jpg", "image_details": {"format": "jpg", "width": "1024px", "height": "768px"}, "label": ["carton","milk_bottle","water_bottle"]}
  ```

![Image example for image classification multi-label.](media/reference-automl-images-schema/multilabel-predictions.jpg)

### Object detection

The following is an example JSONL file for object detection.

```json
{
   "image_url":"azureml://subscriptions/<my-subscription-id>/resourcegroups/<my-resource-group>/workspaces/<my-workspace>/datastores/<my-datastore>/paths/<path_to_image>",
   "image_details":{
      "format":"image_format",
      "width":"image_width",
      "height":"image_height"
   },
   "label":[
      {
         "label":"class_name_1",
         "topX":"xmin/width",
         "topY":"ymin/height",
         "bottomX":"xmax/width",
         "bottomY":"ymax/height",
         "isCrowd":"isCrowd"
      },
      {
         "label":"class_name_2",
         "topX":"xmin/width",
         "topY":"ymin/height",
         "bottomX":"xmax/width",
         "bottomY":"ymax/height",
         "isCrowd":"isCrowd"
      },
      "..."
   ]
}
```
