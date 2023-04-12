|`layers_to_freeze`| How many layers to freeze for your model. For instance, passing 2 as value for `seresnext` means freezing layer0 and layer1 referring to the below supported model layer info. <br> Must be a positive integer. <br><br> - `'resnet'`: `[('conv1.', 'bn1.'), 'layer1.', 'layer2.', 'layer3.', 'layer4.']` <br> - `'mobilenetv2'`: `['features.0.', 'features.1.', 'features.2.', 'features.3.', 'features.4.', 'features.5.', 'features.6.', 'features.7.', 'features.8.', 'features.9.', 'features.10.', 'features.11.', 'features.12.', 'features.13.', 'features.14.', 'features.15.', 'features.16.', 'features.17.', 'features.18.']` <br> - `'seresnext'`: `['layer0.', 'layer1.', 'layer2.', 'layer3.', 'layer4.']` * `'vit'`: `['patch_embed', 'blocks.0.', 'blocks.1.', 'blocks.2.', 'blocks.3.', 'blocks.4.', 'blocks.5.', 'blocks.6.','blocks.7.', 'blocks.8.', 'blocks.9.', 'blocks.10.', 'blocks.11.']` * `'yolov5_backbone'`: `['model.0.', 'model.1.', 'model.2.', 'model.3.', 'model.4.','model.5.', 'model.6.', 'model.7.', 'model.8.', 'model.9.']` <br> - `'resnet_backbone'`: `['backbone.body.conv1.', 'backbone.body.layer1.', 'backbone.body.layer2.','backbone.body.layer3.', 'backbone.body.layer4.']` | no default  |

## Image classification (multi-class and multi-label) specific hyperparameters

The following table summarizes hyperparmeters for image classification (multi-class and multi-label) tasks.

| Parameter name       | Description           | Default  |
| ------------- |-------------|-----|
| `model_name` | Model name to be used for image classification task at hand. <br> <br> Must be one of `mobilenetv2`, `resnet18`, `resnet34`, `resnet50`, `resnet101`, `resnet152`, `resnest50`, `resnest101`, `seresnext`, `vits16r224`, `vitb16r224`, `vitl16r224`. | `seresnext` |
| `weighted_loss` | - 0 for no weighted loss. <br> - 1 for weighted loss with sqrt.(class_weights) <br> - 2 for weighted loss with class_weights. <br> - Must be 0 or 1 or 2. | 0 |
| `validation_resize_size` | - Image size to which to resize before cropping for validation dataset. <br> - Must be a positive integer. <br> <br> *Notes: <br> - `seresnext` doesn't take an arbitrary size. <br> - Training run may get into CUDA OOM if the size is too big*.  | 256  |
| `validation_crop_size` | - Image crop size that's input to your neural network for validation dataset.  <br> - Must be a positive integer. <br> <br> *Notes: <br> - `seresnext` doesn't take an arbitrary size. <br> - *ViT-variants* should have the same `validation_crop_size` and `training_crop_size`. <br> - Training run may get into CUDA OOM if the size is too big*. | 224 |
| `training_crop_size` | - Image crop size that's input to your neural network for train dataset.  <br> - Must be a positive integer. <br> <br> *Notes: <br> - `seresnext` doesn't take an arbitrary size. <br> - *ViT-variants* should have the same `validation_crop_size` and `training_crop_size`. <br> - Training run may get into CUDA OOM if the size is too big*. | 224 |

## Object detection and instance segmentation task specific hyperparameters

The following hyperparameters are for object detection and instance segmentation tasks.

> [!WARNING]
> These parameters are not supported with the `yolov5` architecture. See the [model specific hyperparameters](#model-specific-hyperparameters) section for `yolov5` supported hyperparmeters.

| Parameter name       | Description           | Default  |
| ------------- |-------------|-----|
| `model_name` | Model name to be used for image classification task at hand. <br> - For object detection task, must be one of `yolov5`, `fasterrcnn_resnet18_fpn`, `fasterrcnn_resnet34_fpn`, `fasterrcnn_resnet50_fpn`, `fasterrcnn_resnet101_fpn`, `fasterrcnn_resnet152_fpn`, `retinanet_resnet50_fpn`. <br> - For instance segmentation task, must be one of `maskrcnn_resnet18_fpn`, `maskrcnn_resnet34_fpn`, `maskrcnn_resnet50_fpn`, `maskrcnn_resnet101_fpn`, `maskrcnn_resnet152_fpn` | - For object detection task, `fasterrcnn_resnet50_fpn` <br> - For instance segmentation task, `maskrcnn_resnet50_fpn` |
