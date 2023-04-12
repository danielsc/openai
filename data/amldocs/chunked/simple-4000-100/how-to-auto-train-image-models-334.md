A number of trials between 10 and 20 will likely work well on many datasets. The [time budget](#job-limits) for the AutoML job can still be set, but we recommend doing this only if each trial may take a long time.

> [!Warning]
> Launching automatic sweeps via the UI is not supported at this time.


### Individual trials

In individual trials, you directly control the model architecture and hyperparameters. The model architecture is passed via the `model_name` parameter.

#### Supported model architectures

The following table summarizes the supported models for each computer vision task.

Task |  model architectures | String literal syntax<br> ***`default_model`\**** denoted with \*
---|----------|----------
Image classification<br> (multi-class and multi-label)| **MobileNet**: Light-weighted models for mobile applications <br> **ResNet**: Residual networks<br> **ResNeSt**: Split attention networks<br> **SE-ResNeXt50**: Squeeze-and-Excitation networks<br> **ViT**: Vision transformer networks| `mobilenetv2`   <br>`resnet18` <br>`resnet34` <br> `resnet50`  <br> `resnet101` <br> `resnet152`    <br> `resnest50` <br> `resnest101`  <br> `seresnext`  <br> `vits16r224` (small) <br> ***`vitb16r224`\**** (base) <br>`vitl16r224` (large)|
Object detection | **YOLOv5**: One stage object detection model   <br>  **Faster RCNN ResNet FPN**: Two stage object detection models  <br> **RetinaNet ResNet FPN**: address class imbalance with Focal Loss <br> <br>*Note: Refer to [`model_size` hyperparameter](reference-automl-images-hyperparameters.md#model-specific-hyperparameters) for YOLOv5 model sizes.*| ***`yolov5`\**** <br> `fasterrcnn_resnet18_fpn` <br> `fasterrcnn_resnet34_fpn` <br> `fasterrcnn_resnet50_fpn` <br> `fasterrcnn_resnet101_fpn` <br> `fasterrcnn_resnet152_fpn` <br> `retinanet_resnet50_fpn` 
Instance segmentation | **MaskRCNN ResNet FPN**| `maskrcnn_resnet18_fpn` <br> `maskrcnn_resnet34_fpn` <br> ***`maskrcnn_resnet50_fpn`\****  <br> `maskrcnn_resnet101_fpn` <br> `maskrcnn_resnet152_fpn`


In addition to controlling the model architecture, you can also tune hyperparameters used for model training. While many of the hyperparameters exposed are model-agnostic, there are instances where hyperparameters are task-specific or model-specific. [Learn more about the available hyperparameters for these instances](reference-automl-images-hyperparameters.md). 

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

If you wish to use the default hyperparameter values for a given architecture (say yolov5), you can specify it using the model_name key in the training_parameters section. For example,

```yaml
training_parameters:
    model_name: yolov5
```
# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

If you wish to use the default hyperparameter values for a given architecture (say yolov5), you can specify it using the model_name parameter in the set_training_parameters method of the task specific `automl` job. For example,

```python
image_object_detection_job.set_training_parameters(model_name="yolov5")
```

### Manually sweeping model hyperparameters

When training computer vision models, model performance depends heavily on the hyperparameter values selected. Often, you might want to tune the hyperparameters to get optimal performance. For computer vision tasks, you can sweep hyperparameters to find the optimal settings for your model. This feature applies the hyperparameter tuning capabilities in Azure Machine Learning. [Learn how to tune hyperparameters](how-to-tune-hyperparameters.md).

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
search_space:
  - model_name:
      type: choice
      values: [yolov5]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.01
    model_size:
      type: choice
      values: [small, medium]

  - model_name:
      type: choice
      values: [fasterrcnn_resnet50_fpn]
    learning_rate:
      type: uniform
      min_value: 0.0001
      max_value: 0.001
    optimizer:
      type: choice
      values: [sgd, adam, adamw]
    min_size:
      type: choice
      values: [600, 800]
```
