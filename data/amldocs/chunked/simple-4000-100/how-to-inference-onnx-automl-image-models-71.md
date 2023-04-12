
```python
import mlflow
from mlflow.tracking.client import MlflowClient

# Obtain the tracking URL from MLClient
MLFLOW_TRACKING_URI = ml_client.workspaces.get(
    name=ml_client.workspace_name
).mlflow_tracking_uri

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Specify the job name
job_name = ''

# Get the parent run
mlflow_parent_run = mlflow_client.get_run(job_name)
best_child_run_id = mlflow_parent_run.data.tags['automl_best_child_run_id']
# get the best child run
best_run = mlflow_client.get_run(best_child_run_id)
```

Download the *labels.json* file, which contains all the classes and labels in the training dataset.

```python
local_dir = './automl_models'
if not os.path.exists(local_dir):
    os.mkdir(local_dir)

labels_file = mlflow_client.download_artifacts(
    best_run.info.run_id, 'train_artifacts/labels.json', local_dir
)
```

Download the *model.onnx* file.

```python
onnx_model_path = mlflow_client.download_artifacts(
    best_run.info.run_id, 'train_artifacts/model.onnx', local_dir
)
```
In case of batch inferencing for Object Detection and Instance Segmentation using ONNX models, refer to the section on [model generation for batch scoring](#model-generation-for-batch-scoring).

### Model generation for batch scoring

By default, AutoML for Images supports batch scoring for classification. But object detection and instance segmentation ONNX models don't support batch inferencing. In case of batch inference for object detection and instance segmentation, use the following procedure to generate an ONNX model for the required batch size. Models generated for a specific batch size don't work for other batch sizes.

Download the conda environment file and create an environment object to be used with command job.

```python
#  Download conda file and define the environment

conda_file = mlflow_client.download_artifacts(
    best_run.info.run_id, "outputs/conda_env_v_1_0_0.yml", local_dir

from azure.ai.ml.entities import Environment
env = Environment(
    name="automl-images-env-onnx",
    description="environment for automl images ONNX batch model generation",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.1-cudnn8-ubuntu18.04",
    conda_file=conda_file,
)
```

Use the following model specific arguments to submit the script. For more details on arguments, refer to [model specific hyperparameters](how-to-auto-train-image-models.md#configure-experiments) and for supported object detection model names refer to the [supported model architecture section](how-to-auto-train-image-models.md#supported-model-architectures).

To get the argument values needed to create the batch scoring model, refer to the scoring scripts generated under the outputs folder of the AutoML training runs. Use the hyperparameter values available in the model settings variable inside the scoring file for the best child run.

# [Multi-class image classification ](#tab/multi-class)
For multi-class image classification, the generated ONNX model for the best child-run supports batch scoring by default. Therefore, no model specific arguments are needed for this task type and you can skip to the [Load the labels and ONNX model files](#load-the-labels-and-onnx-model-files) section. 

# [Multi-label image classification ](#tab/multi-label)
For multi-label image classification, the generated ONNX model for the best child-run supports batch scoring by default. Therefore, no model specific arguments are needed for this task type and you can skip to the [Load the labels and ONNX model files](#load-the-labels-and-onnx-model-files) section. 

# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)
```python
inputs = {'model_name': 'fasterrcnn_resnet34_fpn',  # enter the faster rcnn or retinanet model name
         'batch_size': 8,  # enter the batch size of your choice
         'height_onnx': 600,  # enter the height of input to ONNX model
         'width_onnx': 800,  # enter the width of input to ONNX model
         'job_name': job_name,
         'task_type': 'image-object-detection',
         'min_size': 600,  # minimum size of the image to be rescaled before feeding it to the backbone
         'max_size': 1333,  # maximum size of the image to be rescaled before feeding it to the backbone
         'box_score_thresh': 0.3,  # threshold to return proposals with a classification score > box_score_thresh
         'box_nms_thresh': 0.5,  # NMS threshold for the prediction head
         'box_detections_per_img': 100   # maximum number of detections per image, for all classes
         }
```
