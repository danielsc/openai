Optional configurations are available for forecasting tasks, such as enabling deep learning and specifying a target rolling window aggregation. A complete list of parameters is available in the [forecast_settings API doc](/python/api/azure-ai-ml/azure.ai.ml.automl.forecastingjob#azure-ai-ml-automl-forecastingjob-set-forecast-settings).

#### Model search settings

There are two optional settings that control the model space where AutoML searches for the best model, `allowed_training_algorithms` and `blocked_training_algorithms`. To restrict the search space to a given set of model classes, use allowed_training_algorithms as in the following sample:

```python
# Only search ExponentialSmoothing and ElasticNet models
forecasting_job.set_training(
    allowed_training_algorithms=["ExponentialSmoothing", "ElasticNet"]
)
```

In this case, the forecasting job _only_ searches over Exponential Smoothing and Elastic Net model classes. To remove a given set of model classes from the search space, use the blocked_training_algorithms as in the following sample:

```python
# Search over all model classes except Prophet
forecasting_job.set_training(
    blocked_training_algorithms=["Prophet"]
)
```

Now, the job searches over all model classes _except_ Prophet. For a list of forecasting model names that are accepted in `allowed_training_algorithms` and `blocked_training_algorithms`, see [supported forecasting models](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.forecasting) and [supported regression models](/python/api/azureml-train-automl-client/azureml.train.automl.constants.supportedmodels.regression).  

#### Enable deep learning

AutoML ships with a custom deep neural network (DNN) model called `ForecastTCN`. This model is a [temporal convolutional network](https://arxiv.org/abs/1803.01271), or TCN, that applies common imaging task methods to time series modeling. Namely, one-dimensional "causal" convolutions form the backbone of the network and enable the model to learn complex patterns over long durations in the training history.  

:::image type="content" source="media/how-to-auto-train-forecast/tcn-basic.png" alt-text="Diagram showing major components of AutoML's ForecastTCN.":::

The ForecastTCN often achieves higher accuracy than standard time series models when there are thousands or more observations in the training history. However, it also takes longer to train and sweep over ForecastTCN models due to their higher capacity.

You can enable the ForecastTCN in AutoML by setting the `enable_dnn_training` flag in the set_training() method as follows:

```python
# Include ForecastTCN models in the model search
forecasting_job.set_training(
    enable_dnn_training=True
)
```

To enable DNN for an AutoML experiment created in the Azure Machine Learning studio, see the [task type settings in the studio UI how-to](how-to-use-automated-ml-for-ml-models.md#create-and-run-experiment).

> [!NOTE]
> * When you enable DNN for experiments created with the SDK, [best model explanations](how-to-machine-learning-interpretability-automl.md) are disabled.
> * DNN support for forecasting in Automated Machine Learning is not supported for runs initiated in Databricks.
> * GPU compute types are recommended when DNN training is enabled 

#### Target rolling window aggregation

Recent values of the target are often impactful features in a forecasting model. Rolling window aggregations allow you to add rolling aggregations of data values as features. Generating and using these features as extra contextual data helps with the accuracy of the train model.

Consider an energy demand forecasting scenario where weather data and historical demand are available.
The table shows resulting feature engineering that occurs when window aggregation is applied over the most recent three hours. Columns for **minimum, maximum,** and **sum** are generated on a sliding window of three hours based on the defined settings. For instance, for the observation valid on September 8, 2017 4:00am, the maximum, minimum, and sum values are calculated using the **demand values** for September 8, 2017 1:00AM - 3:00AM. This window of three hours shifts along to populate data for the remaining rows.
