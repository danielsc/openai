* Numerical predictor columns in your data are aggregated by sum, mean, minimum value, and maximum value. As a result, automated ML generates new columns suffixed with the aggregation function name and applies the selected aggregate operation.
* For categorical predictor columns, the data is aggregated by mode, the most prominent category in the window.
* Date predictor columns are aggregated by minimum value, maximum value and mode.

The following example sets the frequency to hourly and the aggregation function to summation:

```python
# Aggregate the data to hourly frequency
forecasting_job.set_forecast_settings(
    ...,  # other settings
    frequency='H',
    target_aggregate_function='sum'
)
```

#### Custom cross-validation settings

There are two customizable settings that control cross-validation for forecasting jobs: the number of folds, `n_cross_validations`, and the step size defining the time offset between folds, `cv_step_size`. See [forecasting model selection](./concept-automl-forecasting-sweeping.md#model-selection) for more information on the meaning of these parameters. By default, AutoML sets both settings automatically based on characteristics of your data, but advanced users may want to set them manually. For example, suppose you have daily sales data and you want your validation setup to consist of five folds with a seven-day offset between adjacent folds. The following code sample shows how to set these:

```python
from azure.ai.ml import automl

# Create a job with five CV folds
forecasting_job = automl.forecasting(
    ...,  # other training parameters
    n_cross_validations=5,
)

# Set the step size between folds to seven days
forecasting_job.set_forecast_settings(
    ...,  # other settings
    cv_step_size=7
)
```

### Custom featurization

By default, AutoML augments training data with engineered features to increase the accuracy of the models. See [automated feature engineering](./concept-automl-forecasting-methods.md#automated-feature-engineering) for more information. Some of the preprocessing steps can be customized using the `set_featurization()` method of the forecasting job.

Supported customizations for forecasting include:

|Customization|Description|Options
|--|--|---
|**Column purpose update**|Override the auto-detected feature type for the specified column.|"Categorical", "DateTime", "Numeric"
|**Transformer parameter update**|Update the parameters for the specified imputer.|`{"strategy": "constant", "fill_value": <value>}`, `{"strategy": "median"}`, `{"strategy": "ffill"}`

For example, suppose you have a retail demand scenario where the data includes features like price, an "on sale" flag, and a product type. The following sample shows how you can set customized types and imputers for these features:

```python
from azure.ai.ml.automl import ColumnTransformer

# Customize imputation methods for price and is_on_sale features
# Median value imputation for price, constant value of zero for is_on_sale
transformer_params = {
    "imputer": [
        ColumnTransformer(fields=["price"], parameters={"strategy": "median"}),
        ColumnTransformer(fields=["is_on_sale"], parameters={"strategy": "constant", "fill_value": 0}),
    ],
}

# Set the featurization
# Ensure that product_type feature is interpreted as categorical
forecasting_job.set_featurization(
    mode="custom",
    transformer_params=transformer_params,
    column_name_and_types={"product_type": "Categorical"},
)
```

If you're using the Azure Machine Learning studio for your experiment, see [how to customize featurization in the studio](how-to-use-automated-ml-for-ml-models.md#customize-featurization).

## Run the experiment 

After all settings are configured, you can launch the forecasting job via the `mlcient` as follows:

```python
# Submit the AutoML job
returned_job = ml_client.jobs.create_or_update(
    forecasting_job
)

print(f"Created job: {returned_job}")

# Get a URL for the status of the job
returned_job.services["Studio"].endpoint
``` 
