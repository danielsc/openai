
1. In the graph of the job, select the `batchscoring` step.
1. Select the __Outputs + logs__ tab and then select **Show data outputs**.
1. From __Data outputs__, select the icon to open __Storage Explorer__.

    :::image type="content" source="media/how-to-use-batch-endpoint/view-data-outputs.png" alt-text="Studio screenshot showing view data outputs location." lightbox="media/how-to-use-batch-endpoint/view-data-outputs.png":::

    The scoring results in Storage Explorer are similar to the following sample page:

    :::image type="content" source="media/how-to-use-batch-endpoint/scoring-view.png" alt-text="Screenshot of the scoring output." lightbox="media/how-to-use-batch-endpoint/scoring-view.png":::

## Adding deployments to an endpoint

Once you have a batch endpoint with a deployment, you can continue to refine your model and add new deployments. Batch endpoints will continue serving the default deployment while you develop and deploy new models under the same endpoint. Deployments can't affect one to another.

In this example, you'll learn how to add a second deployment __that solves the same MNIST problem but using a model built with Keras and TensorFlow__.

### Adding a second deployment

1. Create an environment where your batch deployment will run. Include in the environment any dependency your code requires for running. You'll also need to add the library `azureml-core` as it is required for batch deployments to work. The following environment definition has the required libraries to run a model with TensorFlow.

    # [Azure CLI](#tab/azure-cli)
   
    *No extra step is required for the Azure ML CLI. The environment definition will be included in the deployment file as an anonymous environment.*
   
    # [Python](#tab/python)
   
    Let's get a reference to the environment:
   
    ```python
    env = Environment(
        conda_file="./mnist-keras/environment/conda.yml",
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04:latest",
    )
    ```

    # [Studio](#tab/azure-studio)
    
    1. Navigate to the __Environments__ tab on the side menu.
    1. Select the tab __Custom environments__ > __Create__.
    1. Enter the name of the environment, in this case `keras-batch-env`.
    1. On __Select environment type__ select __Use existing docker image with conda__.
    1. On __Container registry image path__, enter `mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04`.
    1. On __Customize__ section copy the content of the file `./mnist-keras/environment/conda.yml` included in the repository into the portal.
    1. Select __Next__ and then on __Create__.
    1. The environment is ready to be used.
    
    
    The conda file used looks as follows:
    
    __mnist-keras/environment/conda.yml__
    
```yaml
name: tensorflow-env
channels:
  - conda-forge
dependencies:
  - python=3.7
  - pip
  - pip:
    - pandas
    - tensorflow
    - pillow
    - azureml-core
    - azureml-dataset-runtime[fuse]

```
    
1. Create a scoring script for the model:
   
   __mnist-keras/code/batch_driver.py__
   
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

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")

    # load the model
    model = load_model(model_path)


def run(mini_batch):
    results = []

    for image in mini_batch:
        data = Image.open(image)
        data = np.array(data)
        data_batch = tf.expand_dims(data, axis=0)

        # perform inference
        pred = model.predict(data_batch)

        # Compute probabilities, classes and labels
        pred_prob = tf.math.reduce_max(tf.math.softmax(pred, axis=-1)).numpy()
        pred_class = tf.math.argmax(pred, axis=-1).numpy()

        results.append([basename(image), pred_class[0], pred_prob])

    return pd.DataFrame(results)

```
