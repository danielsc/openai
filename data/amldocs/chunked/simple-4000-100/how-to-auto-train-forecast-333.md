 
## Forecasting with a trained model

Once you've used AutoML to train and select a best model, the next step is to evaluate the model. If it meets your requirements, you can use it to generate forecasts into the future. This section shows how to write Python scripts for evaluation and prediction. For an example of deploying a trained model with an inference script, see our [example notebook](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-github-dau/auto-ml-forecasting-github-dau.ipynb).
  
### Evaluating model accuracy with a rolling forecast

Before you put a model into production, you should evaluate its accuracy on a test set held out from the training data. A best practice procedure is a rolling evaluation that rolls the trained forecaster forward in time over the test set, averaging error metrics over several prediction windows. Ideally, the test set for the evaluation is long relative to the model's forecast horizon. Estimates of forecasting error may otherwise be statistically noisy and, therefore, less reliable.

For example, suppose you train a model on daily sales to predict demand up to two weeks (14 days) into the future. If there's sufficient historic data available, you might reserve the final several months to even a year of the data for the test set. The rolling evaluation begins by generating a 14-day-ahead forecast for the first two weeks of the test set. Then, the forecaster is advanced by some number of days into the test set and you generate another 14-day-ahead forecast from the new position. The process continues until you get to the end of the test set.

To do a rolling evaluation, you call the `rolling_forecast` method of the `fitted_model`, then compute desired metrics on the result. A rolling evaluation inference script is shown in the following code sample:

```python
"""
This is the script that is executed on the compute instance. It relies
on the model.pkl file which is uploaded along with this script to the
compute instance.
"""

import os
import pandas as pd

from sklearn.externals import joblib


def init():
    global target_column_name
    global fitted_model

    target_column_name = os.environ["TARGET_COLUMN_NAME"]
    # AZUREML_MODEL_DIR is an environment variable created during deployment
    # It is the path to the model folder (./azureml-models)
    # Please provide your model's folder name if there's one
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model.pkl")
    try:
        fitted_model = joblib.load(model_path)
    except Exception:
        print("Loading pickle failed. Trying torch.load()")

        import torch
        model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model.pt") 
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        fitted_model = torch.load(model_path, map_location=device)


def run(mini_batch):
    print(f"run method start: {__file__}, run({mini_batch})")
    resultList = []
    for test in mini_batch:
        if not test.endswith(".csv"):
            continue
        X_test = pd.read_csv(test, parse_dates=[fitted_model.time_column_name])
        y_test = X_test.pop(target_column_name).values

        # Make a rolling forecast, advancing the forecast origin by 1 period on each iteration through the test set
        X_rf = fitted_model.rolling_forecast(
            X_test, y_test, step=1, ignore_data_errors=True
        )

        resultList.append(X_rf)

    return pd.concat(resultList, sort=False, ignore_index=True)
```

In this sample, the step size for the rolling forecast is set to one which means that the forecaster is advanced one period, or one day in our demand prediction example, at each iteration. The total number of forecasts returned by `rolling_forecast` depends on the length of the test set and this step size. For more details and examples, see the [rolling_forecast() documentation](/python/api/azureml-training-tabular/azureml.training.tabular.models.forecasting_pipeline_wrapper_base.forecastingpipelinewrapperbase#azureml-training-tabular-models-forecasting-pipeline-wrapper-base-forecastingpipelinewrapperbase-rolling-forecast) and the [Forecasting away from training data notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-forecast-function/auto-ml-forecasting-function.ipynb). 
