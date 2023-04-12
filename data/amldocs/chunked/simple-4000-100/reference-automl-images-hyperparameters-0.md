
# Hyperparameters for computer vision tasks in automated machine learning

[!INCLUDE [dev v2](../../includes/machine-learning-dev-v2.md)]
> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning you are using:"]
> * [v1](v1/reference-automl-images-hyperparameters-v1.md)
> * [v2 (current version)](reference-automl-images-hyperparameters.md)

Learn which hyperparameters are available specifically for computer vision tasks in automated ML experiments.

With support for computer vision tasks, you can control the model architecture and sweep hyperparameters. These model architectures and hyperparameters are passed in as the parameter space for the sweep. While many of the hyperparameters exposed are model-agnostic, there are instances where hyperparameters are model-specific or task-specific.

## Model-specific hyperparameters

This table summarizes hyperparameters specific to the `yolov5` architecture.

| Parameter name       | Description           | Default  |
| ------------- |-------------|----|
| `validation_metric_type` | Metric computation method to use for validation metrics.  <br> Must be `none`, `coco`, `voc`, or `coco_voc`. | `voc` |
| `validation_iou_threshold` | IOU threshold for box matching when computing validation metrics.  <br>Must be a float in the range [0.1, 1]. | 0.5 |
| `image_size` | Image size for train and validation. <br> Must be a positive integer. <br> <br> *Note: training run may get into CUDA OOM if the size is too big*. | 640 |
| `model_size` | Model size. <br> Must be `small`, `medium`, `large`, or `extra_large`. <br><br> *Note: training run may get into CUDA OOM if the model size is too big*.  | `medium` |
| `multi_scale` | Enable multi-scale image by varying image size by +/- 50% <br> Must be 0 or 1. <br> <br> *Note: training run may get into CUDA OOM if no sufficient GPU memory*. | 0 |
| `box_score_threshold` | During inference, only return proposals with a score greater than `box_score_threshold`. The score is the multiplication of the objectness score and classification probability. <br> Must be a float in the range [0, 1]. | 0.1 |
| `nms_iou_threshold` | IOU threshold used during inference in non-maximum suppression post processing. <br> Must be a float in the range [0, 1]. | 0.5 |
| `tile_grid_size` | The grid size to use for tiling each image. <br>*Note: tile_grid_size must not be None to enable [small object detection](how-to-use-automl-small-object-detect.md) logic*<br> Should be passed as a string in '3x2' format. Example: --tile_grid_size '3x2' | No Default |
| `tile_overlap_ratio` | Overlap ratio between adjacent tiles in each dimension. <br> Must be float in the range of [0, 1) | 0.25 |
| `tile_predictions_nms_threshold` | The IOU threshold to use to perform NMS while merging predictions from tiles and image. Used in validation/ inference. <br> Must be float in the range of [0, 1] | 0.25 |

This table summarizes hyperparameters specific to the `maskrcnn_*` for instance segmentation during inference.

| Parameter name       | Description           | Default  |
| ------------- |-------------|----|
| `mask_pixel_score_threshold` | Score cutoff for considering a pixel as part of the mask of an object. | 0.5 |
| `max_number_of_polygon_points` | Maximum number of (x, y) coordinate pairs in polygon after converting from a mask. | 100 |
| `export_as_image` | Export masks as images. | False |
| `image_type` | Type of image to export mask as (options are jpg, png, bmp).  | JPG |

## Model agnostic hyperparameters

The following table describes the hyperparameters that are model agnostic.

| Parameter name | Description | Default|
| ------------ | ------------- | ------------ |
| `number_of_epochs` | Number of training epochs. <br>Must be a positive integer. |  15 <br> (except `yolov5`: 30) |
| `training_batch_size` | Training batch size.<br> Must be a positive integer.  | Multi-class/multi-label: 78 <br>(except *vit-variants*: <br> `vits16r224`: 128 <br>`vitb16r224`: 48 <br>`vitl16r224`:10)<br><br>Object detection: 2 <br>(except `yolov5`: 16) <br><br> Instance segmentation: 2  <br> <br> *Note: The defaults are largest batch size that can be used on 12 GiB GPU memory*.|
