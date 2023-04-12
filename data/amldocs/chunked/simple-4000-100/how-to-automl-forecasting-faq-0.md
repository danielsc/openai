
# Frequently asked questions about forecasting in AutoML

[!INCLUDE [sdk v2](../../includes/machine-learning-sdk-v2.md)]

This article answers common questions about forecasting in AutoML. See the [methods overview article](./concept-automl-forecasting-methods.md) for more general information about forecasting methodology in AutoML. Instructions and examples for training forecasting models in AutoML can be found in our [set up AutoML for time series forecasting](./how-to-auto-train-forecast.md) article.

## How do I start building forecasting models in AutoML?
You can start by reading our guide on [setting up AutoML to train a time-series forecasting model with Python](./how-to-auto-train-forecast.md). We've also provided hands-on examples in several Jupyter notebooks:  
1. [Bike share example](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-task-bike-share/auto-ml-forecasting-bike-share.ipynb)
2. [Forecasting using deep learning](https://github.com/Azure/azureml-examples/blob/main/sdk/python/jobs/automl-standalone-jobs/automl-forecasting-github-dau/auto-ml-forecasting-github-dau.ipynb)
3. [Many models](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-many-models/auto-ml-forecasting-many-models.ipynb) 
4. [Forecasting Recipes](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-recipes-univariate/auto-ml-forecasting-univariate-recipe-experiment-settings.ipynb)
5. [Advanced forecasting scenarios](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-forecast-function/auto-ml-forecasting-function.ipynb)

## Why is AutoML slow on my data?

We're always working to make it faster and more scalable! To work as a general forecasting platform, AutoML does extensive data validations, complex feature engineering, and searches over a large model space. This complexity can require a lot of time, depending on the data and the configuration. 

One common source of slow runtime is training AutoML with default settings on data containing numerous time series. The cost of many forecasting methods scales with the number of series. For example, methods like Exponential Smoothing and Prophet [train a model for each time series](./concept-automl-forecasting-methods.md#model-grouping) in the training data. **The Many Models feature of AutoML scales to these scenarios** by distributing training jobs across a compute cluster and has been successfully applied to data with millions of time series. For more information, see the [forecasting at scale](./how-to-auto-train-forecast.md#forecasting-at-scale) article. You can also read about [the success of Many Models](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/automated-machine-learning-on-the-m5-forecasting-competition/ba-p/2933391) on a high-profile competition data set.

## How can I make AutoML faster?
See the ["why is AutoML slow on my data"](#why-is-automl-slow-on-my-data) answer to understand why it may be slow in your case.
Consider the following configuration changes that may speed up your job:
- [Block time series models](./how-to-auto-train-forecast.md#model-search-settings) like ARIMA and Prophet
- Turn off look-back features like lags and rolling windows
- Reduce 
  - number of trials/iterations
  - trial/iteration timeout
  - experiment timeout
  - number of cross validation folds.
- Ensure that early termination is enabled.
  
## What modeling configuration should I use?

There are four basic configurations supported by AutoML forecasting:

|Configuration|Scenario|Pros|Cons|
|--|--|--|--|
|**Default AutoML**|Recommended if the dataset has a small number of time series that have roughly similar historic behavior.|- Simple to configure from code/SDK or AzureML Studio <br><br> - AutoML has the chance to cross-learn across different time series since the regression models pool all series together in training. See the [model grouping](./concept-automl-forecasting-methods.md#model-grouping) section for more information.|- Regression models may be less accurate if the time series in the training data have divergent behavior <br> <br> - Time series models may take a long time to train if there are a large number of series in the training data. See the ["why is AutoML slow on my data"](#why-is-automl-slow-on-my-data) answer for more information.|
