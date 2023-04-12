|`wday_lbl`|String feature representing name of the day of the week. |
|`qday`|Numeric feature representing the day within the quarter. It takes values 1 through 92.|1|
|`yday`|Numeric feature representing the day of the year. It takes values 1 through 365, or 1 through 366 in the case of leap year.|1|
|`week`|Numeric feature representing [ISO week](https://en.wikipedia.org/wiki/ISO_week_date) as defined in ISO 8601. ISO weeks always start on Monday and end on Sunday. It takes values 1 through 52, or 53 for years having 1st January falling on Thursday or for leap years having 1st January falling on Wednesday.|52|

The full set of standard calendar features may not be created in all cases. The generated set depends on the frequency of the time series and whether the training data contains datetime features in addition to the time index. The following table shows the features created for different column types:

Column purpose | Calendar features
--- | ---
Time index | The full set minus calendar features that have high correlation with other features. For example, if the time series frequency is daily, then any features with a more granular frequency than daily will be removed since they don't provide useful information.
Other datetime column | A reduced set consisting of  `Year`,  `Month`,  `Day`,  `DayOfWeek`,  `DayOfYear`,  `QuarterOfYear`,  `WeekOfMonth`,  `Hour`,  `Minute`, and `Second`. If the column is a date with no time, `Hour`,  `Minute`, and `Second` will be 0.

## Holiday features

AutoML can optionally create features representing holidays from a specific country or region. These features are configured in AutoML using the `country_or_region_for_holidays` parameter which accepts an [ISO country code](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

> [!NOTE]
> Holiday features can only be made for time series with daily frequency.

The following table summarizes the holiday features:

Feature name | Description
 --- | ----------- |
`Holiday`| String feature that specifies whether a date is a regional or national holiday. Days within some range of a holiday are also marked. 
`isPaidTimeOff`| Binary feature that takes value 1 if the day is a "paid time-off holiday" in the given country or region.

AutoML uses Azure Open Datasets as a source for holiday information. For more information, see the [PublicHolidays](/python/api/azureml-opendatasets/azureml.opendatasets.publicholidays) documentation.

To better understand the holiday feature generation, consider the following example data: 

<img src='./media/concept-automl-forecasting-calendar-features/load_forecasting_sample_data_daily.png' alt='sample_data' width=50%></img>

To make American holiday features for this data, we set the `country_or_region_for_holiday` to 'US' in the [forecast settings](/python/api/azure-ai-ml/azure.ai.ml.automl.forecastingjob#azure-ai-ml-automl-forecastingjob-set-forecast-settings) as shown in the following code sample:
```python
from azure.ai.ml import automl

# create a forcasting job
forecasting_job = automl.forecasting(
    compute='test_cluster',   # Name of single or multinode AML compute infrastructure created by user
    experiment_name=exp_name, # name of experiment 
    training_data=sample_data,  
    target_column_name='demand',
    primary_metric='NormalizedRootMeanSquaredError',
    n_cross_validations=3,
    enable_model_explainability=True
)

# set custom forecast settings
forecasting_job.set_forecast_settings(
    time_column_name='timeStamp',
    country_or_region_for_holidays='US'
)
```
The generated holiday features look like the following:

<a name='output'><img src='./media/concept-automl-forecasting-calendar-features/sample_dataset_holiday_feature_generated.png' alt='sample_data_output' width=75%></img></a>

Note that generated features have the prefix `_automl_` prepended to their column names. AutoML generally uses this prefix to distinguish input features from engineered features.

## Next steps
* Learn more about [how to set up AutoML to train a time-series forecasting model](./how-to-auto-train-forecast.md).
