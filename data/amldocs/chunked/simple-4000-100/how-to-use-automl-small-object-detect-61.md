To choose the optimal value for this parameter for your dataset, you can use hyperparameter search. To do so, you can specify a choice of values for this parameter in your hyperparameter space.

# [CLI v2](#tab/CLI-v2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
search_space:
  - model_name:
      type: choice
      values: ['fasterrcnn_resnet50_fpn']
    tile_grid_size:
      type: choice
      values: ['2x1', '3x2', '5x3']
```

# [Python SDK v2](#tab/SDK-v2)

```python
image_object_detection_job.extend_search_space(
	SearchSpace(
		model_name=Choice(['fasterrcnn_resnet50_fpn']),
		tile_grid_size=Choice(['2x1', '3x2', '5x3'])
	)
)
```

## Tiling during inference

When a model trained with tiling is deployed, tiling also occurs during inference. Automated ML uses the `tile_grid_size` value from training to generate the tiles during inference. The entire image and corresponding tiles are passed through the model, and the object proposals from them are merged to output final predictions, like in the following image.

:::image type="content" source="./media/how-to-use-automl-small-object-detect/tiles-merge.png" alt-text="Diagram that shows object proposals from image and tiles being merged to form the final predictions.":::

> [!NOTE]
> It's possible that the same object is detected from multiple tiles, duplication detection is done to remove such duplicates.
>
> Duplicate detection is done by running NMS on the proposals from the tiles and the image. When multiple proposals overlap, the one with the highest score is picked and others are discarded as duplicates.Two proposals are considered to be overlapping when the intersection over union (iou) between them is greater than the `tile_predictions_nms_thresh` parameter.

You also have the option to enable tiling only during inference without enabling it in training. To do so, set the `tile_grid_size` parameter only during inference, not for training.

Doing so, may improve performance for some datasets, and won't incur the extra cost that comes with tiling at training time.

## Tiling hyperparameters

The following are the parameters you can use to control the tiling feature.

| Parameter Name	| Description	| Default |
| --------------- |-------------| -------|
| `tile_grid_size` |  The grid size to use for tiling each image. Available for use during training, validation, and inference.<br><br>Should be passed as a string in `'3x2'` format.<br><br> *Note: Setting this parameter increases the computation time proportionally, since all tiles and images are processed by the model.*| no default value |
| `tile_overlap_ratio` | Controls the overlap ratio between adjacent tiles in each dimension. When the objects that fall on the tile boundary are too large to fit completely in one of the tiles, increase the value of this parameter so that the objects fit in at least one of the tiles completely.<br> <br>  Must be a float in [0, 1).| 0.25 |
| `tile_predictions_nms_thresh` | The intersection over union  threshold to use to do non-maximum suppression (nms) while merging predictions from tiles and image. Available during validation and inference. Change this parameter if there are multiple boxes detected per object in the final predictions.  <br><br> Must be float in [0, 1]. | 0.25 |


## Example notebooks

See the [object detection sample notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items/automl-image-object-detection-task-fridge-items.ipynb) for detailed code examples of setting up and training an object detection model.

>[!NOTE]
> All images in this article are made available in accordance with the permitted use section of the [MIT licensing agreement](https://choosealicense.com/licenses/mit/).
> Copyright © 2020 Roboflow, Inc.

## Next steps

* Learn more about [how and where to deploy a model](./how-to-deploy-online-endpoints.md).
* For definitions and examples of the performance charts and metrics provided for each job, see [Evaluate automated machine learning experiment results](how-to-understand-automated-ml.md).
