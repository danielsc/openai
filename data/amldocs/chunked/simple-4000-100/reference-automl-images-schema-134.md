
Here, 
- `xmin` = x coordinate of top-left corner of bounding box
- `ymin` = y coordinate of top-left corner of bounding box
- `xmax` = x coordinate of bottom-right corner of bounding box
- `ymax` = y coordinate of bottom-right corner of bounding box



| Key       | Description  | Example |
| -------- |----------|-----|
| `image_url` | Image location in AzureML datastore. <br>`my-subscription-id` needs to be replaced by the Azure subscription where images are located. More information about Azure subscriptions can be found [here](../azure-portal/get-subscription-tenant-id.md). Similarly `my-resource-group`, `my-workspace`, `my-datastore` should be replaced by [resource group name](../azure-resource-manager/management/manage-resource-groups-portal.md#what-is-a-resource-group), [workspace name]( ./concept-workspace.md) and [datastore name](./how-to-datastore.md) respectively. <br> `path_to_image` should be the full path to image on datastore.<br>`Required, String` | `"azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg"` |
| `image_details` | Image details<br>`Optional, Dictionary` | `"image_details":{"format": "jpg", "width": "400px", "height": "258px"}` |
| `format`  | Image type (all the Image formats available in [Pillow](https://pillow.readthedocs.io/en/stable/releasenotes/8.0.1.html) library are supported. But for YOLO only image formats allowed by [opencv](https://pypi.org/project/opencv-python/4.3.0.36/) are supported)<br>`Optional, String from {"jpg", "jpeg", "png", "jpe", "jfif", "bmp", "tif", "tiff"}`  |  `"jpg" or "jpeg" or "png" or "jpe" or "jfif" or "bmp" or "tif" or "tiff"` |
| `width` | Width of the image<br>`Optional, String or Positive Integer`  | `"499px" or 499`|
| `height` | Height of the image<br>`Optional, String or Positive Integer` | `"665px" or 665` |
| `label` (outer key) | List of bounding boxes, where each box is a dictionary of `label, topX, topY, bottomX, bottomY, isCrowd` their top-left and bottom-right coordinates<br>`Required, List of dictionaries` | `[{"label": "cat", "topX": 0.260, "topY": 0.406, "bottomX": 0.735, "bottomY": 0.701, "isCrowd": 0}]` |
| `label` (inner key)| Class/label of the object in the bounding box<br>`Required, String` | `"cat"` |
| `topX` | Ratio of x coordinate of top-left corner of the bounding box and width of the image<br>`Required, Float in the range [0,1]` | `0.260` |
| `topY` | Ratio of y coordinate of top-left corner of the bounding box and height of the image<br>`Required, Float in the range [0,1]` | `0.406` |
| `bottomX` | Ratio of x coordinate of bottom-right corner of the bounding box and width of the image<br>`Required, Float in the range [0,1]` | `0.735` |
| `bottomY` | Ratio of y coordinate of bottom-right corner of the bounding box and height of the image<br>`Required, Float in the range [0,1]` | `0.701` |
| `isCrowd` | Indicates whether the bounding box is around the crowd of objects. If this special flag is set, we skip this particular  bounding box when calculating the metric.<br>`Optional, Bool` | `0` |


Example of a JSONL file for object detection:

```json
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_01.jpg", "image_details": {"format": "jpg", "width": "499px", "height": "666px"}, "label": [{"label": "can", "topX": 0.260, "topY": 0.406, "bottomX": 0.735, "bottomY": 0.701, "isCrowd": 0}]}
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_02.jpg", "image_details": {"format": "jpg", "width": "499px", "height": "666px"}, "label": [{"label": "carton", "topX": 0.172, "topY": 0.153, "bottomX": 0.432, "bottomY": 0.659, "isCrowd": 0}, {"label": "milk_bottle", "topX": 0.300, "topY": 0.566, "bottomX": 0.891, "bottomY": 0.735, "isCrowd": 0}]}
.
.
.
{"image_url": "azureml://subscriptions/my-subscription-id/resourcegroups/my-resource-group/workspaces/my-workspace/datastores/my-datastore/paths/image_data/Image_n.jpg", "image_details": {"format": "jpg", "width": "499px", "height": "666px"}, "label": [{"label": "carton", "topX": 0.0180, "topY": 0.297, "bottomX": 0.380, "bottomY": 0.836, "isCrowd": 0}, {"label": "milk_bottle", "topX": 0.454, "topY": 0.348, "bottomX": 0.613, "bottomY": 0.683, "isCrowd": 0}, {"label": "water_bottle", "topX": 0.667, "topY": 0.279, "bottomX": 0.841, "bottomY": 0.615, "isCrowd": 0}]}
```
