
    # [Python](#tab/python)
    
    ```python
    ml_client.batch_endpoints.begin_create_or_update(endpoint)
    ```
    # [Studio](#tab/azure-studio)
    
    *You'll create the endpoint in the same step you are creating the deployment later.*

## Create a scoring script

Batch deployments require a scoring script that indicates how the given model should be executed and how input data must be processed.

> [!NOTE]
> For MLflow models, Azure Machine Learning automatically generates the scoring script, so you're not required to provide one. If your model is an MLflow model, you can skip this step. For more information about how batch endpoints work with MLflow models, see the dedicated tutorial [Using MLflow models in batch deployments](how-to-mlflow-batch.md).

> [!WARNING]
> If you're deploying an Automated ML model under a batch endpoint, notice that the scoring script that Automated ML provides only works for online endpoints and is not designed for batch execution. Please see [Author scoring scripts for batch deployments](how-to-batch-scoring-script.md) to learn how to create one depending on what your model does.

In this case, we're deploying a model that reads image files representing digits and outputs the corresponding digit. The scoring script is as follows:

__mnist/code/batch_driver.py__

```python
# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import os
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
from azureml.core import Model


def init():
    global g_tf_sess

    # AZUREML_MODEL_DIR is an environment variable created during deployment
    # It is the path to the model folder (./azureml-models)
    # Please provide your model's folder name if there's one
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model")

    # contruct graph to execute
    tf.reset_default_graph()
    saver = tf.train.import_meta_graph(os.path.join(model_path, "mnist-tf.model.meta"))
    g_tf_sess = tf.Session(config=tf.ConfigProto(device_count={"GPU": 0}))
    saver.restore(g_tf_sess, os.path.join(model_path, "mnist-tf.model"))


def run(mini_batch):
    print(f"run method start: {__file__}, run({mini_batch})")
    resultList = []
    in_tensor = g_tf_sess.graph.get_tensor_by_name("network/X:0")
    output = g_tf_sess.graph.get_tensor_by_name("network/output/MatMul:0")

    for image in mini_batch:
        # prepare each image
        data = Image.open(image)
        np_im = np.array(data).reshape((1, 784))
        # perform inference
        inference_result = output.eval(feed_dict={in_tensor: np_im}, session=g_tf_sess)
        # find best probability, and add to result list
        best_result = np.argmax(inference_result)
        resultList.append([os.path.basename(image), best_result])

    return pd.DataFrame(resultList)

```

## Create a batch deployment

A deployment is a set of resources required for hosting the model that does the actual inferencing. To create a batch deployment, you need all the following items:

* A registered model in the workspace.
* The code to score the model.
* The environment in which the model runs.
* The pre-created compute and resource settings.

1. Create an environment where your batch deployment will run. Such environment needs to include the packages `azureml-core` and `azureml-dataset-runtime[fuse]`, which are required by batch endpoints, plus any dependency your code requires for running. In this case, the dependencies have been captured in a `conda.yml`:
    
    __mnist/environment/conda.yml__
        
```yaml
name: mnist-env
channels:
  - conda-forge
dependencies:
  - python=3.6.2
  - pip<22.0
  - pip:
    - tensorflow==1.15.2
    - pillow
    - pandas
    - azureml-core
    - azureml-dataset-runtime[fuse]

```
    
    > [!IMPORTANT]
    > The packages `azureml-core` and `azureml-dataset-runtime[fuse]` are required by batch deployments and should be included in the environment dependencies.
    
    Indicate the environment as follows:
