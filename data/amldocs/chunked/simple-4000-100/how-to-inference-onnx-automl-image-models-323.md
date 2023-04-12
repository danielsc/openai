This example applies the model trained on the [fridgeObjects](https://cvbp-secondary.z19.web.core.windows.net/datasets/image_classification/fridgeObjects.zip) dataset with 134 images and 4 classes/labels to explain ONNX model inference. For more information on training an image classification task, see the [multi-class image classification notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-classification-multiclass-task-fridge-items).

### Input format
    
The input is a preprocessed image.

| Input name  | Input shape  | Input type | Description |
| -------- |----------:|-----|--------|
| input1 | `(batch_size, num_channels, height, width)` | ndarray(float) | Input is a preprocessed image, with the shape `(1, 3, 224, 224)` for a batch size of 1, and a height and width of 224. These numbers correspond to the values used for `crop_size` in the training example. |
    

### Output format

The output is an array of logits for all the classes/labels.
         
| Output name   | Output shape  | Output type | Description |
| -------- |----------|-----|------|
| output1 | `(batch_size, num_classes)` | ndarray(float) | Model returns logits (without `softmax`). For instance, for batch size 1 and 4 classes, it returns `(1, 4)`. |

# [Multi-label image classification](#tab/multi-label)

This example uses the model trained on the [multi-label fridgeObjects dataset](https://cvbp-secondary.z19.web.core.windows.net/datasets/image_classification/multilabelFridgeObjects.zip) with 128 images and 4 classes/labels to explain ONNX model inference. For more information on model training for multi-label image classification, see the [multi-label image classification notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-classification-multilabel-task-fridge-items).

### Input format

Input is a preprocessed image.

| Input name       | Input shape  | Input type | Description |
| -------- |----------|-----|--------|
| input1 | `(batch_size, num_channels, height, width)` | ndarray(float) | Input is a preprocessed image, with the shape `(1, 3, 224, 224)` for a batch size of 1, and a height and width of 224. These numbers correspond to the values used for `crop_size` in the training example. |
        
### Output format

The output is an array of logits for all the classes/labels.
    
      
| Output name       | Output shape  | Output type | Description |
| -------- |----------|-----|------
| output1 | `(batch_size, num_classes)` | ndarray(float) | Model returns logits (without `sigmoid`). For instance, for batch size 1 and 4 classes, it returns `(1, 4)`. |


# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)

This object detection example uses the model trained on the [fridgeObjects detection dataset](https://cvbp-secondary.z19.web.core.windows.net/datasets/object_detection/odFridgeObjects.zip) of 128 images and 4 classes/labels to explain ONNX model inference. This example trains Faster R-CNN models to demonstrate inference steps. For more information on training object detection models, see the [object detection notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items).

### Input format

Input is a preprocessed image.

| Input name       | Input shape  | Input type | Description |
| -------- |----------|-----|--------|
| Input | `(batch_size, num_channels, height, width)` | ndarray(float) | Input is a preprocessed image, with the shape `(1, 3, 600, 800)` for a batch size of 1, and a height of 600 and width of 800.|
        
    
### Output format

The output is a tuple of `output_names` and predictions. Here, `output_names` and `predictions` are lists with length 3*`batch_size` each. For Faster R-CNN order of outputs are boxes, labels and scores, whereas for RetinaNet outputs are boxes, scores, labels. 
  
| Output name       | Output shape  | Output type | Description |
