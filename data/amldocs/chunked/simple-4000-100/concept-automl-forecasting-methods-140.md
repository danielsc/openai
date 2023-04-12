AutoML automatically analyzes time series dataset to determine stationarity. When non-stationary time series are detected, AutoML applies a differencing transform automatically to mitigate the impact of non-stationary behavior.

### Model sweeping
After data has been prepared with missing data handling and feature engineering, AutoML sweeps over a set of models and hyper-parameters using a [model recommendation service](https://www.microsoft.com/research/publication/probabilistic-matrix-factorization-for-automated-machine-learning/). The models are ranked based on validation or cross-validation metrics and then, optionally, the top models may be used in an ensemble model. The best model, or any of the trained models, can be inspected, downloaded, or deployed to produce forecasts as needed. See the [model sweeping and selection](./concept-automl-forecasting-sweeping.md) article for more details.


### Model grouping
When a dataset contains more than one time series, as in the given data example, there are multiple ways to model that data. For instance, we may simply group by the **time series ID column(s)** and train independent models for each series. A more general approach is to partition the data into groups that may each contain multiple, likely related series and train a model per group. By default, AutoML forecasting uses a mixed approach to model grouping. Time series models, plus ARIMAX and Prophet, assign one series to one group and other regression models assign all series to a single group. The following table summarizes the model groupings in two categories, one-to-one and many-to-one:  

Each Series in Own Group (1:1) | All Series in Single Group (N:1)
-------------------| -----------------
Naive, Seasonal Naive, Average, Seasonal Average, Exponential Smoothing, ARIMA, ARIMAX, Prophet | Linear SGD, LARS LASSO, Elastic Net, K Nearest Neighbors, Decision Tree, Random Forest, Extremely Randomized Trees, Gradient Boosted Trees, LightGBM, XGBoost, ForecastTCN

More general model groupings are possible via AutoML's Many-Models solution; see our [Many Models- Automated ML notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-many-models/auto-ml-forecasting-many-models.ipynb) and [Hierarchical time series- Automated ML notebook](https://github.com/Azure/azureml-examples/blob/main/v1/python-sdk/tutorials/automl-with-azureml/forecasting-hierarchical-timeseries/auto-ml-forecasting-hierarchical-timeseries.ipynb).

## Next steps

* Learn more about [model sweeping and selection](./concept-automl-forecasting-sweeping.md) for forecasting in AutoML.
* Learn about how AutoML creates [features from the calendar](./concept-automl-forecasting-calendar-features.md).
* Learn about how AutoML creates [lag features](./concept-automl-forecasting-lags.md).
* Read answers to [frequently asked questions](./how-to-automl-forecasting-faq.md) about forecasting in AutoML.
