However, currently no primary metrics for regression addresses relative difference. All of `r2_score`, `normalized_mean_absolute_error`, and `normalized_root_mean_squared_error` treat a $20k prediction error the same for a worker with a $30k salary as a worker making $20M, if these two data points belongs to the same dataset for regression, or the same time series specified by the time series identifier. While in reality, predicting only $20k off from a $20M salary is very close (a small 0.1% relative difference), whereas $20k off from $30k isn't close (a large 67% relative difference). To address the issue of relative difference, one can train a model with available primary metrics, and then select the model with best `mean_absolute_percentage_error` or `root_mean_squared_log_error`.

| Metric | Example use case(s) |
| ------ | ------- |
| `spearman_correlation` | |
| `normalized_root_mean_squared_error` | Price prediction (house/product/tip), Review score prediction |
| `r2_score` | Airline delay, Salary estimation, Bug resolution time |
| `normalized_mean_absolute_error` |  |

#### Metrics for Time Series Forecasting scenarios

The recommendations are similar to those noted for regression scenarios. 

| Metric | Example use case(s) |
| ------ | ------- |
| `normalized_root_mean_squared_error` | Price prediction (forecasting), Inventory optimization, Demand forecasting | 
| `r2_score` | Price prediction (forecasting), Inventory optimization, Demand forecasting |
| `normalized_mean_absolute_error` | |

#### Metrics for Image Object Detection scenarios 

- For Image Object Detection, the primary metrics supported are defined in the ObjectDetectionPrimaryMetrics Enum

#### Metrics for Image Instance Segmentation scenarios 

- For Image Instance Segmentation scenarios, the primary metrics supported are defined in the InstanceSegmentationPrimaryMetrics Enum

### Data featurization

In every automated ML experiment, your data is automatically transformed to numbers and vectors of numbers plus (i.e. converting text to numeric) also scaled and normalized to help *certain* algorithms that are sensitive to features that are on different scales. This data transformation, scaling and normalization is referred to as featurization. 

> [!NOTE]
> Automated machine learning featurization steps (feature normalization, handling missing data, converting text to numeric, etc.) become part of the underlying model. When using the model for predictions, the same featurization steps applied during training are applied to your input data automatically.

When configuring your automated ML jobs, you can enable/disable the `featurization` settings by using the `.set_featurization()` setter function. 

The following table shows the accepted settings for featurization. 

|Featurization Configuration | Description |
| ------------- | ------------- |
|`"mode": 'auto'`| Indicates that as part of preprocessing, [data guardrails and featurization steps](how-to-configure-auto-features.md#featurization) are performed automatically. **Default setting**.|
|`"mode": 'off'`| Indicates featurization step shouldn't be done automatically.|
|`"mode":`&nbsp;`'custom'`| Indicates customized featurization step should be used.|

The following code shows how custom featurization can be provided in this case for a regression job.

```python
from azure.ai.ml.automl import ColumnTransformer

transformer_params = {
    "imputer": [
        ColumnTransformer(fields=["CACH"], parameters={"strategy": "most_frequent"}),
        ColumnTransformer(fields=["PRP"], parameters={"strategy": "most_frequent"}),
    ],
}
regression_job.set_featurization(
    mode="custom",
    transformer_params=transformer_params,
    blocked_transformers=["LabelEncoding"],
    column_name_and_types={"CHMIN": "Categorical"},
)
```

<a name="exit"></a> 

### Exit criteria

There are a few options you can define in the `set_limits()` function to end your experiment prior to job completion. 

|Criteria| description
