This tutorial uses the NCsv3-series (with V100 GPUs) as this type of compute target leverages multiple GPUs to speed up training. Additionally, you can set up multiple nodes to take advantage of parallelism when tuning hyperparameters for your model.

The following code creates a GPU compute of size `Standard_NC24s_v3` with four nodes.

# [Azure CLI](#tab/cli)

[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]

Create a .yml file with the following configuration.

```yml
$schema: https://azuremlschemas.azureedge.net/latest/amlCompute.schema.json 
name: gpu-cluster
type: amlcompute
size: Standard_NC24s_v3
min_instances: 0
max_instances: 4
idle_time_before_scale_down: 120
```

To create the compute, you run the following CLI v2 command with the path to your .yml file, workspace name, resource group and subscription ID.

```azurecli
az ml compute create -f [PATH_TO_YML_FILE] --workspace-name [YOUR_AZURE_WORKSPACE] --resource-group [YOUR_AZURE_RESOURCE_GROUP] --subscription [YOUR_AZURE_SUBSCRIPTION]
```

The created compute can be provided using `compute` key in the `automl` task configuration yaml: 

```yaml
compute: azureml:gpu-cluster
```

# [Python SDK](#tab/python)

 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

```python
from azure.ai.ml.entities import AmlCompute
compute_name = "gpu-cluster"
cluster_basic = AmlCompute(
    name=compute_name,
    type="amlcompute",
    size="Standard_NC24s_v3",
    min_instances=0,
    max_instances=4,
    idle_time_before_scale_down=120,
)
ml_client.begin_create_or_update(cluster_basic)
```
This compute is used later while creating the task specific `automl` job.


## Experiment setup

You can use an Experiment to track your model training jobs.

# [Azure CLI](#tab/cli)
[!INCLUDE [cli v2](../../includes/machine-learning-cli-v2.md)]
Experiment name can be provided using `experiment_name` key as follows: 

```yaml
experiment_name: dpv2-cli-automl-image-object-detection-experiment
```

# [Python SDK](#tab/python)
 [!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

Experiment name is used later while creating the task specific `automl` job.
```python
exp_name = "dpv2-image-object-detection-experiment"
```

## Visualize input data

Once you have the input image data prepared in [JSONL](https://jsonlines.org/) (JSON Lines) format, you can visualize the ground truth bounding boxes for an image. To do so, be sure you have `matplotlib` installed.

```
%pip install --upgrade matplotlib
```
```python

%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image as pil_image
import numpy as np
import json
import os

def plot_ground_truth_boxes(image_file, ground_truth_boxes):
    # Display the image
    plt.figure()
    img_np = mpimg.imread(image_file)
    img = pil_image.fromarray(img_np.astype("uint8"), "RGB")
    img_w, img_h = img.size

    fig,ax = plt.subplots(figsize=(12, 16))
    ax.imshow(img_np)
    ax.axis("off")

    label_to_color_mapping = {}

    for gt in ground_truth_boxes:
        label = gt["label"]

        xmin, ymin, xmax, ymax =  gt["topX"], gt["topY"], gt["bottomX"], gt["bottomY"]
        topleft_x, topleft_y = img_w * xmin, img_h * ymin
        width, height = img_w * (xmax - xmin), img_h * (ymax - ymin)

        if label in label_to_color_mapping:
            color = label_to_color_mapping[label]
        else:
            # Generate a random color. If you want to use a specific color, you can use something like "red".
            color = np.random.rand(3)
            label_to_color_mapping[label] = color

        # Display bounding box
        rect = patches.Rectangle((topleft_x, topleft_y), width, height,
                                 linewidth=2, edgecolor=color, facecolor="none")
        ax.add_patch(rect)

        # Display label
        ax.text(topleft_x, topleft_y - 10, label, color=color, fontsize=20)

    plt.show()

def plot_ground_truth_boxes_jsonl(image_file, jsonl_file):
    image_base_name = os.path.basename(image_file)
    ground_truth_data_found = False
    with open(jsonl_file) as fp:
        for line in fp.readlines():
            line_json = json.loads(line)
            filename = line_json["image_url"]
            if image_base_name in filename:
                ground_truth_data_found = True
                plot_ground_truth_boxes(image_file, line_json["label"])
                break
    if not ground_truth_data_found:
        print("Unable to find ground truth information for image: {}".format(image_file))
```
