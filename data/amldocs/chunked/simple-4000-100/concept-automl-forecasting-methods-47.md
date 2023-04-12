AutoML accepts time series data in tabular, "wide" format; that is, each variable must have its own corresponding column. AutoML requires one of the columns to be the time axis for the forecasting problem. This column must be parsable into a datetime type. The simplest time series data set consists of a **time column** and a numeric **target column**. The target is the variable one intends to predict into the future. The following is an example of the format in this simple case: 

timestamp | quantity
--------- | --------
2012-01-01 | 100
2012-01-02 | 97
2012-01-03 | 106
...        | ...
2013-12-31 | 347

In more complex cases, the data may contain other columns aligned with the time index. 

timestamp | SKU | price | advertised | quantity
--------- | --- | ----- | ---------- | --------
2012-01-01 | JUICE1 | 3.5 | 0 | 100
2012-01-01 | BREAD3 | 5.76 | 0 | 47
2012-01-02 | JUICE1 | 3.5 | 0 | 97
2012-01-02 | BREAD3 | 5.5 | 1 | 68
... | ... | ... | ... | ...
2013-12-31 | JUICE1 | 3.75 | 0 | 347
2013-12-31 | BREAD3 | 5.7 | 0 | 94

In this example, there's a SKU, a retail price, and a flag indicating whether an item was advertised in addition to the timestamp and target quantity. There are evidently two series in this dataset - one for the JUICE1 SKU and one for the BREAD3 SKU; the `SKU` column is a **time series ID column** since grouping by it gives two groups containing a single series each. Before sweeping over models, AutoML does basic validation of the input configuration and data and adds engineered features.

### Data length requirements
To train a forecasting model, you must have a sufficient amount of historical data. This threshold quantity varies with the training configuration. If you've provided validation data, the minimum number of training observations required per time series is given by,

$T_{\text{user validation}} = H + \text{max}(l_{\text{max}}, s_{\text{window}}) + 1$,

where $H$ is the forecast horizon, $l_{\text{max}}$ is the maximum lag order, and $s_{\text{window}}$ is the window size for rolling aggregation features. If you're using cross-validation, the minimum number of observations is,

 $T_{\text{CV}} = 2H + (n_{\text{CV}} - 1) n_{\text{step}} + \text{max}(l_{\text{max}}, s_{\text{window}}) + 1$,

where $n_{\text{CV}}$ is the number of cross-validation folds and $n_{\text{step}}$ is the CV step size, or offset between CV folds. The basic logic behind these formulas is that you should always have at least a horizon of training observations for each time series, including some padding for lags and cross-validation splits. See [forecasting model selection](./concept-automl-forecasting-sweeping.md#model-selection) for more details on cross-validation for forecasting.

### Missing data handling
AutoML's time series models require regularly spaced observations in time. Regularly spaced, here, includes cases like monthly or yearly observations where the number of days between observations may vary. Prior to modeling, AutoML must ensure there are no missing series values _and_ that the observations are regular. Hence, there are two missing data cases:

* A value is missing for some cell in the tabular data
* A _row_ is missing which corresponds with an expected observation given the time series frequency

In the first case, AutoML imputes missing values using common, configurable techniques.

An example of a missing, expected row is shown in the following table:

timestamp | quantity
--------- | --------
2012-01-01 | 100
2012-01-03 | 106
2012-01-04 | 103
...        | ...
2013-12-31 | 347

This series ostensibly has a daily frequency, but there's no observation for Jan. 2, 2012. In this case, AutoML will attempt to fill in the data by adding a new row for Jan. 2, 2012. The new value for the `quantity` column, and any other columns in the data, will then be imputed like other missing values. Clearly, AutoML must know the series frequency in order to fill in observation gaps like this. AutoML automatically detects this frequency, or, optionally, the user can provide it in the configuration.
