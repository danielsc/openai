
# [Object detection with YOLO](#tab/object-detect-yolo)

For object detection with the YOLO architecture, follow the same preprocessing steps as image classification, except for image cropping. You can resize the image with height `600` and width `800`, and get the expected input height and width with the following code.

```python
batch, channel, height_onnx, width_onnx = session.get_inputs()[0].shape
batch, channel, height_onnx, width_onnx
```

For preprocessing required for YOLO, refer to [yolo_onnx_preprocessing_utils.py](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/automl-standalone-jobs/automl-image-object-detection-task-fridge-items).

```python
import glob
import numpy as np
from yolo_onnx_preprocessing_utils import preprocess

# use height and width based on the generated model
test_images_path = "automl_models_od_yolo/test_images_dir/*" # replace with path to images
image_files = glob.glob(test_images_path)
img_processed_list = []
pad_list = []
for i in range(batch_size):
    img_processed, pad = preprocess(image_files[i])
    img_processed_list.append(img_processed)
    pad_list.append(pad)
    
if len(img_processed_list) > 1:
    img_data = np.concatenate(img_processed_list)
elif len(img_processed_list) == 1:
    img_data = img_processed_list[0]
else:
    img_data = None

assert batch_size == img_data.shape[0]
```

# [Instance segmentation](#tab/instance-segmentation)
>[!IMPORTANT]
> Only Mask R-CNN is supported for instance segmentation tasks. The preprocessing steps are based on Mask R-CNN only.

Perform the following preprocessing steps for the ONNX model inference:

1. Convert the image to RGB.
2. Resize the image. 
3. Change `HxWxC` to `CxHxW`.
4. Convert to float type.
5. Normalize with ImageNet's `mean` = `[0.485, 0.456, 0.406]` and `std` = `[0.229, 0.224, 0.225]`.

For `resize_height` and `resize_width`, you can also use the values that you used during training, bounded by the `min_size` and `max_size` [hyperparameters](reference-automl-images-hyperparameters.md) for Mask R-CNN.

```python
import glob
import numpy as np
from PIL import Image

def preprocess(image, resize_height, resize_width):
    """Perform pre-processing on raw input image
    
    :param image: raw input image
    :type image: PIL image
    :param resize_height: resize height of an input image
    :type resize_height: Int
    :param resize_width: resize width of an input image
    :type resize_width: Int
    :return: pre-processed image in numpy format
    :rtype: ndarray of shape 1xCxHxW
    """

    image = image.convert('RGB')
    image = image.resize((resize_width, resize_height))
    np_image = np.array(image)
    # HWC -> CHW
    np_image = np_image.transpose(2, 0, 1)  # CxHxW
    # normalize the image
    mean_vec = np.array([0.485, 0.456, 0.406])
    std_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(np_image.shape).astype('float32')
    for i in range(np_image.shape[0]):
        norm_img_data[i,:,:] = (np_image[i,:,:]/255 - mean_vec[i])/std_vec[i]
    np_image = np.expand_dims(norm_img_data, axis=0)  # 1xCxHxW
    return np_image

# following code loads only batch_size number of images for demonstrating ONNX inference
# make sure that the data directory has at least batch_size number of images
# use height and width based on the trained model
# use height and width based on the generated model
test_images_path = "automl_models_is/test_images_dir/*" # replace with path to images
image_files = glob.glob(test_images_path)
img_processed_list = []
for i in range(batch_size):
    img = Image.open(image_files[i])
    img_processed_list.append(preprocess(img, height_onnx, width_onnx))
    
if len(img_processed_list) > 1:
    img_data = np.concatenate(img_processed_list)
elif len(img_processed_list) == 1:
    img_data = img_processed_list[0]
else:
    img_data = None

assert batch_size == img_data.shape[0]
```


## Inference with ONNX Runtime

Inferencing with ONNX Runtime differs for each computer vision task.
