The output is a tuple of `output_names` and predictions. Here, `output_names` and `predictions` are lists with length 3*`batch_size` each. For Faster R-CNN order of outputs are boxes, labels and scores, whereas for RetinaNet outputs are boxes, scores, labels. 
  
| Output name       | Output shape  | Output type | Description |
| -------- |----------|-----|------|
| `output_names` | `(3*batch_size)` | List of keys | For a batch size of 2, `output_names` will be `['boxes_0', 'labels_0', 'scores_0', 'boxes_1', 'labels_1', 'scores_1']` |
| `predictions` | `(3*batch_size)` | List of ndarray(float) | For a batch size of 2, `predictions` will take the shape of `[(n1_boxes, 4), (n1_boxes), (n1_boxes), (n2_boxes, 4), (n2_boxes), (n2_boxes)]`. Here, values at each index correspond to same index in `output_names`. |


The following table describes boxes, labels and scores returned for each sample in the batch of images.

| Name       | Shape  | Type | Description |
| -------- |----------|-----|------|
| Boxes | `(n_boxes, 4)`, where each box has `x_min, y_min, x_max, y_max` | ndarray(float) | Model returns *n* boxes with their top-left and bottom-right coordinates. |
| Labels | `(n_boxes)`| ndarray(float) | Label or class ID of an object in each box. |  
| Scores | `(n_boxes)` | ndarray(float) | Confidence score of an object in each box. |    


# [Object detection with YOLO](#tab/object-detect-yolo)

This object detection example uses the model trained on the [fridgeObjects detection dataset](https://cvbp-secondary.z19.web.core.windows.net/datasets/object_detection/odFridgeObjects.zip) of 128 images and 4 classes/labels to explain ONNX model inference. This example trains YOLO models to demonstrate inference steps. For more information on training object detection models, see the [object detection notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items). 

### Input format

The input is a preprocessed image, with the shape `(1, 3, 640, 640)` for a batch size of 1, and a height and width of 640. These numbers correspond to the values used in the training example.        

| Input name       | Input shape  | Input type | Description |
| -------- |----------|-----|--------|
| Input | `(batch_size, num_channels, height, width)` | ndarray(float) | Input is a preprocessed image, with the shape `(1, 3, 640, 640)` for a batch size of 1, and a height of 640 and width of 640.|
        
### Output format
ONNX model predictions contain multiple outputs. The first output is needed to perform non-max suppression for  detections. For ease of use, automated ML displays the output format after the NMS postprocessing step. The output after NMS is a list of boxes, labels, and scores for each sample in the batch. 


| Output name       | Output shape  | Output type | Description |
| -------- |----------|-----|------|
| Output | `(batch_size)`| List of ndarray(float) | Model returns box detections for each sample in the batch |

Each cell in the list indicates box detections of a sample with shape `(n_boxes, 6)`, where each box has `x_min, y_min, x_max, y_max, confidence_score, class_id`.

# [Instance segmentation](#tab/instance-segmentation)

For this instance segmentation example, you use the Mask R-CNN model that has been trained on the [fridgeObjects dataset](https://cvbp-secondary.z19.web.core.windows.net/datasets/object_detection/odFridgeObjectsMask.zip) with 128 images and 4 classes/labels to explain ONNX model inference. For more information on training of the instance segmentation model, see the [instance segmentation notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-instance-segmentation-task-fridge-items).

>[!IMPORTANT]
> Only Mask R-CNN is supported for instance segmentation tasks. The input and output formats are based on Mask R-CNN only.

### Input format

The input is a preprocessed image. The ONNX model for Mask R-CNN has been exported to work with images of different shapes. We recommend that you resize them to a fixed size that's consistent with training image sizes, for better performance.
