
# [Instance segmentation](#tab/instance-segmentation)

```python
from azure.ai.ml import command

job = command(
    code="./onnx_generator_files",  # local path where the code is stored
    command="python ONNX_batch_model_generator_automl_for_images.py --model_name ${{inputs.model_name}} --batch_size ${{inputs.batch_size}} --height_onnx ${{inputs.height_onnx}} --width_onnx ${{inputs.width_onnx}} --job_name ${{inputs.job_name}} --task_type ${{inputs.task_type}} --min_size ${{inputs.min_size}} --max_size ${{inputs.max_size}} --box_score_thresh ${{inputs.box_score_thresh}} --box_nms_thresh ${{inputs.box_nms_thresh}} --box_detections_per_img ${{inputs.box_detections_per_img}}",
    inputs=inputs,
    environment=env,
    compute=compute_name,
    display_name="ONNX-batch-model-generation-maskrcnn",
    description="Use the PyTorch to generate ONNX batch scoring model.",
)
returned_job = ml_client.create_or_update(job)
ml_client.jobs.stream(returned_job.name)
```



Once the batch model is generated, either download it from **Outputs+logs** > **outputs** manually through UI, or use the following method:
```python
batch_size = 8  # use the batch size used to generate the model
returned_job_run = mlflow_client.get_run(returned_job.name)

# Download run's artifacts/outputs
onnx_model_path = mlflow_client.download_artifacts(
    best_run.info.run_id, 'outputs/model_'+str(batch_size)+'.onnx', local_dir
)
```

After the model downloading step, you use the ONNX Runtime Python package to perform inferencing by using the *model.onnx* file. For demonstration purposes, this article uses the datasets from [How to prepare image datasets](how-to-prepare-datasets-for-automl-images.md) for each vision task. 

We've trained the models for all vision tasks with their respective datasets to demonstrate ONNX model inference.
 
## Load the labels and ONNX model files

The following code snippet loads *labels.json*, where class names are ordered. That is, if the ONNX model predicts a label ID as 2, then it corresponds to the label name given at the third index in the *labels.json* file.

```python
import json
import onnxruntime

labels_file = "automl_models/labels.json"
with open(labels_file) as f:
    classes = json.load(f)
print(classes)
try:
    session = onnxruntime.InferenceSession(onnx_model_path)
    print("ONNX model loaded...")
except Exception as e: 
    print("Error loading ONNX file: ", str(e))
```

## Get expected input and output details for an ONNX model

When you have the model, it's important to know some model-specific and task-specific details. These details include the number of inputs and number of outputs, expected input shape or format for preprocessing the image, and output shape so you know the model-specific or task-specific outputs.

```python
sess_input = session.get_inputs()
sess_output = session.get_outputs()
print(f"No. of inputs : {len(sess_input)}, No. of outputs : {len(sess_output)}")

for idx, input_ in enumerate(range(len(sess_input))):
    input_name = sess_input[input_].name
    input_shape = sess_input[input_].shape
    input_type = sess_input[input_].type
    print(f"{idx} Input name : { input_name }, Input shape : {input_shape}, \
    Input type  : {input_type}")  

for idx, output in enumerate(range(len(sess_output))):
    output_name = sess_output[output].name
    output_shape = sess_output[output].shape
    output_type = sess_output[output].type
    print(f" {idx} Output name : {output_name}, Output shape : {output_shape}, \
    Output type  : {output_type}") 
``` 

### Expected input and output formats for the ONNX model

Every ONNX model has a predefined set of input and output formats.

# [Multi-class image classification](#tab/multi-class)

This example applies the model trained on the [fridgeObjects](https://cvbp-secondary.z19.web.core.windows.net/datasets/image_classification/fridgeObjects.zip) dataset with 134 images and 4 classes/labels to explain ONNX model inference. For more information on training an image classification task, see the [multi-class image classification notebook](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-classification-multiclass-task-fridge-items).
