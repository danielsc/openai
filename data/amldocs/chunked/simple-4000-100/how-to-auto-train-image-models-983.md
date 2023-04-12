These attributions give more control to the users to generate custom visualizations or to scrutinize pixel level attribution scores.
Following code snippet describes a way to generate custom visualizations using attribution matrix. For more information on the schema of attributions for multi-class classification and multi-label classification, see the [schema docs](reference-automl-images-schema.md#data-format-for-online-scoring-and-explainability-xai).

Use the exact `valid_resize_size` and `valid_crop_size` values of the selected model to generate the explanations (default values are 256 and 224 respectively). Following code uses [Captum](https://captum.ai/) visualization functionality to generate custom visualizations. Users can utilize any other library to generate visualizations. For more details, please refer to the [captum visualization utilities](https://captum.ai/api/utilities.html#visualization).

```python
import colorcet as cc
import numpy as np
from captum.attr import visualization as viz
from PIL import Image
from torchvision import transforms

def get_common_valid_transforms(resize_to=256, crop_size=224):

    return transforms.Compose([
        transforms.Resize(resize_to),
        transforms.CenterCrop(crop_size)
    ])

# Load the image
valid_resize_size = 256
valid_crop_size = 224
sample_image = "./test_image.jpg"
image = Image.open(sample_image)
# Perform common validation transforms to get the image used to generate attributions
common_transforms = get_common_valid_transforms(resize_to=valid_resize_size,
                                                crop_size=valid_crop_size)
input_tensor = common_transforms(image)

# Convert output attributions to numpy array

# For Multi-class classification:
# Selecting attribution matrix for first input image
# attributions = np.array(predictions[0]["attributions"])

# For  Multi-label classification:
# Selecting first attribution matrix against one of the classes for first input image
attributions = np.array(predictions[0]["attributions"][0])

# visualize results
viz.visualize_image_attr_multiple(np.transpose(attributions, (1, 2, 0)),
                                  np.array(input_tensor),
                                  ["original_image", "blended_heat_map"],
                                  ["all", "absolute_value"],
                                  show_colorbar=True,
                                  cmap=cc.cm.bgyw,
                                  titles=["original_image", "heatmap"],
                                  fig_size=(12, 12))
```

## Large datasets

If you're using AutoML to train on large datasets, there are some experimental settings that may be useful.

> [!IMPORTANT]
> These settings are currently in public preview. They are provided without a service-level agreement. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

### Multi-GPU and multi-node training

By default, each model trains on a single VM. If training a model is taking too much time, using VMs that contain multiple GPUs may help. The time to train a model on large datasets should decrease in roughly linear proportion to the number of GPUs used. (For instance, a model should train roughly twice as fast on a VM with two GPUs as on a VM with one GPU.) If the time to train a model is still high on a VM with multiple GPUs, you can increase the number of VMs used to train each model. Similar to multi-GPU training, the time to train a model on large datasets should also decrease in roughly linear proportion to the number of VMs used. When training a model across multiple VMs, be sure to use a compute SKU that supports [InfiniBand](how-to-train-distributed-gpu.md#accelerating-distributed-gpu-training-with-infiniband) for best results. You can configure the number of VMs used to train a single model by setting the `node_count_per_trial` property of the AutoML job.
