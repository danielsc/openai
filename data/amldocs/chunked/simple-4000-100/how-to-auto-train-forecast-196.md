The table shows resulting feature engineering that occurs when window aggregation is applied over the most recent three hours. Columns for **minimum, maximum,** and **sum** are generated on a sliding window of three hours based on the defined settings. For instance, for the observation valid on September 8, 2017 4:00am, the maximum, minimum, and sum values are calculated using the **demand values** for September 8, 2017 1:00AM - 3:00AM. This window of three hours shifts along to populate data for the remaining rows.

![target rolling window](./media/how-to-auto-train-forecast/target-roll.svg)

You can enable rolling window aggregation features and set the window size through the set_forecast_settings() method. In the following sample, we set the window size to "auto" so that AutoML will automatically determine a good value for your data:

```python
forecasting_job.set_forecast_settings(
    ...,  # other settings
    target_rolling_window_size='auto'
)
```

#### Short series handling

Automated ML considers a time series a **short series** if there aren't enough data points to conduct the train and validation phases of model development. See [training data length requirements](./concept-automl-forecasting-methods.md#data-length-requirements) for more details on length requirements.

AutoML has several actions it can take for short series. These actions are configurable with the `short_series_handling_config` setting. The default value is "auto." The following table describes the settings:

|Setting|Description
|---|---
|`auto`| The default value for short series handling. <br> - _If all series are short_, pad the data. <br> - _If not all series are short_, drop the short series. 
|`pad`| If `short_series_handling_config = pad`, then automated ML adds random values to each short series found. The following lists the column types and what they're padded with: <br> - Object columns with NaNs <br> - Numeric columns  with 0 <br> - Boolean/logic columns with False <br> - The target column is padded with random values with mean of zero and standard deviation of 1. 
|`drop`| If `short_series_handling_config = drop`, then automated ML drops the short series, and it will not be used for training or prediction. Predictions for these series will return NaN's.
|`None`| No series is padded or dropped

In the following example, we set the short series handling so that all short series are padded to the minimum length:

```python
forecasting_job.set_forecast_settings(
    ...,  # other settings
    short_series_handling_config='pad'
)
```

>[!WARNING]
>Padding may impact the accuracy of the resulting model, since we are introducing artificial data just to get past training without failures. If many of the series are short, then you may also see some impact in explainability results

#### Frequency & target data aggregation

Use the frequency and data aggregation options to avoid failures caused by irregular data. Your data is irregular if it doesn't follow a set cadence in time, like hourly or daily. Point-of-sales data is a good example of irregular data. In these cases, AutoML can aggregate your data to a desired frequency and then build a forecasting model from the aggregates. 

You need to set the `frequency` and `target_aggregate_function` settings to handle irregular data. The frequency setting accepts [Pandas DateOffset strings](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects) as input. Supported values for the aggregation function are:

|Function | Description
|---|---
|`sum`| Sum of target values
|`mean`| Mean or average of target values
|`min`| Minimum value of a target  
|`max`| Maximum value of a target  

* The target column values are aggregated according to the specified operation. Typically, sum is appropriate for most scenarios.
* Numerical predictor columns in your data are aggregated by sum, mean, minimum value, and maximum value. As a result, automated ML generates new columns suffixed with the aggregation function name and applies the selected aggregate operation.
