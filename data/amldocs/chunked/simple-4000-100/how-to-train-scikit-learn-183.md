
For more information on creating and using environments, see [Create and use software environments in Azure Machine Learning](how-to-use-environments.md).

## Configure and submit your training job

In this section, we'll cover how to run a training job, using a training script that we've provided. To begin, you'll build the training job by configuring the command for running the training script. Then, you'll submit the training job to run in AzureML.


### Prepare the training script

In this article, we've provided the training script *train_iris.py*. In practice, you should be able to take any custom training script as is and run it with AzureML without having to modify your code.

> [!NOTE]
> The provided training script does the following:
> - shows how to log some metrics to your AzureML run;
> - downloads and extracts the training data using `iris = datasets.load_iris()`; and
> - trains a model, then saves and registers it.

To use and access your own data, see [how to read and write data in a job](how-to-read-write-data-v2.md) to make data available during training.

To use the training script, first create a directory where you will store the file.

```python
import os

src_dir = "./src"
os.makedirs(src_dir, exist_ok=True)
```

Next, create the script file in the source directory.

```python
%%writefile {src_dir}/train_iris.py
# Modified from https://www.geeksforgeeks.org/multiclass-classification-using-scikit-learn/

import argparse
import os

# importing necessary libraries
import numpy as np

from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

import joblib

import mlflow
import mlflow.sklearn

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    # Start Logging
    mlflow.start_run()

    # enable autologging
    mlflow.sklearn.autolog()

    args = parser.parse_args()
    mlflow.log_param('Kernel type', str(args.kernel))
    mlflow.log_metric('Penalty', float(args.penalty))

    # loading the iris dataset
    iris = datasets.load_iris()

    # X -> features, y -> label
    X = iris.data
    y = iris.target

    # dividing X, y into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # training a linear SVM classifier
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel=args.kernel, C=args.penalty)
    svm_model_linear = svm_model_linear.fit(X_train, y_train)
    svm_predictions = svm_model_linear.predict(X_test)

    # model accuracy for X_test
    accuracy = svm_model_linear.score(X_test, y_test)
    print('Accuracy of SVM classifier on test set: {:.2f}'.format(accuracy))
    mlflow.log_metric('Accuracy', float(accuracy))
    # creating a confusion matrix
    cm = confusion_matrix(y_test, svm_predictions)
    print(cm)

    registered_model_name="sklearn-iris-flower-classify-model"

    ##########################
    #<save and register model>
    ##########################
    # Registering the model to the workspace
    print("Registering the model via MLFlow")
    mlflow.sklearn.log_model(
        sk_model=svm_model_linear,
        registered_model_name=registered_model_name,
        artifact_path=registered_model_name
    )

    # # Saving the model to a file
    print("Saving the model via MLFlow")
    mlflow.sklearn.save_model(
        sk_model=svm_model_linear,
        path=os.path.join(registered_model_name, "trained_model"),
    )
    ###########################
    #</save and register model>
    ###########################
    mlflow.end_run()

if __name__ == '__main__':
    main()
```

### Build the training job

Now that you have all the assets required to run your job, it's time to build it using the AzureML Python SDK v2. For this, we'll be creating a `command`.
