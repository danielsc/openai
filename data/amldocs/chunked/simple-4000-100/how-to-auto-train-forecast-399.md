In this sample, the step size for the rolling forecast is set to one which means that the forecaster is advanced one period, or one day in our demand prediction example, at each iteration. The total number of forecasts returned by `rolling_forecast` depends on the length of the test set and this step size. For more details and examples, see the [rolling_forecast() documentation](/python/api/azureml-training-tabular/azureml.training.tabular.models.forecasting_pipeline_wrapper_base.forecastingpipelinewrapperbase#azureml-training-tabular-models-forecasting-pipeline-wrapper-base-forecastingpipelinewrapperbase-rolling-forecast) and the [Forecasting away from training data notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-forecast-function/auto-ml-forecasting-function.ipynb). 
    
### Prediction into the future

The [forecast_quantiles()](/python/api/azureml-training-tabular/azureml.training.tabular.models.forecasting_pipeline_wrapper_base.forecastingpipelinewrapperbase#azureml-training-tabular-models-forecasting-pipeline-wrapper-base-forecastingpipelinewrapperbase-forecast-quantiles) generates forecasts for given quantiles of the prediction distribution. This method thus provides a way to get a point forecast with a cone of uncertainty around it. Learn more in the [Forecasting away from training data notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-forecast-function/auto-ml-forecasting-function.ipynb).

In the following example, you first replace all values in `y_pred` with `NaN`. The forecast origin is at the end of training data in this case. However, if you replaced only the second half of `y_pred` with `NaN`, the function would leave the numerical values in the first half unmodified, but forecast the `NaN` values in the second half. The function returns both the forecasted values and the aligned features.

You can also use the `forecast_destination` parameter in the `forecast_quantiles()` function to forecast values up to a specified date.

```python
label_query = test_labels.copy().astype(np.float)
label_query.fill(np.nan)
label_fcst, data_trans = fitted_model.forecast_quantiles(
    test_dataset, label_query, forecast_destination=pd.Timestamp(2019, 1, 8)
)
```

No quantiles are specified here, so only the point forecast is generated. You may want to understand the predictions at a specific quantile of the distribution. For example, when the forecast is used to control inventory like grocery items or virtual machines for a cloud service. In such cases, the control point is usually something like "we want the item to be in stock and not run out 99% of the time". The following sample demonstrates how to specify forecast quantiles, such as 50th or 95th percentile: 

```python
# Get forecasts for the 5th, 50th, and 90th percentiles 
fitted_model.quantiles = [0.05, 0.5, 0.9]
fitted_model.forecast_quantiles(
    test_dataset, label_query, forecast_destination=pd.Timestamp(2019, 1, 8)
)
```

You can calculate model metrics like, root mean squared error (RMSE) or mean absolute percentage error (MAPE) to help you estimate the models performance. See the Evaluate section of the [Bike share demand notebook](~/azureml-examples-main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-bike-share/auto-ml-forecasting-bike-share.ipynb) for an example. 

After the overall model accuracy has been determined, the most realistic next step is to use the model to forecast unknown future values. 

Supply a data set in the same format as the test set `test_dataset` but with future datetimes, and the resulting prediction set is the forecasted values for each time-series step. Assume the last records in the data set were for December 31, 2018. To forecast demand, create a time series record for each store starting on January 1, 2019.

```output
day_datetime,store,week_of_year
01/01/2019,A,1
01/01/2019,A,1
```

Repeat the necessary steps to load this future data to a data frame and then run `best_run.forecast_quantiles(test_dataset)` to predict future values.
