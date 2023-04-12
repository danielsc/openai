
### With PyTorch

```python
import glob
import torch
import numpy as np
from PIL import Image
from torchvision import transforms

def _make_3d_tensor(x) -> torch.Tensor:
    """This function is for images that have less channels.

    :param x: input tensor
    :type x: torch.Tensor
    :return: return a tensor with the correct number of channels
    :rtype: torch.Tensor
    """
    return x if x.shape[0] == 3 else x.expand((3, x.shape[1], x.shape[2]))

def preprocess(image, resize_size, crop_size_onnx):
    transform = transforms.Compose([
        transforms.Resize(resize_size),
        transforms.CenterCrop(crop_size_onnx),
        transforms.ToTensor(),
        transforms.Lambda(_make_3d_tensor),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
    
    img_data = transform(image)
    img_data = img_data.numpy()
    img_data = np.expand_dims(img_data, axis=0)
    return img_data

# following code loads only batch_size number of images for demonstrating ONNX inference
# make sure that the data directory has at least batch_size number of images

test_images_path = "automl_models_multi_cls/test_images_dir/*"  # replace with path to images
# Select batch size needed
batch_size = 8
# you can modify resize_size based on your trained model
resize_size = 256
# height and width will be the same for classification
crop_size_onnx = height_onnx_crop_size 

image_files = glob.glob(test_images_path)
img_processed_list = []
for i in range(batch_size):
    img = Image.open(image_files[i])
    img_processed_list.append(preprocess(img, resize_size, crop_size_onnx))
    
if len(img_processed_list) > 1:
    img_data = np.concatenate(img_processed_list)
elif len(img_processed_list) == 1:
    img_data = img_processed_list[0]
else:
    img_data = None

assert batch_size == img_data.shape[0]
```

# [Multi-label image classification](#tab/multi-label)

Perform the following preprocessing steps for the ONNX model inference. These steps are the same for multi-class image classification.

1. Convert the image to RGB.
2. Resize the image to `valid_resize_size` and `valid_resize_size` values that correspond to the values used in the transformation of the validation dataset during training. The default value for `valid_resize_size` is 256.
3. Center crop the image to `height_onnx_crop_size` and `width_onnx_crop_size`. This corresponds to `valid_crop_size` with the default value of 224.
4. Change `HxWxC` to `CxHxW`.
5. Convert to float type.
6. Normalize with ImageNet's `mean` = `[0.485, 0.456, 0.406]` and `std` = `[0.229, 0.224, 0.225]`.

If you chose different values for the [hyperparameters](reference-automl-images-hyperparameters.md) `valid_resize_size` and `valid_crop_size` during training, then those values should be used.

Get the input shape needed for the ONNX model.

```python
batch, channel, height_onnx_crop_size, width_onnx_crop_size = session.get_inputs()[0].shape
batch, channel, height_onnx_crop_size, width_onnx_crop_size
```

### Without PyTorch

```python
import glob
import numpy as np
from PIL import Image

def preprocess(image, resize_size, crop_size_onnx):
    """Perform pre-processing on raw input image
    
    :param image: raw input image
    :type image: PIL image
    :param resize_size: value to resize the image
    :type image: Int
    :param crop_size_onnx: expected height of an input image in onnx model
    :type crop_size_onnx: Int
    :return: pre-processed image in numpy format
    :rtype: ndarray 1xCxHxW
    """

    image = image.convert('RGB')
    # resize
    image = image.resize((resize_size, resize_size))
    # center  crop
    left = (resize_size - crop_size_onnx)/2
    top = (resize_size - crop_size_onnx)/2
    right = (resize_size + crop_size_onnx)/2
    bottom = (resize_size + crop_size_onnx)/2
    image = image.crop((left, top, right, bottom))

    np_image = np.array(image)
    # HWC -> CHW
    np_image = np_image.transpose(2, 0, 1) # CxHxW

    # normalize the image
    mean_vec = np.array([0.485, 0.456, 0.406])
    std_vec = np.array([0.229, 0.224, 0.225])
    norm_img_data = np.zeros(np_image.shape).astype('float32')
    for i in range(np_image.shape[0]):
        norm_img_data[i,:,:] = (np_image[i,:,:] / 255 - mean_vec[i]) / std_vec[i]    
    np_image = np.expand_dims(norm_img_data, axis=0) # 1xCxHxW
    return np_image

# following code loads only batch_size number of images for demonstrating ONNX inference
# make sure that the data directory has at least batch_size number of images

test_images_path = "automl_models_multi_label/test_images_dir/*" # replace with path to images
# Select batch size needed
batch_size = 8
# you can modify resize_size based on your trained model
resize_size = 256
# height and width will be the same for classification
crop_size_onnx = height_onnx_crop_size 

image_files = glob.glob(test_images_path)
img_processed_list = []
for i in range(batch_size):
    img = Image.open(image_files[i])
    img_processed_list.append(preprocess(img, resize_size, crop_size_onnx))
    
if len(img_processed_list) > 1:
    img_data = np.concatenate(img_processed_list)
elif len(img_processed_list) == 1:
    img_data = img_processed_list[0]
else:
    img_data = None

assert batch_size == img_data.shape[0]

```
