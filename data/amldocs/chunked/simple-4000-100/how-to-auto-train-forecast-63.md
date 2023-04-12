
You can specify [validation data](concept-automated-ml.md#training-validation-and-test-data) in a similar way, by creating a MLTable and an input data object. Alternatively, if you don't supply validation data, AutoML automatically creates cross-validation splits from your training data to use for model selection. See our article on [forecasting model selection](./concept-automl-forecasting-sweeping.md#model-selection) for more details. Also see [training data length requirements](./concept-automl-forecasting-methods.md#data-length-requirements) for details on how much training data you need to successfully train a forecasting model.

Learn more about how AutoML applies cross validation to [prevent over fitting](concept-manage-ml-pitfalls.md#prevent-overfitting).

## Compute to run experiment
AutoML uses AzureML Compute, which is a fully managed compute resource, to run the training job. In the following example, a compute cluster named `cpu-compute` is created:

```python
from azure.ai.ml.entities import AmlCompute

# specify aml compute name.
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4
    )
    ml_client.compute.begin_create_or_update(compute).result()
```

## Configure experiment

There are several options that you can use to configure your AutoML forecasting experiment. These configuration parameters are set in the automl.forecasting() task method. You can also set job training settings and exit criteria with the set_training() and set_limits() functions, respectively.

The following example shows how to create a forecasting job with normalized root mean squared error as the primary metric and automatically configured cross-validation folds:

```python
from azure.ai.ml import automl

# note that the below is a code snippet -- you might have to modify the variable values to run it successfully
forecasting_job = automl.forecasting(
    compute=compute_name,
    experiment_name=exp_name,
    training_data=my_training_data_input,
    target_column_name=target_column_name,
    primary_metric="NormalizedRootMeanSquaredError",
    n_cross_validations="auto",
)

# Limits are all optional
forecasting_job.set_limits(
    timeout_minutes=120,
    trial_timeout_minutes=30,
    max_concurrent_trials=4,
)
```

### Configuration settings
Forecasting tasks have many settings that are specific to forecasting. Use the set_forecast_settings() method of a ForecastingJob to set forecasting parameters. In the following example, we provide the name of the time column in the training data and set the forecast horizon: 

```python
# Forecasting specific configuration
forecasting_job.set_forecast_settings(
    time_column_name=time_column_name,
    forecast_horizon=24
)
```

The time column name is a required setting and you should generally set the forecast horizon according to your prediction scenario. If your data contains multiple time series, you can specify the names of the **time series ID columns**. These columns, when grouped, define the individual series. For example, suppose that you have data consisting of hourly sales from different stores and brands. The following sample shows how to set the time series ID columns assuming the data contains columns named "store" and "brand": 

```python
# Forecasting specific configuration
# Add time series IDs for store and brand
forecasting_job.set_forecast_settings(
    ...,  # other settings
    time_series_id_column_names=['store', 'brand']
)
```

AutoML tries to automatically detect time series ID columns in your data if none are specified.

Other settings are optional and reviewed in the [optional settings](#optional-settings) section.

### Optional settings

Optional configurations are available for forecasting tasks, such as enabling deep learning and specifying a target rolling window aggregation. A complete list of parameters is available in the [forecast_settings API doc](/python/api/azure-ai-ml/azure.ai.ml.automl.forecastingjob#azure-ai-ml-automl-forecastingjob-set-forecast-settings).
