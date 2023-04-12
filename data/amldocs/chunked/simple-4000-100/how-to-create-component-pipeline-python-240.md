* The `keras_train_component` function defines one input `input_data` where training data comes from, one input `epochs` specifying epochs during training, and one output `output_model` where outputs the model file. The default value of `epochs` is 10. The execution logic of this component is from `train()` function in `train.py` above.

The train-model component has a slightly more complex configuration than the prep-data component. The `conda.yaml` is like following:

```yaml
name: imagekeras_train_conda_env
channels:
  - defaults
dependencies:
  - python=3.7.11
  - pip=20.0
  - pip:
    - mldesigner==0.1.0b4
    - azureml-mlflow==1.42.0
    - tensorflow==2.7.0
    - numpy==1.21.4
    - scikit-learn==1.0.1
    - pandas==1.3.4
    - matplotlib==3.2.2
    - protobuf==3.20.0

```

Now, you've prepared all source files for the `Train Image Classification Keras` component.

### Create the score-model component

In this section, other than the previous components, you'll create a component to score the trained model via Yaml specification and script.

If you're following along with the example in the [AzureML Examples repo](https://github.com/Azure/azureml-examples/tree/main/sdk/python/jobs/pipelines/2e_image_classification_keras_minist_convnet), the source files are already available in `score/` folder. This folder contains three files to construct the component:

- `score.py`: contains the source code of the component.
- `score.yaml`: defines the interface and other details of the component.
- `conda.yaml`: defines the run-time environment of the component.

#### Get a script containing execution logic

The `score.py` file contains a normal Python function, which performs the training model logic.

```python
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.utils import to_categorical
from keras.callbacks import Callback
from keras.models import load_model

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import mlflow


def get_file(f):

    f = Path(f)
    if f.is_file():
        return f
    else:
        files = list(f.iterdir())
        if len(files) == 1:
            return files[0]
        else:
            raise Exception("********This path contains more than one file*******")


def parse_args():
    # setup argparse
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument(
        "--input_data", type=str, help="path containing data for scoring"
    )
    parser.add_argument(
        "--input_model", type=str, default="./", help="input path for model"
    )

    parser.add_argument(
        "--output_result", type=str, default="./", help="output path for model"
    )

    # parse args
    args = parser.parse_args()

    # return args
    return args


def score(input_data, input_model, output_result):

    test_file = get_file(input_data)
    data_test = pd.read_csv(test_file, header=None)

    img_rows, img_cols = 28, 28
    input_shape = (img_rows, img_cols, 1)

    # Read test data
    X_test = np.array(data_test.iloc[:, 1:])
    y_test = to_categorical(np.array(data_test.iloc[:, 0]))
    X_test = (
        X_test.reshape(X_test.shape[0], img_rows, img_cols, 1).astype("float32") / 255
    )

    # Load model
    files = [f for f in os.listdir(input_model) if f.endswith(".h5")]
    model = load_model(input_model + "/" + files[0])

    # Log metrics of the model
    eval = model.evaluate(X_test, y_test, verbose=0)

    mlflow.log_metric("Final test loss", eval[0])
    print("Test loss:", eval[0])

    mlflow.log_metric("Final test accuracy", eval[1])
    print("Test accuracy:", eval[1])

    # Score model using test data
    y_predict = model.predict(X_test)
    y_result = np.argmax(y_predict, axis=1)

    # Output result
    np.savetxt(output_result + "/predict_result.csv", y_result, delimiter=",")


def main(args):
    score(args.input_data, args.input_model, args.output_result)


# run script
if __name__ == "__main__":
    # parse args
    args = parse_args()

    # call main function
    main(args)

```
