| `model_name` | Model name to be used for image classification task at hand. <br> - For object detection task, must be one of `yolov5`, `fasterrcnn_resnet18_fpn`, `fasterrcnn_resnet34_fpn`, `fasterrcnn_resnet50_fpn`, `fasterrcnn_resnet101_fpn`, `fasterrcnn_resnet152_fpn`, `retinanet_resnet50_fpn`. <br> - For instance segmentation task, must be one of `maskrcnn_resnet18_fpn`, `maskrcnn_resnet34_fpn`, `maskrcnn_resnet50_fpn`, `maskrcnn_resnet101_fpn`, `maskrcnn_resnet152_fpn` | - For object detection task, `fasterrcnn_resnet50_fpn` <br> - For instance segmentation task, `maskrcnn_resnet50_fpn` |
| `validation_metric_type` | Metric computation method to use for validation metrics.  <br> Must be `none`, `coco`, `voc`, or `coco_voc`. | `voc` |
| `validation_iou_threshold` | IOU threshold for box matching when computing validation metrics.  <br>Must be a float in the range [0.1, 1]. | 0.5 |
| `min_size` | Minimum size of the image to be rescaled before feeding it to the backbone. <br> Must be a positive integer. <br> <br> *Note: training run may get into CUDA OOM if the size is too big*.| 600 |
| `max_size` | Maximum size of the image to be rescaled before feeding it to the backbone. <br> Must be a positive integer.<br> <br> *Note: training run may get into CUDA OOM if the size is too big*. | 1333 |
| `box_score_threshold` | During inference, only return proposals with a classification score greater than `box_score_threshold`. <br> Must be a float in the range [0, 1].| 0.3 |
| `nms_iou_threshold` | IOU (intersection over union) threshold used in non-maximum suppression (NMS) for the prediction head. Used during inference.  <br>Must be a float in the range [0, 1]. | 0.5 |
| `box_detections_per_image` | Maximum number of detections per image, for all classes. <br> Must be a positive integer.| 100 |
| `tile_grid_size` | The grid size to use for tiling each image. <br>*- `tile_grid_size` must not be None to enable [small object detection](how-to-use-automl-small-object-detect.md) logic.*<br>*- `tile_grid_size` is not supported for instance segmentation tasks.*<br> Should be passed as a string in '3x2' format. Example: --tile_grid_size '3x2' | No Default |
| `tile_overlap_ratio` | Overlap ratio between adjacent tiles in each dimension. <br> Must be float in the range of [0, 1) | 0.25 |
| `tile_predictions_nms_threshold` | The IOU threshold to use to perform NMS while merging predictions from tiles and image. Used in validation/ inference. <br> Must be float in the range of [0, 1] | 0.25 |

## Next steps

* Learn how to [Set up AutoML to train computer vision models with Python](how-to-auto-train-image-models.md).

* [Tutorial: Train an object detection model with AutoML and Python](tutorial-auto-train-image-models.md).
