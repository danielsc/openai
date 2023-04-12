
# Convert custom ML models to MLflow formatted models

In this article, learn how to convert your custom ML model into MLflow format. [MLflow](https://www.mlflow.org) is an open-source library for managing the lifecycle of your machine learning experiments. In some cases, you might use a machine learning framework without its built-in MLflow model flavor support. Due to this lack of built-in MLflow model flavor, you cannot log or register the model with MLflow model fluent APIs. To resolve this, you can convert your model to an MLflow format where you can leverage the following benefits of Azure Machine Learning and MLflow models.

With Azure Machine Learning, MLflow models get the added benefits of, 

* No code deployment
* Portability as an open source standard format
* Ability to deploy both locally and on cloud

MLflow provides support for a variety of [machine learning frameworks](https://mlflow.org/docs/latest/models.html#built-in-model-flavors) (scikit-learn, Keras, Pytorch, and more); however, it might not cover every use case. For example, you may want to create an MLflow model with a framework that MLflow does not natively support or you may want to change the way your model does pre-processing or post-processing when running jobs. To know more about MLflow models read [From artifacts to models in MLflow](concept-mlflow-models.md).

If you didn't train your model with MLFlow and want to use Azure Machine Learning's MLflow no-code deployment offering, you need to convert your custom model to MLFLow. Learn more about [custom Python models and MLflow](https://mlflow.org/docs/latest/models.html#custom-python-models).

## Prerequisites
 
Only the mlflow package installed is needed to convert your custom models to an MLflow format. 

## Create a Python wrapper for your model

Before you can convert your model to an MLflow supported format, you need to first create a Python wrapper for your model.
The following code demonstrates how to create a Python wrapper for an `sklearn` model.

```python

# Load training and test datasets
from sys import version_info
import sklearn
import mlflow.pyfunc


PYTHON_VERSION = "{major}.{minor}.{micro}".format(major=version_info.major,
                                                  minor=version_info.minor,
                                                  micro=version_info.micro)

# Train and save an SKLearn model
sklearn_model_path = "model.pkl"

artifacts = {
    "sklearn_model": sklearn_model_path
}

# create wrapper
class SKLearnWrapper(mlflow.pyfunc.PythonModel):

    def load_context(self, context):
        import pickle
        self.sklearn_model = pickle.load(open(context.artifacts["sklearn_model"], 'rb'))
    
    def predict(self, model, data):
        return self.sklearn_model.predict(data)
```

## Create a Conda environment 

Next, you need to create Conda environment for the new MLflow Model that contains all necessary dependencies. If not indicated, the environment is inferred from the current installation. If not, it can be specified.

```python

import cloudpickle
conda_env = {
    'channels': ['defaults'],
    'dependencies': [
      'python={}'.format(PYTHON_VERSION),
      'pip',
      {
        'pip': [
          'mlflow',
          'scikit-learn=={}'.format(sklearn.__version__),
          'cloudpickle=={}'.format(cloudpickle.__version__),
        ],
      },
    ],
    'name': 'sklearn_env'
}
```

## Load the MLFlow formatted model and test predictions

Once your environment is ready, you can pass the SKlearnWrapper, the Conda environment, and your newly created artifacts dictionary to the mlflow.pyfunc.save_model() method. Doing so saves the model to your disk.

```python
mlflow_pyfunc_model_path = "sklearn_mlflow_pyfunc_custom"
mlflow.pyfunc.save_model(path=mlflow_pyfunc_model_path, python_model=SKLearnWrapper(), conda_env=conda_env, artifacts=artifacts)

```

To ensure your newly saved MLflow formatted model didn't change during the save, you can load your model and print out a test prediction to compare your original model.
