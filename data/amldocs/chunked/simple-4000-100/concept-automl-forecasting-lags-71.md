| 3/1/2001   | 20    | 2/1/2001  | 10        | 1       |
| 3/1/2001   | 20    | 1/1/2001  | 0         | 2       |
| 3/1/2001   | 20    | 12/1/2000 | -         | 3       |
| 4/1/2001   | 30    | 3/1/2001  | 20        | 1       |
| 4/1/2001   | 30    | 2/1/2001  | 10        | 2       |
| 4/1/2001   | 30    | 1/1/2001  | 0         | 3       |
| 5/1/2001   | 40    | 4/1/2001  | 30        | 1       |
| 5/1/2001   | 40    | 3/1/2001  | 20        | 2       |
| 5/1/2001   | 40    | 2/1/2001  | 10        | 3       |
| 6/1/2001   | 50    | 4/1/2001  | 40        | 1       |
| 6/1/2001   | 50    | 4/1/2001  | 30        | 2       |
| 6/1/2001   | 50    | 3/1/2001  | 20        | 3       |


In the final table, we've changed the name of the lag column to $y_{t-1}^{(h)}$ to reflect that the lag is generated with respect to a specific horizon. The table shows that the lags we generated with respect to the horizon can be mapped to the conventional ways of generating lags in the previous tables.

Table 5 is an example of the data augmentation that AutoML applies to training data to enable direct forecasting from regression models. When the configuration includes lag features, AutoML creates horizon dependent lags along with an integer-valued horizon feature. This enables AutoML's forecasting regression models to make a prediction at horizon $h$ without regard to the prediction at $h-1$, in contrast to recursively defined models like ARIMA.

> [!NOTE]
> Generation of horizon dependent lag features adds new _rows_ to the dataset. The number of new rows is proportional to forecast horizon. This dataset size growth can lead to out-of-memory errors on smaller compute nodes or when dataset size is already large. See the [frequently asked questions](./how-to-automl-forecasting-faq.md#how-do-i-fix-an-out-of-memory-error) article for solutions to this problem.       

Another consequence of this lagging strategy is that lag order and forecast horizon are decoupled. If, for example, your forecast horizon is seven, and you want AutoML to use lag features, you do not have to set the lag order to seven to ensure prediction over a full forecast horizon. Since AutoML generates lags with respect to horizon, you can set the lag order to one and AutoML will augment the data so that lags of any order are valid up to forecast horizon.

## Next steps
* Learn more about [how to set up AutoML to train a time-series forecasting model](./how-to-auto-train-forecast.md).
* Browse [AutoML Forecasting Frequently Asked Questions](./how-to-automl-forecasting-faq.md).
* Learn about [calendar features for time series forecasting in AutoML](./concept-automl-forecasting-calendar-features.md).
* Learn about [how AutoML uses machine learning to build forecasting models](./concept-automl-forecasting-methods.md).
