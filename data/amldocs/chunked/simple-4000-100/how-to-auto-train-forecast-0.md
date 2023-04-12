
# Set up AutoML to train a time-series forecasting model with Python

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

> [!div class="op_single_selector" title1="Select the version of the Azure Machine Learning SDK you are using:"]
> * [v1](./v1/how-to-auto-train-forecast-v1.md)
> * [v2 (current version)](how-to-auto-train-forecast.md)

In this article, you'll learn how to set up AutoML training for time-series forecasting models with Azure Machine Learning automated ML in the [Azure Machine Learning Python SDK](/python/api/overview/azure/ai-ml-readme).

To do so, you: 

> [!div class="checklist"]
> * Prepare data for training.
> * Configure specific time-series parameters in a [Forecasting Job](/python/api/azure-ai-ml/azure.ai.ml.automl.forecastingjob).
> * Get predictions from trained time-series models.

For a low code experience, see the [Tutorial: Forecast demand with automated machine learning](tutorial-automated-ml-forecast.md) for a time-series forecasting example using automated ML in the [Azure Machine Learning studio](https://ml.azure.com/).

AutoML uses standard machine learning models along with well-known time series models to create forecasts. Our approach incorporates multiple contextual variables and their relationship to one another during training. Since multiple factors can influence a forecast, this method aligns itself well with real world forecasting scenarios. For example, when forecasting sales, interactions of historical trends, exchange rate, and price can all jointly drive the sales outcome. For more details, see our article on [forecasting methodology](./concept-automl-forecasting-methods.md). 

## Prerequisites

For this article you need, 

* An Azure Machine Learning workspace. To create the workspace, see [Create workspace resources](quickstart-create-resources.md).

* The ability to launch AutoML training jobs. Follow the [how-to guide for setting up AutoML](how-to-configure-auto-train.md) for details.

## Training and validation data

Input data for AutoML forecasting must contain valid time series in tabular format. Each variable must have its own corresponding column in the data table. AutoML requires at least two columns: a **time column** representing the time axis and the **target column** which is the quantity to forecast. Other columns can serve as predictors. For more details, see [how AutoML uses your data](./concept-automl-forecasting-methods.md#how-automl-uses-your-data). 

> [!IMPORTANT]
> When training a model for forecasting future values, ensure all the features used in training can be used when running predictions for your intended horizon. <br> <br> For example, a feature for current stock price could massively increase training accuracy. However, if you intend to forecast with a long horizon, you may not be able to accurately predict future stock values corresponding to future time-series points, and model accuracy could suffer.

AutoML forecasting jobs require that your training data is represented as an **MLTable** object. An MLTable specifies a data source and steps for loading the data. For more information and use cases, see the [MLTable how-to guide](./how-to-mltable.md). As a simple example, suppose your training data is contained in a CSV file in a local directory, `./train_data/timeseries_train.csv`. You can define a new MLTable by copying the following YAML code to a new file, `./train_data/MLTable`:

```yml
$schema: https://azuremlschemas.azureedge.net/latest/MLTable.schema.json

type: mltable
paths:
    - file: ./timeseries_train.csv

transformations:
    - read_delimited:
        delimiter: ','
        encoding: ascii
```

You can now define an input data object, which is required to start a training job, using the AzureML Python SDK as follows: 

```python
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import Input

# Training MLTable defined locally, with local data to be uploaded
my_training_data_input = Input(
    type=AssetTypes.MLTABLE, path="./train_data"
)
```
