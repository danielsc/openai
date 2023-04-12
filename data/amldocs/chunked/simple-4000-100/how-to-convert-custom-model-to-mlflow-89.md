To ensure your newly saved MLflow formatted model didn't change during the save, you can load your model and print out a test prediction to compare your original model.

The following code prints a test prediction from the mlflow formatted model and a test prediction from the sklearn model that's saved to your disk for comparison. 

```python
loaded_model = mlflow.pyfunc.load_model(mlflow_pyfunc_model_path)

input_data = "<insert test data>"
# Evaluate the model
import pandas as pd
test_predictions = loaded_model.predict(input_data)
print(test_predictions)

# load the model from disk
import pickle
loaded_model = pickle.load(open(sklearn_model_path, 'rb'))
result = loaded_model.predict(input_data)
print(result)
```

## Register the MLflow formatted model

Once you've confirmed that your model saved correctly, you can create a test run, so you can register and save your MLflow formatted model to your model registry.

```python

mlflow.start_run()

mlflow.pyfunc.log_model(artifact_path=mlflow_pyfunc_model_path, 
                        loader_module=None, 
                        data_path=None, 
                        code_path=None,
                        python_model=SKLearnWrapper(),
                        registered_model_name="Custom_mlflow_model", 
                        conda_env=conda_env,
                        artifacts=artifacts)
mlflow.end_run()
```

> [!IMPORTANT]
> In some cases, you might use a machine learning framework without its built-in MLflow model flavor support. For instance, the `vaderSentiment` library is a standard natural language processing (NLP) library used for sentiment analysis. Since it lacks a built-in MLflow model flavor, you cannot log or register the model with MLflow model fluent APIs. See an example on [how to save, log and register a model that doesn't have a supported built-in MLflow model flavor](https://mlflow.org/docs/latest/model-registry.html#registering-an-unsupported-machine-learning-model).

## Next steps

* [No-code deployment for Mlflow models](how-to-deploy-mlflow-models-online-endpoints.md)
* Learn more about [MLflow and Azure Machine Learning](concept-mlflow.md)
