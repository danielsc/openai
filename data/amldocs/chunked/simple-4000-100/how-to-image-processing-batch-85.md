We need to create a scoring script that can read the images provided by the batch deployment and return the scores of the model. The following script:

> [!div class="checklist"]
> * Indicates an `init` function that load the model using `keras` module in `tensorflow`.
> * Indicates a `run` function that is executed for each mini-batch the batch deployment provides.
> * The `run` function read one image of the file at a time
> * The `run` method resizes the images to the expected sizes for the model.
> * The `run` method rescales the images to the range `[0,1]` domain, which is what the model expects.
> * It returns the classes and the probabilities associated with the predictions.

__imagenet_scorer.py__

```python
import os
import numpy as np
import pandas as pd
import tensorflow as tf
from os.path import basename
from PIL import Image
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

def run(mini_batch):
    results = []

    for image in mini_batch:
        data = Image.open(image).resize((input_width, input_height)) # Read and resize the image
        data = np.array(data)/255.0 # Normalize
        data_batch = tf.expand_dims(data, axis=0) # create a batch of size (1, 244, 244, 3)

        # perform inference
        pred = model.predict(data_batch)

        # Compute probabilities, classes and labels
        pred_prob = tf.math.reduce_max(tf.math.softmax(pred, axis=-1)).numpy()
        pred_class = tf.math.argmax(pred, axis=-1).numpy()

        results.append([basename(image), pred_class[0], pred_prob])

    return pd.DataFrame(results)
```

> [!TIP]
> Although images are provided in mini-batches by the deployment, this scoring script processes one image at a time. This is a common pattern as trying to load the entire batch and send it to the model at once may result in high-memory pressure on the batch executor (OOM exeptions). However, there are certain cases where doing so enables high throughput in the scoring task. This is the case for instance of batch deployments over a GPU hardware where we want to achieve high GPU utilization. See [High throughput deployments](#high-throughput-deployments) for an example of a scoring script that takes advantage of it.

> [!NOTE]
> If you are trying to deploy a generative model (one that generates files), please read how to author a scoring script as explained at [Deployment of models that produces multiple files](how-to-deploy-model-custom-output.md).

### Creating the deployment

One the scoring script is created, it's time to create a batch deployment for it. Follow the following steps to create it:

1. We need to indicate over which environment we are going to run the deployment. In our case, our model runs on `TensorFlow`. Azure Machine Learning already has an environment with the required software installed, so we can reutilize this environment. We are just going to add a couple of dependencies in a `conda.yml` file.

   # [Azure CLI](#tab/cli)
   
   No extra step is required for the Azure ML CLI. The environment definition will be included in the deployment file.
   
   # [Python](#tab/sdk)
   
   Let's get a reference to the environment:
   
   ```python
   environment = Environment(
       conda_file="./imagenet-classifier/environment/conda.yml",
       image="mcr.microsoft.com/azureml/tensorflow-2.4-ubuntu18.04-py37-cpu-inference:latest",
   )
   ```

1. Now, let create the deployment.

   > [!NOTE]
   > This example assumes you have an endpoint created with the name `imagenet-classifier-batch` and a compute cluster with name `cpu-cluster`. If you don't, please follow the steps in the doc [Use batch endpoints for batch scoring](how-to-use-batch-endpoint.md).
