[!Notebook-python[] (~/azureml-examples-main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb?name=pass-arguments)]



## Data augmentation 

In general, deep learning model performance can often improve with more data. Data augmentation is a practical technique to amplify the data size and variability of a dataset which helps to prevent overfitting and improve the model’s generalization ability on unseen data. Automated ML applies different data augmentation techniques based on the computer vision task, before feeding input images to the model. Currently, there's no exposed hyperparameter to control data augmentations. 

|Task | Impacted dataset | Data augmentation technique(s) applied |
|-------|----------|---------|
|Image classification (multi-class and multi-label) | Training <br><br><br> Validation & Test| Random resize and crop, horizontal flip, color jitter (brightness, contrast, saturation, and hue), normalization using channel-wise ImageNet’s mean and standard deviation <br><br><br>Resize, center crop, normalization |
|Object detection, instance segmentation| Training <br><br> Validation & Test |Random crop around bounding boxes, expand, horizontal flip, normalization, resize <br><br><br>Normalization, resize
|Object detection using yolov5| Training <br><br> Validation & Test  |Mosaic, random affine (rotation, translation, scale, shear), horizontal flip <br><br><br> Letterbox resizing|

Currently the augmentations defined above are applied by default for an Automated ML for image job. To provide control over augmentations, Automated ML for images exposes below two flags to turn-off certain augmentations. Currently, these flags are only supported for object detection and instance segmentation tasks. 
 1. **apply_mosaic_for_yolo:** This flag is only specific to Yolo model. Setting it to False turns off the mosaic data augmentation which is applied at the training time.
 2. **apply_automl_train_augmentations:** Setting this flag to false turns off the augmentation applied during training time for the object detection and instance segmentation models. For augmentations, see the details in the table above.
    - For non-yolo object detection model and instance segmentation models, this flag turns off only the first three augmentations i.e., *Random crop around bounding boxes, expand, horizontal flip*. The normalization and resize augmentations are still applied regardless of this flag.
    - For Yolo model, this flag turns off the random affine and horizontal flip augmentations.

These two flags are supported via *advanced_settings* under *training_parameters* and can be controlled in the following way.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_parameters:
  advanced_settings: >
    {"apply_mosaic_for_yolo": false}
```
```yaml
training_parameters:
  advanced_settings: >
    {"apply_automl_train_augmentations": false}
```
 Please note that these two flags are independent of each other and can also be used in combination using the following settings.
 ```yaml
training_parameters:
  advanced_settings: >
    {"apply_automl_train_augmentations": false, "apply_mosaic_for_yolo": false}
```

# [Python SDK](#tab/python)

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
 
```python
from azure.ai.ml import automl

image_object_detection_job = automl.image_object_detection(...)

image_object_detection_job.set_training_parameters(
    ...,
    advanced_settings='{"apply_mosaic_for_yolo": false}'
)
```

```python
from azure.ai.ml import automl

image_object_detection_job = automl.image_object_detection(...)

image_object_detection_job.set_training_parameters(
    ...,
    advanced_settings='{"apply_automl_train_augmentations": false}'
)
```
 Please note that these two flags are independent of each other and can also be used in combination using the following settings.
