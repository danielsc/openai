
# [Object detection with YOLO](#tab/object-detect-yolo)

```python
inputs = {'model_name': 'yolov5',  # enter the yolo model name
          'batch_size': 8,  # enter the batch size of your choice
          'height_onnx': 640,  # enter the height of input to ONNX model
          'width_onnx': 640,  # enter the width of input to ONNX model
          'job_name': job_name,
          'task_type': 'image-object-detection',
          'img_size': 640,  # image size for inference
          'model_size': 'small',  # size of the yolo model
          'box_score_thresh': 0.1,  # threshold to return proposals with a classification score > box_score_thresh
          'box_iou_thresh': 0.5
        }
```

# [Instance segmentation](#tab/instance-segmentation)

```python
inputs = {'model_name': 'maskrcnn_resnet50_fpn',  # enter the maskrcnn model name
         'batch_size': 8,  # enter the batch size of your choice
         'height_onnx': 600,  # enter the height of input to ONNX model
         'width_onnx': 800,  # enter the width of input to ONNX model
         'job_name': job_name,
         'task_type': 'image-instance-segmentation',
         'min_size': 600,  # minimum size of the image to be rescaled before feeding it to the backbone
         'max_size': 1333,  # maximum size of the image to be rescaled before feeding it to the backbone
         'box_score_thresh': 0.3,  # threshold to return proposals with a classification score > box_score_thresh
         'box_nms_thresh': 0.5,  # NMS threshold for the prediction head
         'box_detections_per_img': 100  # maximum number of detections per image, for all classes
         }
```


Download and keep the `ONNX_batch_model_generator_automl_for_images.py` file in the current directory to submit the script. Use the following command job to submit the script `ONNX_batch_model_generator_automl_for_images.py` available in the [azureml-examples GitHub repository](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs), to generate an ONNX model of a specific batch size. In the following code, the trained model environment is used to submit this script to generate and save the ONNX model to the outputs directory.

# [Multi-class image classification ](#tab/multi-class)
For multi-class image classification, the generated ONNX model for the best child-run supports batch scoring by default. Therefore, no model specific arguments are needed for this task type and you can skip to the [Load the labels and ONNX model files](#load-the-labels-and-onnx-model-files) section. 

# [Multi-label image classification ](#tab/multi-label)
For multi-label image classification, the generated ONNX model for the best child-run supports batch scoring by default. Therefore, no model specific arguments are needed for this task type and you can skip to the [Load the labels and ONNX model files](#load-the-labels-and-onnx-model-files) section. 

# [Object detection with Faster R-CNN or RetinaNet](#tab/object-detect-cnn)
```python
from azure.ai.ml import command

job = command(
    code="./onnx_generator_files",  # local path where the code is stored
    command="python ONNX_batch_model_generator_automl_for_images.py --model_name ${{inputs.model_name}} --batch_size ${{inputs.batch_size}} --height_onnx ${{inputs.height_onnx}} --width_onnx ${{inputs.width_onnx}} --job_name ${{inputs.job_name}} --task_type ${{inputs.task_type}} --min_size ${{inputs.min_size}} --max_size ${{inputs.max_size}} --box_score_thresh ${{inputs.box_score_thresh}} --box_nms_thresh ${{inputs.box_nms_thresh}} --box_detections_per_img ${{inputs.box_detections_per_img}}",
    inputs=inputs,
    environment=env,
    compute=compute_name,
    display_name="ONNX-batch-model-generation-rcnn",
    description="Use the PyTorch to generate ONNX batch scoring model.",
)
returned_job = ml_client.create_or_update(job)
ml_client.jobs.stream(returned_job.name)
```

# [Object detection with YOLO](#tab/object-detect-yolo)

```python
from azure.ai.ml import command

job = command(
    code="./onnx_generator_files",  # local path where the code is stored
    command="python ONNX_batch_model_generator_automl_for_images.py --model_name ${{inputs.model_name}} --batch_size ${{inputs.batch_size}} --height_onnx ${{inputs.height_onnx}} --width_onnx ${{inputs.width_onnx}} --job_name ${{inputs.job_name}} --task_type ${{inputs.task_type}} --img_size ${{inputs.img_size}} --model_size ${{inputs.model_size}} --box_score_thresh ${{inputs.box_score_thresh}} --box_iou_thresh ${{inputs.box_iou_thresh}}",
    inputs=inputs,
    environment=env,
    compute=compute_name,
    display_name="ONNX-batch-model-generation",
    description="Use the PyTorch to generate ONNX batch scoring model.",
)
returned_job = ml_client.create_or_update(job)
ml_client.jobs.stream(returned_job.name)
```
