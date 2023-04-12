
    | file                        | class | probabilities | label        |
    |-----------------------------|-------|---------------| -------------|
    | n02088094_Afghan_hound.JPEG | 161   | 0.994745	    | Afghan hound |
    | n02088238_basset            | 162	| 0.999397      | basset       |
    | n02088364_beagle.JPEG       | 165   | 0.366914      | bluetick     |
    | n02088466_bloodhound.JPEG   | 164   | 0.926464	    | bloodhound   |
    | ...                         | ...   | ...           | ...          |
    

## High throughput deployments

As mentioned before, the deployment we just created processes one image a time, even when the batch deployment is providing a batch of them. In most cases this is the best approach as it simplifies how the models execute and avoids any possible out-of-memory problems. However, in certain others we may want to saturate as much as possible the utilization of the underlying hardware. This is the case GPUs for instance.

On those cases, we may want to perform inference on the entire batch of data. That implies loading the entire set of images to memory and sending them directly to the model. The following example uses `TensorFlow` to read batch of images and score them all at once. It also uses `TensorFlow` ops to do any data preprocessing so the entire pipeline will happen on the same device being used (CPU/GPU).

> [!WARNING]
> Some models have a non-linear relationship with the size of the inputs in terms of the memory consumption. Batch again (as done in this example) or decrease the size of the batches created by the batch deployment to avoid out-of-memory exceptions.

__imagenet_scorer_batch.py__

```python
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model

def init():
    global model
    global input_width
    global input_height

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")

    # load the model
    model = load_model(model_path)
    input_width = 244
    input_height = 244

def decode_img(file_path):
    file = tf.io.read_file(file_path)
    img = tf.io.decode_jpeg(file, channels=3)
    img = tf.image.resize(img, [input_width, input_height])
    return img/255.

def run(mini_batch):
    images_ds = tf.data.Dataset.from_tensor_slices(mini_batch)
    images_ds = images_ds.map(decode_img).batch(64)

    # perform inference
    pred = model.predict(images_ds)

    # Compute probabilities, classes and labels
    pred_prob = tf.math.reduce_max(tf.math.softmax(pred, axis=-1)).numpy()
    pred_class = tf.math.argmax(pred, axis=-1).numpy()

    return pd.DataFrame([mini_batch, pred_prob, pred_class], columns=['file', 'probability', 'class'])
```

Remarks:
* Notice that this script is constructing a tensor dataset from the mini-batch sent by the batch deployment. This dataset is preprocessed to obtain the expected tensors for the model using the `map` operation with the function `decode_img`.
* The dataset is batched again (16) send the data to the model. Use this parameter to control how much information you can load into memory and send to the model at once. If running on a GPU, you will need to carefully tune this parameter to achieve the maximum utilization of the GPU just before getting an OOM exception.
* Once predictions are computed, the tensors are converted to `numpy.ndarray`.


## Considerations for MLflow models processing images

MLflow models in Batch Endpoints support reading images as input data. Remember that MLflow models don't require a scoring script. Have the following considerations when using them:

> [!div class="checklist"]
> * Image files supported includes: `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp` and `.gif`.
> * MLflow models should expect to recieve a `np.ndarray` as input that will match the dimensions of the input image. In order to support multiple image sizes on each batch, the batch executor will invoke the MLflow model once per image file.
