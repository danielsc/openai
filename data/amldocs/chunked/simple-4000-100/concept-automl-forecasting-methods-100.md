This series ostensibly has a daily frequency, but there's no observation for Jan. 2, 2012. In this case, AutoML will attempt to fill in the data by adding a new row for Jan. 2, 2012. The new value for the `quantity` column, and any other columns in the data, will then be imputed like other missing values. Clearly, AutoML must know the series frequency in order to fill in observation gaps like this. AutoML automatically detects this frequency, or, optionally, the user can provide it in the configuration.

The imputation method for filling missing values can be [configured](./how-to-auto-train-forecast.md#custom-featurization) in the input. The default methods are listed in the following table:

Column Type | Default Imputation Method 
----------- | ---------------
Target      | Forward fill (last observation carried forward)
Numeric Feature     | Median value

Missing values for categorical features are handled during numerical encoding by including an additional category corresponding to a missing value. Imputation is implicit in this case.

### Automated feature engineering
AutoML generally adds new columns to user data to increase modeling accuracy. Engineered feature can include the following:

Feature Group | Default/Optional
------------ | ----------------
[Calendar features](./concept-automl-forecasting-calendar-features.md) derived from the time index (for example, day of week) | Default
Categorical features derived from time series IDs | Default
Encoding categorical types to numeric type | Default
Indicator features for holidays associated with a given country or region | Optional
[Lags of target quantity](./concept-automl-forecasting-lags.md) | Optional
Lags of feature columns | Optional
Rolling window aggregations (for example, rolling average) of target quantity | Optional
Seasonal decomposition ([STL](https://otexts.com/fpp3/stl.html)) | Optional

You can configure featurization from the AutoML SDK via the [ForecastingJob](/python/api/azure-ai-ml/azure.ai.ml.automl.forecastingjob#azure-ai-ml-automl-forecastingjob-set-forecast-settings) class or from the [AzureML Studio web interface](how-to-use-automated-ml-for-ml-models.md#customize-featurization).

### Non-stationary time series detection and handling

A time series where mean and variance change over time is called a **non-stationary**. For example, time series that exhibit stochastic trends are non-stationary by nature. To visualize this, the following image plots a series that is generally trending upward. Now, compute and compare the mean (average) values for the first and the second half of the series. Are they the same? Here, the mean of the series in the first half of the plot is significantly smaller than in the second half. The fact that the mean of the series depends on the time interval one is looking at, is an example of the time-varying moments. Here, the mean of a series is the first moment.

:::image type="content" source="media/how-to-auto-train-forecast/non-stationary-retail-sales.png" alt-text="Diagram showing retail sales for a non-stationary time series.":::

Next, let's examine the following image, which plots the original series in first differences, $\Delta y_{t} = y_t - y_{t-1}$. The mean of the series is roughly constant over the time range while the variance appears to vary. Thus, this is an example of a first order stationary times series. 


:::image type="content" source="media/how-to-auto-train-forecast/weakly-stationary-retail-sales.png" alt-text="Diagram showing retail sales for a weakly stationary time series.":::

AutoML regression models can't inherently deal with stochastic trends, or other well-known problems associated with non-stationary time series. As a result, out-of-sample forecast accuracy can be  poor if such trends are present.

AutoML automatically analyzes time series dataset to determine stationarity. When non-stationary time series are detected, AutoML applies a differencing transform automatically to mitigate the impact of non-stationary behavior.
