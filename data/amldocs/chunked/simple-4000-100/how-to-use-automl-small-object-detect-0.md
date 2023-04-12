
# Train a small object detection model with AutoML

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]
> [!div class="op_single_selector" title1="Select the version of Azure Machine Learning CLI extension you are using:"]
> * [v1](v1/how-to-use-automl-small-object-detect-v1.md)
> * [v2 (current version)](how-to-use-automl-small-object-detect.md)


In this article, you'll learn how to train an object detection model to detect small objects in high-resolution images with [automated ML](concept-automated-ml.md) in Azure Machine Learning.

Typically, computer vision models for object detection work well for datasets with relatively large objects. However, due to memory and computational constraints, these models tend to under-perform when tasked to detect small objects in high-resolution images. Because high-resolution images are typically large, they are resized before input into the model, which limits their capability to detect smaller objects--relative to the initial image size.

To help with this problem, automated ML supports tiling as part of the computer vision capabilities. The tiling capability in automated ML is based on the concepts in [The Power of Tiling for Small Object Detection](https://openaccess.thecvf.com/content_CVPRW_2019/papers/UAVision/Unel_The_Power_of_Tiling_for_Small_Object_Detection_CVPRW_2019_paper.pdf).

When tiling, each image is divided into a grid of tiles. Adjacent tiles overlap with each other in width and height dimensions. The tiles are cropped from the original as shown in the following image.

:::image type="content" source="./media/how-to-use-automl-small-object-detect/tiles-generation.png" alt-text="Diagram that shows an image being divided into a grid of overlapping tiles.":::

## Prerequisites

* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* This article assumes some familiarity with how to configure an [automated machine learning experiment for computer vision tasks](how-to-auto-train-image-models.md).

## Supported models

Small object detection using tiling is supported for all models supported by Automated ML for images for object detection task.

## Enable tiling during training

To enable tiling, you can set the `tile_grid_size` parameter to a value like '3x2'; where 3 is the number of tiles along the width dimension and 2 is the number of tiles along the height dimension. When this parameter is set to '3x2', each image is split into a grid of 3 x 2 tiles. Each tile overlaps with the adjacent tiles, so that any objects that fall on the tile border are included completely in one of the tiles. This overlap can be controlled by the `tile_overlap_ratio` parameter, which defaults to 25%.

When tiling is enabled, the entire image and the tiles generated from it are passed through the model. These images and tiles are resized according to the `min_size` and `max_size` parameters before feeding to the model. The computation time increases proportionally because of processing this extra data.

For example, when the `tile_grid_size` parameter is '3x2', the computation time would be approximately seven times higher than without tiling.

You can specify the value for `tile_grid_size` in your training parameters as a string.

# [CLI v2](#tab/CLI-v2)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

```yaml
training_parameters:
  tile_grid_size: '3x2'
```

# [Python SDK v2](#tab/SDK-v2)

```python
image_object_detection_job.set_training_parameters(
	tile_grid_size='3x2'
)
```

The value for `tile_grid_size` parameter depends on the image dimensions and size of objects within the image. For example, larger number of tiles would be helpful when there are smaller objects in the images.

To choose the optimal value for this parameter for your dataset, you can use hyperparameter search. To do so, you can specify a choice of values for this parameter in your hyperparameter space.

# [CLI v2](#tab/CLI-v2)
