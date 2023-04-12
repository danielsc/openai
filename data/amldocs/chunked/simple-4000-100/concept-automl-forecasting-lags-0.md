
# Lagged features for time series forecasting in AutoML
This article focuses on AutoML's methods for creating lag and rolling window aggregation features for forecasting regression models. Features like these that use past information can significantly increase accuracy by helping the model to learn correlational patterns in time. See the [methods overview article](./concept-automl-forecasting-methods.md) for general information about forecasting methodology in AutoML. Instructions and examples for training forecasting models in AutoML can be found in our [set up AutoML for time series forecasting](./how-to-auto-train-forecast.md) article.

## Lag feature example
AutoML generates lags with respect to the forecast horizon. The example in this section illustrates this concept. Here, we use a forecast horizon of three and target lag order of one. Consider the following monthly time series:

Table 1: Original time series <a name="tab:original-ts"></a> 

| Date     | $y_t$ | 
|:---      |:---   |
| 1/1/2001 | 0     |
| 2/1/2001 | 10    |
| 3/1/2001 | 20    |
| 4/1/2001 | 30    |
| 5/1/2001 | 40    | 
| 6/1/2001 | 50    |

First, we generate the lag feature for the horizon $h=1$ only. As you continue reading, it will become clear why we use individual horizons in each table.

Table 2: Lag featurization for $h=1$ <a name="tbl:classic-lag-1"></a>

| Date       | $y_t$ | Origin    | $y_{t-1}$ | $h$ |
|:---        |:---   |:---       |:---       |:---     | 
| 1/1/2001   | 0     | 12/1/2000 | -         | 1       |
| 2/1/2001   | 10    | 1/1/2001  | 0         | 1       |
| 3/1/2001   | 20    | 2/1/2001  | 10        | 1       |
| 4/1/2001   | 30    | 3/1/2001  | 20        | 1       |
| 5/1/2001   | 40    | 4/1/2001  | 30        | 1       |
| 6/1/2001   | 50    | 4/1/2001  | 40        | 1       |

Table 2 is generated from Table 1 by shifting the $y_t$ column down by a single observation. We've added a column named `Origin` that has the dates that the lag features originate from. Next, we generate the lagging feature for the forecast horizon $h=2$ only.

Table 3: Lag featurization for $h=2$ <a name="tbl:classic-lag-2"></a>

| Date       | $y_t$ | Origin    | $y_{t-2}$ | $h$ |
|:---        |:---   |:---       |:---       |:---     | 
| 1/1/2001   | 0     | 11/1/2000 | -         | 2       |
| 2/1/2001   | 10    | 12/1/2000 | -         | 2       |
| 3/1/2001   | 20    | 1/1/2001  | 0         | 2       |
| 4/1/2001   | 30    | 2/1/2001  | 10        | 2       |
| 5/1/2001   | 40    | 3/1/2001  | 20        | 2       |
| 6/1/2001   | 50    | 4/1/2001  | 30        | 2       |

Table 3 is generated from Table 1 by shifting the $y_t$ column down by two observations. Finally, we will generate the lagging feature for the forecast horizon $h=3$ only.

Table 4: Lag featurization for $h=3$ <a name="tbl:classic-lag-3"></a>

| Date       | $y_t$ | Origin    | $y_{t-3}$ | $h$ |
|:---        |:---   |:---       |:---       |:---     | 
| 1/1/2001   | 0     | 10/1/2000 | -         | 3       |
| 2/1/2001   | 10    | 11/1/2000 | -         | 3       |
| 3/1/2001   | 20    | 12/1/2000 | -         | 3       |
| 4/1/2001   | 30    | 1/1/2001  | 0         | 3       |
| 5/1/2001   | 40    | 2/1/2001  | 10        | 3       |
| 6/1/2001   | 50    | 3/1/2001  | 20        | 3       |

Next, we concatenate Tables 1, 2, and 3 and rearrange the rows. The result is in the following table:

Table 5: Lag featurization complete <a name="tbl:automl-lag-complete"></a>

| Date       | $y_t$ | Origin    | $y_{t-1}^{(h)}$ | $h$ |
|:---        |:---   |:---       |:---       |:---     | 
| 1/1/2001   | 0     | 12/1/2000 | -         | 1       |
| 1/1/2001   | 0     | 11/1/2000 | -         | 2       |
| 1/1/2001   | 0     | 10/1/2000 | -         | 3       |
| 2/1/2001   | 10    | 1/1/2001  | 0         | 1       |
| 2/1/2001   | 10    | 12/1/2000 | -         | 2       |
| 2/1/2001   | 10    | 11/1/2000 | -         | 3       |
| 3/1/2001   | 20    | 2/1/2001  | 10        | 1       |
| 3/1/2001   | 20    | 1/1/2001  | 0         | 2       |
